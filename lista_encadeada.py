class Membro:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"


class Noh:
    def __init__(self, valor_inicial):
        self._dados = valor_inicial
        self._proximo = None

    def getData(self):
        return self._dados

    def getNext(self):
        return self._proximo

    def setNext(self, novo_proximo):
        self._proximo = novo_proximo


class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_membro(self, nome, email):
        novo_membro = Membro(nome, email)
        novo_noh = Noh(novo_membro)

        if self.is_empty():
            self.head = novo_noh
            novo_noh.setNext(novo_noh)
        else:
            atual = self.head
            while atual.getNext() != self.head:
                atual = atual.getNext()
            atual.setNext(novo_noh)
            novo_noh.setNext(self.head)

    def remover_membro(self, nome):
        if self.is_empty():
            return "Lista vazia."

        atual = self.head
        anterior = None

        while True:
            if atual.getData().nome == nome:
                if atual == atual.getNext():
                    self.head = None
                else:
                    if atual == self.head:
                        ultimo = self.head
                        while ultimo.getNext() != self.head:
                            ultimo = ultimo.getNext()
                        self.head = self.head.getNext()
                        ultimo.setNext(self.head)
                    else:
                        anterior.setNext(atual.getNext())

                return f"Membro '{nome}' removido."

            anterior = atual
            atual = atual.getNext()
            if atual == self.head:
                break

        return f"Membro '{nome}' não encontrado."

    def proximo_responsavel(self):
        if not self.is_empty():
            nome = self.head.getData().nome
            self.head = self.head.getNext()
            return f"Próximo responsável: {nome}"
        else:
            return "Lista vazia."

    def mostrar_lista(self):
        if self.is_empty():
            return "Lista vazia."
        
        membros = []
        atual = self.head
        while True:
            membros.append(str(atual.getData()))
            atual = atual.getNext()
            if atual == self.head:
                break
        
        return "\n".join(membros)



###Testes###
lista = ListaEncadeadaCircular()

# Adicionando membros
lista.add_membro("Abel", "abel@email.com")
lista.add_membro("Bia", "bia@email.com")
lista.add_membro("Carlos", "carlos@example.com")

# Mostrar como a lista ficou
print("Lista depois das adições:")
print(lista.mostrar_lista())
print('\n')

# Removendo membros
remover = lista.remover_membro("Abel")
print(remover)
print('\n')

# Mostrar como a lista ficoou
print("Lista depois de remover 'Abel':")
print(lista.mostrar_lista())
print('\n')

# Removendo membro não existente
remover2 = lista.remover_membro("Davi")
print(remover2)
print('\n')

# Mostrar próximo responsável
proximo_responsavel = lista.proximo_responsavel()
print(proximo_responsavel)
print('\n')

# Mostra como ficou
print("Lista depois de obter o próximo responsável:")
print(lista.mostrar_lista())
print('\n')

# Removendo todos os membros
remover3 = lista.remover_membro("Bia")
print(remover3)
remover4 = lista.remover_membro("Carlos")
print(remover4)

# Mostra como ficou a lista
print("Lista final depois de remover todos:")
print(lista.mostrar_lista())