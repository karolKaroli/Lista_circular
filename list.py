from no import No
class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def push(self, valor,inicio=False):
        novo_no = No(valor)
        if self.inicio == None:
            self.inicio = novo_no
            self.fim = novo_no
        elif inicio:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            
        else: 
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.fim.proximo = self.inicio

    def pop(self, valor):
        if self.inicio == None:
            return
        #removendo do final
        atual = self.inicio
        anterior = None
        while atual.valor != valor:
            if atual.proximo == self.inicio:
                return
            anterior = atual
            atual = atual.proximo

        if anterior != None:
            anterior.proximo = atual.proximo
        else:
            while atual.proximo != self.inicio:
                atual = atual.proximo
            atual.proximo = self.inicio.proximo
            self.inicio = self.inicio.proximo

    def imprimir(self):
        if self.inicio == None:
            return

        atual = self.inicio
        while atual:
            print(atual.valor, end=' ')
            atual = atual.proximo
            if atual == self.inicio:
                print()
                break


lista = ListaCircular()


# lista.push(1)
# lista.push(2)
# lista.push(3,True)

# lista.imprimir() # Saída: 1 2 3

# lista.pop(3)

lista.imprimir() # Saída: 1 3



'''Exemplos de adicionar no inicio e fim'''
print("Adicionado")
print("No inicio")

#Adiconando no inicio
lista.push(2)
lista.push(4,True)
lista.push(6)

lista.imprimir()

print("No ifm")

#Adicionando no fim
lista.push(8)
lista.push(10)

lista.imprimir()

print("Removendo")

'''Exemplos de remover no inicio, meio e fim'''
print("Do inicico")

#Removendo do inicio
lista.pop(4)

lista.imprimir()

print("Meio")

#Removendo do meio
lista.pop(6)

lista.imprimir()

print("Fim")

#Removendo do fim
lista.pop(10)

lista.imprimir()