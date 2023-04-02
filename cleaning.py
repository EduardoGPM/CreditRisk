import pandas as pd


df = pd.read_csv(
    'C:/projetos/AnaliseDeCredito/credito.csv', na_values='na')


df[df['default'] == 0].shape

df[df['default'] == 1].shape

qtd_total, _ = df.shape
qtd_adimplentes, _ = df[df['default'] == 0].shape
qtd_inadimplentes, _ = df[df['default'] == 1].shape


# Schema
# Colunas e seus respectivos tipos de dados

df.dtypes

# Atributos categóricos

df.select_dtypes('object').describe().transpose()

# Atributos numéricos

df.drop('id', axis=1).select_dtypes('number').describe().transpose()

# verificar quais colunas possuem dados faltantes

df.isna().any()

# A função abaixo levanta algumas estatisticas sobre as colunas dos dados faltantes


def stats_dados_faltantes(df: pd.DataFrame) -> None:

    stats_dados_faltantes = []
    for col in df.columns:
        if df[col].isna().any():
            qtd, _ = df[df[col].isna()].shape
            total, _ = df.shape
            dict_dados_faltantes = {
                col: {'quantidade': qtd, "porcentagem": round(100 * qtd/total, 2)}}
            stats_dados_faltantes.append(dict_dados_faltantes)

    # for stat in stats_dados_faltantes:
    #     print(stat)


stats_dados_faltantes(df=df)

stats_dados_faltantes(df=df[df['default'] == 0])

stats_dados_faltantes(df=df[df['default'] == 1])


# Correção de schema
# testando função `lambda` para limpar os dados

def fn(valor): return float(valor.replace(".", "").replace(",", "."))


valores_originais = ['12.691,51', '8.256,96',
                     '3.418,56', '3.313,03', '4.716,22']
valores_limpos = list(map(fn, valores_originais))


# Aplicando nos dados

df['valor_transacoes_12m'] = df['valor_transacoes_12m'].apply(fn)
df['limite_credito'] = df['limite_credito'].apply(fn)

# Remoção de dados faltantes

df.dropna(inplace=True)

qtd_total_novo, _ = df.shape
qtd_adimplentes_novo, _ = df[df['default'] == 0].shape
qtd_inadimplentes_novo, _ = df[df['default'] == 1].shape

# Os dados estão prontos, vamos criar diversas visualizações para correlacionar variáveis explicativas com a variável resposta para buscar entender qual fator leva um cliente a inadimplencia
classes = [0.00, 2000.00, 4000.00, 6000.00, 8000.00,
           10000.00, 12000.00, 14000.00, 16000.00, 18000.00]
labels = ["K", "H", 'G', 'F', 'E', 'D', 'C', 'B', 'A']

classes = pd.cut(x=df.valor_transacoes_12m, bins=classes, labels=labels)
df['valor_transacoes_12m_classe'] = classes


classes = [0, 20, 40, 60, 80, 100, 120, 140]
labels = ['G', 'F', 'E', 'D', 'C', 'B', 'A']

classes = pd.cut(x=df.qtd_transacoes_12m, bins=classes, labels=labels)

df['qtd_transacoes_12m_classe'] = classes

df.head()
