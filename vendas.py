import sqlalchemy as sa

engine = sa.create_engine("sqlite:///BD//vendas.db")

import sqlalchemy.orm as orm

base = orm.declarative_base()

#Tabela cliente
class cliente(base):
    __tablename__ = 'cliente'
    
    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))
    
#Tabela fornecedor
class fornecedor(base):
    __tablename__ = 'fornecedor'
    
    registro_fornecedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50), nullable=False)
    uf = sa.Column(sa.CHAR(2), nullable=False)
    
#Tabela produto
class produto(base):
    __tablename__ = 'produto'
    
    codBarras = sa.Column(sa.INTEGER, primary_key = True, index = True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey('fornecedor.registro_fornecedor', ondelete="NO ACTION", onupdate="CASCADE"))
    dscproduto = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    
#Tabela vendedor
class vendedor(base):
    __tablename__ = 'vendedor'
    
    registro_vendedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    
#Tabela vendas
class vendas(base):
    __tablename__ = 'vendas'
    
    idTransacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("cliente.cpf", ondelete="NO ACTION", onupdate="CASCADE"))
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("vendedor.registro_vendedor", ondelete="NO ACTION",onupdate="CASCADE"))
    codBarras = sa.Column(sa.INTEGER, sa.ForeignKey("produto.codBarras", ondelete="NO ACTION",onupdate="CASCADE"))
    
try:
    base.metadata.create_all(engine) #criar as tabelas
    print("Tabelas ok!")
except ValueError:
    ValueError()