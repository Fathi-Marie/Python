from json import *


def est_base(c):
    return len(c) == 1 and c in "ATGC"


def est_adn(s):
    i = 0
    while i < len(s) and est_base(s[i]):
        i += 1
    return i >= len(s)


def arn(adn):
    if not est_adn(adn):
        return None
    s = ""
    i = 0
    while i < len(adn):
        if adn[i] == "T":
            s += "U"
        else:
            s += adn[i]
        i += 1
    return s


def arn_to_codons(arn):
    codons = []
    i = 0
    while i < len(arn) - 2:
        codons.append(arn[i] + arn[i + 1] + arn[i + 2])
        i += 3
    return codons


def load_dico_codons_aa(filename):
    fichier = open(filename, "r")
    strjson = fichier.read()
    fichier.close()
    return loads(strjson)


def codons_stop(dico):
    stop = []
    bases = "AUGC"
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            k = 0
            while k < 4:
                if bases[i] + bases[j] + bases[k] not in dico:
                    stop.append(bases[i] + bases[j] + bases[k])
                k += 1
            j += 1
        i += 1
    return stop


def codons_to_aa(codons, dico):
    aa = []
    i = 0
    while i < len(codons) and codons[i] in dico:
        aa.append(dico[codons[i]])
        i += 1
    return aa

def nextIndice(tab,i,elements):
    while i < len(tab):
        if tab[i] in elements:
            return i
        else:
            i+=1
    else:
        return len(tab)

def decoupe_sequence(seq, start, stop):
    tab = []
    d = 0
    while d < len(seq):
        tab_tab = []
        d = nextIndice(seq,d,start)
        fin = nextIndice(seq,d,stop)
        while d < fin :
            val = seq[d+1]
            if val not in stop:
                tab_tab.append(val)
            d+=1
        if len(tab_tab) != 0:
            tab.append(tab_tab)
        d = fin+1
    return tab

dico=load_dico_codons_aa("data\codons_aa.json")
def codons_to_seq_codantes(seq_codons,dico ):
    start=["AUG"]
    stop = codons_stop(dico)
    seq_codantes = decoupe_sequence(seq_codons, start, stop)
    return seq_codantes


def seq_codantes_to_seq_aas(seq_codantes, dico):
    i=0
    tab_seq=[]
    while i<len(seq_codantes):
        s = seq_codantes[i]
        tab_seq.append(codons_to_aa(s ,dico))
        i+=1
    return tab_seq


def adn_encode_molecule(badn,dico,molecule):
    ar = arn(badn)
    an = arn_to_codons(ar)
    brin_arn = codons_to_aa(an ,dico)
    if brin_arn != molecule:
        return True
    else:
        return False