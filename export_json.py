import psycopg2
import json

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cursor = conn.cursor()


cursor.execute("SELECT region_name, region_description FROM region")
region_data = cursor.fetchall()


cursor.execute("SELECT name, cost, health, attack, unit_id FROM unit_card")
unit_data = cursor.fetchall()


cursor.execute("SELECT cost, effect, name, spell_id FROM spell_card")
spell_card_data = cursor.fetchall()


cursor.execute("SELECT region_name, unit_id FROM region_units")
region_units_data = cursor.fetchall()


cursor.execute("SELECT region_name, spell_id FROM region_spells")
region_spells_data = cursor.fetchall()


cursor.execute("SELECT cost, attack, health, champion_name FROM champion_card")
champion_card_data = cursor.fetchall()


cursor.execute("SELECT region_name, champion_name FROM champion_region")
champion_region_data = cursor.fetchall()

data_to_export = {
    "region": region_data,
    "unit_card": unit_data,
    "spell_card": spell_card_data,
    "region_units": region_units_data,
    "region_spells": region_spells_data,
    "champion_card": champion_card_data,
    "champion_region": champion_region_data
}

# Зберегти дані у JSON файл
with open('exported_data.json', 'w') as json_file:
    json.dump(data_to_export, json_file, indent=2)

cursor.close()
conn.close()
