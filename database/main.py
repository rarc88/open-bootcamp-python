import sqlite3
from getpass import getpass


def main():
    username = input('Into your username: ')
    password = getpass('Input your passwrod: ')

    # if login(username, password):
    #     print('Welcome')
    # else:
    #     print('Not authorized')

    createUser(username, password)


def login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    return data is not None


def createUser(username, password):
    conn = sqlite3.connect('database.db', isolation_level=None)
    cursor = conn.cursor()

    query = 'INSERT INTO users (id, username, password) VALUES ((SELECT COALESCE(MAX(id),0)+1 FROM users), ?, ?)'

    rows = cursor.execute(query, (username, password))
    # conn.commit()
    print(rows)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
