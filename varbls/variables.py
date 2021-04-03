#en el conjunto de variables
class punto:
    n = 0;
    lt = ""

class recta:
    paso = 0;   dr = 0;
    lt = ""
    def __init__(self, lt):
        self.lt = lt;

class circunferecia:
    ctr = 0; rd = 0;
    lt = "";

class elipse:
    ctr = 0; f1 = 0; f2 = 0;
    ejmy = 0; ejmn = 0; dr1 = 0; dr2 = 0;
    lt = ""

class sistema:
    u = 0; org = 0;


#en pila
class var:
    root = 0;
    lt = "";
    def __init__(self, root):
        self.lt = root.lt;
        self.root = root;

class num:
    n = 0;
    lt = "";
    def __init__(self, n):
        self.n = n;
        self.lt = str(n);





