print("--Act 9 clases v3--")
print("--Luis Herrera-Mat: 22308051281207--")

# zona de class
class Operadores1207: 
# zona de funciones
    # SUMA
    def suma1207(self,L,H):
            s1207=L+H
            print(f"La suma de {L} + {H} = {s1207}")
    # RESTA
    def resta1207(self,L,H):
            r1207=L-H
            print(f"La resta de {L} - {H} = {r1207}")
    # MULTIPLICACION
    def multi1207(self,L,H):
            m1207=L*H
            print(f"La multiplicacion de {L} * {H} = {m1207}")
    # DIVISION
    def div1207(self,L,H):
            d1207=L/H
            print(f"La division de {L} / {H} = {d1207}")
    # MODULO
    def mod1207(self,L,H):
            M1207=L%H
            print(f"El modulo de {L} % {H} = {M1207}")
    # EXPONENTE
    def expo1207(self,L,H):
            e1207=L**H
            print(f"El exponente de {L} ** {H} = {e1207}")
    # COCIENTE
    def cos1207(self,L,H):
            c1207=L//H
            print(f"El cociente de {L} // {H} = {c1207}")
    #zona de creacion del objeto
operaeherra=Operadores1207()
    #zona del uso de objetos
print("--Funcion suma--")
operaeherra.suma1207(5,7)

print("--Funcion resta--")
operaeherra.resta1207(6,8)

print("--Funcion multiplicacion--")
operaeherra.multi1207(5,8)

print("--Funcion division--")
operaeherra.div1207(9,4)

print("--Funcion modulo--")
operaeherra.mod1207(2,7)

print("--Funcion exponente--")
operaeherra.expo1207(9,2)

print("--Funcion cociente--")
operaeherra.cos1207(5,4)