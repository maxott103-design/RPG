# Auditoria do simulador e dos números publicados

Data: 13/09/2026. Fonte: [código original preservado](../versao-claude/Regras/ferramentas/simulador-combate.py) e [manual v2, §9](../regras/regras-partida-piloto.md).

## Conclusão

Há um simulador com 10.000 repetições configuradas e tabelas de resultados no manual. **Isso não equivale a playtest de mesa nem comprova o balanceamento atual.** Nesta revisão foi feita inspeção do código; as 10.000 simulações por cenário não foram reexecutadas.

## Divergências demonstráveis no código

| Trecho | Problema | Consequência |
| --- | --- | --- |
| Ataques dos PJs reduzem PF inimigo a 0, mas só removem do vetor em um ataque posterior bem-sucedido | Ralé deveria sair imediatamente a 0 PF | Exige ações adicionais contra alvos já fora de combate e alonga confrontos |
| Ataque pesado inimigo usa uma chamada aleatória para distinguir Leve/Grave; contra PJ Quebrado também faz teste | Modelo contém rolagens do lado inimigo, não sustentadas pelo princípio de só jogadores rolarem | Não reproduz fielmente o procedimento documentado; primeiro resolver D01 |
| Quando todos os PJs caem, só sai do laço de inimigos; laço de rodadas continua até 30 | Derrota não encerra imediatamente o combate | A duração média dos cenários letais pode ser inflada |
| Teto fixo de 30 rodadas retorna o mesmo formato que término normal | Não distingue censura/limite de combate encerrado | Médias não revelam quantos combates ficaram sem desfecho |
| Defende apenas quando o custo é até 2 e sobra pelo menos 1 PF | Não modela a terceira defesa de 3 PF e usa uma política específica | Resultado depende dessa estratégia, não de todas as escolhas possíveis |
| PJ: PF9, competência +2, arma Peso1, quatro participantes | Grupo real tem cinco fichas heterogêneas | As médias não são previsão para o piloto reunido |
| Sem semente aleatória definida | Execução varia a cada rodada de simulação | Tabelas não são reprodução exata garantida |

O próprio arquivo declara que exclui armaduras, habilidades, ataques pesados dos PJs, sangramento, Exaustão, armas de fogo, cobertura, críticos, moral, fuga e terreno. Não chamar seus números de limite matemático “pessimista”: sem demonstrar monotonicidade dessas omissões, eles são resultados de um modelo simplificado.

A Ralé de facão pode ferir alvos em desvantagem prevista. A frase “nunca fere” em resumos não descreve todas as situações do manual.

## Ordem proposta para correção

1. Decidir gravidade/defesa inimiga e o fim de combate.
2. Corrigir retirada de Ralé e interrupção por derrota.
3. Introduzir semente, identificação de versão e contagem de resultados truncados.
4. Comparar linha de base e mudanças isoladas, declarando todas as hipóteses.
5. Só depois modelar as cinco fichas e habilidades v4, sem confundir simulação com mesa.

O código histórico permanece intacto. Não foi criada uma mecânica nova para fazer o simulador “passar”.
