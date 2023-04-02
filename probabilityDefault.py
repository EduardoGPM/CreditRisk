from cleaning import df
import numpy as np

dependentes = 0
sexo = "M"
estado_civil = "solteiro"
escolaridade = "mestrado"
salario_anual = "$80K - $120K"
tipo_cartao = "silver"
qtd_produtos = 3
valor_transacoes_12m_classe = "K"
qtd_transacoes_12m_classe = "E"

probabilistic_var = {
    "dependentes": dependentes,
    "sexo": sexo,
    "estado_civil": estado_civil,
    "escolaridade": escolaridade,
    "salario_anual": salario_anual,
    "tipo_cartao": tipo_cartao,
    "qtd_produtos": qtd_produtos,
    "valor_transacoes_12m_classe": valor_transacoes_12m_classe,
    "qtd_transacoes_12m_classe": qtd_transacoes_12m_classe


}
# def find(x, var):


keys = list(probabilistic_var)

statistical_var = []
# (df[key] == 2)
for var in keys:
    value_defaulted = df.loc[(df[var] == probabilistic_var[var])
                             & ((df["default"] == 1))].count()[var]
    value_undefaulted = df.loc[(df[var] == probabilistic_var[var])
                               & ((df["default"] == 0))].count()[var]

    item = {
        var: {
            "defaulted": value_defaulted,
            "undefaulted": value_undefaulted,
        }
    }
    statistical_var.append(item)

index = 0
item_undefaulted_list = []
for item in statistical_var:
    key = keys[index]
    formattedItem = item[key]
    item_undefaulted = (formattedItem['undefaulted'] /
                        (formattedItem['undefaulted']+formattedItem['defaulted']))*100
    item_undefaulted_list.append(item_undefaulted)
    index += 1

probabilistic_undefaulted = np.mean(item_undefaulted_list)


print(probabilistic_undefaulted)

# print(formattedItem)
