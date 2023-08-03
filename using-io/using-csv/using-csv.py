import csv


def main():

    # Writing a csv file:
    with open('friends.csv', 'a', newline = '') as csvfile:
        fields_names = ["id", "first-name", "last-name"]
        writer = csv.DictWriter(csvfile, fieldnames = fields_names, lineterminator = "\n")
        writer.writeheader()
        writer.writerow({'id': "1",  'first-name': "charles", 'last-name': "whitfield"})
        writer.writerow({'id': "2",  'first-name': "svetlana", 'last-name': "rosemond"})
        writer.writerow({'id': "3",  'first-name': "annabelle", 'last-name': "vodianova"})
        writer.writerow({'id': "4",  'first-name': "natalya", 'last-name': "sivakova"})
    
    # Reading a csv file:
    with open("friends.csv", newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["id"], row["first-name"].title(), row["last-name"].title())
                
if __name__ == "__main__":
    main()
