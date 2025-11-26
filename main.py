import random

def jogo():
numero_secreto = random.randint(1, 100)
tentativas = 0

```
print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
```

if **name** == "**main**":
jogo()
