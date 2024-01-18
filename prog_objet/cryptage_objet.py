class CodeCesar:
    def __init__(self, cle):
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def decale(self, lettre):
        num1 = self.alphabet.find(lettre)
        num2 = num1+self.cle
        if num2 >= 26:num2 -= 26
        elif num2 < 0:num += 26
        
        return self.alphabet[num2]
    
    def decaleinverse(self, lettre):
        num1 = self.alphabet.find(lettre)
        num2 = num1-self.cle
        if num2 >= 26:num2 += 26
        elif num2 < 0:num -= 26
        
        return self.alphabet[num2]
    
    def crypt(self, mot):
        if len(mot)==1: return self.decale(mot)
        else: return self.decale(mot[0]) + self.crypt(mot[1:])
    
    def decrypt(self, mot):
        if len(mot)==1: return self.decaleinverse(mot)
        else: return self.decaleinverse(mot[0]) + self.decrypt(mot[1:])
        

code = CodeCesar(3)
mot = code.crypt("NSI")
print(mot)
print(code.decrypt(mot))