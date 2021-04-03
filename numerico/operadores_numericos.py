import numerico.operadores_basicos as opb
import numerico.objetos_numericos as obj

def ssum(n1, n2):
    t1 = n1.tp[0:2]; t2 = n1.tp[0:2]

    if ((t1 == 'al' or t1 == 'pl') and (t2 == 'al' or t2 == 'pl')):
        return opb.pl_s_pl(n1, n2)

    else:
        return obj.sum([n1, n2]);

def smul(n1, n2):
    t1 = n1.tp[0:2]; t2 = n1.tp[0:2]

    if (t1 == 'al' and t2 == 'al'):
        return opb.al_m_al(n1, n2);

    else:
        return obj.mul(n1, n2);

