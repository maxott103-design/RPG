# -*- coding: utf-8 -*-
"""
Simulador de combate — regras v2 (28/08/2026)
Uso:  python3 simulador-combate.py

PARA QUE SERVE: comparar configurações de encontro entre si.
PARA QUE NÃO SERVE: prever o que vai acontecer na mesa.

O QUE O MODELO INCLUI
  - 3d6 + competência − Ameaça, com as três faixas (<=9 / 10-14 / 15+)
  - Fôlego como moeda de resistência: ataque simples 0 PF, pesado 1 PF, defesas 1/2/3
  - Defesa escalonada, com o Fôlego gasto mesmo quando a defesa falha
  - Quebrado não age; alvo Quebrado é ferido em vez de drenado
  - Ralé sai da luta com qualquer Ferimento ou a 0 de Fôlego
  - Resistência: 2 Graves | 3 Leves | 1 Grave + 2 Leves
  - Retomar Fôlego como turno perdido

O QUE O MODELO **NÃO** INCLUI  (por isso os números são um piso pessimista)
  - Aparo / armadura: todos lutam sem proteção nenhuma
  - Habilidades (Instrução Militar, Aguentar o Tranco, Último Fôlego, Sujeira...)
  - Ataque pesado do lado dos jogadores (no modelo todos usam arma Peso 1)
  - Sangramento, Exaustão, armas de fogo, cobertura, crítico e falha crítica
  - Moral, fuga, terreno e posicionamento — inclusive não deixar ser cercado,
    que é a decisão tática mais importante do sistema
  Os personagens simulados ficam parados trocando golpe. Jogador real joga melhor.
"""
import random

REPETICOES = 10000
PF_MAX     = 9    # Vigor 2 + 7
COMPETENCIA= 2    # Prático
AMEACA     = 2
PESO_PJ    = 1    # arma dos personagens (1 = facão: só desgasta)
PF_RALE    = 4
TETO_RODADAS = 30

def d6():
    return random.randint(1,6)+random.randint(1,6)+random.randint(1,6)

def cai(leves, graves):
    return graves >= 2 or leves >= 3 or (graves >= 1 and leves >= 2)

def combate(n_inimigos, n_marretas=0, n_pj=4, foco=False):
    """foco=True: os inimigos concentram no personagem com menos Fôlego."""
    margem = COMPETENCIA - AMEACA
    pj = [{'pf': PF_MAX, 'l': 0, 'g': 0, 'out': False} for _ in range(n_pj)]
    inim = [{'pf': PF_RALE, 'peso': 2 if k < n_marretas else 1} for k in range(n_inimigos)]
    turnos_quebrado = 0

    for rodada in range(1, TETO_RODADAS+1):
        # ---- turno dos personagens ----
        for p in pj:
            if p['out'] or not inim: continue
            if p['pf'] == 0:                       # Quebrado: só Retomar Fôlego
                p['pf'] = 4; continue
            i = min(range(len(inim)), key=lambda k: inim[k]['pf'])   # foco de fogo
            r = d6() + margem
            if inim[i]['pf'] == 0:                 # alvo Quebrado: fere -> Ralé sai
                if r >= 10: inim.pop(i)
            elif r >= 15: inim[i]['pf'] = max(0, inim[i]['pf'] - (2+PESO_PJ))
            elif r >= 10: inim[i]['pf'] = max(0, inim[i]['pf'] - (1+PESO_PJ))

        if not inim:
            return rodada, sum(p['l']+p['g'] for p in pj), sum(p['out'] for p in pj), turnos_quebrado

        # ---- turno dos inimigos ----
        custo = {id(p): 1 for p in pj}
        for e in inim:
            if e['pf'] == 0: continue              # inimigo Quebrado não age
            vivos = [p for p in pj if not p['out']]
            if not vivos: break
            p = min(vivos, key=lambda x: x['pf']) if foco else random.choice(vivos)

            if p['pf'] == 0:                       # alvo Quebrado: ferimento
                if d6() + margem >= 10:
                    p['l'] += 1
                    if cai(p['l'], p['g']): p['out'] = True
                continue

            c = custo[id(p)]
            if c <= 2 and p['pf'] - c >= 1:        # heurística de defesa
                p['pf'] -= c; custo[id(p)] = c + 1
                if d6() + margem >= 10: continue   # defendeu

            if e['peso'] == 2 and e['pf'] >= 1:    # ataque pesado: fere
                e['pf'] -= 1
                if d6() + margem >= 15: p['g'] += 1
                else: p['l'] += 1
                if cai(p['l'], p['g']): p['out'] = True
            else:                                  # ataque simples: desgasta
                p['pf'] = max(0, p['pf'] - (1 + e['peso']))

        turnos_quebrado += sum(1 for p in pj if p['pf'] == 0 and not p['out'])

    return TETO_RODADAS, sum(p['l']+p['g'] for p in pj), sum(p['out'] for p in pj), turnos_quebrado

def rodar(rotulo, **kw):
    R = [combate(**kw) for _ in range(REPETICOES)]
    n = float(REPETICOES)
    print(f"  {rotulo:<34} rodadas {sum(x[0] for x in R)/n:5.1f} | "
          f"ferimentos {sum(x[1] for x in R)/n:5.2f} | "
          f"PJs caidos {sum(x[2] for x in R)/n:4.2f} | "
          f"turnos-Quebrado {sum(x[3] for x in R)/n:5.1f}")

if __name__ == "__main__":
    print(f"\n{REPETICOES} combates por linha | 4 PJ, Folego {PF_MAX}, competencia +{COMPETENCIA} | Rale Ameaca {AMEACA}, Folego {PF_RALE}\n")
    print("QUANTIDADE (Rale toda de facao, alvo aleatorio):")
    for n in (4,5,6,7,8,10): rodar(f"{n} inimigos", n_inimigos=n)
    print("\nARMAMENTO (4 inimigos, variando quantas marretas):")
    for m in (0,1,2,4): rodar(f"4 inimigos, {m} com Peso 2", n_inimigos=4, n_marretas=m)
    print("\nFOCO DE FOGO (inimigos concentram no mais fraco):")
    for n in (4,6,8): rodar(f"{n} inimigos, com foco", n_inimigos=n, foco=True)
    print("\nA MISTURA RECOMENDADA:")
    rodar("6 inimigos, 2 com Peso 2", n_inimigos=6, n_marretas=2)
    print()
