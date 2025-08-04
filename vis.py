import sqlite3 as lite
import pandas as pd
from data_base import DataB

class Visualizar:
    def __init__(self):
        #CONEXÃO
        self.con = lite.connect('dados.db')
        self.datab_instance = DataB('dados.db')
    
    #FUNÇÃO DADOS NA TABELA
    def tabela(self):
        despesas = self.datab_instance.ver_despesas()
        receitas = self.datab_instance.ver_receitas()

        tabela_lista = []

        for i in despesas:
            tabela_lista.append(i)

        for i in receitas:
            tabela_lista.append(i)

        return tabela_lista

    #FUNÇÃO GRÁFICO DE BARRAS
    def bar_valores(self):
        #RECEITA TOTAL
        receitas = self.datab_instance.ver_receitas()
        receitas_lista = []

        for i in receitas:
            receitas_lista.append(i[3])

        receitas_total = sum(receitas_lista)

        #DESPESA TOTAL
        despesas = self.datab_instance.ver_despesas()
        despesas_lista = []

        for i in despesas:
            despesas_lista.append(i[3])

        despesas_total = sum(despesas_lista)

        #SALDO
        saldo_total = receitas_total - despesas_total

        return [receitas_total, despesas_total, saldo_total]

    #FUNÇÃO GRÁFICO CIRCULAR
    def cir_valores(self):
        despesas = self.datab_instance.ver_despesas()

        tabela_lista = []

        for i in despesas:
            tabela_lista.append(i)

        dataframe = pd.DataFrame(tabela_lista, columns=['id', 'categoria', 'Data', 'valor'])

        dataframe = dataframe.groupby('categoria')['valor'].sum()

        lista_valores = dataframe.values.tolist()
        lista_categorias = []

        for i in dataframe.index:
            lista_categorias.append(i)

        return [lista_categorias, lista_valores]

    #BARRA DE PERCENTAGEM
    def per_valores(self):
        #RECEITA TOTAL
        receitas = self.datab_instance.ver_receitas()
        receitas_lista = []

        for i in receitas:
            receitas_lista.append(i[3])

        receitas_total = sum(receitas_lista)

        #DESPESA TOTAL
        despesas = self.datab_instance.ver_despesas()
        despesas_lista = []

        for i in despesas:
            despesas_lista.append(i[3])

        despesas_total = sum(despesas_lista)

        #CALCULA PERCENTAGEM, EXCEPÇÃO DIV POR 0
        total = 0 if receitas_total == 0 else ((receitas_total - despesas_total) / receitas_total) * 100

        return [total]