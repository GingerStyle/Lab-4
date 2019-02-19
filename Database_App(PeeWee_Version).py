from peewee import *

#which database
db = SqliteDatabase('chainsaw_juggling_records.db')

class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} if from {self.country} and performed {self.catches} catches'

#connect to database
db.connect()
#create tables based on the model
db.create_tables([Record])

def menu_print():
    print('1. Add Record')
    print('2. Search by Name')
    print('3. Update Catches')
    print('4. Delete Record')
    print('5. Exit')
    user_input = int(input('Enter the number of your selection. '))
    return user_input

#method to add records to the database
def add_record():
    #get required information
    person = input("What is this person's name? ")
    origin_country = input('What country is this person from? ')
    number = int(input('How many catches did this person perform? '))
    #add record to database
    entry = Record(name = person, country = origin_country, catches = number)
    #commit the changes
    entry.save()

#method that searches records by name then prints the record
def search_record():
    #get user input
    person = input('Who do you want to search for? ')
    #get record if it exists
    for record in Record.select().where(Record.name == person):
        print(record)

#method that updates number of catches in a record
def update_record():
    #get row to update
    person = input('Who do you want to update the number of catches for? ')
    number = int(input('What is their new record of catches? '))
    #update the record
    query = Record.update(catches = number).where(Record.name == person)
    #commit the changes
    query.execute()

#method to delete a record
def delete_record():
    #get the record to delete
    person = input("What is the name of the person who's record you want to delete? ")
    #delete the record
    query = Record.delete().where(Record.name == person)
    #commit the changes
    query.execute()

def main():
    #display menu and get user input
    user_input = menu_print()
    #call appropriate method
    while user_input != 5:
        if user_input == 1:
            add_record()
        elif user_input == 2:
            search_record()
        elif user_input == 3:
            update_record()
        elif user_input == 4:
            delete_record()
        #re-display the menu
        user_input = menu_print()

    #when 5 is selected, exit the program
    exit()


main()


