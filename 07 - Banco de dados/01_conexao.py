import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "MEU_BANCO.db")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


def inserir_registro(conexao, cursor, nome, email):
    data = (nome,email)
    cursor.execute('INSERT INTO cliente(nome, email) VALUES(?,?);',data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome,email,id)
    cursor.execute('UPDATE cliente SET nome=?, email=? WHERE id=?', data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM cliente WHERE id=?', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO cliente (nome,email) VALUES (?,?)', dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM cliente WHERE ID=?', (id,))
    resultado = cursor.fetchone()
    return resultado

def visualizar_clientes(cursor):
    return cursor.execute("SELECT * FROM cliente ORDER BY nome;")


clientes = visualizar_clientes(cursor)
for cliente in clientes:
    print(cliente)


