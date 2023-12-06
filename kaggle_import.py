import csv
import psycopg2

csv_file_path = 'data.csv'

data_list = []

with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data_list.append(row)


add_region = [data_list[59][0], "Divided city,people live both poverly and wealthy"]
add_unit = [data_list[59][9], data_list[59][3], data_list[59][4], data_list[59][2], "1pnz"]
add_spell = [data_list[58][3],data_list[58][5][:-35], data_list[58][9], "1spnz"]

insert_query_region = "INSERT INTO region (region_name, region_description) VALUES (%s, %s);"
insert_query_unit = "INSERT INTO unit_card (name, cost, health, attack, unit_id) VALUES (%s, %s, %s, %s, %s);"
insert_query_spell = "INSERT INTO spell_card (cost, effect, name, spell_id) VALUES (%s, %s, %s, %s);"
insert_query_spell_region = "INSERT INTO region_spells (region_name, spell_id) VALUES (%s, %s);"
insert_query_unit_region = "INSERT INTO region_units (region_name, unit_id) VALUES (%s, %s);"

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cursor = conn.cursor()

cursor.execute(insert_query_region, add_region)
cursor.execute(insert_query_unit, add_unit)
cursor.execute(insert_query_spell, add_spell)
region_unit = [add_region[0], add_unit[-1]]
region_spell = [add_region[0], add_spell[-1]]
cursor.execute(insert_query_spell_region, region_spell)
cursor.execute(insert_query_unit_region, region_unit)

conn.commit()