import random

S = 10  # Alfabeto de 10 numeros


def createRandomVector(n):
    temp =  range(n)
    random.shuffle(temp)
    return temp


def myindex(k,l, element):
    #print "valor de k:",k
    length = len(l)
    count = 0
    for i in range(length):
        if element == l[(k+i)%length]:
            return count
        count = count + 1
        #print "valor de cout:",count
        #print "valor comparado:",l[(k+i)%length]



class rotor:

    def __init__(self,r,starting_position):
        self.r = r
        self.starting_position = starting_position
        self.count = 0
        self.flag = False

    def cifra(self,x):
        assert x >= 0
        assert x < len(self.r)
        assert x < S
        return self.r[(self.starting_position+x)%len(self.r)]

    def decifra(self,x):
        assert x >= 0
        assert x < len(self.r)
        assert x < S
        return myindex(self.starting_position,self.r,x)
        #return (self.r.index(x) + (len(self.r) - self.starting_position))

    # Anda uma casa. o "primeiro" elemento vai para o fim
    def rot(self):
        self.starting_position = (self.starting_position + 1)%len(self.r)
        self.count = (self.count + 1)%len(self.r)
        #print self.count
        #print self.r
        if(self.count == len(self.r)):
            self.flag = True


    # Responde se eu acabei de completar um ciclo. Se SIM, a rotacao deve ser propagada
    # para o proximo rotor
    def stepNext(self):
        aux = self.flag
        if self.flag == True:
            self.flag = False
        return aux


    def minuslist(self):

        for i in range(len(self.r)):
            if self.r[i] > 0:
                self.r[i] = self.r[i] - 1
            else:
                self.r[i]= len(self.r) - 1


class enigma:

    def __init__(self, rotors):
        self.rotors = []
        for i in rotors:
            self.rotors.append(rotor(i[0],i[1]))


    # Chama o cifra de cada um dos rotores.
    # Executa a rotacao do primeiro (sempre)
    # e dos demais (quando necessario)
    def ecifra(self,x):
        aux = self.rotors[0].cifra(x)
        self.rotors[0].rot()
        self.rotors[0].minuslist()
        flag = self.rotors[0].stepNext()
        #print " "
        #print self.rotors[0].r
        #print "cifra rotor 0: ", aux

        if len(self.rotors) > 1:
            for i in range(1,len(self.rotors)):
                #print self.rotors[i].r

                if flag == True:
                    #print "passou"
                    self.rotors[i].rot()
                    self.rotors[i].minuslist()
                    flag = self.rotors[i].stepNext()

                #print "rotor:", i, "entrada:", aux
                aux = self.rotors[i].cifra(aux)
                #print "cifra rotor", i,":",aux
                #print "rotor:", i, "resultado:", aux
                #print " "

        return aux


    def edecifra(self,x):

        aux = x

        for i in range(len(self.rotors)-1,-1,-1):
            #print "passou",i
            aux = self.rotors[i].decifra(aux)

        #print aux

        self.rotors[0].rot()
        self.rotors[0].minuslist()
        flag = self.rotors[0].stepNext()

        if len(self.rotors) > 1:
            for i in range(1,len(self.rotors)):
                if flag == True:
                    self.rotors[i].rot()
                    self.rotors[i].minuslist()
                    flag = self.rotors[i].stepNext()

        return aux

"""
    def edecifra(self,x):
        print " "
        print len(self.rotors)-1
        print self.rotors[len(self.rotors)-1].starting_position
        aux = self.rotors[len(self.rotors)-1].decifra(x)
        print aux
        flag = self.rotors[len(self.rotors)-1].stepNext()
        #self.rotors[len(self.rotors)-1].rot()
        print self.rotors[len(self.rotors)-1].r
        print "cifra rotor",len(self.rotors)-1,":", aux
        for i in range(1,len(self.rotors)):
            print self.rotors[len(self.rotors)-1 - i].r
            if flag == True:
                print "AAaAAAAAAAAAAAAAAAAAAAAAA"
                self.rotors[len(self.rotors) - 1 - i].rot()
                flag = self.rotors[len(self.rotors)- 1 - i].stepNext()

            aux = self.rotors[len(self.rotors)- 1 - i].decifra(aux)
            print "cifra rotor",len(self.rotors)- 1 - i,":",aux

        return aux

"""

"""
segredo1 = createRandomVector(S)
segredo2 = createRandomVector(S)
segredo3 = createRandomVector(S)
"""

"""
segredo1 = [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo2 = [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo3 = [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]




print 'segredo1:',segredo1
print 'segredo2:',segredo2
print 'segredo3:',segredo3
# 5,3 e 4 Sao os deslocamentos iniciais.. fazem parte da chave

"""

"""

e = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
d = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
"""

"""
segredo: [4, 2, 8, 0, 6, 5, 3, 1, 7, 9]

texto claro = [0,0,0,0,0....]

Texto cifrado:

[4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0]
"""

segredo = [4, 2, 8, 0, 6, 5, 3, 1, 7, 9]

e = enigma( [(segredo,0)] )
d = enigma( [(segredo,0)] )

"""

e = enigma ( [ (segredo3,4),(segredo2,2),(segredo1,5)])
d = enigma ( [ (segredo3,4),(segredo2,2),(segredo1,5)])

"""

'''
for k in range(5):
    for i in range(2):
        print ""
        print "texto claro: ",i
        x = e.ecifra(i)
        print "Criptografado: ",x
        y = d.edecifra(x)
        print "Decriptografado: ",y
        assert i==y
'''
'''
for i in range(S):
    for i in d.rotors:
        print i.flag
        print i.starting_position

'''

"""
for k in range(5):
    for i in range(S):
        x = e.ecifra(i)
        y = d.edecifra(x)
        #assert i==y

"""
p=[0]*100

#p = [i for i in range(100)]


c=[e.ecifra(_p) for _p in p]

print c

print [d.edecifra(_c) for _c in c]






'''
Saida do programa:


segredo1: [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo2: [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo3: [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]
[8, 1, 4, 3, 1, 4, 9, 2, 1, 5, 9, 1, 7, 6, 1, 5, 3, 6, 4, 4, 1, 5, 1, 9, 3, 8, 7, 6, 5, 2, 7, 5, 0, 1, 5, 8, 7, 5, 1, 3, 7, 1, 6, 0, 1, 3, 2, 9, 5, 7, 2, 5, 6, 0, 5, 3, 1, 6, 8, 7, 1, 8, 4, 9, 8, 1, 7, 9, 2, 5, 7, 2, 4, 8, 2, 6, 1, 7, 4, 5, 1, 4, 8, 0, 4, 3, 0, 1, 4, 6, 0, 4, 7, 8, 4, 6, 8, 2, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
