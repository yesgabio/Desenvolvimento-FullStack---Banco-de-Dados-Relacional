import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine('sqllite:///BD//ocorrencias.db')

metadado = sa.MetaData(bind=engine)
sa.MetaData.reflect(metadado)

tbMunicipio = metadado.tables[oc.municipio.__tablename__]

atualiza_regiao = sa.delete(tbMunicipio).where(
                                tbMunicipio.c.regiao == "Capital"
                            )
                            
try:
    engine.execute(atualiza_regiao)
    print("Dados deletados")
except ValueError:
    ValueError()