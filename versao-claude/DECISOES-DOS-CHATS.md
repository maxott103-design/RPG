# Decisões fechadas nos chats do Claude — consolidado para compatibilização

Extraído da memória do projeto e dos documentos da pasta local. Data de referência: **28/08/2026** (regras v2, habilidades v4, cânone de mundo). Quando um documento e este resumo divergirem, vale o documento — este arquivo é um atalho, não a fonte.

Cada item traz o **onde** (arquivo que detalha) para a comparação ponto a ponto com a versão da raiz do repositório.

---

## 1. Núcleo de resolução

- 3d6 + bônus de competência − Ameaça. **≤9 falha | 10–14 sucesso fraco | 15+ sucesso decisivo.** Só jogadores rolam; o mestre pensa um número (Ameaça).
- Só a competência entra na rolagem. **Atributos nunca somam na rolagem.**
- Crítico no **18 natural**, falha crítica no **3 natural**.
- Ranks de competência: Aprendiz +1, Prático +2, Profissional +3, Mestre +4. Ameaça jogável 1–5; Ameaça 6 não se resolve com rolagem direta.
- No piloto: Ameaça 2 e competência principal em Prático (+2) como referência de calibragem.

Onde: `Regras/regras-partida-piloto.md` §1; `Regras/roadmap-desenvolvimento.md` 1.2 e 2.2.

## 2. Chassi do personagem (fechado em 28/08 para preencher as fichas)

- Cinco atributos, escala 1–4: Vigor, Agilidade, Percepção, Intelecto, Vontade.
- **Orçamento de criação: 10 pontos, mínimo 1, máximo 3.** O 4 só em jogo. Não existe atributo 0.
- Derivados: **Fôlego máx = Vigor + 7** (fallback Vigor + 5 se as lutas arrastarem) | **nº de competências = 3 + Intelecto** | **nº em Profissional/Mestre = Vontade** | **teto de Exaustão = Vontade + 1** | Resistência igual para todos.
- Vontade **não** gera pool/barra mental. Estresse e medo, quando falhados, custam Exaustão — sem subsistema separado.
- Competências em pirâmide, sem distribuição de pontos: âncora em um atributo, rank máximo = atributo âncora + 1, Mestre exige atributo 3+. Criação: 1 Profissional, 2 Práticos, resto Aprendiz.
- **Sem classes rígidas.** A síntese de julho mencionava classes; foi substituída pela pirâmide + origens.
- Origens (proficiências, conhecimentos, equipamento inicial): função definida, conteúdo ainda não escrito — é o próximo passo do chassi.

Onde: `Regras/atributos.md`, `Regras/competencias.md`, `Regras/roadmap-desenvolvimento.md` fase 2.

> Nota de compatibilização: fichas vindas de outro chat usavam Fôlego = Vigor + 6 e dois personagens com Intelecto 0. Foi corrigido para o chassi acima.

## 3. Fôlego — a mudança estrutural da v2

Fôlego deixou de ser moeda de ação e virou **moeda de resistência**: bater é de graça, não ser atingido é que custa.

- Ataque simples custa **0 PF**; ataque pesado **1 PF**; tiro **1 PF**; defesas **1/2/3 PF**.
- **Quebrado (0 PF) não ataca** — o ataque simples custa 0 mas exige ter Fôlego. Preserva a tese "drenar o inimigo é desarmá-lo".
- **Ataque pesado exige arma Peso 2.** Arma leve só fere alvo Quebrado, caído, imobilizado ou desprevenido (ciclo "desgasta primeiro, fere depois").
- Retomar Fôlego é permitido mesmo engajado. Fôlego volta em 2 minutos fora de combate.
- Sangramento: contador 6 e trava a recuperação de Fôlego.
- Peso da armadura desconta de Furtividade/Acrobacia/Atletismo — fecha a dicotomia "pesado apara, leve esquiva".
- Fôlego fora de combate também está definido (§10).

Onde: `Regras/regras-partida-piloto.md` §2, §5, §7, §10.

## 4. Ferimentos, Resistência e Exaustão

- Ferimento é **Local × Gravidade × Tipo**. Ferido = realmente ferido: ferimento cria situação, não penalidade abstrata.
- Resistência cai com **2 Graves, 3 Leves, ou 1 Grave + 2 Leves**.
- Cabeça Leve = −2.
- Tipos: só **Sangramento** está fechado. Fratura, Corpo Estranho e Trauma são propostas.
- **Exaustão: −2 PF máx por ponto**, teto = Vontade + 1 (Esgotado no teto, Colapso acima). Exaustão é a moeda universal de esforço, ferimento forçado, medo e privação — risco de saturar; se saturar, calibrar pela taxa de recuperação, não removendo fontes.

Onde: `Regras/regras-partida-piloto.md` §3, §4, §8.

## 5. Armas

- Revólver: 5 tiros. Arma de repetição **não** existe como rajada no cenário.
- **Arco praticamente não existe no cenário.** A arma de projétil tensionado que sobreviveu é a **besta**: mecanismo, gatilho, peça de guilda, fabricável e reparável. Quem não tem oficina não tem arma de tiro. Besta: fraco desgasta 2 PF, decisivo causa Leve, não emperra. Nenhum personagem do piloto carrega besta.
- Orcs e meio-orcs do Norte caçam em contato, como neandertais — em grupo, cercando, lança pesada contra megafauna. Não usam arco. É isso que os torna mercenários competentes sem treino de guerra.

Onde: `Regras/regras-partida-piloto.md` §6 e §6.1; `Mundo/visao-geral-do-mundo.md`; `Mundo/Estetica, Armas e Armaduras.md`.

## 6. Inimigos (§9 e §9.5, escritos em 28/08)

- Régua de Ameaça; o Fôlego do inimigo é recurso, não barra de vida; **Ferimento no inimigo = Ameaça caindo**.
- **A regra que restringe tudo: o mestre não rola.** Habilidade de inimigo só pode custar Fôlego dele, mudar o que o jogador paga/rola, ou mudar posição. Se exige rolagem do mestre, está errada. Regra do telegrama: aparece na ficção uma batida antes.
- Três tipos: **Ralé** (sem habilidade — o que assusta são táticas de custo 0: cercar, focar o mais fraco, revezar, cortar o fôlego de quem Retoma, fechar a saída, chamar reforço, cobrar o preço da armadura em terreno ruim), **Nomeado** (1 ou 2 habilidades, nunca mais; catálogo de 9; nunca some com o turno do jogador), **Coisa** (uma exceção única na ficha, que é o quebra-cabeça do encontro).
- Ações comuns a qualquer inimigo, pagando Fôlego: Agarrar, Derrubar, Desarmar, Investida, Bloquear, Empurrar para o perigo.
- **Fichas de inimigo do piloto não usam mais Corrompidos** — viraram cão-de-ruína, saqueador, pregador humano da Igreja.

Onde: `Regras/regras-partida-piloto.md` §9, §9.5.

## 7. Calibragem de encontro (simulada, 10k combates por cenário)

1. Com ataque pesado restrito a Peso 2, inimigo de facão **nunca fere**, só drena. Ferimentos num 4×4: 0,02 sem marreta; 0,57 com 2 de 4 marretas; 2,90 com 4 de 4. ~5 rodadas em todos.
2. Aumentar o **número** resolve por outro caminho e custa tempo: 6 facões = 0,50 ferimento em 8,5 rodadas; 8 = 3,57 ferimentos mas 14,6 rodadas; 10 = colapso.
3. **Foco de fogo é a variável mais forte do sistema**: 6×4 salta de 0,50 para 4,00 ferimentos com 1 PJ caído se o mestre concentrar no mais fraco.

Conclusão: armamento controla quanto machuca; número controla quanto dura. São dials diferentes e não se substituem. Regra de bolso: 1 a 1,5 inimigos por jogador, pelo menos um terço com Peso 2.

Onde: `Regras/regras-partida-piloto.md` §9 (tabelas); `Regras/ferramentas/simulador-combate.py`.

## 8. Habilidades (v4)

- Toda habilidade é **Passiva ou Ativável** e **quebra uma regra do sistema sob condição visível**. Bônus numérico é o último recurso; quando aparece, é "ignora N de Ameaça".
- **Teste do trunfo**: (1) verbo, não adjetivo; (2) quebra uma regra, sob condição — a condição é o preço; (3) muda a decisão de alguém. Referência: D&D (Fúria, Ataque Furtivo, Trespassar), não bônus subjetivo.
- Travas: condição visível (nunca "sempre"); preço na mesma moeda (PF, Exaustão ou abrir mão de algo); nunca some o turno do outro; Ativável nunca passa de uma cena.
- Exploração/social ganha sal por **autoridade narrativa** (Já Estive Aqui, Bolso Fundo) ou **prêmio tático** (Cheiro de Sangue). Informação subjetiva não é habilidade.
- Cortadas por veredito do autor: **Improviso** ("criatividade do jogador, não habilidade") e **Fogo de Contenção** (pressupunha rajada; virou "Deixa Vir").
- Habilidades com requisito narrativo devem nascer na mesa. Nada da v4 passou pelo simulador ainda; riscos listados em "Vigiar no piloto".

Onde: `Regras/habilidades.md` (v4); versões anteriores em `Regras/.bkp-habilidades-v1/v2/v3.md`.

## 9. Os cinco personagens do piloto (Vigor/Agilidade/Percepção/Intelecto/Vontade)

| Ficha | Atributos | Habilidades (Passiva + Ativável) | Arma |
|---|---|---|---|
| Anão Combatente | 2/1/2/2/3 | Expedição + Aguentar o Tranco; Medicina Aprendiz | Machado grande |
| Anão Minerador | 3/2/3/1/1 | Subsolo + Sujeira | Picareta |
| Humano Operário | 1/2/2/3/2 | Máquinas + Sabotagem (alt.: Pó na Cara) | Marreta industrial + revólver |
| Humano Combatente | 2/2/3/1/2 | Instrução Militar + Ordem (alt.: Deixa Vir) | Rifle de repetição |
| Meio-Orc Caçador | 3/2/3/1/1 | Rastro + Bote | Lança pesada |

- Quatro dos cinco têm arma Peso 2 (requisito para ferir); o soldado fere de longe.
- Ninguém tinha Medicina — o Anão Combatente recebeu Medicina Aprendiz.
- Raça no piloto é ficção, não número de ficha.

Onde: `Personagens/Ficha 0X — *.md`; estado cru anterior em `Personagens/.bkp/`.

## 10. Mundo — direção fechada em 28/08

- **Corrompidos** (antes "vampiros") saíram do papel de ameaça cotidiana. Não são espécie, facção nem população — são quase um evento sobrenatural. Encontrar um faz a mesa perguntar "por que existe um aqui?".
- **A Wasteland é perigosa por motivos mundanos**: bandido, escravagista, tribo, predador, fome, sede, clima, ruína instável. Referência: *Kenshi*.
- Cidades não crescem porque manter território é caríssimo → expedição vira atividade economicamente relevante (premissa da campanha).
- Corrupção distorce quem existia (trabalhador → massa muscular; soldado → fundido às armas; técnico → integrado à máquina). Influência: *Berserk* como camada oculta, não estética.
- Ruínas como contenção (porta enterrada = para impedir algo de sair): proposta forte, **ainda não canônica**.
- Igreja anti-magia ganha ambiguidade: "o arcano destruiu o mundo" é parcialmente verdadeiro; a Igreja pode saber de corrupção, contenção e símbolos. Termos "antiarcano" (atual) e "arcano corrompido" (transcrição antiga) são a mesma coisa.
- **Escala de raridade** (contrato com a mesa): cotidiano toda sessão > regional sessão sim/sessão não > ruínas por arco > corrupção como pista > horror uma vez e a mesa lembra.
- Tom: dark fantasy pós-apocalíptica de baixa magia, dieselpunk, mil anos depois de uma guerra que juntou magia, indústria e algo de fora.

Onde: `Mundo/visao-geral-do-mundo.md` (cânone); `Mundo/Lore e Worldbuilding.txt` (transcrição bruta, nunca editar como regra); `Regras/regras-partida-piloto.md` §13.

## 11. O que continua aberto (do lado do Claude)

- Origens (conteúdo).
- Progressão de personagem.
- Tipos de ferimento além de Sangramento (Fratura, Corpo Estranho, Trauma).
- Equipamento/economia e ciclo de sobrevivência.
- Ficha de personagem final e documento de regras v0.2 (para substituir `Sintese Desatualizada.txt`).
- Aventura piloto escrita (conceito: escolta até vila isolada) e playtest real.

Onde: `Regras/roadmap-desenvolvimento.md`.

---

## Mapa rápido para os itens marcados como "não recuperado" em `ideias/pendencias.md` (raiz)

| Pendência da raiz | Onde está nesta pasta |
|---|---|
| Documento consolidado na outra IA | esta pasta inteira; começar por `Regras/regras-partida-piloto.md` |
| Atributos, competências e habilidades completos | `Regras/atributos.md`, `competencias.md`, `habilidades.md` |
| Fôlego e Exaustão (valores contraditórios) | §2 e §3 acima; `regras-partida-piloto.md` §2 e §4 |
| Consequências das faixas de 3d6 | `regras-partida-piloto.md` §1 |
| Anexos e fichas (números) | `Personagens/Ficha 0X — *.md` |
| Defesa, aparo, ações, sangramento, recuperação, morte | `regras-partida-piloto.md` §2, §3, §5, §8 |
| Classes vs sem classes | sem classes — pirâmide de competências + origens |
