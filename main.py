import sqlite3
import requests
from bs4 import BeautifulSoup
while (True):
    print('1. Add website')
    print('2. Find Keyword')
    print('3. Delete Website')
    print('4. Exit')
    print('5. Show database')
    command = int(input())
    if (command == 1):
        print("Please input the domain of website with https")
        url = input()
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute('Create table if not exists website(name text)')
        cur.execute("insert into website(name) values(?)", (url, ))
        connection.commit()
        connection.close()
        print("success")
    elif (command == 2):
        print("Please input the domain of website with https")
        url = input()
        print("Please input the keyword from website")
        key = input()
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute('select * from website where name = ?', (url, ))
        row = cur.fetchall()
        if row:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            cnt = text.lower().count(key.lower())
            print('Found ' + str(cnt) + ' keywords.')
        else:
            print("No such website is in the Database")
        connection.commit()
        connection.close()
        print("success")
    elif (command == 3):
        print("what website do you want to delete?")
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute("SELECT * FROM website")
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            print(row[0])
        print('Which website do you want to delete?')
        id = input()
        sql = 'DELETE FROM website WHERE name = ?'
        conn = sqlite3.connect('main.sl3')
        cur = conn.cursor()
        cur.execute(sql, (id, ))
        conn.commit()
        conn.close()

    elif (command == 4):
        break

    else:
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute("SELECT * FROM website")
        rows = cur.fetchall()
        print(rows)
