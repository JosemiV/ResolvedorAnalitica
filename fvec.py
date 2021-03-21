import frac

#   -v      v+v     v-v 
#   -n      n+n     n-n     n**n    n/n    sqr(n)   n*n
#   v*n
#   v = vec(n, n)

#asumimos que v es un vector

def norma(v):
    return sqr(v.c1**2 + v.c2**2);

def unit(v):
    u1 = v.c1/norma(v);
    u2 = v.c2/norma(v);

    return vec(u1, u2);

def pscalar(v1, v2):
    return v1.c1*v2.c1 + v1.c2*v2.c2

def ort(v):
    return vec(-v.c2, v.c1);

#v1 se proyecta en v2
def comp(v1, v2):
    return pscalar(v1, v2)/(norma(v1)*norma(v2));

def proy(v1, v2):
    return comp(v1, v2) * unit(v2);

#pendiente de un vector v.c2/v.c1
def pndv(v):
    return v.c2 / v.c1;

def tanv(v1, v2):
    return v1.c2-v2.c2 / (1 + v1.c1*v2.c1)





