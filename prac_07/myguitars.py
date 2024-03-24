import csv
from guitar import Guitar


def main():
    languages = []
    in_file = open('guitar.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = Guitar(parts[0], parts[1], reflection)
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)


main()


def using_csv():
    in_file = open('guitar.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()