# RPG — estado consolidado

Revisão documental: **13/09/2026**. Repositório-base: [27721db](https://github.com/maxott103-design/RPG/tree/27721dbca38a1d1ed52656995b9318318237aa79). Foram inspecionados os **82 arquivos** de main, seus conteúdos atuais, backups, cinco commits, a única branch e as coleções de issues/PRs (vazias na consulta inicial). [Inventário completo](fontes/inventario.md).

## Resultado

O RPG tem **um núcleo de regras e um cânone de trabalho bem mais completos do que a documentação da raiz sugeria**. O material Claude já resolve muitas lacunas da recuperação GPT. Por outro lado, não é correto adotar toda a pasta Claude como pacote mais recente: seus resumos e HTML contêm informações superadas, e a raiz conserva decisões e detalhes de campanha que não aparecem nos resumos Claude.

A organização agora segue assunto, com documentos completos de regras, cinco fichas e complementos de mundo na raiz. A pasta versao-claude é preservada como fonte histórica. Os arquivos anteriores da raiz continuam recuperáveis pelo commit-base.

Não há evidência de playtest real. “Consolidado” aqui significa reunido e rastreável; não significa aprovação de regras novas ou balanceamento definitivo.

## O que usar como referência

| Área | Referência de trabalho | Situação |
| --- | --- | --- |
| Mecânica principal | [Manual do piloto v2](regras/regras-partida-piloto.md) | Escrito, com ambiguidades operacionais identificadas |
| Criação | [Atributos v1](regras/atributos.md) + [competências v1](regras/competencias.md) | 10 pontos; pirâmide; origens/progressão abertas |
| Habilidades | [Catálogo v4](regras/habilidades.md) | 33 habilidades; ranks descritos, aquisição e testes pendentes |
| Personagens | [Cinco fichas completas](personagens/README.md) | Números coerentes; biografia do meio-orc em conciliação |
| Mundo | [Visão unificada](worldbuilding/visao-geral.md) + [cânone completo](worldbuilding/canone-do-mundo.md) | Premissas definidas; geografia e detalhes políticos abertos |
| Estética | [Base completa](estetica/base-estetica.md) + briefings de agosto/setembro | Carvão/vapor; sem diesel corrente; modelos específicos abertos |
| Cosmologia | [Eras e colapso](lore/cosmologia-e-colapso.md) | Núcleo definido; várias aberturas recuperadas, cronologia a confirmar |
| Instituições | [Economia e Expedicionários](worldbuilding/economia-e-faccoes.md) | Financiamento por status recuperado da fala autoral |
| Aventura | [Entreposto/Pedra Negra/SEDP/redomas](aventuras/piloto.md) | Roteiro mais detalhado disponível; preparação incompleta |
| Testes | [Auditoria e plano de mesa](playtests/README.md) | Simulador histórico existe; não valida o conjunto atual |

## Decisões documentadas

- 3d6 + competência − Ameaça; atributos não somam; apenas jogadores rolam.
- Três resultados: até 9 falha, 10–14 fraco, 15+ decisivo; 3/18 naturais têm efeitos especiais.
- Cinco atributos, orçamento 10, mínimo 1/máximo 3 na criação.
- Fôlego = Vigor + 7; Exaustão reduz 2 por ponto, teto Vontade + 1.
- Uma Passiva + uma Ativável; classes rígidas e “disciplinas” não são a estrutura escolhida.
- Ataque simples 0 PF; pesado 1 PF, exige Peso 2 e competência. Quebrado não ataca.
- Retomar engajado permitido; 4 − Peso de carga, mínimo 1. Fora de perigo, 2 minutos; sangramento bloqueia essa recuperação.
- Resistência comum: 2 Graves, 3 Leves ou 1 Grave + 2 Leves; cabeça Grave derruba.
- Sangramento 6; cura exige tratamento e tempo. Fratura, Corpo Estranho e Trauma ainda são propostas.
- Perigos de estrada principalmente mundanos; Corrompidos raros, ligados a acontecimentos excepcionais.
- Tecnologia cotidiana industrial de carvão/vapor; o documento estético rejeita diesel corrente.
- Os Expedicionários recebem investimento aristocrático por prestígio; exploração de trabalhadores/escravos faz parte do conceito autoral.

## Conciliações que merecem atenção

**Ficha e resumo não são a mesma versão.** O anão combatente usa Já Estive Aqui + Aguenta Mais Um; o meio-orc usa Cheiro de Sangue + Trespassar. O resumo de decisões ainda trazia habilidades anteriores. Os HTML têm valores antigos, arco e até atributo 0.

**Mundo não é apenas regra.** A importação recente dos números não substitui automaticamente os briefings GPT de agosto/setembro, a SEDP, redomas, Igreja e NPCs.

**A transcrição é fonte de autoria, mas também contém sugestões da IA.** Recuperamos a motivação aristocrática dos Expedicionários e o aceite geral à política de Pedra Negra. Não promovemos a cânone todos os nomes, conselhos, lemas ou exemplos sugeridos.

**O simulador não comprova as tabelas como descrição fiel do jogo.** Ralé a 0 permanece até ataque posterior; derrota pode correr até 30 rodadas; há dados inimigos e omissões importantes. [Detalhes](playtests/auditoria-simulador.md).

## O que precisa de decisão primeiro

1. Ataques e manobras inimigas, Alerta/surpresa e interação com defesa.
2. PF mínimo/pagamento a zero, ferimentos acumulados, Aparo/tiro e sangramento.
3. Interações de habilidades usadas na primeira mesa e exceções dos inimigos escolhidos.
4. Escopo do piloto, encontros e condições de retorno.
5. Biografia do meio-orc: salto de trem ou anos de mineração e fuga furtiva.

Depois: origens, progressão, economia/sobrevivência, condições adicionais, geografia, Igreja, política detalhada, cronologia do Portal e artes finais. Não é necessário fechar toda a cosmologia para testar uma briga de bar.

A lista completa tem **33 frentes de trabalho**, separadas por tipo e prioridade, em [pendências](ideias/pendencias.md); **17 grupos de divergências** estão em [conciliação](ideias/divergencias.md). Não são 33 perguntas para responder de uma vez.

## Limites

Esta revisão cobre o repositório encontrado, não todos os históricos privados do GPT/Claude. As transcrições e resumos preservados têm lacunas de data e autoria. Nenhum arquivo de imagem final nem relato de mesa foi localizado. HTML foi inspecionado como fonte textual/código, não testado como produto visual.
