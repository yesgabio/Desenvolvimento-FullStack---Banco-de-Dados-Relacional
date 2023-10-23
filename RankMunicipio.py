import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine('sqllite:///BD//ocorrencias.db')
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

'''
Suponha que o Governador do Estado do RJ tenha te ligado e solicitado uma análise
relacionada ao ranqueamento de todos os municípios, através da quantidade total de
ocorrências relacionadas a Roubo de Veículos (é preciso verificar como o dado está cadastrado
na tabela, para realizar o filtro!!!!)
'''

RankMunic = pd.DataFrame(
                sessao.query(
                oc.municipio.municipio.label("Município"),
                sa.func.sum(oc.ocorrencia.qtde).label("Total")
                ).join(
                    oc.ocorrencia,
                    oc.ocorrencia.codIBGE == oc.municipio.codIBGE
                ).where(
                    oc.ocorrencia.ocorrencias == "roubo_veiculo"
                ).group_by(
                    oc.municipio.municipio
                ).order_by(
                    sa.func.sum(oc.ocorrencia.qtde).desc()
                ).all()
            )
print (RankMunic)