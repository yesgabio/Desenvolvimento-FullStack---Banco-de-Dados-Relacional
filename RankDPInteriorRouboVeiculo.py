import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine('sqllite:///BD//ocorrencias.db')
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

'''
• Suponha que o Delegado da Delegacia de Roubos e Furtos de Veículos tenha te solicitado uma
análise relacionada ao ranqueamento de todas as DPs, através da quantidade total de
ocorrências relacionadas a Roubo e furto de Veículos, no Interior do Estado do RJ (é preciso
verificar como o dado está cadastrado na tabela, para realizar o filtro!!!!).
• O resultado desse ranqueamento deve ser enviado em uma tabela, contendo as seguintes
colunas: DP e Total
'''

RankDP = pd.DataFrame(
            sessao.query(
                oc.delegacia.nome.label('DP'),
                sa.func.sum(oc.ocorrencia.qtde).label('Total')
            ).join(
                oc.ocorrencia,
                oc.ocorrencia.codDP == oc.delegacia.codDP
            ).join(
                oc.municipio,
                oc.ocorrencia.codIBGE == oc.municipio.codIBGE
            ).where(
                oc.municipio.regiao == "interior",
                sa.or_(oc.ocorrencia.ocorrencias == "roubo_veiculo", oc.ocorrencia.ocorrencias == "furto_veiculo")
            ).group_by(
                oc.delegacia.nome
            ).order_by(
                sa.func.sum(oc.ocorrencia.qtde).label('Total').desc()
            ).all()
        )
print(RankDP)