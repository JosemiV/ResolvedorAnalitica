import math

class frac:
    n = 0; d = 0;
    lt = "";

    def simp(self):
        s = math.gcd(self.n, self.d);
        self.n = int(self.n/s);
        self.d = int(self.d/s);

    def genl(self):
        self.lt = "\frac{" + str(self.n) + "}{" + str(self.d) + "}";

    def __init__(self, _n, _d):
        s = math.gcd(_n, _d);
        _n = int(_n/s);
        _d = int(_d/s);

        self.n = _n;
        self.d = _d;
        if (_d == 1):
            self.lt = str(_n);
        else:
            self.lt =  "frac{" + str(self.n) + "}{" + str(self.d) + "}";

    def __inv__(self):
        return frac(-self.n, self.d);

    def __add__(self, f2):
        if (type(f2) is int):
            f2 = frac(f2, 1);

        nr = int(f2.n*self.d+f2.d*self.n)
        dr = int(self.d*f2.d)
        return frac(nr, dr);

#self - f2;
    def __sub__(self, f2):
        if (type(f2) is int):
            f2 = frac(f2, 1);

        f2 = -f2;
        return self+f2;

    def __mul__(self, f2):
        if (type(f2) is int):
            f2 = f2, 1;

        #si es fraccion
        nr = self.n*f2.n;
        dr = self.d*f2.d;

        return frac(nr, dr);

    def __div__(self, f2):
        if (type(f2) is int):
            f2 = frac(f2, 1);

        return frac(f2.d*self.n, self.d*f2.n);

class vec:
    #numero de la clase frac
    c1 = 0;
    c2 = 0;
    def __init__(self, _c1, _c2):
        self.c1 = _c1;
        self.c2 = _c2;


#testing part
a = int(input());
b = int(input());
c = int(input());
d = int(input());

f1 = frac(a, b);
f2 = frac(c, d);

f1 = f1+f2;
print(f1.lt);
