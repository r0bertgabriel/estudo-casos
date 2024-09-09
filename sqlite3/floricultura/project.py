#%% imports
import sqlite3 as con
#%%
# Criar tabelas
sql_clientes = """
CREATE TABLE IF NOT EXISTS Cliente (
ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
RG VARCHAR(12) NOT NULL,
Nome_Cliente VARCHAR(30) NOT NULL,
Sobrenome_CLiente VARCHAR(40) NOT NULL,
Telefone VARCHAR(12),
Rua VARCHAR(40),
Numero VarChar(5),
Bairro VARCHAR(25)
);

"""

sql_produtos = """
CREATE TABLE IF NOT EXISTS Produto (
ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
Nome_Produto VARCHAR(30) NOT NULL,
Tipo_Produto VARCHAR(25) NOT NULL,
Preco DECIMAL(10,2) NOT NULL,
Qtde_Estoque SMALLINT NOT NULL
);
"""

sql_vendas = """
CREATE TABLE IF NOT EXISTS Venda (
ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
Nota_Fiscal SMALLINT NOT NULL,
ID_Cliente INTEGER NOT NULL,
Data_Compra DATETIME,
ID_Produto INTEGER NOT NULL,
Quantidade SMALLINT NOT NULL,
FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
FOREIGN KEY (ID_Produto) REFERENCES Produto(ID_Produto)
);
"""

#%%
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no Banco de dados", erro)
finally:
    if conexao:
        conexao.close()

# %% para verificarr se tabelas foram criadas
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    res = cursor.execute("SELECT name from sqlite_master")
    print(res.fetchall())
except con.DatabaseError as erro:
    print("Erro no Banco de dados", erro)
finally:
    if conexao:
        conexao.close()
# %% INSERINDO dados na tabela Cliente
insert_cliente = """
INSERT INTO Cliente (RG, Nome_Cliente, Sobrenome_CLiente, Telefone, Rua, Numero, Bairro)
VALUES
('123456789', 'João', 'Silva', '123456789', 'Rua 1', '123', 'Centro'),
('987654321', 'Maria', 'Santos', '987654321', 'Rua 2', '456', 'Bela Vista')

"""
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(insert_cliente)

    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no Banco de dados", erro)
else:
    #verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Cliente;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()

# %% inserir dados na tabela Produtos
insert_produto = """
INSERT INTO Produto (Nome_Produto, Tipo_Produto, Preco, Qtde_Estoque)
VALUES
('Rosa', 'Flor', 10.00, 100),
('Girassol', 'Flor', 5.00, 50),
('Violeta', 'Flor', 3.00, 200),
('Vaso', 'Acessorio', 20.00, 30),
('Orquidea', 'Flor', 15.00, 80)

"""
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    conexao.execute(insert_produto)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no Banco de dados", erro)
else:
    # verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Produto;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()

# %% inserir dados na tabela Vendas
insert_venda = """
INSERT INTO Venda(Nota_Fiscal, ID_Cliente, Data_Compra, ID_Produto, Quantidade)
VALUES
(123, 1, '2021-09-01', 1, 10),
(124, 2, '2021-09-02', 2, 5),
(125, 1, '2021-09-03', 3, 20),
(126, 2, '2021-09-04', 4, 2),
(127, 1, '2021-09-05', 5, 10)
"""

try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(insert_venda)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no Banco de dados", erro)
else: # verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Venda;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()

# %%
