# RPG — Documentação de desenvolvimento

Repositório: **RPG**. O título final do jogo permanece em aberto.

Este repositório organiza o desenvolvimento do RPG e preserva os motivos das decisões.

## Navegação

| Espaço | Conteúdo |
| --- | --- |
| [Worldbuilding](worldbuilding/README.md) | Geografia, povos, sociedade, economia e funcionamento do mundo |
| [Lore](lore/README.md) | História, cosmologia, acontecimentos e segredos |
| [Regras](regras/README.md) | Mecânicas, criação de personagens e testes |
| [Personagens](personagens/README.md) | Personagens de jogadores e NPCs |
| [Aventuras](aventuras/README.md) | Cenários, encontros e registros de sessões |
| [Estética](estetica/README.md) | Direção visual, armas, armaduras e referências |
| [Decisões](decisoes/README.md) | O que foi decidido e por quê |
| [Ideias](ideias/README.md) | Propostas e dúvidas ainda abertas |
| [Playtests](playtests/README.md) | Observações de mesa e ajustes a avaliar |
| [Modelos](modelos/README.md) | Formulários para novos registros |

## Como usar

1. Abra o arquivo da área desejada e use o lápis do GitHub para editar.
2. Para uma nova entrada, copie um modelo para a pasta correspondente, usando um nome como `nome-do-assunto.md`.
3. Indique o estado: **Proposto**, **Em teste**, **Consolidado**, **Descartado** ou **Substituído**.
4. Quando tomar uma decisão importante, registre-a em `decisoes/` e atualize o documento temático correspondente.
5. Ao mudar uma decisão, preserve o registro anterior e indique qual decisão a substituiu.

Os documentos temáticos descrevem a versão atual; o registro de decisões preserva o histórico e os motivos. Uma proposta não passa a ser canônica automaticamente.

## Versões paralelas a compatibilizar

| Pasta | Origem | Estado |
| --- | --- | --- |
| Raiz (`regras/`, `worldbuilding/`, `lore/`, …) | Organização feita em outra IA a partir dos chats | Revisão, com pendências e divergências registradas |
| [`versao-claude/`](versao-claude/README.md) | Cópia fiel da pasta local `Projeto RPG` desenvolvida nos chats do Claude (regras v2, 28/08/2026) | Fonte mais recente; ver [decisões dos chats](versao-claude/DECISOES-DOS-CHATS.md) |

As duas ficam separadas até a comparação ponto a ponto. Nada da raiz foi alterado ao adicionar `versao-claude/`.

## Conteúdo organizado

As pastas já contêm documentos temáticos sobre o mundo, a Igreja, as mecânicas recuperadas, os cinco personagens, NPCs, a aventura piloto e a direção visual.

- [Fontes e cobertura da revisão](fontes/README.md)
- [Divergências entre versões](ideias/divergencias.md)
- [Pendências e material da outra IA](ideias/pendencias.md)
- [Anão combatente](personagens/anao-combatente.md)

**Atenção à versão das regras:** o resumo antigo foi preservado com seu estado de versão. Foi identificada divergência com um anexo de ficha recuperado separadamente, cuja importação ficou pendente. O conteúdo da outra IA ainda não foi incorporado.

Esta é uma revisão do material disponível, não uma transcrição integral de todos os chats. As [notas iniciais](ideias/notas-iniciais.md) foram preservadas como registro histórico.

## Compartilhamento

Lore e aventuras podem conter segredos do mestre. As pastas não têm permissões separadas: quem acessa o repositório pode ler tudo. Para jogadores, prepare cópias específicas dos materiais que deseja compartilhar.
