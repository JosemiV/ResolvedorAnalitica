import numerico.objetos_numericos
from copy import copy

'''
#aqui se definen los principales manipuladores de grafos numericos
#los de mas frecuente uso tanto para el desarrollo como para la simplificacion
#de expresiones matematicas

#multiplicacion de alometricos
def al_m_al(n1, n2):

    rstp = "al"

    #se hara iteracion de doble puntero en sus dependencias
    l1 = n1.dp; l2 = n2.dp;
    pt1 = pt2 = 0;

    rsins = [];

    while( pt1 < len(l1) and pt2 < len(l2) ):
        if (l1[pt1] == l2[pt2]):
            gr1 = gr2 = 0;
            if (n1.ins[pt1].tp == "vi"):
                gr1 = 1
            else:
                gr1 = n1.ins[pt1].ins[1].v;

            if (n2.ins[pt2].tp == "vi"):
                gr2 = 1;
            else:
                gr2 = n1.ins[pt2].ins[1].v;

            rsins.append(pow(var(l1[pt1]), num(gr1+gr2)));
            rsdp.append(l1[pt1]);
            pt1 +=1; pt2 +=1;

        elif (l1[pt1] < l2[pt2]):
            rsins.append(l1[pt1])
            pt1 += 1

        else:
            rsins.append(l2[pt2])
            pt2 += 1;

        if (pt1 != len(l1)):
            while(pt1 == len(l1)):
                rsins.append(l1[pt1]); pt1+=1;
        elif (pt2 != len(l2)):
            while(pt2 == len(l2)):
                rsins.append(l2[pt2]); pt2+=1;
        #creo que este problema pudo haberse hecho mas rapido
        #copiando uno de los objetos, pero lo dejo asi

    if (len(rsins) == 1):
        return rsins[0];
    else:
        return mul(rsins, rstp);

def gr_al(n):
    if (type (n) is num):
        return 0

    elif (type(n) is var):
        return 1

    elif (type(n) is pow):
        return n.ins[1].v

    elif (type(n) is mul):
        return n

def completar_al(n):
    if (n.tp == "var"):
        n = pow(n, 1);
    if (type(n) is pow):
        n = mul(n, 1);

#es muy fastidioso estar en cada funcion de alometricos poniendo if-elif para completar
#los casos en los que pueden ser variables, se pierde de esta manera legibilidad
#y es un proceso normal completarlos inconscientemente al operarlos
#si bien se pierde un par de operaciones al ingresar un dato para luego leerlo, se
#gana legibilidad. Aqui surge la discusion si este es un proceso destructivo o no

def ord_al(n1, n2):
    #funcion que me dice si dos alometricas se factorizan entre si, o no
    #en cada caso devuelve la de mayor jerarquia o una lista con las dos si son fact
    pt1 = 0; pt2 = 0;
    while (pt1 < len(n1.dp) and pt2 < len(n2.dp)):
        if (n1.dp[pt1] > n2.dp[pt2]):
            return
        pt1 +=1 ; pt2 += 1;



def pl_m_pl(n1, n2):
    #se usara igualmente la tecnica de merge con doble puntero pero creo que
    #puede hacerse tambien copiando uno de los objetos, no estoy seguro cual es
    #la mejor forma

    l1 = n1.ins; l2 = n2.ins;
    pt1 = pt2 = 0;
    while (pt1 < len(l1) and pt2 < len(l2)):
        if (l1[pt1] )

'''

#Al encontrar el articulo de funciones y estructuras para polinomios Sparse
#decidi volver a hacer esta parte, ya que anteriormente usaba otro ordenamiento

#Desde luego que a continuacion se usara el orden standar de Sparse

def hom_al (n):
    #homogeneizando las formas
    if (type(n) is not mul):
        n = mul(n, 1)
    for i in n.ins:
        if (type(i) is var):
            i = pow(i, 1)



def cmp_al(n1, n2):
    #funcion que retorna n1 > n2, en orden Sparse
    #funciona si son diferentes variables
    #hay que considerar que si hay varibles en los coeficientes debe separar dp_al
    #ademas la parte alometrica debe estar al inicio siempre

    #homogenizacion
    hom_al (n1); hom_al (n2);

    it = 0;
    while (it < len(n1.dp) and it < len(n2.dp)):
        if (n1.dp[it] < n2.dp[it]):
            return True
        elif(n1.dp[it] > n2.dp[it]):
            return False
        else:
            #establecer grados, por legibilidad
            gr1 = n1.ins[it].ins[1].v
            gr2 = n2.ins[it].ins[1].v;

            if (gr1 < gr2):
                return False
            elif (gr1 > gr2):
                return True

        it += 1;

    if (len(n1.dp) > len(n2.dp)):
        return True
    elif (len(n1.dp) < len(n2.dp)):
        return False
    else:
        return False


def pl_s_pl (n1, n2):
    #se usa merge sum
    i = j = 0; l1 = n1.ins; l2 = n2.ins; lr = [];
    while (i < len(l1) and j < len(l2)):
        if (cmp_al(l1[i], l2[j])):    #considerar desde aqui formas homogeneas
            lr.append(l1[i]); i+=1;
        elif (cmp_al(n2, n1)):
            lr.append(l2[j]); j+=1;
        else:
            #aqui lo malo es que solo funciona para enteros, recomiendo usar
            #al_s_al
            cf1 = l1[i].ins[-1].v; cf2 = l2[j].ins[-1].v
            i+=1; j+=1;
            if (cf1 + cf2 == 0):
                continue;
            r = copy(l1[i]);
            r.ins[-1].v += cf2
            lr.append(r)
    while (i < len(l1)):
        lr.append(l1[i]); i+=1;
    while (j < len(l2)):
        lr.append(l2[j]); j+=1;

    return sum(lr);

def al_m_al (n1, n2):
    #homogenizacion
    hom_al (n1); hom_al(n2);

    i = j = 0; l1 = n1.dp; l2 = n2.dp; lr = [];
    while (i < len(l1) and j < len(l2)):
        if (l1[i] < l2[j]):
            lr.append(n1.ins[i]); i+=1;
        elif(l1[i] > l2[j]):
            lr.append(n2.ins[j]); j+=1;
        else:
            ex1 = n1.ins[i].ins[1].v;
            ex2 = n2.ins[j].ins[1].v;
            #no contempla la cancelacion, exponentes negativos

            lr.append(pow(l1[i], ex1+ex2)); i+=1; j+=1;

    while (i < len(l1)):
        lr.append(n1.ins[i]); i+=1;
    while (j < len(l2)):
        lr.append(n2.ins[j]); j+=1;

    return mul(lr)

#heap    arbol binario de busqueda

def pl_m_pl (n1, n2):
    l = []; lr = []
    for i in n1.ins:
        for i2 in n2.ins:
            l.append(al_m_al(i, i2))

        factor = sum(l); r = pl_m_pl(r, factor);

    return r









