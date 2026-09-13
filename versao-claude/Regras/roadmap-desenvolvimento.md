# Roadmap de Desenvolvimento do Sistema

Ordem lógica de desenvolvimento. Cada bloco depende dos anteriores — resolver fora de ordem gera retrabalho. Status: ✅ fechado | 🔶 parcial | ⬜ não iniciado.

**Atualizado em 28/08/2026** (regras v2 + cânone de mundo).

---

## Fase 1 — Fundação (o que o jogo É)

### 1.1 Pilares de experiência ✅
- Difícil mas não frustrante; ferido = realmente ferido; poucas habilidades, muito impactantes; combate perigoso e rápido; ciclo explorar → sofrer → recuperar → explorar.
- Só jogadores rolam; o mestre pensa um número (Ameaça).

### 1.2 Resolução central ✅
- 3d6 + bônus de competência − Ameaça.
- Resultado: ≤9 falha | 10–14 sucesso fraco | 15+ sucesso decisivo.
- Fonte única de bônus: só a competência entra na rolagem. Atributos NUNCA somam na rolagem.

---

## Fase 2 — Chassi do personagem (quem o personagem É)

### 2.1 Atributos ✅ (função) / 🔶 (derivados exatos)
Escala 1–4. Cinco atributos:

| Atributo | Deriva |
|---|---|
| Vigor | Fôlego máximo, Resistência (nº de Ferimentos) |
| Agilidade | Defesa (elaborar) |
| Percepção | Alerta (passivo vs surpresa/emboscada), possivelmente Iniciativa |
| Intelecto | Largura da pirâmide de competências |
| Vontade | Altura da pirâmide; limite de Exaustão antes do colapso; pré-requisito de habilidades de determinação |

**Vontade — decisões fechadas:** NÃO gera pool/barra mental (nenhum recurso novo para gerenciar). Seu peso mecânico vem de: (a) altura da pirâmide; (b) teto de Exaustão suportável — resolve a pendência antiga do limite de Exaustão; (c) pré-requisito para habilidades que forçam o corpo além do limite (Último Fôlego, ignorar Ferimentos), cujo custo é pago em Exaustão. Estresse/medo, quando falhados em Sangue Frio, também custam Exaustão — sem subsistema separado.
**Risco a monitorar:** Exaustão vira moeda universal (esforço + ferimento forçado + medo + privação). Se saturar, calibrar pela taxa de recuperação, não removendo fontes.

**Pendente:** fórmulas exatas de cada derivado (quanto Fôlego por Vigor etc.) — depende do bloco de combate (4.x).

### 2.2 Competências ✅
- Quatro ranks: Aprendiz +1, Prático +2, Profissional +3, Mestre +4.
- Faixa de Ameaça jogável resultante: 1–5. Ameaça 6 = "não se resolve com rolagem direta" (exige tática, grupo, equipamento, Fôlego).
- Estrutura de pirâmide (sem distribuição de pontos):
  - **Largura** (nº total de competências) = 3 + Intelecto.
  - **Altura** (nº de competências em Profissional/Mestre) = Vontade.
  - **Âncora**: cada competência é ligada a um atributo; rank máximo = atributo âncora + 1. Mestre exige atributo 3+.
- Criação: 1 Profissional, 2 Práticos, resto Aprendiz. Mestre só em jogo.
- Lista completa e âncoras: `competencias.md`. Questões residuais (sobreposições, Erudição) ficam registradas lá e se resolvem em jogo.

### 2.3 Origens ⬜ ← **PRÓXIMO PASSO**
- Função definida (proficiências, conhecimentos, equipamento inicial, possivelmente 1 habilidade). Conteúdo não iniciado.
- Depende de: 2.2 (fechado). Desbloqueado — é o último buraco do chassi antes da ficha.

---

## Fase 3 — Validação matemática do núcleo

### 3.1 Régua de Ameaça calibrada ✅
- Tabela rank × Ameaça e descrições fechadas em `regras-partida-piloto.md` (seções 1 e 9).

### 3.2 Playtest de mesa seco (sem combate) ⬜
- Testar criação de ficha + testes simples antes de integrar combate.

---

## Fase 4 — Combate (subsistema, chat separado)

### 4.1 Reconciliar combate com o novo chassi ✅
- Feito em `regras-partida-piloto.md` v1 e revisado na **v2 (28/08)**: Fôlego virou moeda de resistência (ataque simples 0 PF), ataque pesado restrito a arma Peso 2, Resistência cai no 2º Grave, Exaustão −2 por ponto com teto Vontade+1, Sangramento 6 travando recuperação, Peso da armadura descontando de Furtividade/Acrobacia/Atletismo.
- Novo eixo de Ferimento: **Local × Gravidade × Tipo**. Sangramento fechado; Fratura, Corpo Estranho e Trauma seguem como propostas.

### 4.2 Fôlego fora de combate ✅
- 1 PF = +1 na rolagem, declarado antes, 1× por teste. Recuperação: 2 minutos fora de perigo (bloqueada por Sangramento).

### 4.3 Resistência mental 🔶
- SEM pool. Testes pontuais de Sangue Frio em gatilhos; falha custa Exaustão e/ou estado discreto temporário.
- Horror é elemento do cenário, não gênero definidor — frequência baixa, impacto pontual.
- Gatilhos esboçados em `regras-partida-piloto.md` seção 13 e a frequência de horror está no cânone de mundo. Pendente: catálogo de estados temporários.

---

## Fase 5 — Habilidades e progressão

### 5.1 Grafo de habilidades 🔶
- Premissas fixadas: sem classes/árvores; requisitos mecânicos + narrativos + de equipamento; categorias só para organização de ficha; toda habilidade precisa de origem plausível (aprendeu/sobreviveu/nasceu/treinou/descobriu).
- Atributos como pré-requisitos: distribuir entre atributos para nenhum virar pedágio universal.
- 11 habilidades iniciais escritas em `habilidades.md` (sincronizadas com a v2). Falta o grafo propriamente dito: o que cada uma abre.

### 5.2 Progressão ⬜
- Como se ganha ranks e habilidades (marcos? XP?). Sem inflação numérica — progressão via capacidades novas.
- Depende de: 5.1.

---

## Fase 6 — Mundo mecânico

### 6.1 Equipamento e economia ⬜ (armas/armaduras 🔶 no chat de combate)
### 6.2 Ciclo de sobrevivência ⬜ (recuperação, Exaustão, custo de ficar parado)
### 6.3 Bestiário / fichas de inimigos 🔶 (estrutura definida + 7 fichas prontas no piloto; Corrompidos removidos das fichas comuns por decisão de lore de 28/08)

---

## Fase 7 — Consolidação

### 7.1 Ficha de personagem ⬜
### 7.2 Documento de regras v0.2 ⬜ (substituir "Sintese Desatualizada.txt")
### 7.3 Aventura piloto + playtest real ⬜ (conceito já existe: escolta para vila isolada)

---

## Próximos 3 passos concretos

1. **Rodar o piloto** e preencher a seção 11 de `regras-partida-piloto.md`. Os oito pontos de observação da v2 só se resolvem na mesa — não adianta continuar ajustando no papel.
2. **Origens** (2.3) — último buraco do chassi; trava a ficha de personagem (7.1).
3. **Fechar as condições de tipo de dano** (Fratura, Corpo Estranho, Trauma) — só depois de ver se o eixo Local × Gravidade já basta na prática.

*Fora da fila, quando a primeira ruína aparecer: gatilhos de Sangue Frio e catálogo de estados temporários (4.3).*
