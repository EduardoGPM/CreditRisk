# CreditRisk

# Exploração de Dados

Os dados estão no formato CSV e
contém informações sobre clientes de uma instituição financeira. Em especial, estamos
interessados em explicar a segunda coluna, chamada de default, que indica se um cliente é
adimplente( default = 0 ), ou inadimplente ( default = 1 ), ou seja, queremos entender
o porque um cliente deixa de honrar com suas dívidas baseado no comportamento de outros
atributos, como salário, escolaridade e movimentação financeira. Uma descrição completa dos
atributos está abaixo.

O atributo de interesse ( default ) é conhecido como variável resposta ou
variável dependente, já os demais atributos que buscam explicá-la ( idade ,
salário , etc.) são conhecidas como variáveis explicatívas, variáveis
independentes ou até variáveis preditoras.

# Análise Estatística

Criamos um algoritmo que utiliza o conceito de classificadores probabilísticos "Naive Bayes", eu poderia ter utilizado a função Gaussian Naive Bayes com a ajuda da biblioteca numpy que me retorna um boolean, só que no caso preciso que me retorne mais detalhes e decidi criar de forma manual onde me retorna a probabilidade de inadimplência de acordo com a característica que selecionamos como parâmetro da analise e o mais interessante e que o código pode ser utilizado em qualquer dataframe apenas modificando as variáveis probabilísticas que deseja estudar.



A analise probabilística e muito utilizada para estudo da politica de credito de acordo com a carteira de clientes interna, onde conseguimos identificar quais os critérios que mais precisam de atenção na analise de credito, como por exemplo na analise exploratória identificamos que a relação entre valor e quantidade de transações no ultimo ano os clientes inadimplentes tem baixa movimentação, deixando em destaque a utilização dessa característica como variável probabilística de peso na analise.
