class var:
    tp = "vi";
    #string que indica la variable
    v = "";

class num:
    tp = "ni";
    #int
    v = 0;

class op:
    #punteros a operados
    ins = [];
    #string del op
    v = '';
    #tipo de expresion que es el operador
    tp = "";
    #latex asociado
    lt = "";

class sum(op):
    #string
    v = '+';
    def tip():
        grado = 0;
        for i in ins:
            a = int(i.tp[2]);
            if (a>grado):
                grado = a;


class mul(op):
    v = '.';
    def genl(self):
        pass

class inad(op):
    v = '-';
class inml(op):
    v = '/';

#numero en grafo
class ng:
    #op
    head = 0;
    def __init__(self, opini):
        self.head = opini;

    def __add__(self, gr):
        paso = op(op='+');
        paso.adin(self.head);
        paso.adin(gr);
        self.head = paso;

    def __sub__(self, gr):
        paso = op(op = '-');
        paso.adin(gr);
        self = self + paso;

    def __mul__(self, gr):
        paso = op(op = '*');
        paso.adin(self.head);
        paso.adin(gr);
        self.head = paso;

    def genl(self):



a = sum();
