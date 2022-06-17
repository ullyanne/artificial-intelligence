# artificial-intelligence
my code for artificial intelligence class

# Problemas

## :one: Missionários e Canibais

Três missionários e três canibais estão em um lado do rio, juntamente com um barco que pode conter uma ou duas pessoas. Descubra um meio de fazer todos atravessarem o rio, sem deixar que um grupo de missionários de um lado fique em número menor que o número de canibais nesse lado do rio. 

Esse problema é famoso em IA, porque foi assunto do primeiro artigo que abordou a formulação de problemas a partir de um ponto de vista analítico (Amarel, 1968). 

Implemente e resolva o problema de forma ótima, utilizando um algoritmo de busca
apropriado. É boa ideia verificar a existência de estados repetidos?

:white_check_mark: [Resolução](missionaries%20'n%20cannibals.py)

## :two: Problema do metrô de Paris

Suponha que queremos construir um sistema para auxiliar um usuário do metrô de Paris a saber o **trajeto mais rápido** entre a estação onde ele se encontra e a estação de destino. O usuário tem um painel com o mapa, podendo selecionar a sua estação de destino. O sistema então acende as luzes sobre o mapa mostrando o melhor trajeto a seguir (em termos de quais estações ele vai atravessar., e quais as conexões mais
rápidas a fazer – se for o caso).

Considere que:
- a distância em linha reta entre duas estações quaisquer é dada em uma tabela.
Para facilitar a vida, considere apenas 4 linhas do metrô;
- a velocidade média de um trem é de 30km/h;
- tempo gasto para trocar de linha dentro de mesma estação (fazer baldeação) é de
4 minutos;

**Formule** e **implemente** este problema em termos de estado inicial, estado final,
operadores e função de avaliação para **Busca heurística com A***.

### Mapa do Metrô de Paris
![Mapa do Metrô de Paris](docs/imgs/paris%20metro%20map.png)

### Tabela de distâncias do Metrô de Paris
![Tabela de distâncias do Metrô de Paris](docs/imgs/paris%20metro%20dist.png)

:white_check_mark: [Resolução](paris%20metro.py)

## :three: O problema do caixeiro viajante

Um caixeiro viajante precisa visitar 10 cidades do interior de Pernambuco. Ele pede a um agente de busca que determine uma rota para sua visita tal que cada cidade só seja visitada *uma única vez*, e ele percorra o *menor espaço possível* (em Km). O agente de busca tem um mapa do estado, e portanto sabe as distâncias entre as cidades.

**Formule** e **implemente** este problema em termos de estado inicial, estado final, operadores e função de avaliação para **Busca por melhoras iterativas com Hill-Climbing**.

O operador considerado para gerar os filhos do estado corrente é permutar as
cidades da rota atual duas a duas, e verificar em seguida se o caminho está
conectado (segundo a tabela abaixo, que representa o mapa da questão). A cidade
inicial deve ser mantida, uma vez que o caixeiro mora lá :smiley: A rota é fechada (ele volta
à cidade de origem no final).

### Tabela de distâncias das cidades
![Tabela de distâncias das cidades](docs/imgs/travelling%20salesman.png)

:white_check_mark: [Resolução](travelling%20salesman.py)

## :four: Jogo para dois jogadores

Escolha um jogo para dois jogadores (ex.: jogo da velha, othelo, damas, xadrez, etc.) e
implemente-o utilizando o minimax.

:white_check_mark: [Resolução](tic%20tac%20toe.py)