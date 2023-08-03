- [Writing a `csv` file](#writing-a-csv-file)
- [Reading a `csv` file](#reading-a-csv-file)
#### <a name="writing-a-csv-file"></a>Writing a `csv` file:
```python
with open('friends.csv', 'a', newline='') as csvfile:
    fields_names = ["id", "first-name", "last-name"]
    writer = csv.DictWriter(csvfile, fieldnames = fields_names, lineterminator = "\n")
    writer.writeheader()
    writer.writerow({'id': "1",  'first-name': "charles", 'last-name': "whitfield"})
    writer.writerow({'id': "2",  'first-name': "svetlana", 'last-name': "rosemond"})
    writer.writerow({'id': "3",  'first-name': "annabelle", 'last-name': "vodianova"})
    writer.writerow({'id': "4",  'first-name': "natalya", 'last-name': "sivakova"})
```
#### <a name="reading-a-csv-file"></a>Reading a `csv` file:
```python
with open("friends.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["id"], row["first-name"].title(), row["last-name"].title())
```
