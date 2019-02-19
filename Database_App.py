import sqlite3

#connect to database
db = sqlite3.connect('chainsaw_juggling_records.db')

#allows you to access columns by column name
db.row_factory = sqlite3.Row

#create cursor object to execute commands
cur = db.cursor()

#create a table named records if it doesn't exist
cur.execute('create table if not exists records(Name text, Country text, Num_Catches integer)')

#prints menu selections and gets/returns selection
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
    name = input("What is this person's name? ")
    country = input('What country is this person from? ')
    catches = int(input('How many catches did this person perform? '))
    #add record to database
    cur.execute('insert into records values(?, ?, ?)', (name, country, catches))
    #commit the changes
    db.commit()

#method that searches records by name then prints the record
def search_record():
    #get user input
    name = input('Who do you want to search for? ')
    #get record if it exists
    cur.execute('select * from records where name = ?', (name,))
    #I got the idea for the next few lines from https://pynative.com/python-mysql-select-query-to-fetch-data/
    records = cur.fetchall()
    for record in records:
        #print record
        print('Name: ', record[0], ' Country: ', record[1], ' Catches: ', record[2])


#method that updates number of catches in a record
def update_record():
    #get row to update
    name = input('Who do you want to update the number of catches for? ')
    catches = int(input('What is their new record of catches? '))
    #update the record
    cur.execute('update records set Num_Catches = ? where name = ?', (catches, name))
    #commit the changes
    db.commit()

#method to delete a record
def delete_record():
    #get the record to delete
    name = input("What is the name of the person who's record you want to delete? ")
    #delete the record
    cur.execute('delete from records where name = ?', (name,))
    #commit the changes
    db.commit()

#main method
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
