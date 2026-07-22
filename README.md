# Análise Financeira com Python

Este projeto foi desenvolvido como parte do desafio prático de análise financeira com Python.

O objetivo é ler um arquivo CSV com transações bancárias, validar os dados, calcular métricas mensais, identificar movimentações suspeitas e gerar um relatório em JSON.

## Funcionalidades

- leitura do arquivo `transacoes.csv`;
- validação dos registros;
- separação entre transações válidas e inválidas;
- agrupamento das transações por mês;
- cálculo de créditos, débitos, saldo, média, maior e menor valor;
- identificação de transações acima de R$ 10.000,00;
- exibição de relatório no terminal;
- geração do arquivo `relatorio.json`.

## Arquivos do projeto

- `desafio-final.ipynb`: notebook principal com o desenvolvimento e as saídas;
- `transacoes.csv`: arquivo utilizado como entrada;
- `relatorio.json`: arquivo gerado com o resultado da análise;
- `analise_pandas.py`: versão alternativa da análise utilizando pandas;
- `grafico.png`: gráfico com o saldo mensal das transações.
- `README.md`: descrição do projeto.

## Como executar

1. Abra o arquivo `desafio-final.ipynb` no Google Colab.
2. No menu lateral esquerdo, clique no ícone de pasta.
3. Faça o upload do arquivo `transacoes.csv`.
4. Execute todas as células do notebook em ordem.

Ao final da execução, o relatório será exibido e o arquivo `relatorio.json` será gerado.

## Tecnologias utilizadas

- Python
- CSV
- JSON
- datetime
- pandas
- matplotlib

## Resultado

O projeto gera um resumo mensal das transações, mostra o período analisado, contabiliza os registros válidos e inválidos e apresenta as transações consideradas suspeitas.
