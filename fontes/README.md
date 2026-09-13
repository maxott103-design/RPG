# Fontes, cobertura e precedência

Revisão unificada: 13/09/2026. Base imutável: [27721dbca38a1d1ed52656995b9318318237aa79](https://github.com/maxott103-design/RPG/tree/27721dbca38a1d1ed52656995b9318318237aa79). [Inventário de todos os arquivos](inventario.md).

## Escopo efetivamente acessado

82 arquivos (incluindo backups, dois HTML e simulador), cinco commits, uma branch main. Issues e PRs estavam vazios na consulta inicial. Não foram acessados históricos privados externos das IAs; C01–C06/M01/R01 abaixo descrevem a procedência da revisão anterior, não novas consultas feitas nesta consolidação.

O estado importado do Claude está em [versao-claude](../versao-claude/README.md). O texto original foi preservado ali. Os documentos anteriores da raiz são recuperáveis no commit-base; alterações atuais têm registro próprio.

## Precedência adotada

1. **Escolha explícita do autor, com escopo e contexto identificáveis**, é evidência mais forte que uma sugestão da IA.
2. Documento detalhado designado como fonte de trabalho prevalece sobre seu resumo, índice ou roadmap quando descrevem a mesma versão. Assim, fichas completas e habilidades v4 prevalecem sobre a tabela atrasada de DECISOES-DOS-CHATS.
3. Substituição explícita e versões internas estabelecem sequência: piloto v2 substitui v1; habilidades v4 substituem v1–v3; chassi mínimo 1 substitui fichas com atributo 0.
4. A extensão do arquivo não resolve precedência. O GUIA DO JOGADOR.txt é guia v2, enquanto outros TXT são transcrições antigas. Nem todo MD está correto.
5. **Data de importação não é data de decisão.** Todos os commits consultados são de 13/09/2026; conteúdos remetem a julho, agosto e setembro. Não usar “Claude entrou depois” como aprovação de todo o seu conteúdo.
6. Quando a ordem não está provada, preservar as variantes com fontes. Silêncio de um resumo não revoga um detalhe autoral; proposta não vira regra.

## Cronologia do Git

| Commit | Data/hora UTC | Conteúdo |
| --- | --- | --- |
| 2c0a9ee | 13/09/2026 21:26:00 | Inicial |
| 1bf9161 | 13/09/2026 21:28:40 | Estrutura e modelos |
| 8acc7e4 | 13/09/2026 21:30:22 | Notas iniciais |
| da5f10b | 13/09/2026 21:43:49 | Organização temática GPT |
| 27721db | 13/09/2026 23:17:26 | Importação Claude sem compatibilização |

## Estado das fontes

| Material | Tratamento |
| --- | --- |
| Piloto v2, atributos/competências v1, habilidades v4 | Incorporados integralmente na área de regras, com referências e avisos de conflito |
| Fichas Markdown atuais | Incorporadas com números e habilidades atuais; complementadas pelo material GPT |
| Cânone de mundo e estética | Incorporados e ligados aos complementos de lore/localidades |
| Transcrição de mundo | Extração de informação omitida nos resumos, distinguindo fala do autor de sugestões |
| Regras Gerais / Síntese Desatualizada / backups | História de design; não são manual atual |
| HTML de personagens | Layouts de referência com regras antigas; não fichas prontas da versão atual |
| Simulador | Artefato histórico auditado, não comprovação de balanceamento |
| Resumos da raiz | Atualizados; originais preservados no Git |
| Artes finais e chats ausentes | Recuperação pendente; não presumir que não existam fora do repositório |

## Procedência herdada da recuperação GPT

O bloco abaixo é o registro anterior, preservado para rastreabilidade. Frases como “outra IA não acessível” e “ficha não importada” descrevem aquela etapa e foram superadas pela revisão atual.

---

# Procedência, cobertura e limites

Organização documental: **13/09/2026**. Esta revisão organiza o conteúdo acessível, não declara ter recuperado integralmente todos os chats.

## Fontes utilizadas

| Código | Origem | Acesso nesta revisão |
| --- | --- | --- |
| C01 | Regras Gerais do Jogo — 26/07/2026 | Trechos visíveis do projeto sobre atributos, competências, arquétipos e rejeição do nome “disciplina”; conversa integral não recuperada |
| C02 | Lore e Worldbuilding RPG — 26/07/2026 | Trechos visíveis sobre armas, armaduras e Igreja; detalhes complementados pelo resumo M01 |
| C03 | Berserk No Horror RPG — 27/08/2026 | Trechos visíveis sobre Comissário, cenas cotidianas, personagens e alteração do meio-orc; resumo M01 para sequência da aventura |
| C04 | Branch · Berserk No Horror RPG — 31/08/2026; consulta de atributos — 31/08/2026 | Pedidos visuais do meio-orc e localidades disponíveis; resposta integral sobre atributos não recuperada |
| C05 | Ficha HTML Interativa — 29/08/2026 | Pedido de ficha como plaqueta metálica; anexo localizado, mas separado desta publicação dos chats |
| C06 | Ideias de artes identitárias — 29/08 a 09/09/2026 | Resumo disponível de preferências e referências de armas; imagens originais não inspecionadas |
| M01 | Resumo de continuidade do projeto fornecido nesta conversa | Informação secundária sobre cenário, aventura, personagens e regras; não equivale a transcrição |
| R01 | Recuperação de contexto de uma síntese canônica enviada pelo usuário em 26/07/2026 | Resumo de recuperação, não texto integral; identificado como protótipo v0.1 aguardando playtest |
| G01 | README e notas iniciais existentes no GitHub | Lidos na revisão; são organização anterior do mesmo material, não fonte independente |

As datas de chats identificam sua origem, não necessariamente o instante em que cada decisão foi tomada. Não foram fabricados links para conversas não disponíveis.

## Estados usados

- **Decisão registrada:** escolha ou alteração explícita recuperada nos trechos ou identificada como tal no contexto.
- **Registrado no contexto:** informação preservada no resumo; sem garantia de que seja a última versão.
- **Divergência:** fontes têm valores ou formulações diferentes.
- **Não recuperado:** não foi encontrado material suficiente; isso não significa que o autor ainda não tenha decidido.
- **Proposto:** possibilidade discutida sem aceite recuperado.

“Consolidado aqui” não implica prevalecer sobre material posterior da outra IA. Esta organização não aprova regras novas.

## Limites concretos

A busca de conversas retornou somente parte do histórico. O restante do conteúdo foi organizado a partir dos trechos visíveis e de M01. Não foram recuperados integralmente todos os chats ou o documento canônico v0.1.

Um anexo de ficha foi localizado e lido, mas sua transcrição e os detalhes extraídos exclusivamente dele foram separados desta publicação. Resultados de outros projetos foram excluídos.

As imagens finais e a ficha HTML não foram importadas. O material desenvolvido na outra IA não está acessível nesta revisão.

## Como integrar o material externo

Importar os textos fornecidos pelo autor com identificação de origem/versão, comparar com [divergências](../ideias/divergencias.md), atualizar os documentos temáticos afetados e registrar substituições no histórico de decisões. Não usar a data desta organização como prova de que o conteúdo é mais novo.


---

## Regra de manutenção

Edite o documento temático atual. Registre a decisão em decisoes/, citando o trecho/fonte, e atualize pendências e fichas afetadas. Mantenha propostas marcadas; arquive o substituído com indicação da nova referência.
