# Import writer class from csv module
from csv import writer

# Path: server.py
def write_to_csv(data):
    with open('database.csv', 'a') as database:
        csv_writer = writer(database)
        csv_writer.writerow(data)
