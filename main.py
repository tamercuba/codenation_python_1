# coding: utf-8
import csv
import operator


# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
class FifaData:
    def __init__(self):
        self.items = []

    def set_items(self):
        with open('data.csv', 'r') as data_file:
            for row in csv.DictReader(data_file):
                self.items.append(row)
    
    def get_items(self):
        return self.items

fifa_data = FifaData()
fifa_data.set_items()
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    nationality = []
    for row in fifa_data.get_items():
        if row['nationality'] not in nationality:
            nationality.append(row['nationality'])
    return len(nationality)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    clubs = []
    for row in fifa_data.get_items():
        if row['club'] not in clubs:
            clubs.append(row['club'])
    return len(clubs)
    

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    palyers_name = []
    for row in fifa_data.get_items():
        palyers_name.append(row['full_name'])
        if len(palyers_name) == 20:
            break
    return palyers_name


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    top_ten = []
    sorted_players = sorted(fifa_data.get_items(), key=lambda row: float(row['eur_wage']), reverse=True)
    for player in sorted_players[:10]:
        top_ten.append(player['full_name'])
    return top_ten

#Q5. Quem são os 10 jogadores mais velhos?
def q_5():
    top_ten = []
    sorted_palyers = sorted(fifa_data.get_items(), key=lambda row: int(row['age']), reverse = True)
    for player in sorted_palyers[:10]:
        top_ten.append(player['full_name'])
    return top_ten

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    ages = {}
    for row in fifa_data.get_items():
        if int(row['age']) in ages:
            ages[int(row['age'])] += 1
        else:
            ages[int(row['age'])] = int(1) 
    return ages


