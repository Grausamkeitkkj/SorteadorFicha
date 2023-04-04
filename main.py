import random
import math

racas = ["Anão", "Elfo", "Goblin", "Humano", "Halfling", "Gnomo"]
habilidades = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
armas = {
    1: ['Adaga', 'Alabarda', 'Cimitarra', 'Clava', 'Cajado', 'Espada bastarda', 'Espada curta', 'Espada longa', 'Falcione', 'Florete', 'Glaive', 'Kama', 'Lança', 'Machado de batalha', 'Machado de guerra', 'Maça', 'Maça leve', 'Martelo de guerra', 'Punhal', 'Rapieira', 'Sabre', 'Tonfa', 'Tridente'],
    2: ['Arco curto', 'Arco longo', 'Besta de mão', 'Besta leve', 'Besta pesada', 'Corrente', 'Shuriken'],
    3: ['Adaga','Espada curta','Kukri','Rapieira,Chicote']
}
instrumento_musical = ["Alaúde","Violão","Flauta","Lira","Clarinete","Violino",]
foco_arcano = ["Varinha","Cajado","Pingente"]
armaduras = {14: ["Alcochada", "Couro", "Couro Batido", "Camisão de Malha", "Gibão de Peles", "Cota de Escamas"], 16: ["Cota de Malha", "Peitoral de Aço", "Cota de Talas", "Meia Armadura"], 18: ["Completa"]}
biografia =['Acólito', 'Detetive', 'Estudioso','Artista', 'Apostador', 'Apresentador','Acrobata', 'Discípulo Marcial', 'Marinheiro','Caçador','Criança de Rua','Criminoso', 'Funileiro','Encantador de Animais','Eremita','Gladiador', 'Guarda','Herbalista', 'Lavrador', 'Nômade','Operário', 'Prisioneiro', 'Soldado','Taverneiro']
esquemas_ladino = ["Rufião","Ladrão", "Malandro"]

class personagem:
  def __init__(self, forca = 10, destreza = 10, constituicao = 10, inteligencia = 10, sabedoria = 10, carisma = 10,       arma = 0, arma2 = 0, armadura = 0, CA = 10, HP = 0, biografia = 0, raca = 0):
    self.raca = raca
    self.forca = forca
    self.destreza = destreza
    self.constituicao = constituicao
    self.inteligencia = inteligencia
    self.sabedoria = sabedoria
    self.carisma = carisma
    self.arma= arma
    self.arma2 = arma2
    self.armadura = armadura
    self.CA = CA
    self.HP = HP
    self.biografia = biografia
    
      
  def __str__(self):
        
    return f'Personagem:\nRaça: {self.raca}\nForça: {self.forca} \nDestreza: {self.destreza} \nConstituição: {self.constituicao}\nInteligência: {self.inteligencia}\nSabedoria: {self.sabedoria} \nCarisma: {self.carisma} \nArma: {self.arma}\nArma secundária: {self.arma2}\nArmadura: {self.armadura}\nBiografia : {self.biografia}\nCA: {self.CA}\nHP:{self.HP}'

meu_personagem = personagem()

escolha = int(input("Qual classe você gostaria de escolher?\n1 - Guerreiro\n2 - Mago\n3 - Ladino\n4 - Campeão\n5 - Feiticeiro\n6 - Bardo\n7 - Druida\n8 - Bárbaro\n9 - Patrulheiro\n10 - Clérigo\n11 - Alquimsita\n12 - Monge\n"))


def sorteia_ficha():
  raca_sorteada = random.choice(racas)
  meu_personagem.raca = raca_sorteada
  biografia_sorteada = random.choice(biografia)
  meu_personagem.biografia = biografia_sorteada

  if escolha in [1, 4, 9, 12]:
    habilidade_escolhida = random.choice(["forca", "destreza"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) + 2)
    
    
  elif escolha in [2,11]:
    setattr(meu_personagem, 'inteligencia', getattr(meu_personagem, 'inteligencia')+2)

  elif escolha == 3:
    esquema_sorteado = random.choice(esquemas_ladino)
    if esquema_sorteado == "Rufião":
      setattr(meu_personagem, 'forca', getattr(meu_personagem , 'forca')+2)
    elif esquema_sorteado == 'Ladrão':
      setattr(meu_personagem, 'destreza', getattr(meu_personagem, 'destreza')+2)
    elif esquema_sorteado == 'Malandro':
      setattr(meu_personagem, 'carisma', getattr(meu_personagem, 'carisma')+2)
  
  elif escolha in [5, 6]:
    setattr(meu_personagem, 'carisma', getattr(meu_personagem, 'carisma')+2)

  elif escolha in [7,10]:
    setattr(meu_personagem, 'sabedoria', getattr(meu_personagem, 'sabedoria')+2)

  elif escolha == 8:
    setattr(meu_personagem, 'forca', getattr(meu_personagem, 'forca')+2)

  if raca_sorteada == 'Anão':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP') +10 +(meu_personagem.constituicao - 10)/2)
    setattr(meu_personagem, 'forca', getattr(meu_personagem, 'forca') +2)
    setattr(meu_personagem, 'sabedoria', getattr(meu_personagem, 'sabedoria') +2)
    setattr(meu_personagem, 'carisma', getattr(meu_personagem, 'carisma') -2)
    habilidades.remove('forca')
    habilidades.remove('sabedoria')
    habilidade_escolhida = random.choice(habilidades)

  elif raca_sorteada == 'Elfo':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP') + 6 +(meu_personagem.constituicao - 10)/2)
    setattr(meu_personagem, 'destreza', getattr(meu_personagem, 'destreza') +2)
    setattr(meu_personagem, 'inteligencia', getattr(meu_personagem, 'inteligencia') +2)
    setattr(meu_personagem, 'constituicao', getattr(meu_personagem, 'constituicao') -2)
    habilidades.remove('destreza')
    habilidades.remove('inteligencia')
    habilidade_escolhida = random.choice(habilidades)

  elif raca_sorteada == 'Gnomo':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP') + 8 +(meu_personagem.constituicao - 10)/2)
    setattr(meu_personagem, 'constituicao', getattr(meu_personagem, 'constituicao') +2)
    setattr(meu_personagem, 'carisma', getattr(meu_personagem, 'carisma') +2)
    setattr(meu_personagem, 'forca', getattr(meu_personagem, 'forca') -2)
    habilidades.remove('constituicao')
    habilidades.remove('carisma')
    habilidade_escolhida = random.choice(habilidades)

  elif raca_sorteada == 'Goblin':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP') + 6 + (meu_personagem.constituicao - 10)/2)
    setattr(meu_personagem, 'destreza', getattr(meu_personagem, 'destreza') +2)
    setattr(meu_personagem, 'carisma', getattr(meu_personagem, 'carisma') +2)
    setattr(meu_personagem, 'sabedoria', getattr(meu_personagem, 'sabedoria') -2)
    habilidades.remove('destreza')
    habilidades.remove('carisma')
    habilidade_escolhida = random.choice(habilidades)

  elif raca_sorteada == 'Halfling':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP') + 6 +(meu_personagem.constituicao - 10)/2)
    setattr(meu_personagem, 'destreza', getattr(meu_personagem, 'destreza') +2)
    setattr(meu_personagem, 'sabedoria', getattr(meu_personagem, 'sabedoria') +2)
    setattr(meu_personagem, 'forca', getattr(meu_personagem, 'forca') -2)
    habilidades.remove('destreza')
    habilidades.remove('sabedoria')
    habilidade_escolhida = random.choice(habilidades)

  elif raca_sorteada == 'Humano':
    setattr(meu_personagem, 'HP', getattr(meu_personagem, 'HP')  +8 +(meu_personagem.constituicao - 10)/2)
    habilidade_escolhida = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) + 2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2) + 2)

  if escolha == [1, 12, 9, 4]:
    setattr(meu_personagem, meu_personagem.HP, getattr(meu_personagem, meu_personagem.HP) + 10 +         math.floor(meu_personagem.constituicao - 10/2))

  elif escolha == [2, 5]:
    setattr(meu_personagem, meu_personagem.HP, getattr(meu_personagem, meu_personagem.HP) + 6 + math.floor(meu_personagem.constituicao - 10/2))

  elif escolha == [3, 6, 11, 7, 10]:
    setattr(meu_personagem, meu_personagem.HP, getattr(meu_personagem, meu_personagem.HP) + 8 + math.floor(meu_personagem.constituicao - 10/2))

  elif escolha == 8:
    setattr(meu_personagem, meu_personagem.HP, getattr(meu_personagem, meu_personagem.HP) + 12 + math.floor(meu_personagem.constituicao - 10/2))
  
    
  if biografia == ['Acólito', 'Detetive', 'Estudioso']:
    habilidade_escolhida = random.choice(["sabedoria", "inteligencia"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)
  
  elif biografia == ['Artista', 'Apostador', 'Apresentador']:
    habilidade_escolhida = random.choice(["carisma", "destreza"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Acrobata', 'Discípulo Marcial', 'Marinheiro']:
    habilidade_escolhida = random.choice(["força", "destreza"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Advogado', 'Charlatão', 'Emissário', 'Mercador', 'Nobre', 'Vidente']:
    habilidade_escolhida = random.choice(["inteligencia", "carisma"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == 'Artesão':
    habilidade_escolhida = random.choice(["força", "inteligencia"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Batedor', 'Caçador de Recompensas', 'Mineiro']:
    habilidade_escolhida = random.choice(["força", "sabedoria"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == 'Caçador':
    habilidade_escolhida = random.choice(["destreza", "sabedoria"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == 'Criança de Rua':
    habilidade_escolhida = random.choice(["destreza", "constituicao"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Criminoso', 'Funileiro']:
    habilidade_escolhida = random.choice(["inteligencia", "destreza"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == 'Encantador de Animais':
    habilidade_escolhida = random.choice(['sabedoria', 'carisma'])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia =='Eremita':
    habilidade_escolhida = random.choice(["inteligencia", "constituicao"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Gladiador', 'Guarda']:
    habilidade_escolhida = random.choice(["força", "carisma",])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Herbalista', 'Lavrador', 'Nômade']:
    habilidade_escolhida = random.choice(["constituicao", "sabedoria"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == ['Operário', 'Prisioneiro', 'Soldado']:
    habilidade_escolhida = random.choice(["forca", "constituicao"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  elif biografia == 'Taverneiro':
    habilidade_escolhida = random.choice(["carisma", "constituicao"])
    setattr(meu_personagem, habilidade_escolhida, getattr(meu_personagem, habilidade_escolhida) +2)
    habilidades.remove(habilidade_escolhida)
    habilidade_escolhida2 = random.choice(habilidades)
    setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2)+2)

  if meu_personagem.forca <= 14:
    armadura_valor = 14
  elif 15 <= personagem.forca <=17:
    armadura_valor = 16
  else:
    armadura_valor = 18

  armadura_sorteada = random.choice(armaduras[armadura_valor])
  meu_personagem.armadura = armadura_sorteada

  if armadura_sorteada == 'Alcochoada':
    setattr(meu_personagem, 'CA', getattr(meu_personagem,'CA') + 1 + min(meu_personagem.destreza, 3))

  elif armadura_sorteada == 'Couro':
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 1 + min(meu_personagem.destreza, 4))

  elif armadura_sorteada in ['Couro Batido', 'Camisão de Malha']:
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 2 + min(meu_personagem.destreza, 3))

  elif armadura_sorteada in ['Gibão de Peles', 'Cota de Escamas']:
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 3 + min(meu_personagem.destreza, 2))

  elif armadura_sorteada in ['Cota de Malha', 'Peitoral de Aço']:
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 4 + min(meu_personagem.destreza, 1))

  elif armadura_sorteada in ['Cota de Talas', 'Meia Armadura']:
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 5 + min(meu_personagem.destreza, 1))

  elif armadura_sorteada == 'Completa':
    setattr(meu_personagem, 'CA', getattr(meu_personagem, 'CA') + 6)


  if meu_personagem.forca > meu_personagem.destreza:
    meu_personagem.arma = random.choice(armas[1])
    meu_personagem.arma2 = random.choice(armas[1])

  elif meu_personagem.forca <= meu_personagem.destreza:
    meu_personagem.arma = random.choice(armas[2])
    meu_personagem.arma2 = random.choice(armas[3])

habilidades_copia = list(habilidades)

habilidade_escolhida1 = random.choice(habilidades_copia)
setattr(meu_personagem, habilidade_escolhida1, getattr(meu_personagem, habilidade_escolhida1) +2)
habilidades_copia.remove(habilidade_escolhida1)

habilidade_escolhida2 = random.choice(habilidades_copia)
setattr(meu_personagem, habilidade_escolhida2, getattr(meu_personagem, habilidade_escolhida2) +2)
habilidades_copia.remove(habilidade_escolhida2)

habilidade_escolhida3 = random.choice(habilidades_copia)
setattr(meu_personagem, habilidade_escolhida3, getattr(meu_personagem, habilidade_escolhida3) +2)
habilidades_copia.remove(habilidade_escolhida3)

habilidade_escolhida4 = random.choice(habilidades_copia)
setattr(meu_personagem, habilidade_escolhida4, getattr(meu_personagem, habilidade_escolhida4) +2)



sorteia_ficha()
print(meu_personagem)