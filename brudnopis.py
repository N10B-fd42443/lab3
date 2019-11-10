import random
lista = []
def genArray(self,size):
    for i in range(0,size):
        self.append(random.randint(0,99))
def averageValue(self):
   averageValue = sum(self)/float(len(self))
   return averageValue


genArray(lista,20)
averageValue(lista)

print(lista)
print(sorted(lista))
print(min(lista),max(lista),averageValue(lista))
