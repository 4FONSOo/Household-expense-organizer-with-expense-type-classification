import sqlite3 as lite


class DataB:
    def __init__(self, nome):
        self.nome = nome
        self.con = lite.connect(nome)

        #CRIAR TABELA CATEGORIA
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

        #CRIAR TABELA RECEITAS
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

        #CRIAR TABELA GASTOS
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

# -------------FUNÇÕES DE INSERÇÃO-------------

    #INSERIR CATEGORIA
    def inserir_categoria(self, i):
        with self.con:
            self.cur = self.con.cursor()
            self.query = "INSERT INTO Categoria (nome) VALUES (?)"
            self.cur.execute(self.query, i)

    #INSERIR RECEITAS
    def inserir_receitas(self, i):
        with self.con:
            self.cur = self.con.cursor()
            self.query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
            self.cur.execute(self.query, i)

    #INSERIR DESPESAS
    def inserir_despesas(self, i):
        with self.con:
            self.cur = self.con.cursor()
            self.query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
            self.cur.execute(self.query, i)

    # -------------FUNÇÕES DE ELIMINAÇÃO-------------

    #ELIMINAR RECEITAS
    def eliminar_receitas(self, i):
        with self.con:
            self.cur = self.con.cursor()
            self.query = "DELETE FROM Receitas WHERE id=?"
            self.cur.execute(self.query, i)

    #ELIMINAR DESPESAS
    def eliminar_despesas(self, i):
        with self.con:
            self.cur = self.con.cursor()
            self.query = "DELETE FROM Gastos WHERE id=?"
            self.cur.execute(self.query, i)

    # -------------FUNÇÕES PARA VER OS DADOS-------------

    #VER CATEGORIA
    def ver_categoria(self):
        lista_itens = []

        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM Categoria")
            linhas = self.cur.fetchall()
            for l in linhas:
                lista_itens.append(l)

        return lista_itens

    #VER RECEITAS
    def ver_receitas(self):
        lista_itens = []

        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM Receitas")
            linhas = self.cur.fetchall()
            for l in linhas:
                lista_itens.append(l)

        return lista_itens

    # VER DESPESAS
    def ver_despesas(self):
        lista_itens = []

        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM Gastos")
            linhas = self.cur.fetchall()
            for l in linhas:
                lista_itens.append(l)

        return lista_itens

    #PESQUISAR DADOS
    def pesquisar_dados(self, termo):
        resultados = []

        with self.con:
            self.cur = self.con.cursor()

            #PESQUISAR NA TABELA CATEGORIA
            self.cur.execute("SELECT * FROM Categoria WHERE nome LIKE ?", ('%' + termo + '%',))
            resultados.extend(self.cur.fetchall())

            #PESQUISAR NA TABELA RECEITAS
            self.cur.execute(
                "SELECT * FROM Receitas WHERE categoria LIKE ? OR adicionado_em LIKE ? OR valor LIKE ?",
                ('%' + termo + '%', '%' + termo + '%', '%' + termo + '%'))
            resultados.extend(self.cur.fetchall())

            #PESQUISAR NA TABELA GASTOS
            self.cur.execute("SELECT * FROM Gastos WHERE categoria LIKE ? OR retirado_em LIKE ? OR valor LIKE ?",
                             ('%' + termo + '%', '%' + termo + '%', '%' + termo + '%'))
            resultados.extend(self.cur.fetchall())

        return resultados