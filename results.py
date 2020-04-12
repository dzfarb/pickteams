import os
import csv

results = {}

print("these are the games you have logged")
for file in os.listdir("./"):
    file = os.path.splitext(file)
    if file[1] == ".csv":
        print(file[0])

print()
file = input("what game are you playing: ")
file = file + ".csv"
os.system('clear')

print("input results as {player score}")
print("input \"done\" when all results have been added")
result = input("add result: ")
while result != "done":
    resultlist = result.split(' ')
    results[resultlist[0]] = int(resultlist[1])
    result = input("add result: ")


# open old file
if os.path.exists(file):
    with open(file,'rt')as f:
        data = csv.reader(f)
        for row in data:
            # gets name of person
            name = row[0]
            if name in results:
                results[name] += int(row[1])
            else:
                results[name] = row[1]

# write data to new file
with open(file, mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for key in results.keys():
        writer.writerow([key, results[key]])


os.system('clear')
#print(results)
print("results have been logged")
