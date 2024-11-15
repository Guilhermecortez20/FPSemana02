
frase = input("Digite uma frase: ")
contagem = {}

for char in frase:
 
    if char.isalpha():  
     
        char = char.lower()

        if char in contagem:
            contagem[char] += 1 
        else:
            contagem[char] = 1  
print(contagem)
