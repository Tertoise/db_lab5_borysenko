import psycopg2
import csv

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cursor = conn.cursor()

# Збереження даних з таблиці region
cursor.execute("SELECT region_name, region_description FROM region")
region_data = cursor.fetchall()

with open('region.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['region_name', 'region_description'])
    csv_writer.writerows(region_data)


# Збереження даних з таблиці unit_card
cursor.execute("SELECT name, cost, health, attack, unit_id FROM unit_card")
unit_data = cursor.fetchall()

with open('unit_card.csv', 'w', encoding='UTF8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['name', 'cost', 'health', 'attack', 'unit_id'])
    
# Збереження даних з таблиці spell_card
cursor.execute("SELECT cost, effect, name, spell_id FROM spell_card")
spell_card_data = cursor.fetchall()

with open('spell_card.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['cost', 'effect', 'name', 'spell_id'])
    csv_writer.writerows(spell_card_data)

# Збереження даних з таблиці region
cursor.execute("SELECT region_name, region_description FROM region")
region_data = cursor.fetchall()

with open('region.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['region_name', 'region_description'])
    csv_writer.writerows(region_data)

# Збереження даних з таблиці region_units
cursor.execute("SELECT region_name, unit_id FROM region_units")
region_units_data = cursor.fetchall()

with open('region_units.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['region_name', 'unit_id'])
    csv_writer.writerows(region_units_data)

# Збереження даних з таблиці region_spells
cursor.execute("SELECT region_name, spell_id FROM region_spells")
region_spells_data = cursor.fetchall()

with open('region_spells.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['region_name', 'spell_id'])
    csv_writer.writerows(region_spells_data)

# Збереження даних з таблиці champion_card
cursor.execute("SELECT cost, attack, health, champion_name FROM champion_card")
champion_card_data = cursor.fetchall()

with open('champion_card.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['cost', 'attack', 'health', 'champion_name'])
    csv_writer.writerows(champion_card_data)

# Збереження даних з таблиці champion_region
cursor.execute("SELECT region_name, champion_name FROM champion_region")
champion_region_data = cursor.fetchall()

with open('champion_region.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['region_name', 'champion_name'])
    csv_writer.writerows(champion_region_data)

cursor.close()
conn.close()
