from os import system
from pprint import pprint


def main():
    system('clear')
    users = userList()
    pprint(users)


def userList():
    f = open('/etc/passwd', 'r')
    data = f.readlines()
    f.close()
    users = []
    for line in data:
        if line[0] == '#' or line[0] == '_':
            continue
        user = line.split(':')[0]
        users.append(user)
    return users


if __name__ == '__main__':
    main()
