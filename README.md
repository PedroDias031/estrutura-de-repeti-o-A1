🎯 Visão Geral do Projeto

Este projeto é um repositório de exemplos práticos em Python focado em demonstrar e documentar os Fundamentos de Programação, com ênfase nas Estruturas de Controle, como os laços de repetição (for e while) e estruturas condicionais.

O objetivo principal é servir como um material de referência e aprendizado, utilizando a documentação de código e a representação de algoritmos através de Pseudocódigo para facilitar o entendimento.

⚙️ Estrutura de Repetição no Código de Exemplo
O código fornecido demonstra duas formas de realizar repetições: com o laço for e com o laço while em Python.

1. Repetição com for (Laço de Contagem)
Este bloco de código simula um sistema de contagem de voltas, iterando um número predefinido de vezes.

📝 Pseudocódigo do FOR

ALGORITMO ContagemDeVoltas

VARIAVEIS

    voltas: INTEIRO
    
INÍCIO

    ESCREVER "Sistemas de voltas"
    PARA voltas DE 1 ATÉ 10 FAÇA
        ESCREVER voltas + "ª volta"
    FIM PARA
    FIM ALGORITMO


2. Repetição com while (Laço Condicional)
Este bloco implementa um laço de repetição que exige que o usuário insira um número positivo. O laço só é encerrado quando a condição de entrada (number > 0) é atendida, garantindo a validação do dado.

📝 Pseudocódigo do WHILE

ALGORITMO EntradaDeNumeroPositivo

VARIAVEIS

    number: INTEIRO
    
INÍCIO

    ENQUANTO VERDADEIRO FAÇA
        LEIA number
        SE number > 0 ENTÃO
            ESCREVER "Seu numero é o ", number
            PARE (SAIA DO LAÇO)
        SENÃO
            ESCREVER "Isso não é um número (positivo)"
        FIM SE
    FIM ENQUANTO
    FIM ALGORITIMO

💡 Representação de Algoritmo: Pseudocódigo

O Pseudocódigo é uma forma de representação de algoritmos que utiliza uma linguagem natural (como português ou inglês) combinada com elementos de estruturas de programação (como ENQUANTO, SE...ENTÃO, PARA), sem a rigidez da sintaxe de uma linguagem específica.

Benefícios:

Compreensão Universal: Ajuda a focar na lógica do algoritmo, independentemente da linguagem de programação final.

Planejamento: É uma etapa essencial no planejamento de um programa.

Debugging Lógico: Permite identificar erros de lógica antes de escrever o código.

🚀 Como Executar o Código

Pré-requisito: Certifique-se de ter o Python instalado em sua máquina.

Salve o código: Copie o código de exemplo para um arquivo e salve-o como, por exemplo, laços_exemplo.py.

Execute via terminal ou IDEs.

Interação: O programa executará a contagem de voltas e, em seguida, entrará no laço while, onde solicitará que você insira um número positivo.

📝 Licença
Este projeto é de natureza educacional e está sob a licença MIT (ou outra licença apropriada, se aplicável).
