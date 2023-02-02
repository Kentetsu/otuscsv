import csv
import json
import os

os.chdir('../data')
FILES_DIR = os.getcwd()


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


complete_book = []
CSV_FILE_PATH = get_path(filename="books.csv")
with open(CSV_FILE_PATH, newline='') as csvfile:
    books = csv.DictReader(csvfile, delimiter=',')
    for book in books:
        complete_book.append(book)


JSON_FILE_PATH = get_path(filename="users.json")
with open(JSON_FILE_PATH, newline='') as jsonfile:
    users = json.loads(jsonfile.read())


for user in users:
    user.update(books=[])


while bool(complete_book):
    for user in users:
        try:
            user['books'].append(complete_book.pop())
        except IndexError:
            break

with open('result.json', 'w') as output_file:
    output_file.write(json.dumps(users, indent=4))