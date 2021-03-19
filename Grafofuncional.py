#funcion que me dice si un operador o variable es alometrico
def isal(s):
    if (s== "ni" or s== "vi" or s[0:2] == "al"):
        return True;
    else:
        return False;

#funcion que retorna el grado de una alometria
def gral(s):
    if (s == "ni"):
        return 0;
    if (s == "vi"):
        return 1;
    else:
        return int(s[2]);

#solo se puede ingresar numeros enteros directamente en la pila
class num:
    #numero entero
    tp = "ni";
    v = 0;
    lt = "";
    def __init__(self, v_):
        self.v = v_;
        self.lt = str(self.v);

    def genl(self):
        return self.lt;

class var:
    #varibale en string
    tp = "vi";
    v = 'x';
    lt = "";
    def __init__(self, v_):
        self.v = v_;
        self.lt = v_;

    #potencialmente mas cosas, pila de variables, punteros a expresiones, etc;

class op:
    #punteros a operados
    ins = [];
    #tipo de expresion que forma
    tp = "";
    #latex
    lt = "";

class sum(op):
    def __init__(self, s1, s2):
        self.ins.append(s1);
        self.ins.append(s2);

        #tipado del operador
        t1 = s1.tp; t2 = s2.tp;

        #si fuera polinomico y se forma con dos alometricos
        if(isal(t1) and isal(t2)):
            self.tp = "pl";
            #hallando grado;
            self.tp += str(max(gral(t1)), gral(t2));

        #haciendo latex
        self.lt = s1.lt + '+' + s2.lt;

class mul(op):
    def __init__(self, s1, s2):
        self.ins.append(s1);
        self.ins.append(s2);

        t1 = s1.tp; t2 = s2.tp;

        #en la multiplicacion nada se simplifica automaticamente;
        if (isal(t1) and isal(t2)):
            self.tp = "al";
            #hallando grado;
            self.tp += str(gral(t1)+gral(t2));

        #hay funciones especiales de ordenamiento en el latex;
        self.lt = s1.lt + '.' + s2.lt;


class n:
    #head sera generalmente un operador pero puede tambien ser una variable
    head = 0;
    def __add__(self, s):
        return sum(self, s);

    def __mul__(self, s):
        return mul(self, s);


#testing part

a = input();
b = int(input());
ap = var(a);
bp = num(b);

s = mul(ap, bp);
print(s.lt);
print(s.tp);


