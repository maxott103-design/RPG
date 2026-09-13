# Atributos — referência objetiva

> Consolidação documental de 13/09/2026. Fonte: [original preservado](../versao-claude/Regras/atributos.md). Versão de trabalho para teste; balanceamento ainda sem playtest registrado.

Status: v1 (28/08/2026). Este é o lugar onde os atributos e seus derivados estão descritos de forma fechada. Antes disso a informação estava espalhada entre [pendências de desenvolvimento](../ideias/pendencias.md) (2.1) e `competencias.md`.

---

## 1. A regra de ouro

**Atributo NUNCA soma na rolagem.** A rolagem é sempre `3d6 + competência − Ameaça`.

Atributo serve para três coisas, e só:
1. **Derivar números da ficha** (Fôlego, quantas competências, teto de Exaustão).
2. **Limitar o quanto uma competência pode subir** (rank máximo = atributo âncora + 1; Mestre exige atributo 3+).
3. **Ser pré-requisito de habilidades.**

## 2. Escala e criação

- Escala **1 a 4**. Na criação, **mínimo 1 e máximo 3** — o 4 só se alcança em jogo.
- **Orçamento de criação: 10 pontos** distribuídos entre os cinco atributos.
- Distribuições típicas: `3-3-2-1-1` (especialista), `3-2-2-2-1` (competente), `2-2-2-2-2` (equilibrado).

Não existe atributo 0. Um personagem com 1 é ruim naquilo — não é incapaz.

## 3. Os cinco atributos

| Atributo | Do que trata | O que deriva |
|---|---|---|
| **Vigor** | força, resistência física, capacidade de aguentar | **Fôlego máximo = Vigor + 7** |
| **Agilidade** | velocidade, precisão, mãos, corpo | nada direto — aparece via competências (esquivar é Acrobacia) |
| **Percepção** | sentidos, atenção, leitura de ambiente | **Alerta** (passivo, decide surpresa e emboscada) |
| **Intelecto** | educação, raciocínio técnico, conhecimento | **Largura da pirâmide = 3 + Intelecto** (quantas competências você tem) |
| **Vontade** | disciplina, teimosia, autocontrole, presença | **Altura da pirâmide = Vontade** (quantas podem chegar a Profissional/Mestre)<br>**Teto de Exaustão = Vontade + 1** |

### Competências ancoradas em cada atributo

- **Vigor** — Pugilismo, Armas Pesadas, Atletismo, Labuta, Resiliência, Força Bruta, Intimidação
- **Agilidade** — Armas Leves, Arcos e Bestas, Furtividade, Mãos Leves, Acrobacia, Arrombamento, Condução
- **Percepção** — Armas de Fogo, Busca, Rastrear, Sobrevivência, Intuição, Avaliar
- **Intelecto** — Medicina, Mecânica, Química, Saberes Antigos, Naturalismo
- **Vontade** — Persuasão, Enganação, Barganha, Comando, Adestramento, Sangue Frio

Detalhe de cada uma em `competencias.md`.

## 4. Bloco derivado da ficha

Todo personagem calcula estes cinco números, e só estes:

| Número | Fórmula |
|---|---|
| **Fôlego máximo** | Vigor + 7 |
| **Nº de competências** | 3 + Intelecto |
| **Nº delas em Profissional/Mestre** | Vontade (na criação, sempre 1 Profissional + 2 Práticos + resto Aprendiz) |
| **Teto de Exaustão** | Vontade + 1 — no teto está *Esgotado*; acima dele, *Colapso*. Cada ponto tira **2** do Fôlego máximo |
| **Resistência a Ferimentos** | **igual para todos**: cai com 2 Graves, 3 Leves, ou 1 Grave + 2 Leves. Grave na cabeça derruba na hora. Só habilidade muda isso |

*Por que a Resistência não deriva de Vigor: já deriva o Fôlego. Se derivasse os dois, Vigor viraria o único atributo que importa. Ser mais resistente é escolha de habilidade, não de ficha.*

## 5. Por que cada atributo vale a pena

Teste de sanidade do chassi — nenhum atributo pode ser pedágio universal nem lixo:

- **Vigor** — mais Fôlego, ou seja, mais rodadas de pé numa luta. É o atributo mais direto do combate.
- **Agilidade** — não dá número, dá *teto*: é o que permite ser Profissional em Armas Leves, Furtividade ou Acrobacia. Personagem de agilidade baixa pode até ter a competência, mas não chega longe nela.
- **Percepção** — decide quem é emboscado, e ancora Armas de Fogo e toda a leitura de Wasteland. Num jogo de expedição, é o atributo que evita o combate acontecer nos termos do inimigo.
- **Intelecto** — largura da ficha. Personagem de Intelecto 1 é fundo e estreito; de Intelecto 3 é largo e versátil. Nenhum dos dois é errado.
- **Vontade** — profundidade da ficha **e** quanto de estrada o personagem aguenta. Vontade 1 significa teto de Exaustão 2: forte por uma tarde, inútil numa semana de viagem.

## 6. Em aberto

- Atributo 4 em jogo: por qual moeda de progressão? (roadmap 5.2)
- Se raças/povos modificam atributo ou só dão permissão ficcional. Hoje as fichas do piloto tratam raça como ficção, não como número — e isso está funcionando.
