##SOLUÇAO EM PYTHON
import random as r
def StableMaching(PrefHomens, PrefMulheres):
    N = len(PrefHomens)
    HDisp = [i for i in range(N)]
    DicMulheres = [i[0] for i in PrefMulheres]
    PrefMulheres = [i[1] for i in PrefMulheres]
    DicHomens = [i[0] for i in PrefHomens]
    PrefHomens = [i[1] for i in PrefHomens]
    print(PrefHomens)
    parzinhos = [-1 for mulher in PrefHomens]
    while len(HDisp) > 0:
        r.shuffle(HDisp)
        m = HDisp[0]
        w = DicMulheres.index(PrefHomens[m][0])
        if parzinhos[w] == -1:
            parzinhos[w] = HDisp.pop(HDisp.index(m))
            PrefHomens[m].pop(0)
        elif PrefMulheres[w].index(DicHomens[m]) < PrefMulheres[w].index(DicHomens[parzinhos[w]]):
            HDisp.append(parzinhos.pop(w))
            parzinhos.insert(w, m)
            PrefHomens[m].pop(0)
        else:
            PrefHomens[m].pop(0)
    return [(DicHomens[x], DicMulheres[parzinhos.index(x)]) for x in parzinhos]
