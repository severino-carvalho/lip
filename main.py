print('\n')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
mensagem = 'Seja bem-vindo!'

# Convertendo a variável idade de string para inteiro
idade = int(idade)

def helloWorld():
    print("Hello World!")

def apresentacao(nome, idade, mensagem):
    print(f"Olá, {nome}! {mensagem}")
    print(f"Você tem {idade} anos.")

def main():
    helloWorld()
    apresentacao(nome, idade, mensagem)
print('\n')
main()

# Path: main.py
