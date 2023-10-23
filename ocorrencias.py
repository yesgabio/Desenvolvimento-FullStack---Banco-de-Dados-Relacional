import sqlalchemy as sa

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

import sqlalchemy.orm as orm

base = orm.declarative_base()

#Tabela delegacia
class delegacia(base):
    __tablename__ = 'delegacia'
    
    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(255), nullable=False)
    
#Tabela responsavel
class responsavel(base):
    __tablename__ = 'responsavel'
    
    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)
    
#Tabela municipio
class municipio(base):
    __tablename__ = 'municipio'
    
    codIBGE = sa.Column(sa.INTEGER, primary_key=True, index=True)
    municipio = sa.Column(sa.VARCHAR(100), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)
    
#Tabela ocorrencias
class ocorrencias(base):
    __tablename__ = 'ocorrencias'
    
    idRegistro = sa.Column(sa.INTEGER, primary_key=True, index=True)
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey('delegacia.codDP', ondelete="NO ACTION", onupdate="CASCADE"))
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey('municipio.codIBGE', ondelete="NO ACTION", onupdate="CASCADE"))
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.CHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.INTEGER, nullable=False)
    
try:
    base.metadata.create_all(engine) #criar as tabelas
    print("Tabelas ok!")
except ValueError:
    ValueError()  
    