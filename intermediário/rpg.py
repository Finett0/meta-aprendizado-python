class Personagem:
    def __init__(self,nome,vida,nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel,habilidade):
        super().__init__(nome, vida, nivel)

        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel,tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo 

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_tipo()}"


class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self):
        self.heroi =  Heroi(nome="Herói",vida=100,nivel=5,habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego",vida=50,nivel=3,tipo="Voador")

        
    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escola = input("Escolha (1- Ataque Normal, 2 - Ataque Especial): ")

#Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
