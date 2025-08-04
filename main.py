from vis import Visualizar
from data_base import DataB
import sqlite3 as lite
from dataB_users import DataB_U
from feedback import Feedback
from export import ExportarDados

from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.colorchooser import askcolor

# cores
co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
but = "#d3d3d3" #botoes

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#LOGIN COM JANELA DE REGISTO
class LoginApp:
    def __init__(self):
        self.datab_u_instance = DataB_U('user.db')
        self.criar_janela_login()

    def criar_janela_login(self):
        self.janela_login = Tk()
        self.janela_login.title('Login - Orçamento Familiar')
        self.janela_login.geometry('300x200')
        self.janela_login.configure(background=co1)
        self.janela_login.resizable(width=False, height=False)

        #CONFIGURAÇÃO DOS ELEMENTOS DA JANELA DE LOGIN
        self.l_username = Label(self.janela_login, text='Username:', font=('Verdana', 10, 'bold'), background=co1)
        self.l_username.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.e_username = Entry(self.janela_login, font=('Verdana', 10))
        self.e_username.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.l_pin = Label(self.janela_login, text='PIN:', font=('Verdana', 10, 'bold'), background=co1)
        self.l_pin.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.e_pin = Entry(self.janela_login, show='*', font=('Verdana', 10))
        self.e_pin.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.frame_botoes = Frame(self.janela_login, background=co1)
        self.frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

        botao_estilo = {'font': ('Verdana', 10, 'bold'), 'background': co6, 'foreground': '#ffffff', 'overrelief': 'ridge'}

        self.botao_login = Button(self.frame_botoes, text='Login', command=self.verificar_login, **botao_estilo)
        self.botao_login.grid(row=0, column=0, padx=5)

        self.botao_registo = Button(self.frame_botoes, text='Registar', command=self.abrir_janela_registo,
                                     **botao_estilo)

        self.botao_registo.grid(row=0, column=1, padx=5)

        self.janela_login.mainloop()

    def verificar_login(self):
        username = self.e_username.get()
        pin = self.e_pin.get()

        if username and pin:
            if self.datab_u_instance.verificar_credenciais(username, pin):
                self.janela_login.destroy()
                self.iniciar_app_principal()
            else:
                messagebox.showerror('Erro', 'Credenciais inválidas. Tente novamente.')
                self.janela_login.lift()
        else:
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
            self.janela_login.lift()

    def abrir_janela_registo(self):
        self.janela_registo = Toplevel(self.janela_login)
        self.janela_registo.title('Registar - Orçamento Familiar')
        self.janela_registo.geometry('330x200')
        self.janela_registo.configure(background=co1)
        self.janela_registo.resizable(width=False, height=False)

        #CONFIGURAÇÃO DOS ELEMENTOS DA JANELA DE REGISTO
        self.l_username_registo = Label(self.janela_registo, text='Novo Username:', font=('Verdana', 10, 'bold'), background=co1)
        self.l_username_registo.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.e_username_registo = Entry(self.janela_registo, font=('Verdana', 10))
        self.e_username_registo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.l_pin_registo = Label(self.janela_registo, text='Novo PIN:', font=('Verdana', 10, 'bold'), background=co1)
        self.l_pin_registo.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.e_pin_registo = Entry(self.janela_registo, show='*', font=('Verdana', 10))
        self.e_pin_registo.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.l_confirmar_pin_registo = Label(self.janela_registo, text='Confirmar PIN:', font=('Verdana', 10, 'bold'), background=co1)
        self.l_confirmar_pin_registo.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.e_confirmar_pin_registo = Entry(self.janela_registo, show='*', font=('Verdana', 10))
        self.e_confirmar_pin_registo.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.frame_botoes_registo = Frame(self.janela_registo, background=co1)            
        self.frame_botoes_registo.grid(row=3, column=0, columnspan=2, pady=10)

        botao_registo_estilo = {'font': ('Verdana', 10, 'bold'), 'background': co6, 'foreground': '#ffffff', 'overrelief': 'ridge'}

        self.botao_confirmar_registo = Button(self.frame_botoes_registo, text='Confirmar Registo', command=self.confirmar_registo, **botao_registo_estilo)
        self.botao_confirmar_registo.grid(row=0, column=0, padx=5)

        self.botao_voltar_login = Button(self.frame_botoes_registo, text='Voltar para Login', command=self.voltar_para_login, **botao_registo_estilo)
        self.botao_voltar_login.grid(row=0, column=1, padx=5)

    def confirmar_registo(self):
        username = self.e_username_registo.get()
        pin = self.e_pin_registo.get()
        confirmar_pin = self.e_confirmar_pin_registo.get()

        if username and pin and confirmar_pin:
            if pin == confirmar_pin:
                self.datab_u_instance.adicionar_utilizador(username, pin)
                messagebox.showinfo('Sucesso', 'Usuário registrado com sucesso.')
                self.janela_registo.destroy()
            else:
                messagebox.showerror('Erro', 'Os PINs não coincidem. Tente novamente.')
        else:
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')

    def voltar_para_login(self):
        self.janela_registo.destroy()

    def iniciar_app_principal(self):
        with open('feedback.txt', 'w'):
            pass
        app = OrcamentoFamiliarApp()



class OrcamentoFamiliarApp:
    def __init__(self):
        self.vis_instance = Visualizar()
        self.datab_instance = DataB('dados.db')
        self.exportador = ExportarDados(self.vis_instance)

        self.janela = Tk()
        self.janela.title('Orçamento Familiar')
        self.janela.geometry('900x720')  # largura x comprimento
        self.janela.configure(background=co9)
        self.janela.resizable(width=False, height=False)

        style = ttk.Style(self.janela)
        style.theme_use("clam")

        #CRIAR FRAMES DIVISORES DA TELA
        self.frameC = Frame(self.janela, width=1043, height=50, background=co1, relief="flat")
        self.frameC.grid(row=0, column=0)

        self.frameM = Frame(self.janela, width=1043, height=361, background=co1, pady=20, relief="raised")
        self.frameM.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.frameB = Frame(self.janela, width=1043, height=300, background=co1, relief="flat")
        self.frameB.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

        self.frameBB = Frame(self.janela, width=1043, height=70, background=co1, relief="flat")
        self.frameBB.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

        #ACEDER IMG
        app_img = Image.open('logo.png')
        app_img = app_img.resize((40, 30))
        app_img = ImageTk.PhotoImage(app_img)

        #ADD LOGO A LABEL
        app_logo = Label(self.frameC, image=app_img, text="  Orçamento Familiar", width=900, compound=LEFT, padx=5,
                         relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
        app_logo.place(x=0, y=0)

        #FRAMES DENTRO DO FRAME BAIXO
        #FRAME TABEL
        self.frame_tabela = Frame(self.frameB, width=220, height=250, background=co1)
        self.frame_tabela.grid(row=0, column=0)

        #FRAME DESPESAS
        self.frame_des = Frame(self.frameB, width=220, height=250, background=co1)
        self.frame_des.grid(row=0, column=1, padx=5)

        #FRAME RECEITAS
        self.frame_rec = Frame(self.frameB, width=300, height=250, background=co1)
        self.frame_rec.grid(row=0, column=2, padx=5)

        #FRAME GRAF CIRCULAR
        self.frame_graf_cir = Frame(self.frameM, width=500, height=250, background=co1)
        self.frame_graf_cir.place(x=415, y=5)

        #CONFIGURAÇÃO DE WIDGETS (BOTÕES, ENTRADAS, LABELS, etc.)

        #CONFIGURAÇÃO DE DESPESAS
        self.l_despesas = Label(self.frame_des, text='Insira a despesa:', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1,
                           fg=co4)
        self.l_despesas.place(x=10, y=10)

        #LABEL CATEGORIA
        l_categoria = Label(self.frame_des, text='Categoria:', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_categoria.place(x=10, y=40)

        #OBTER CATEGORIA
        categoria_d = self.datab_instance.ver_categoria()
        categoria = []

        for i in categoria_d:
            categoria.append(i[1])

        self.comb_categoria_despesa = ttk.Combobox(self.frame_des, width=10, font=('Ivy 10'))
        self.comb_categoria_despesa['values'] = (categoria)
        self.comb_categoria_despesa.place(x=110, y=41)

        #LABEL DATA DESPESA
        self.l_data = Label(self.frame_des, text='Data:', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_data.place(x=10, y=70)

        #CALENDARIO
        self.e_calendario_des = DateEntry(self.frame_des, width=12, background='darkblue', foreground='white', borderwidth=2,
                                     year=2024)
        self.e_calendario_des.place(x=110, y=71)
        # e = entry

        #LABEL QUANTIA DESPESA
        self.l_quantia_des = Label(self.frame_des, text='Quantia:', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_quantia_des.place(x=10, y=100)

        #ENTRADA VALOR
        self.e_quantia_des = Entry(self.frame_des, width=14, justify='left', relief='solid')
        self.e_quantia_des.place(x=110, y=101)

        #BOTAO ADD DESPESA
        #ACEDER IMAGEM
        add_img_des = Image.open('add.png')
        add_img_des = add_img_des.resize((17, 17))
        add_img_des = ImageTk.PhotoImage(add_img_des)

        self.botao_add_des = Button(self.frame_des, image=add_img_des, command=self.inserir_despesas_b, text=" Adicionar".upper(),
                               width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0,
                               overrelief=RIDGE)
        self.botao_add_des.place(x=110, y=131)

        #LABEL ELIMINAR
        self.l_eliminar = Label(self.frame_des, text='Eliminar', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.l_eliminar.place(x=10, y=190)

        #BOTAO ELIMINAR DESPESA
        #ACEDER IMAGEM
        del_img = Image.open('del.png')
        del_img = del_img.resize((17, 17))
        del_img = ImageTk.PhotoImage(del_img)

        self.botao_del = Button(self.frame_des, image=del_img, command=self.eliminar_dados, text=" Eliminar".upper(), width=80,
                           compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
        self.botao_del.place(x=110, y=190)

        # BOTAO FEEDBACK---------------------------------------------------------

        self.botao_feed = Button(self.frameBB, command=self.abrir_janela_feedback, text=" Feedback", width=10,
                                 compound=RIGHT, anchor=NW, font=('Ivy 10 bold'), bg=but, fg=co0,
                                 overrelief=RIDGE)
        self.botao_feed.place(x=760, y=10)
        #----------------------------------------------------------------------

        # BOTAO EXPORT---------------------------------------------------------
        botao_exportar = Button(self.frameBB, text="Exportar Dados", command=self.exportador.exportar_dados_excel,
                                font=('Ivy 10 bold'), bg=but, fg=co0, overrelief=RIDGE)
        botao_exportar.place(x=620, y=10)
        # -----------------------------------------------------------------------

        # BOTAO PESQUISA-------------------------------------------------------------

        self.entry_pesquisa = Entry(self.frameBB, width=12, font=('Verdana', 10), relief='solid')
        self.entry_pesquisa.place(x=100, y=14)

        # Adicione um botão para acionar a pesquisa
        botao_pesquisa = Button(self.frameBB, text="Pesquisar", command=self.exibir_resultados_pesquisa,
                                font=('Ivy 10 bold'),
                                bg=but, fg=co0, overrelief=RIDGE)
        botao_pesquisa.place(x=10, y=10)
        #----------------------------------------------------------------------

        #CONFIGURACAO DE RECEITAS
        self.l_receitas = Label(self.frame_rec, text='Insira a receita:', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1,
                           fg=co4)
        self.l_receitas.place(x=10, y=10)

        #LABEL DATA RECEITAS
        self.l_data_rec = Label(self.frame_rec, text='Data:', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_data_rec.place(x=10, y=40)

        #CALENDARIO
        self.e_calendario_rec = DateEntry(self.frame_rec, width=12, background='darkblue', foreground='white', borderwidth=2,
                                     year=2024)
        self.e_calendario_rec.place(x=110, y=41)

        #ÇABEL QUANTIA RECEITA
        self.l_quantia_rec = Label(self.frame_rec, text='Quantia:', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_quantia_rec.place(x=10, y=70)

        #ENTRADA DO VALOR
        self.e_quantia_rec = Entry(self.frame_rec, width=14, justify='left', relief='solid')
        self.e_quantia_rec.place(x=110, y=71)

        #ACEDER A IMAGEM
        add_img_rec = Image.open('add.png')
        add_img_rec = add_img_rec.resize((17, 17))
        add_img_rec = ImageTk.PhotoImage(add_img_rec)

        #BOTAO ADD RECEITA
        self.botao_add_rec = Button(self.frame_rec, image=add_img_rec, command=self.inserir_receitas_b, text=" Adicionar".upper(),
                               width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0,
                               overrelief=RIDGE)
        self.botao_add_rec.place(x=110, y=111)

        #CONFIGURACAO ADD CATEGORIA
        self.l_categoria = Label(self.frame_rec, text='Categoria:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.l_categoria.place(x=10, y=160)

        #ENTRADA DA CATEGORIA
        self.e_categoria_rec = Entry(self.frame_rec, width=14, justify='left', relief='solid')
        self.e_categoria_rec.place(x=110, y=160)

        #ACEDER A IMAGEM
        add_img_cat = Image.open('add.png')
        add_img_cat = add_img_cat.resize((17, 17))
        add_img_cat = ImageTk.PhotoImage(add_img_cat)

        #BOTAO ADD CATEGORIA
        self.botao_add_cat = Button(self.frame_rec, command=self.inserir_categoria_b, image=add_img_cat, text=" Adicionar".upper(),
                               width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0,
                               overrelief=RIDGE)
        self.botao_add_cat.place(x=110, y=190)

        self.percentagem()
        self.grafico_bar()
        self.resumo()
        self.grafico_cir()
        self.tabela_b()
        self.janela.mainloop()


    #FUNÇÃO PARA INSERIR CATEGORIA
    def inserir_categoria_b(self):
        nome = self.e_categoria_rec.get()

        lista_inserir = [nome]

        for i in lista_inserir:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        #PASSA A LISTA PARA A FUNÇÃO INSERIR_CATEGORIAS NO VIS.PY
        self.datab_instance.inserir_categoria(lista_inserir)

        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

        self.e_categoria_rec.delete(0, 'end')

        #PEGA NOS VALORES DA CATEGORIA
        categorias_funcao = self.datab_instance.ver_categoria()
        categoria = []

        for i in categorias_funcao:
            categoria.append(i[1])

        #ATUALIZAR LISTA DE CATEGORIAS
        self.comb_categoria_despesa['values'] = (categoria)

    #FUNÇÃO PARA INSERIR RECEITAS
    def inserir_receitas_b(self):
        nome = 'Receita'
        data = self.e_calendario_rec.get()
        quantia = self.e_quantia_rec.get()

        lista_inserir = [nome, data, quantia]

        for i in lista_inserir:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        #PASSA A LISTA PARA A FUNÇÃO INSERIR_RECEITAS NO DATA_BASE.PY
        self.datab_instance.inserir_receitas(lista_inserir)

        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

        self.e_calendario_rec.delete(0, 'end')
        self.e_quantia_rec.delete(0, 'end')

        #ATUALIZAR DADOS
        self.tabela_b()
        self.percentagem()
        self.grafico_bar()
        self.resumo()
        self.grafico_cir()

    #FUNÇÃO PARA INSERIR DESPESAS
    def inserir_despesas_b(self):
        nome = self.comb_categoria_despesa.get()
        data = self.e_calendario_des.get()
        quantia = self.e_quantia_des.get()

        lista_inserir = [nome, data, quantia]

        for i in lista_inserir:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        #PASSA A LISTA PARA A FUNÇÃO INSERIR_DESPESAS NO DATA_BASE.PY
        self.datab_instance.inserir_despesas(lista_inserir)

        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

        self.comb_categoria_despesa.delete(0, 'end')
        self.e_calendario_des.delete(0, 'end')
        self.e_quantia_des.delete(0, 'end')

        #ATUALIZAR DADOS
        self.tabela_b()
        self.percentagem()
        self.grafico_bar()
        self.resumo()
        self.grafico_cir()

    #FUNÇÃO PARA ELIMINAR DADOS
    def eliminar_dados(self):
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0]
            nome = treev_lista[1]

            if nome == 'Receita':
                self.datab_instance.eliminar_receitas([valor])
                messagebox.showinfo('Sucesso', 'Dados eliminados com sucesso')

                #ATUALIZAR DADOS
                self.tabela_b()
                self.percentagem()
                self.grafico_bar()
                self.resumo()
                self.grafico_cir()
            else:
                self.datab_instance.eliminar_despesas([valor])
                messagebox.showinfo('Sucesso', 'Dados eliminados com sucesso')

                #ATUALIZAR DADOS
                self.tabela_b()
                self.percentagem()
                self.grafico_bar()
                self.resumo()
                self.grafico_cir()

        except IndexError:
            messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


    #PERCENTAGEM (BARRA)
    def percentagem(self):
        l_nome = Label(self.frameM, text="Percentagem da Receita Restante", height=1, anchor=NW, font=('Verdana 12'),
                       bg=co1, fg=co4)
        l_nome.place(x=7, y=5)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='#daed6b')
        style.configure("Tprogressbar", thickness=25)

        bar = Progressbar(self.frameM, length=180, style='black.Horizontal.TProgressbar')
        bar.place(x=10, y=35)
        bar['value'] = self.vis_instance.per_valores()[0]

        valor = self.vis_instance.per_valores()[0]

        l_percentagem = Label(self.frameM, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1,
                              fg=co4)
        l_percentagem.place(x=200, y=35)

    # Gráfico barras
    def grafico_bar(self):
        lista_cat = ['Receitas', 'Despesas', 'Saldo']
        lista_val = self.vis_instance.bar_valores()

        #FAZER A FIGURA E ATRIBUIR OBJETOS DO EIXO
        figura = plt.Figure(figsize=(4, 3.45), dpi=60)
        ax = figura.add_subplot(111)

        ax.bar(lista_cat, lista_val, color=colors, width=0.9)

        c = 0

        #BARRAS INDIVIDUAIS
        for i in ax.patches:
            ax.text(i.get_x() - .001, i.get_height() + .5, str("{:,.0f}".format(lista_val[c])), fontsize=17,
                    fontstyle='italic', verticalalignment='bottom', color='dimgrey')
            c += 1

        ax.set_xticklabels(lista_cat, fontsize=12)

        ax.patch.set_facecolor('#ffffff')
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['right'].set_linewidth(0)
        ax.spines['top'].set_linewidth(0)
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['left'].set_linewidth(1)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(False, color='#EEEEEE')
        ax.xaxis.grid(False)

        canva = FigureCanvasTkAgg(figura, self.frameM)
        canva.get_tk_widget().place(x=10, y=70)

    #RESUMO
    def resumo(self):
        valor = self.vis_instance.bar_valores()

        #LINHA
        l_linha = Label(self.frameM, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=52)
        l_sumario = Label(self.frameM, text="Total Orçamento Mensal".upper(), anchor=NW, font=('Verdana 11'), bg=co1,
                          fg='#83a9e6')
        l_sumario.place(x=309, y=35)
        l_sumario = Label(self.frameM, text="{:,.2f}€".format(valor[0]), anchor=NW, font=('Arial 15'), bg=co1, fg='#545454')
        l_sumario.place(x=309, y=70)

        #LINHA
        l_linha = Label(self.frameM, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=132)
        l_sumario = Label(self.frameM, text="Total Despesas Mensais   ".upper(), anchor=NW, font=('Verdana 11'), bg=co1,
                          fg='#83a9e6')
        l_sumario.place(x=309, y=115)
        l_sumario = Label(self.frameM, text="{:,.2f}€".format(valor[1]), anchor=NW, font=('Arial 15'), bg=co1, fg='#545454')
        l_sumario.place(x=309, y=150)

        #LINHA
        l_linha = Label(self.frameM, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
        l_linha.place(x=309, y=207)
        l_sumario = Label(self.frameM, text="Total Saldo                       ".upper(), anchor=NW, font=('Verdana 11'),
                          bg=co1, fg='#83a9e6')
        l_sumario.place(x=309, y=190)
        l_sumario = Label(self.frameM, text="{:,.2f}€".format(valor[2]), anchor=NW, font=('Arial 15'), bg=co1, fg='#545454')
        l_sumario.place(x=309, y=220)

    #GRÁFICO CIRCULAR
    def grafico_cir(self):
        #FIGURA E ATRIBUIR EIXO
        figura = plt.Figure(figsize=(5, 3), dpi=90)
        ax = figura.add_subplot(111)

        lista_valores = self.vis_instance.cir_valores()[1]
        lista_categorias = self.vis_instance.cir_valores()[0]

        explode = []
        for i in lista_categorias:
            explode.append(0.05)

        ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,
               shadow=True, startangle=90)

        ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

        canva_categoria = FigureCanvasTkAgg(figura, self.frame_graf_cir)
        canva_categoria.get_tk_widget().grid(row=0, column=0)

    #FUNÇÃO PARA A TABELA
    def tabela_b(self):
        #TITULOS
        tabela_cabeçalho = ['Id', 'Categoria', 'Data', 'Quantia']

        #DADOS INSERIDOS NA TABELA ['Id','Categoria', 'Data', 'Quantia'] (exemplo)
        #UMA LISTA DE LISTAS E CADA LISTA TEM 4 VALORES
        lista_itens = self.vis_instance.tabela()

        #TORNAR TREE GLOBAL POIS VAMOS USAR DENTRO DE OUTRAS FUNÇÕES
        global tree

        tree = ttk.Treeview(self.frame_tabela, selectmode="extended", columns=tabela_cabeçalho, show="headings")
        #SCROLL VERTICAL
        vsb = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=tree.yview)
        #SCROLL HORIZONTAL
        hsb = ttk.Scrollbar(self.frame_tabela, orient="horizontal", command=tree.xview)
        #SCROLL
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        #PSOCIONAR TABELA
        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        hsb.grid(column=0, row=1, sticky="ew")

        #ORGANIZAÇÃO DA TABELA
        hd = ["center", "center", "center", "center"]  # Centralizar valores
        h = [30, 100, 100, 100]  # Tamanhos das colunas
        n = 0

        for col in tabela_cabeçalho:
            tree.heading(col, text=col.title(), anchor=CENTER)
            #AJUSTAR LARGURA DAS COLUNAS COM O CABEÇALHO DA TABELA
            tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        #INSERIR VALORES NA TABELA
        for item in lista_itens:
            tree.insert('', 'end', values=item)

    def abrir_janela_feedback(self):
        feedback_app = Feedback(Tk())
        feedback_app.mainloop()

    #PESQUISAR DADOS NA DB
    def exibir_resultados_pesquisa(self):
        termo_pesquisa = self.entry_pesquisa.get()
        resultados = self.datab_instance.pesquisar_dados(termo_pesquisa)

        #CRIA A JANELA POP-UP
        janela_resultados = Toplevel(self.janela)
        janela_resultados.title("Resultados da Pesquisa")

        #LISTA PARA MOSTRAR RESULTADOS NA JANELA
        lista_resultados_pesquisa = Listbox(janela_resultados, width=50, height=10)
        lista_resultados_pesquisa.pack(padx=10, pady=10)

        for resultado in resultados:
            lista_resultados_pesquisa.insert("end", str(resultado))

if __name__ == "__main__":
    login_app = LoginApp()
