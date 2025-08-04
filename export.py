import openpyxl
from openpyxl.styles import Alignment
from tkinter import messagebox
from data_base import DataB

class ExportarDados:
    def __init__(self, datab_instance):
        self.datab_instance = DataB('dados.db')

    def exportar_dados_excel(self, nome_arquivo='dados_exportados.xlsx'):
        try:
            dados_receitas = self.datab_instance.ver_receitas()
            dados_despesas = self.datab_instance.ver_despesas()

            #CRIA FICHEIRO EXCEL
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            #CABEÇALHO
            header = ['Categoria', 'Tipo', 'Data', 'Quantia']
            sheet.append(header)
            for cell in sheet[1]:
                cell.alignment = Alignment(horizontal='center')

            #ESCREVE DADOS DAS RECEITAS
            for receita in dados_receitas:
                linha = ['Receita', receita[1], receita[2], '{:.2f}€'.format(receita[3])]
                sheet.append(linha)

            #ESCREVE DADOS DAS DESPESAS
            for despesa in dados_despesas:
                linha = ['Despesa', despesa[1], despesa[2], '{:.2f}€'.format(despesa[3])]
                sheet.append(linha)

            #GUARDA ARQUIVO EXCEL
            workbook.save(nome_arquivo)

            messagebox.showinfo('Sucesso', 'Dados exportados com sucesso para {}'.format(nome_arquivo))
        except Exception as e:
            messagebox.showerror('Erro', 'Ocorreu um erro durante a exportação de dados: {}'.format(str(e)))