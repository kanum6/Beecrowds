"""Turma: 2B Informática Vespertino
Nomes: Celso Hector Silva Sales
       André Luís Bento Ferreira
       
       """
import random
from time import sleep

class Pokemon:
    def __init__ (self, nome, overall, tipo, hp, spd, kg, ataque, defesa, altura):
        self.nome = nome
        self.overall = overall
        self.tipo = tipo
        self.hp = hp
        self.spd = spd
        self.kg = kg
        self.ataque = ataque
        self.defesa = defesa
        self.altura = altura

    def exibirCarta (self):
        print ("Nome:", self.nome,
        "\nOverall:", self.overall,
        "\nTipo:", self.tipo,
        "\nHp:", self.hp,
        "\nSpd:", self.spd,
        "\nKg:", self.kg,
        "\nAtaque:", self.ataque,
        "\nDefesa:", self.defesa,
        "\nAltura:", self.altura)

    def embaralhar():
        print ("Embaralhando...")
        sleep(1)
        pokemonlist = [rayquaza, urshifu, pichu, empoleon, mewtwo, pikachu, froakie, deino]
        random.shuffle(pokemonlist)

        pokemon1 = pokemonlist[1]
        pokemon2 = pokemonlist[2]     

        print ("Embaralhado!")
        print (pokemon1, pokemon2)


    def escolher_atributo(self):
        atributo = input("Qual atributo você deseja comparar?\n[1] Overall\n[2] Hp\n[3] Spd\n[4] Kg\n[5] Ataque\n[6] Defesa\n[7] Altura\nR: ")
        if atributo == 1:
            atributo = self.overall
        
        elif atributo == 2:
            atributo = self.hp

        elif atributo == 3:
            atributo = self.spd

        elif atributo == 4:
            atributo = self.kg

        elif atributo == 5:
            atributo = self.ataque

        elif atributo == 6:
            atributo = self.defesa

        if atributo == 7:
            atributo = self.altura

    def compararCartas(self, pokemon1, pokemon2, atributo):
        if self.pokemon1.atributo > self.pokemon2.atributo:
            return True
        if self.pokemon1.atributo < self.pokemon2.atributo:
            return False
        else: 
            return None

rayquaza = Pokemon("Rayquaza", "99", "Dragão Voador", "105", "95", "206.5", "150", "90", "7.0")
urshifu = Pokemon("Urshifu", "72", "Água", "96", "89", "92.0", "85", "74", "1.9")
pichu = Pokemon("Pichu", "56", "Elétrico", "20", "60", "2.0", "40", "15", "0.3")
empoleon = Pokemon("Empoleon", "84", "Água", "84", "60", "84.0", "86", "88", "1.7")
mewtwo = Pokemon("Mewtwo", "99", "Psíquico", "106", "130", "122.0", "110", "90", "2.0")
pikachu = Pokemon("Pikachu", "64", "Elétrico", "35", "90", "6.0", "55", "40", "0.4")
froakie = Pokemon("Froakie", "60", "Água", "41", "71", "7.0", "56", "40", "0.3")
deino = Pokemon("Deino", "65", "Dragão" "Sombrio", "52", "38", "17.0", "65", "50", "0.8")

Pokemons = [     Pokemon("Rayquaza", "99", "Dragão Voador", "105", "95", "206.5", "150", "90", "7.0"),     Pokemon("Urshifu", "72", "Água", "96", "89", "92.0", "85", "74", "1.9"),     Pokemon("Pichu", "56", "Elétrico", "20", "60", "2.0", "40", "15", "0.3"),     Pokemon("Empoleon", "84", "Água", "84", "60", "84.0", "86", "88", "1.7"),     Pokemon("Mewtwo", "99", "Psíquico", "106", "130", "122.0", "110", "90", "2.0"),     Pokemon("Pikachu", "64", "Elétrico", "35", "90", "6.0", "55", "40", "0.4"),     Pokemon("Froakie", "60", "Água", "41", "71", "7.0", "56", "40", "0.3"),     Pokemon("Deino", "65", "Dragão | Sombrio", "52", "38", "17.0", "65", "50", "0.8")    ]

Pokemon.embaralhar("")


