# Desafio-Engenheiro-de-dados

# O Problema

O desafio consiste em calcular o ganho total da empresa Acquirer LTDA, que o obtêm na prestação do
serviço de locação de máquinas de cartão de crédito para seus clientes. Esse ganho é calculado sobre um percentual 
das transações de cartão de crédito realizadas por eles. O cálculo é feito baseado em dois conjuntos de dados, 
transações e contratos.
                                #Transações
     _____________________________________________________________
    |transaction_id | client_id| total_amount| discount_percentage|
    |             1 |      3545|         3000|                6.99|
    |             2 |      3509|         4500|                0.45|
    |             3 |      3510|        69998|                   0|
    |             4 |      3510|            1|                null|
    |             5 |      4510|           34|                  40|
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    
                                    #Contratos
     ______________________________________________________________________
    |   contract_id | client_id|      client_name|  percentage|  is_active|
    |             3 |      3545|   Magazine Luana|        6.99|       true|
    |             4 |      3545|   Magazine Luana|        0.45|      false|
    |             5 |      3509|  Lojas Italianas|           0|       true|
    |             6 |      3510|       Carrerfive|        null|       true|
     ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

O resultado esperado é o ganho total da Acquirer LTDA, que para o exemplo é: 845,411.

O cálculo deve ser feito cruzando os dados de transações com contratos (considerando apenas o contrato 
ativo do cliente). Para se obter o ganho total, é necessário multiplicar o percentual do contrato pelo valor líquido 
da transação, ou seja, já descontando o valor do desconto aplicado na transação.

#A Pergunta
Além do código acima, considere que uma escala de ~200 milhões de transações por dia e que o cálculo 
deverá apresentar um resultado do valor total do mês. Descreva em até 500 palavras que tecnologias e arquitetura 
você usaria para escalar a solução acima.
