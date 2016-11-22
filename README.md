# parse-data-file

A regra é a seguinte:

Tem vários arquivos em uma pasta com o nome nesse padrão: strategy_num_arena_seed.txt

strategy: Uma String
num: pode ser: 1,5,10 ou 20
arena: Uma String
seed: um int

Dentro do arquivo vai ter uma linha assim: "Result = {valor}", esse é um número inteiro.

Ex: de nomes de arquivos:

buy_1_newYork_1.txt

sell_5_Chigago_2.txt

trade_10_newOrleans_3.txt

O que precisa ser feito é agrupar os "strategy"/"arena" e somar todos os valores do result dentro do arquivo e calcular essa soma e a média também.

Retorno para os arquivos de exemplo:

[{'arena': 'Chigago', 'result': 2}, {'arena': 'michigan', 'result': 1}, {'arena': 'newOrleans', 'result': 3}, {'arena': 'newYork', 'result': 4}]

[{'result': 2, 'strategy': 'buy'}, {'result': 1, 'strategy': 'give'}, {'result': 4, 'strategy': 'sell'}, {'result': 3, 'strategy': 'trade'}]
