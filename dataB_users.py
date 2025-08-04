import sqlite3 as lite
import hashlib

class DataB_U:
    def __init__(self, nome):
        self.nome = nome
        self.con = lite.connect(nome)

        with self.con:
            try:
                self.cur = self.con.cursor()

                # Verificar se a tabela já existe
                self.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Utilizadores'")
                if self.cur.fetchone()[0] == 1:
                    print("A tabela 'Utilizadores' já existe.")
                    return

                # Criar a tabela se não existir
                self.cur.execute(
                    "CREATE TABLE IF NOT EXISTS Utilizadores (id INTEGER PRIMARY KEY, username TEXT, pin TEXT)")
                self.con.commit()
                print("Tabela 'Utilizadores' criada com sucesso.")

            except lite.Error as e:
                print(f"Erro ao criar a tabela 'Utilizadores': {e}")

    def criar_tabela_utilizadores(self, con):
        try:
            self.cur = con.cursor()

            # Verificar se a tabela já existe
            self.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Utilizadores'")
            if self.cur.fetchone()[0] == 1:
                print("A tabela 'Utilizadores' já existe.")
                return

            # Criar a tabela se não existir
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Utilizadores (id INTEGER PRIMARY KEY, username TEXT, pin TEXT)")
            con.commit()
            print("Tabela 'Utilizadores' criada com sucesso.")

        except lite.Error as e:
            print(f"Erro ao criar a tabela 'Utilizadores': {e}")

    def adicionar_utilizador(self, username, pin):
        hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
        try:
            self.cur = self.con.cursor()
            self.cur.execute("INSERT INTO Utilizadores (username, pin) VALUES (?, ?)", (username, hashed_pin))
            self.con.commit()
            print("User adicionado com sucesso.")
        except lite.Error as e:
            print(f"Erro ao adicionar user: {e}")

    def verificar_credenciais(self, username, pin):
        hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
        try:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM Utilizadores WHERE username=? AND pin=?", (username, hashed_pin))
            return self.cur.fetchone() is not None
        except lite.Error as e:
            print(f"Erro ao verificar credenciais: {e}")
            return False
