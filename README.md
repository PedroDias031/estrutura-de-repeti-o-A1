# estrutura-de-repeti-o-A1

🔄 Estruturas de Repetição em Python: For e While

- Este projeto combina dois exemplos fundamentais de estruturas de repetição (laços) em Python: o laço for (para iteração definida) e o laço while (para repetição condicional até que uma condição seja satisfeita).

🚀 Funcionalidades

O código apresenta duas funcionalidades distintas:

- Contador de Voltas (for): Simula a contagem de voltas de 1 a 10.

- Validador de Número Positivo (while): Solicita repetidamente um número ao usuário até que um valor positivo seja fornecido.

⚙️ Como Funciona

1. Repetição com FOR
   
- O laço for é usado quando o número de repetições é conhecido.

for voltas in range(1, 11):

range(1, 11) gera uma sequência de números inteiros de 1 a 10.

O código dentro do laço é executado dez vezes.

Em cada execução, o valor atual da sequência é atribuído à variável voltas.

2. Repetição com WHILE
   
- O laço while é usado para repetir um bloco de código enquanto uma condição for verdadeira.

while True: Cria um laço infinito, garantindo que o bloco interno será executado pelo menos uma vez e continuará até que um break seja encontrado.

number = int(input('Informe um numero positivo: ')): Solicita e converte a entrada para um número inteiro.

if number > 0:: Verifica a condição de saída.

Se verdadeiro (o número é positivo), exibe a mensagem de sucesso e o comando break encerra o laço.

else:

Se falso (o número é zero ou negativo), exibe uma mensagem de erro e o laço continua (volta para while True).

🔧 Requisitos e Execução

- Este código é puramente Python.
  
- Python 3 instalado.

Execução:
- Salve o código acima em um arquivo chamado, por exemplo, loops.py.

- Abra seu IDE, e execute o script python loops.py.

- A primeira parte (for) será impressa imediatamente.

- A segunda parte (while) solicitará interativamente que você digite números até que um número positivo seja fornecido.
