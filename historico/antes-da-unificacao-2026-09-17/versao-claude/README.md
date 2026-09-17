# versao-claude — material desenvolvido nos chats do Claude (Cowork)

Esta pasta é uma cópia fiel da pasta local `Projeto RPG` (estado de 13/09/2026), mais um arquivo de decisões consolidadas extraído dos chats. Ela foi criada **separada** do restante do repositório de propósito: o conteúdo na raiz (`regras/`, `worldbuilding/`, `lore/` etc.) veio de outra IA, e a ideia é comparar as duas versões ponto a ponto antes de fundir.

Nada aqui foi editado para "encaixar" no resto do repositório. O que está aqui é o que estava na pasta local.

## Comece por aqui

| Arquivo | O que é |
|---|---|
| **[DECISOES-DOS-CHATS.md](DECISOES-DOS-CHATS.md)** | Resumo das decisões fechadas nos chats, com data e motivo. É o atalho para a compatibilização. |
| [README-projeto.md](README-projeto.md) | README original da pasta local (premissa, tom, status). |
| [Regras/sistema-de-regras.md](Regras/sistema-de-regras.md) | Índice da pasta `Regras/`: diz qual arquivo é cânone e qual está superado. |

## O que é cânone dentro desta pasta

| Área | Fonte de verdade | Versão | Superado / histórico |
|---|---|---|---|
| Regras (lado do mestre) | `Regras/regras-partida-piloto.md` | v2 — 28/08/2026 | `Regras Gerais.txt`, `Sintese Desatualizada.txt`, `.bkp-*` |
| Regras (lado do jogador) | `Regras/GUIA DO JOGADOR.txt` | v2 sincronizado | `.bkp-guia-v1.txt` |
| Atributos e criação | `Regras/atributos.md` | v1 (28/08) | — |
| Competências | `Regras/competencias.md` | v1 | — |
| Habilidades | `Regras/habilidades.md` | v4 (28/08) | `.bkp-habilidades-v1/v2/v3.md` |
| Mundo | `Mundo/visao-geral-do-mundo.md` | 28/08 | `Lore e Worldbuilding.txt` (transcrição bruta de julho) |
| Estética | `Mundo/Estetica, Armas e Armaduras.md` | — | — |
| Personagens do piloto | `Personagens/Ficha 0X — *.md` | 28/08 | `Personagens/.bkp/` (estado cru, antes do chassi fechado) |
| Fichas em HTML | `Personagens/*.html` | 27/08 | são arte/layout, não regra |
| Calibragem | `Regras/ferramentas/simulador-combate.py` | 28/08 | reproduz as tabelas da seção 9 das regras |

Regra geral: quando um `.md` e um `.txt` divergirem, vale o `.md`. Os `.txt` são transcrições de chat de julho e ficaram como registro.

## Como comparar com a versão da raiz

Sugestão de ordem, do mais estrutural para o mais fino:

1. `DECISOES-DOS-CHATS.md` contra `decisoes/` e `ideias/divergencias.md` da raiz — resolve as contradições grandes (Fôlego, Corrompidos, arco vs besta, classes).
2. `Regras/atributos.md` + `competencias.md` contra `regras/atributos-e-competencias.md`.
3. `Regras/regras-partida-piloto.md` contra `regras/folego-exaustao-e-defesa.md`, `regras/ferimentos-e-dano.md` e `regras/resolucao.md`.
4. `Regras/habilidades.md` contra `regras/habilidades.md`.
5. `Mundo/visao-geral-do-mundo.md` contra `worldbuilding/` e `lore/`.
6. Fichas: `Personagens/Ficha 0X` contra `personagens/*.md`.

Critério que vale para tudo: **data mais recente ganha**, e dentro desta pasta a data de referência é 28/08/2026. Vários itens listados como "não recuperado" em `ideias/pendencias.md` da raiz existem aqui por completo (atributos, competências, catálogo de habilidades, Fôlego/Exaustão, consequências das faixas de 3d6, procedimento de combate).
