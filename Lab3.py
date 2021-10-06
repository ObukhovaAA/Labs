'''
                         

'''

import json
import csv

json_data = []
D = ["vitamin" , "vitamers" , "solubility" , "daily_requirement" , "deficiency_diseases"]
path = ' C:\\Users\\NA\\Desktop\\Proga\\vitamins\\vitamins(1) '

сsv_file = open("vitamins.csv", "w")
file_writer = csv.writer(csv_file)
file_writer.writerow(D)

for file_name in os.listdir(path):
    with open(file_name) as cur_file:
    cur_file_read = cur_file.readlines()
    for n in range(len(cur_file_read) - 1) :
        cur_file_read[n] = cur_file_read[n].strip()
        cur_file_read[1] = cur_file_read[1].split(' , ')
        cur_file_read[4] = cur_file_read[4].split(' , ')
        file_writer.writerow(cur_file_read) # в csv формат
    for i in range(len(D)):
        d = {D[i] : cur_file_read[i] for i in range(len(D))}
    json_data.append(d)

сsv_file.close()

with open("vitamins.json", "w") as json_file :
    json.dump(json_data, json_file)
