# Regras da Partida Piloto — v2

Status: consolidado em 28/08/2026. Incorpora as decisões manuscritas no GUIA DO JOGADOR e a rodada de design do dia 28 (eixo de tipo de dano, filosofia de Ferimentos, lore dos Corrompidos).

**Mudança estrutural da v1 para a v2:** Fôlego deixou de ser moeda de ação e virou **moeda de resistência**. Atacar é de graça; defender-se, forçar o corpo e agir sob pressão é que custa. Ver seção 2.

---

## 1. Resolução

- **3d6 + competência − Ameaça.** Resultado: **≤9 falha | 10–14 sucesso fraco | 15+ sucesso decisivo.**
- Só jogadores rolam. Atributos NUNCA somam na rolagem.

### Tabela de probabilidade (a curva real do 3d6)

Margem = competência − Ameaça. É o único número que importa.

| Margem | Falha (≤9) | Fraco (10–14) | **Decisivo (15+)** |
|---:|---:|---:|---:|
| −2 | 62,5% | 35,6% | **1,9%** |
| −1 | 50,0% | 45,4% | **4,6%** |
| **0** | 37,5% | 53,2% | **9,3%** |
| +1 | 25,9% | 57,9% | **16,2%** |
| +2 | 16,2% | 57,9% | **25,9%** |
| +3 | 9,3% | 53,2% | **37,5%** |
| +4 | 4,6% | 45,4% | **50,0%** |

### Crítico e falha crítica

Lidos nos **dados naturais**, antes de qualquer soma ou subtração. Cada um sai **1 vez em 216** (0,46%).

- **18 natural = Crítico.** O melhor resultado possível daquela ação **e a ação não custa Fôlego**.
  - Ataque (corpo a corpo ou tiro): **Ferimento Grave no local à escolha**, seja qual for a arma. Esta é a única forma de uma faca abrir um Grave num alvo de pé — a sorte ou a perícia extrema aparecendo.
  - Defesa: evita o ataque, não gasta Fôlego, e o atacante fica exposto (**+2** no próximo ataque contra ele nesta rodada).
  - Teste comum: sucesso decisivo mais uma vantagem concreta dada pelo mestre.
- **3 natural = Falha crítica.** A falha acontece **e vem uma complicação**:
  - Corpo a corpo: você se abre — a **próxima defesa nesta rodada custa +1**.
  - Tiro: a arma **emperra**. Destravar é um turno inteiro (1 PF) + teste de Mecânica.
  - Defesa: a guarda cede — **perde 1 Aparo** (a peça danifica) ou, sem armadura, cai no chão.
  - Teste comum: falha e algo quebra, faz barulho ou chama atenção.

**Aviso de calibragem para o piloto:** em margem −1 a falha é 50% e o Fôlego de defesa é gasto mesmo assim. Regra de bolso: **a Ameaça do piloto fica em 2**, e cada personagem entra com a competência principal em **Prático (+2)** ou melhor. Ameaça 3+ é para inimigos que os jogadores devem evitar ou emboscar, não enfrentar de frente.

## 2. Fôlego (PF)

**Fôlego não é vida e não é energia de ação. É a sua capacidade de continuar inteiro.** Ele paga defesa, esforço extremo e teimosia. Bater não custa nada — o que custa é não ser atingido.

- **Fôlego máximo = Vigor + 7** (resulta em 8–11).

### Tabela de custos

| Ação | Custo |
|---|---|
| Mover-se normalmente no seu turno | 0 |
| **Ataque simples** | **0** |
| **Ataque pesado** (exige arma Peso 2) | **1** |
| Disparo | 1 |
| Correr, levantar-se, arrombar, usar item sob pressão | 1 |
| **1ª defesa da rodada** | **1** |
| **2ª defesa da rodada** | **2** |
| **3ª defesa em diante** | **3** |
| Habilidades | conforme a habilidade |

O contador de defesas zera no início do seu turno. Ferimentos aumentam custos (seção 3).

**Consequência central:** estar cercado é matematicamente letal. Dois inimigos batendo em você custam 3 PF por rodada só para você não ser ferido — e eles não pagam nada para atacar. **Controlar quantos te alcançam é a decisão tática mais importante do jogo.**

### Defesa (reação, opcional)
- Rolagem: 3d6 + **proficiência da arma empunhada** (aparar) ou **Acrobacia** (esquivar) − Ameaça. Sucesso = ataque evitado. O Fôlego é gasto mesmo se a defesa falhar.
- Pode escolher não defender (não gasta nada, sofre o resultado). Às vezes é a escolha certa.

### Quebrado (0 PF)
- **Não defende e não age.** Só pode **andar** e **Retomar Fôlego**.
- Ataque simples custa 0, mas exige ter Fôlego: quem está Quebrado não ataca.
- É por isso que drenar o Fôlego do inimigo não é dano desperdiçado — **é desarmá-lo**.

### Retomar Fôlego
- **Ação de turno inteiro.** Pode ser feita engajado com inimigo (perder o turno já é punição suficiente). Ainda pode defender nessa rodada, pagando o custo normal.
- Recupera **4 − Peso de carga (armadura + escudo)**, mínimo 1.
- Torso com Ferimento Grave: recupera **apenas 1**. Sangrando: recupera **apenas 1**.

### Último Fôlego
- **Não é universal — é habilidade especial.** Ver seção 12.

## 3. Ferimentos

### Filosofia (regra de ouro para o mestre)

**Ferimento deve criar situação, não penalidade numérica.** Antes de inventar um efeito, prefira, nesta ordem: *não consegue mais fazer X* > *X passa a custar mais Fôlego* > *precisa de ajuda, apoio ou equipamento para X* > *−1/−2 em rolagens*. O estado físico dos personagens deve mudar as decisões da mesa, não só a conta do dado.

### Estrutura: Local × Gravidade × Tipo

- **Local:** cabeça, torso, braço, perna. Quando o atacante não escolhe, role d6 → **1 cabeça | 2–3 torso | 4 braço | 5–6 perna** (o alvo diz qual braço/perna).
- **Gravidade:** Leve ou Grave. É o que carrega o peso mecânico.
- **Tipo:** cortante, perfurante ou contusão. Peso narrativo e condições associadas (seção 3.3). Uma perna cortada e uma perna quebrada limitam a mesma coisa — o que muda é o tratamento e o que vem junto.

**Vira Grave direto:** 2º ferimento no mesmo local | golpe decisivo de ataque pesado | tiro decisivo | crítico (18 natural).

### 3.1 Efeitos por local

| Local | Leve | Grave |
|---|---|---|
| **Braço** | Ações com esse braço custam +1 PF | Braço inutilizado; derruba o que segurava; armas de duas mãos ficam fora de uso |
| **Perna** | Não corre; deslocamento reduzido à metade | Só se move apoiado ou rastejando; defesas custam +1 PF |
| **Torso** | +1 PF em TODA ação que custe Fôlego | Retomar Fôlego recupera só 1; sem Último Fôlego |
| **Cabeça** | Tonto e desorientado: **−2 em todas as rolagens** | Inconsciente |

### 3.2 Queda e morte (Resistência)

- **Base igual para todos.** O personagem cai fora de combate ao acumular:

| Acumulou | Resultado |
|---|---|
| 2 Ferimentos Graves | cai |
| 3 Ferimentos Leves | cai |
| 1 Grave + 2 Leves | cai |
| Grave na cabeça | cai na hora, a qualquer momento |

- Habilidades especiais mexem nisso — é assim que um personagem é "mais resistente", sem atributo derivado. Na v4 quem faz isso é **Não Cai** (você não cai: continua de pé até o fim da cena e desaba depois) e **Pele de Ferro** (Aparo 2 natural, sem armadura).
- **Cair ≠ morrer.** Morte: sofrer novo Ferimento Grave estando inconsciente; Sangramento chegar a 0 sem socorro; golpe de misericórdia.

### 3.3 Condições por tipo de dano

**Sangramento — FECHADO.**
- **Fontes:** Ferimento Grave cortante ou perfurante. Em golpe decisivo cortante, o atacante pode escolher aplicar Sangramento em vez de escolher o local.
- **Contador: começa em 6.** No fim de cada rodada, reduz 1. **Ao chegar a 0: inconsciente**, e morre em minutos sem socorro.
- **Enquanto sangra, o corpo não se recompõe:** Retomar Fôlego recupera apenas 1, e a recuperação fora de combate (seção 8) não funciona até o sangramento ser estancado.
- **Estancar**: ação de turno inteiro com pano/curativo em mãos. Sob pressão (em combate), exige teste de **Medicina − Ameaça**. Fora de combate, automático com material.
- Vários sangramentos = um contador cada; estanca-se um por ação.
- *Por que 6 e não 3: o contador precisa sobreviver ao combate. A urgência boa é a de depois da luta — carregar o ferido, achar o curativo, decidir se para ou continua.*

**Propostas ainda não fechadas** (não usar no piloto sem combinar na mesa):
- **Fratura** (contusão): o membro não aguenta carga. Direção — Grave contuso em braço/perna impede não só usar, mas apoiar, carregar peso e ser tratado sem tala.
- **Corpo Estranho** (perfurante): algo ficou dentro. Direção — o ferimento não pode ser tratado antes de remover, e remover em campo custa Exaustão ou piora a gravidade.
- **Trauma** (contusão na cabeça): direção — confusão que atrapalha a *cena*, não a rolagem: esquece o que ia fazer, não reconhece quem está falando, perde a noção de tempo.

## 4. Exaustão

**Ganha 1 ponto ao**: terminar um combate Quebrado (fonte universal de combate); usar habilidades que forçam o corpo (seção 12); falhar em Sangue Frio num gatilho de horror; passar um dia sem comida, água ou sono; marcha forçada, frio ou calor extremo sem proteção.

**Efeitos:**

| Nível | Efeito |
|---|---|
| Cada ponto | **−2 Fôlego máximo** |
| Teto de Exaustão = **Vontade + 1** | No teto o personagem está **Esgotado**: sem ataque pesado, sem habilidades que custem Exaustão |
| Ganhar Exaustão acima do teto | **Colapso**: desmaia; só volta a funcionar abaixo do teto |

**Recuperação**: 1 ponto por dia de descanso real (abrigo + comida + água + noite de sono). Conforto de cidade (cama, comida quente, segurança): 2 por dia. Descanso ruim (relento, ração pela metade): 0.

*Leitura para o mestre: a −2 por ponto, a Exaustão é o preço explícito de continuar na estrada. Um personagem com Vontade 2 e teto 3 pode perder 6 do Fôlego máximo — mais da metade. É esse número que faz a viagem de volta valer tanto quanto o combate.*

## 5. Estrutura do combate

- **Iniciativa**: os jogadores agem primeiro, salvo emboscada (Percepção/Alerta decide se o grupo foi surpreendido — surpresos, os inimigos agem primeiro e a 1ª defesa da rodada custa 2). Dentro do grupo, ordem livre.
- **Turno**: mover + 1 ação + reações (defesas, quando atacado).

### Ataques corpo a corpo

- **Ataque simples (0 PF)** — **desgasta**. Fraco: o alvo perde **1 + Peso da arma** de Fôlego. Decisivo: perde **2 + Peso**.
- **Ataque pesado (1 PF)** — **fere**. Exige **arma de Peso 2** e a proficiência correspondente. Fraco: **Ferimento Leve** (rola local). Decisivo: **Ferimento Grave no local à escolha**. Arma cortante em decisivo: pode trocar a escolha de local por Sangramento.
- **Ferir com arma leve**: contra alvo **Quebrado, caído, imobilizado ou desprevenido**, um ataque simples causa **Ferimento Leve** (rola local) em vez de drenar. É o fecho do ciclo: *desgasta primeiro, fere depois*.
- **Sem proficiência**: rola sem bônus e não pode fazer ataque pesado.

### Peso das armas

| Peso | Armas | Ataque pesado |
|---|---|---|
| 0 | Faca, soco-inglês, coronhada, porrete leve | não |
| 1 | Facão, machadinha, baioneta, pá afiada, sabre, azagaia | não |
| 2 | Marreta, picareta, machado grande, macuahuitl, **lança pesada de caça** | **sim** |

*Consequência de design: armas leves não ferem alguém de pé e inteiro. Elas drenam. Quem luta de faca precisa de vantagem — cercar, derrubar, pegar desprevenido, esperar o cara quebrar. Quem carrega uma marreta fere, mas paga em Peso e em velocidade. Isso é intencional. Vigiar no piloto (seção 11).*

## 6. Armas de fogo

- **Disparo (1 PF)**: 3d6 + Armas de Fogo − Ameaça. Fraco = **Ferimento Leve** (rola local) | Decisivo = **Ferimento Grave no local à escolha** | Falha = erra e gasta a munição. Contra Ralé: qualquer acerto derruba.
- **Não existe esquivar de bala.** O recurso defensivo é **cobertura**: leve (caixote, esquina) = −2 na rolagem do atirador; pesada (muro, rocha) = sem linha de tiro.
- **Inimigo atirando num jogador**: em cobertura = o tiro não pega (salvo flanqueado). Exposto = pode gastar 1 PF e testar **Atletismo − Ameaça** para se jogar (sucesso: evita, fica caído); senão sofre **Ferimento Leve** no local rolado — **Grave** se pegar a cabeça ou se for espingarda à queima-roupa.
- **Aparo contra bala**: 1 ponto nega um Leve ou reduz Grave → Leve (a peça é destruída).
- **Recarga**: revólver — até 5 tiros, **não recarrega em combate**; rifle/espingarda — 1 turno (1 PF); besta anã — recarrega de graça no próprio turno, mas fere pouco à distância.
- **Munição conta.** Cada tiro é riscado da ficha.
- **Rifle de repetição** (raro, militar): 5 tiros no carregador — acionar a alavanca já está incluído no disparo. Encher o carregador é 1 turno (1 PF).

### 6.1 Bestas

A arma de projétil tensionado deste mundo é a **besta** — mecanismo, gatilho, peça de guilda. É o que sobreviveu à industrialização porque é fabricável e a munição se recupera. Arco é coisa de povo sem oficina, e nenhum dos povos do cenário atual depende dele. **Nenhum personagem do piloto carrega besta**; a regra existe para quando aparecer numa mão inimiga ou numa loja.

Não é arma de fogo: **não emperra**, e o virote às vezes volta.

- **Disparo (1 PF)**: 3d6 + Arcos e Bestas − Ameaça.
- **Fraco**: o alvo perde **2 de Fôlego** (desgasta, como corpo a corpo).
- **Decisivo**: **Ferimento Leve** no local à escolha. **Grave** se for besta pesada, ou à queima-roupa.
- **Cobertura** protege igual à das armas de fogo, e vale o mesmo −2 para cobertura leve.
- **Recarga**: besta comum, 1 turno (1 PF); besta anã, de graça no próprio turno.
- **Falha crítica (3 natural)**: a corda solta ou o virote se perde — nada emperra.

*Por que fere menos que a bala: a arma de fogo é o item raro e caro do cenário e precisa continuar assustando. A besta é o que se leva quando não se pode gastar munição — e a diferença é justamente que ela desgasta antes de ferir.*

## 7. Armadura, escudo e reparo

| Equipamento | Aparo | Peso |
|---|---|---|
| Nenhuma | 0 | 0 |
| Leve | 1 | 0 |
| Média | 2 | 1 |
| Pesada | 3 | 2 |
| Escudo | +1 | +1 |

- **Aparo**: ao sofrer um Ferimento, o jogador PODE gastar: **1 ponto → nega um Leve** | **2 pontos → negam um Grave** | **1 ponto → reduz Grave para Leve**. Ponto gasto = peça danificada.
- **Peso** reduz o Retomar Fôlego (4 − Peso) **e subtrai das rolagens de Furtividade, Acrobacia e Atletismo** (Peso 1 = −1, Peso 2 = −2), quando a situação envolver silêncio, agilidade ou fôlego prolongado. Isso inclui **esquivar**: quem usa armadura pesada apara, não esquiva.
- **Reparo**: no acampamento, teste de Mecânica + sucata = recupera 1 Aparo por descanso. Oficina de cidade = restaura tudo, pagando.

## 8. Recuperação fora de combate

- **Fôlego**: fora de perigo, **2 minutos de descanso** restauram ao máximo (já descontada a Exaustão). Não funciona enquanto houver Sangramento não estancado.
- **Ferimentos**: tratado o ferimento (curativo; Grave exige kit médico + Medicina), **o corpo fecha 1 ferimento por dia de descanso**: Grave → Leve em 1 dia, Leve → curado em 1 dia. Sem tratamento, não melhora — e Grave sem tratamento infecciona: +1 Exaustão por dia.
- **Itens**: curativo (trata Leve, estanca sangramento) | kit médico (necessário para Grave).

## 9. Inimigos

Ficha mínima: **Ameaça + Fôlego + arma**. Só isso precisa estar escrito.

### Régua de Ameaça
1 civil valente | 2 bandido, saqueador | 3 soldado veterano | 4 matador de elite | 5 monstro raro | 6 não se resolve com rolagem direta (exige tática, grupo, equipamento).

### O Fôlego do inimigo é um recurso, não uma barra de vida

O inimigo funciona pela mesma economia dos jogadores:
- **Ataque simples: 0 PF** — dreno no jogador que não se defender (1 + Peso da arma).
- **Ataque pesado: 1 PF** — Ferimento no jogador que não se defender. Exige arma Peso 2.
- **Habilidade especial: 1–2 PF.**
- **Retomar Fôlego**: turno inteiro, recupera 4 − peso. O mestre pode e deve usar — telegrafa que o inimigo está mal.
- **Quebrado (0 PF): não ataca mais.** É o momento de matar.

### Ferimentos no inimigo = Ameaça caindo

| Estado do inimigo | Efeito |
|---|---|
| Cada **Ferimento Leve** | **−1 Ameaça** |
| Cada **Ferimento Grave** | **−2 Ameaça** + efeito do local |
| **Quebrado** (0 PF) | **−2 Ameaça**, não age |

Ameaça nunca cai abaixo de 0. Os efeitos somam.

**Efeito do local no Grave (inimigo):** braço → derruba a arma | perna → não persegue nem recua, fica onde está | torso → não pode Retomar Fôlego | cabeça → fora de combate na hora.

Por que funciona: Ameaça é o único número que o mestre segura de cabeça, e é o mesmo número que os jogadores subtraem para atacar **e** para se defender. Ferir o inimigo torna ele mais fácil de acertar e mais fácil de aparar ao mesmo tempo.

### Os três tipos

**Ralé** — capangas, saqueadores, soldados de linha.
- Só Fôlego. **Qualquer Ferimento tira da luta na hora** (Leve = caído, fugindo, gritando; Grave = morto ou morrendo).
- A 0 PF: fora de combate (foge, se rende, desaba).
- **Fôlego padrão: 4.** Fraco (faminto, civil armado): 3. Duro (soldado, capanga veterano): 6.

**Nomeado** — o capataz, o pregador, o mercenário com nome.
- **Fôlego = 10 + Ameaça.**
- Ferimentos contam individualmente, como os dos jogadores. **Cai no 2º Ferimento Grave** (ou Grave na cabeça).
- A 0 PF fica **Quebrado** — sem ataque, sem defesa efetiva, Ameaça −2.
- Pode ter Aparo (armadura) e 1–2 habilidades.
- **Moral**: um Nomeado Quebrado ou com 1 Grave raramente luta até o fim. Foge, se rende, negocia. Isso é do tom do mundo.

**Coisa** — aberrações, máquinas antigas, o que sai das ruínas.
- **Fôlego 20+**, não Retoma Fôlego, não sente moral.
- Regras próprias: pode ser imune a dreno de Fôlego (não se cansa) e só cair por Ferimentos; pode ignorar Ferimentos em certos locais; pode ter um ponto vulnerável que aceita Grave direto.
- Regra de ouro: toda Coisa tem **uma** exceção escrita na ficha, não cinco.
- **Uma Coisa não é encontro de rotina.** Ver seção 13.

## 9.5 Inimigos não são bonecos

### A regra que restringe tudo

**O mestre não rola.** Uma habilidade de inimigo, portanto, só pode fazer uma destas três coisas:

1. **custar Fôlego dele** para produzir um efeito;
2. **mudar quanto o jogador paga ou rola**;
3. **mudar a posição** de alguém.

Se a ideia exige uma rolagem do mestre, ela está errada para este sistema — reescreva como custo ou como pressão.

**Regra do telegrama:** o jogador não tem teste para descobrir o que o inimigo sabe fazer. Então a habilidade aparece na ficção **uma batida antes** de acontecer. "Ele para de trocar golpes e começa a rodear." "O pregador levanta a mão e os dois de trás avançam." Habilidade que surpreende sem aviso é o mestre jogando contra a mesa.

---

### A. Táticas — valem para qualquer inimigo e custam 0

Não são habilidades. São decisões de mestre, e são o que separa um encontro vivo de quatro bonecos batendo.

- **Cercar.** Dois inimigos no mesmo personagem fazem a defesa custar 1 + 2 = **3 PF por rodada**. É a coisa mais letal do sistema e não exige regra nenhuma.
- **Foco no mais fraco.** Bater em quem já está sangrando o Fôlego em vez de espalhar. **O mesmo encontro de 6 sai de 0,50 para 3,97 ferimentos e 1 personagem caído** (seção 9, simulação). É a alavanca mais forte que o mestre tem — use consciente, não por acidente.
- **Revezar.** Quem atacou muito recua uma fileira e entra quem está inteiro. Nunca deixe o grupo drenar os mesmos quatro.
- **Cortar o fôlego.** Alguém sempre engaja quem parou para Retomar Fôlego. Retomar é permitido engajado, mas quem está sendo atacado ainda paga defesa — o turno "de descanso" vira o turno mais caro.
- **Fechar a saída.** Um inimigo na porta, na escada, no corredor. Transforma "vamos embora" numa decisão cara.
- **Assobio.** Ele chama mais gente. Não precisa chegar ninguém — o relógio já mudou o comportamento da mesa.
- **Cobrar o preço da armadura.** Terreno ruim, água, subida, perseguição. Quem carrega Peso 2 recupera 2 de Fôlego e rola −2 em Atletismo.

**Ralé não recebe habilidade.** A ficha mínima (Ameaça + Fôlego + arma) é uma vantagem: o mestre segura seis inimigos de cabeça. O que faz a Ralé assustar é a lista acima.

---

### B. Ações comuns — qualquer inimigo pode, pagando Fôlego

Um vocabulário curto para o mestre ter verbos além de "eu ataco".

| Ação | Custo | O que muda para o jogador |
|---|---|---|
| **Agarrar** | 1 PF | O alvo não se move e suas defesas custam **+1** enquanto estiver preso. Soltar-se é uma ação + teste de Força Bruta ou Acrobacia − Ameaça |
| **Derrubar** | 1 PF | Alvo caído: defesas custam **+1**, e levantar-se é uma ação (1 PF) |
| **Desarmar** | 1 PF (no lugar do ataque) | O alvo perde a arma. **Sem arma não se apara** — só esquivar (Acrobacia), e quem está de armadura pesada rola −2 nisso |
| **Investida** | 1 PF | Fecha a distância e ataca no mesmo turno. Quem não se defender também é derrubado |
| **Bloquear** | 0 PF (reação) | Ninguém atravessa a posição dele sem sofrer um ataque primeiro |
| **Empurrar para o perigo** | 1 PF | Fogo, buraco, beira, maquinário, linha de tiro do companheiro. O dano é do cenário, não dele |

---

### C. Habilidades de Nomeado — uma ou duas por ficha, nunca mais

Escolha pensando no que você quer que a mesa **faça**, não no que o inimigo sofre. Cada uma cabe numa linha da ficha.

| Habilidade | Custo | Efeito | O que ela força |
|---|---|---|---|
| **Grita Ordens** | 1 PF | Dois Ralé atacam imediatamente, fora do turno deles | Matar o Nomeado primeiro vira prioridade real |
| **Lê a Guarda** | passiva | A **primeira** defesa contra ele em cada rodada custa 2 em vez de 1 | Não dá para trocar golpe com ele indefinidamente |
| **Não Solta** | 1 PF | Agarra, e enquanto agarrado o alvo **não pode Retomar Fôlego** | Alguém tem que ir tirar o companheiro dali |
| **Mira no Ferido** | passiva | Contra alvo que já tem Ferimento, os ataques dele **ferem mesmo com arma leve** | O grupo precisa cobrir o ferido em vez de continuar atacando |
| **Segunda Onda** | 1× por combate | Retoma Fôlego como ação livre, sem perder o turno | Desfaz o trabalho de desgaste — e telegrafa: ele respira fundo e volta |
| **Escudo Humano** | 1 PF | Transfere um ataque recebido para um Ralé adjacente | Isolar ele antes de atacar |
| **Aguenta Calado** | passiva | O primeiro Ferimento **Leve** não derruba a Ameaça dele | Tira o feedback do grupo por uma rodada: parece que não está funcionando |
| **Recuo Calculado** | 0 PF | Ao ficar Quebrado, ele foge — e volta em outra cena | Deixa dívida em aberto em vez de fechar o encontro |
| **Chuta a Lamparina** | 1 PF | Apaga a luz, derruba a fumaça, fecha a porta | Muda a cena inteira sem tocar em ninguém |

Regra de contenção: **uma habilidade de Nomeado nunca some com o turno do jogador.** Ela encarece, reposiciona ou obriga a mudar de alvo. "Perde a vez" não é interessante para ninguém.

---

### D. Coisas — a exceção única

Coisa não tem habilidade: tem **uma** exceção escrita na ficha, e ela é o quebra-cabeça do encontro.

- **Não se cansa** — imune a dreno de Fôlego. Só cai por Ferimento.
- **Não sente** — Ferimento não derruba a Ameaça dela. O grupo perde o termômetro.
- **Membros demais** — Grave em perna ou braço não tira nada de função.
- **Sem cabeça** — o golpe que encerraria a luta não existe aqui.
- **Ponto vulnerável** — um lugar específico aceita Grave direto de qualquer arma. Descobrir isso é a vitória; o resto é sobreviver até descobrir.
- **Cresce** — a cada Ferimento que sofre, +1 de Ameaça em vez de −1. Fugir é a resposta certa.

---

### Fichas prontas para o piloto

| Inimigo | Tipo | Ameaça | Fôlego | Arma / notas |
|---|---|---|---|---|
| Cão-de-ruína (matilha) | Ralé | 1 | 3 | Mordida (Peso 0). Vem em número, cerca. |
| Saqueador | Ralé | 2 | 4 | Facão (Peso 1) |
| Saqueador com marreta | Ralé | 2 | 4 | Marreta (Peso 2) — este fere de verdade |
| Capanga veterano | Ralé | 3 | 6 | Sabre (Peso 1), Aparo 1 |
| Pregador da Igreja | Nomeado | 3 | 13 | Marreta (Peso 2), Aparo 1. **Grita Ordens** + **Aguenta Calado**. Fala enquanto luta. |
| Capataz da mina | Nomeado | 4 | 14 | Espingarda + picareta (Peso 2), Aparo 2. **Não Solta** + **Recuo Calculado** |
| Coisa do poço | Coisa | 4 | 24 | Imune a dreno de Fôlego. Só cai por Ferimentos. Sem cabeça. |

### Calibragem de encontro (regra de bolso)
Grupo de 4 personagens: **um Ralé de Ameaça 2 por jogador** é uma luta séria de 3 a 5 rodadas. **Um Nomeado + metade dessa Ralé** é um combate de sessão. **Dois Nomeados** já é ameaça de morte.

### ⚠ Arme a oposição com Peso 2 (consequência direta da v2)

Como ataque pesado agora exige arma **Peso 2**, um inimigo de facão **não consegue ferir ninguém**: ele só drena Fôlego. Se toda a Ralé vier de arma leve, o sistema de Ferimentos simplesmente não dispara — a luta vira contabilidade.

Simulação de 10.000 combates, 4 personagens × 4 Ralé de Ameaça 2 (Fôlego 9, competência +2):

| Ralé com arma Peso 2 | Rodadas | Ferimentos no grupo | Personagens caídos |
|---|---:|---:|---:|
| 0 de 4 | 5,3 | **0,02** | 0,00 |
| 1 de 4 | 5,3 | 0,08 | 0,00 |
| **2 de 4** | 5,2 | **0,58** | 0,00 |
| 4 de 4 | 4,9 | 2,80 | 0,12 |

**Regra de bolso: pelo menos metade da Ralé carrega marreta, picareta, lança pesada ou machado — ou tem arma de fogo.** Facão é para quem cerca e desgasta; a marreta é quem machuca. Isso também é bom no ficcional: o saqueador da marreta é a ameaça que a mesa aprende a identificar e a matar primeiro.

### Número não substitui armamento

A pergunta óbvia é se dá para resolver o mesmo problema jogando mais inimigos na mesa. Dá — mas por outro caminho e por um preço. Mesma simulação, 4 personagens, Ralé toda de facão:

| Inimigos | Rodadas | Ferimentos no grupo | PJs caídos | Turnos gastos Quebrado |
|---:|---:|---:|---:|---:|
| 4 | 5,3 | 0,01 | 0,00 | 0,3 |
| 5 | 6,7 | 0,12 | 0,00 | 1,4 |
| **6** | **8,5** | **0,50** | 0,01 | 3,7 |
| 7 | 10,8 | 1,44 | 0,05 | 7,6 |
| 8 | 14,5 | 3,55 | 0,41 | 13,1 |
| 10 | 28,1 | 10,91 | 3,37 | 17,6 |

**Seis facões produzem o mesmo tanto de ferimento que quatro inimigos com duas marretas — em 60% mais rodadas.** E o ferimento chega por outra via: não vem do golpe, vem do colapso (Fôlego → Quebrado → ferido). A coluna da direita é o custo escondido: são turnos em que o jogador não decide nada, só Retoma Fôlego.

**Foco de fogo é a variável mais forte do sistema.** Os números acima assumem inimigos espalhando ataques. Se o mestre concentrar no personagem mais fraco, o encontro de **6 salta de 0,50 para 3,97 ferimentos e 1 personagem caído**. O mesmo encontro no papel é trivial ou letal conforme uma decisão de mesa — é o pilar "estar cercado é letal" funcionando, mas exige que o mestre saiba que está puxando essa alavanca.

**Conclusão prática:** armamento controla *quanto machuca*; número controla *quanto dura e quanto desgasta*. Faixa boa: **1 a 1,5 inimigos por jogador, com pelo menos um terço em arma Peso 2**. Acima de 1,5 por jogador sem nenhuma arma pesada, você não tem uma luta difícil — tem uma luta longa.

## 10. Fôlego fora de combate

- Antes de uma rolagem crítica, declarado antes de rolar: gastar **1 PF = +1 na rolagem** (máx. 1 por teste).

## 11. Observar no piloto

1. **Ataque simples de graça (a mudança mais arriscada da v2).** Fôlego agora só sai para defesa e esforço. Se as lutas 1×1 arrastarem, o conserto é **baixar o Fôlego máximo para Vigor + 5**, não devolver custo ao ataque — o custo era o que fazia o jogador ficar parado sem opção.
2. **Ataque pesado só com Peso 2.** Duas coisas a vigiar: se quem escolheu arma leve está frustrado, e se os Ferimentos estão aparecendo (ver a tabela de simulação na seção 9 — se a oposição não tiver Peso 2, não aparecem). Válvulas, em ordem de preferência: (a) armar mais inimigos com Peso 2; (b) ampliar o "ferir alvo em desvantagem" para alvo apenas flanqueado; (c) só em último caso, deixar o **decisivo (15+) com arma leve causar Ferimento Leve** — testado em simulação, encurta a luta em ~1 rodada e devolve o caminho de ferir para quem usa faca.
3. **Cai no 2º Grave.** Combinado com Grave direto no decisivo, dois golpes bem-sucedidos derrubam um personagem. Se virar carnificina, o ajuste é restringir o Grave direto, não subir a Resistência.
4. **Cabeça Leve a −2.** É o ferimento mais duro do jogo por larga margem. Se dominar tudo, trocar por −1 e um efeito de situação (perde a noção de onde estão os inimigos).
5. **Exaustão a −2 por ponto com teto Vontade+1.** É o número que define o ritmo da viagem. Calibrar pela taxa de recuperação, não removendo fontes.
6. **Fôlego de Nomeado (10 + Ameaça).** Com ataque de graça, o chefe drena mais rápido. Se cair fácil demais, subir para 14 + Ameaça — nunca subir a Ameaça.
7. **Sangramento 6 + bloqueio de recuperação**: mede se a pressão pós-combate aparece de verdade ou se vira só contabilidade.
8. **Defesa: aparar vs esquivar.** Com a penalidade de Peso em Acrobacia, a escolha ficou ligada à armadura. Ver se ainda existe decisão real.

## 12. Habilidades no piloto

Catálogo completo e filosofia em `habilidades.md` (**v4**). Padrão de criação: **1 Passiva + 1 Ativável**, validadas pela origem que o jogador descreveu.

A v4 subiu o teto de propósito — habilidade agora **quebra regra sob condição visível**, em vez de dar +1. As que tocam diretamente as regras acima:

| Habilidade | Regra que ela quebra |
|---|---|
| **Ponto Fraco** | arma leve fere alvo de pé e inteiro, em decisivo (é a válvula (c) da seção 11, entregue a um personagem em vez de virar regra geral) |
| **Pele de Ferro** | Aparo sem armadura, sem Peso, auto-reparável |
| **Não Cai** | a contagem de queda da seção 3.2 fica suspensa até o fim da cena |
| **Trespassar** | um ataque, dois alvos |
| **Segunda Lâmina** | ataque de graça encadeado a cada inimigo que sai da luta |
| **Muralha / Instrução Militar** | atacam de frente o pilar "estar cercado é letal" — ver o aviso na seção 11 |
| **Estopim** | +2 de dreno e imunidade a Leve, ao preço de não poder defender nem Retomar Fôlego |
| **A Hora É Essa** | Ferimento Grave com qualquer arma, sem rolagem, contra alvo já fora de forma |
| **Último Fôlego** | ação livre para recuperar 3 PF, mesmo engajado |

**O que continua verdade:** sem habilidade, a única saída do Quebrado é **Retomar Fôlego**. Criar espaço, empurrar, derrubar e fechar portas continua valendo tanto quanto bater.

**Aviso de calibragem:** nenhuma habilidade da v4 passou pelo simulador ainda. A lista de riscos conhecidos está no fim de `habilidades.md` ("Vigiar no piloto"), com o conserto previsto para cada uma.

## 13. Horror na mesa (frequência)

Regra de frequência, não de mecânica. O mundo é perigoso de forma mundana; o sobrenatural é raro e caro.

| Camada | Frequência esperada |
|---|---|
| Perigo cotidiano (fome, sede, clima, animais, bandidos) | toda sessão |
| Perigo regional (tribos, escravagistas, predadores grandes) | sessão sim, sessão não |
| Ruínas (máquinas antigas, armadilhas, sistemas desconhecidos) | por arco |
| Corrupção (sinais de que algo está errado) | por arco, como pista |
| Horror (um Corrompido, um fenômeno incompreensível) | uma vez, e a mesa lembra |

**Um Corrompido não é um encontro. É um acontecimento.** Se aparecer um, a pergunta que a mesa deve fazer é "*por que existe um aqui?*", não "*como matamos isso?*". Ver `Mundo/visao-geral-do-mundo.md`.

**Sangue Frio**: testes em gatilhos pontuais (ver o que um Corrompido é por dentro, entrar num espaço que não obedece à geometria, reconhecer alguém dentro da criatura). Falha custa 1 Exaustão e um estado discreto e temporário. Sem barra mental — decidido.
