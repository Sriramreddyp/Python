import csv

with open("data.csv", "w") as file:
    Writer = csv.writer(file)  # have to open it as file object
    Writer.writerow(["Trasaction_id"])
    Writer.writerow(["100"])

with open("data.csv") as file:
    Reader = csv.reader(file)  # have to open it as file object
    # Converting it to a list changes reader's starting postion so it cant interate
    print(list(Reader))
    for row in Reader:
        print(row)

    # Main Concept - Manipulation
    # Python return an object all the time - iterable ,non-iterable
