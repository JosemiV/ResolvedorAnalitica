import operadores_numericos
import variables

vrs_rels = {};
pila = [];

def new(a):
    if (a[0] == 'n'):
        vrs_rels[a[2:]] = nm();


def comando(s):
    if (s[0..3] == 'new'):
        new(s[4:])

    elif (s[0..3] == 'sum'):
        pila[0] += pila[1]

    elif (s[0..3] == 'mul'):
        pila[0] *= pila[1];


