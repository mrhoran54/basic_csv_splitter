import csv

dic = {"John": "place#place.com", "Mom": "mom@example.com", "Prince Harry": "Princeharry_place.com", "your mom": "is_a_hoe.com"} #dictionary

csv = open('FunTEs1.csv', 'wb')

column_title_header = "name, email\n"
    
x = csv.write(column_title_header)

for key in dic.keys():
	name = key
	email = dic[key]
	row = name + "," + email + "\n"
	csv.write(row)

