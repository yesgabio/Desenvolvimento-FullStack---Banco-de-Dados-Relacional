import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

endereco = "C:\\Users\\olive\\Dropbox\\PC\\Downloads\\BD_Ocorrencias\\"

delegacia = pd.read_csv(endereco + "DP.csv", sep=",")
responsavel = pd.read_excel(endereco + "ResponsavelDP.xlsx")
municipio = pd.read_csv(endereco + "Municipio.csv",sep=",")
ocorrencias = pd.read_excel(endereco + "ocorrencias.xlsx")

delegacia = pd.DataFrame(delegacia)
responsavel = pd.DataFrame(responsavel)
municipio = pd.DataFrame(municipio)
ocorrencias = pd.DataFrame(ocorrencias)

engine = sa.create_engine("sqlite:///BD//Ocorrencias.db")

conn = engine.connect()

metadata = sa.schema.MetaData(bind=engine)

Sessao = orm.sessionmaker(bind=engine) 
sessao = Sessao()

DadosDP = delegacia.to_dict(orient='records')
delegacia = sa.Table(oc.dp.__tablename__, metadata, autoload=True)

try:
    conn.execute(delegacia.insert(), DadosDP)
    sessao.commit()
except ValueError:
    print(ValueError())

print("Tabela Delegacias criada!")

DadosRespoDP = responsavel.to_dict(orient='records')

tabela_respDP = sa.Table(oc.responsavel.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_respDP.insert(), DadosRespoDP)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbResponsavelDP criada!")


DadosMunicipio = municipio.to_dict(orient='records')

tabela_municipio = sa.Table(oc.municipio.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

try:
    conn.execute(tabela_municipio.insert(), DadosMunicipio)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbMunicipio criada!")


DadosOcorrencias = ocorrencias.to_dict(orient='records')

tabela_ocorrencias = sa.Table(oc.ocorrencias.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_ocorrencias.insert(), DadosOcorrencias)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbOcorrencias criada!")

sessao.close_all()

print("Módulo de inserção de dados finalizado!")