import os
import csv
import operator

#this script will parse and calculate total weight for each keyword from all csv files
# weight calculated from total search volume for this word in all keyphrases

csv_folder = "d:\Dropbox\Amazon\Puzzles\Keywords"

def get_pathes(folder):
    list = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            list.append(os.path.join(root, f))
    return list

def parse_and_calculate(files_list):
    out = {}
    for f in files_list:
        with open(f) as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                phrase = row[0]
                volume = int(row[1])
                words = phrase.split()
                for w in words:
                    if w not in out:
                        out[w] = volume
                    else:
                        out[w] += volume

    return out


all_files_list = get_pathes(csv_folder)
print(all_files_list)
calculated_data = parse_and_calculate(all_files_list)
#print(calculated_data)
sorted_data = sorted(calculated_data.items(), key=operator.itemgetter(1), reverse=True)
for i in sorted_data:
    print ("{:<15} {}".format(i[0], i[1]))