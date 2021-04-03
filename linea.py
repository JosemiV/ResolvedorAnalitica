import varbls.variables as variables
import numerico.operadores_numericos as ops_numericos

#conjunto donde estaran las relaciones que se guarden, cada relacion tiene un nombre
#que es guarda en string, y esta en tupla con un par de numeros completos
#rels = {}

#solo se pueden hacer operacion binarias de objetos en la pila, llamar variables
#llamar relacione, asignar variables o relaciones
#aparentemente no es dificil que se operen inmediatamente varios slots de la
#pila pero para apurar el trabajo lo hago asi
#la barra al principio es para ejecutar comandos y si no lo esta es para llamar
#varibles o relaciones

strin = ""
pila = []

vrs = {};

rels = {};

dts = {};


def str_ls (st):
    ls = []; pl = "";
    for i in st:
        if (i != " "):
            pl += i;
        else:
            ls.append(pl);
            pl = "";
    ls.append(pl);
    return ls;


def nueva_variable (st):
    if (st[0] == 'recta'):
        vrs[st[1]] = variables.recta(st[1]);

    elif (st[0] == 'circunf'):
        vrs[st[1]] = variables.cincunferencia(st[1]);

def comandos(st):
    st = str_ls(st)
    #  print(st[1:]);
    #st es una lista con las palabras comando
    if (st[0] == 'new'):
        nueva_variable(st[1:])

    #val es el objeto en el conjunto de variables
    elif (st[0] == 'call'):
        obj = 0;
        try:
            obj = vrs[st[1]]
        except KeyError:
            try:
                obj = rels[st[1]];
            except KeyError:
                try:
                    obj = dts[st[1]];
                except KeyError:
                    #
                    print("No existe el objeto")
                    #
                    return;

        #agregarpila(variables.var(obj));
        pila.insert(0, variables.var(obj));

    elif (st[0] == 'dcl'):
        #en la pila ecuacion en forma de asignacion
        eq = pila[0]
        if (eq.t1.tp == 'vi' and eq.t2.tp == 'n'):
            eq.t1.root.v = eq.t2

        dts[st[1]] = eq

    elif (st[0] == 'set'):
        #igualdad en la pila
        eq = pila[0];
        if (eq.validez== False):
            #
            print("Declare la igualdad como dato")
            #
            return;

        #vi es la variables independiente
        if (eq.t1.tp == 'vi' and eq.t2.tp == 'n'):
            #asignar a esa variable
            eq.t1.root.v = eq.t2
        else:
            rls[st[1]] = eq

        del pila[0]

    elif (st[0] == 'int'):
        pila.insert(0, variables.num(int(st[1])));

    elif(st[0] == 'sum'):
        pila[0] = pila[0] + pila[1]
        del pila[1];

    elif (st[0] == 'mul'):
        pila[0] = pila[0] * pila[1]

    elif (st[0] == 'desarr'):
        pass
        #wbds locas


while True:
    strin = input()
    comandos(strin)
    print(pila)
    for i in reversed(pila):
        print(i.lt);
    print("\n");



