
class op:
    #punteros a operados
    ins = [];
    #tipo de expresion que forma
    tp = "";
    #variables de las que depende en orden
    dp = [];
    #latex
    lt = "";

class sum(op):
    def __init__(self, s1, s2):

        self.ins.extend([s1, s2]);

        #provisionalmente genero latex en el constructor, ya que 
        #no siempre es asi de claro. Lo mismo para los otros op
        self.lt = self.ins[0].lt;
        for i in self.ins[1:]:
            self.lt = '+' + i.lt;
        #creo que en esta parte esta volviendo a generar los latexs, si es necesario
        #algunas veces pero no se si siempre; aunque creo que si en el caso de polis

class mul(op):
    def __init__(self, ins, tp):

        self.ins.extend(ins);

        for i in self.ins:
            self.lt = '(' + i.lt + ')'

#en ins siempre [numerador, denominador]
class div(op):
    def __init__(self, n, d):

        self.ins.extend([n, d]);

        self.lt = '\\frac{' + n.lt + '}{' + d.lt + '}'

class inv(op):
    def __init__(self, i1):

        self.ins.append(i1);
        self.lt = '-' + i1.lt

#en ins siempre [base, exponente]
class pow(op):
    def __init__(self, b, e):
        self.ins.extend([b, e]);

        self.lt = b.lt + '^{' + e.lt + '}'

#funcion de optimizacion, para generar mas facilmente latex de raiz
#y por ser muy utilizada en la geometria
class sqr(op):
    def __init__(self, rd):
        self.ins.append(rd);

        self.lt = '\\sqrt{' + rd.lt + '}'


#grafo que se construye con los nodos antes declarados
class nm:
    #el head puede tambien ser una variable, cuando el grafo es por ejemplo
    #un lugar en la pila. Sera el operador principal
    head = 0;

    #sobrecarga de operadores
    def __add__(self, s):
        return sum(self, s);

    def __mul__(self, s):
        return mul(self, s);




