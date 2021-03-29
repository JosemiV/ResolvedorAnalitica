import comandos

'''
#diccionario donde estaran las varibles en parejas con sus valores o con un "None"
#en caso se desconozca su valor.
vrs = {};

#conjunto donde estaran las relaciones que se guarden, cada relacion tiene un nombre
#que es guarda en string, y esta en tupla con un par de numeros completos
rels = {}
'''

strin = "";

#solo se pueden hacer operacion binarias de objetos en la pila, llamar variables
#llamar relacione, asignar variables o relaciones
#aparentemente no es dificil que se operen inmediatamente varios slots de la
#pila pero para apurar el trabajo lo hago asi
#la barra al principio es para ejecutar comandos y si no lo esta es para llamar
#varibles o relaciones

def leer():
    strin = input();
    comando(strin);
    print(pila);

while (True):
    leer();





