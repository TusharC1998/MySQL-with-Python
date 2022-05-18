from DBClass import Dbuser

db = Dbuser()

print()
print('*****WELCOME TO MYSQL WITH PYTHON*****')
print()
print('Press 1 to fecth all details from User table.')
print('Press 2 to enter user in User table.')
print('Press 3 to select user with userId.')
print('Press 4 to update details in User table.')
print('Press 5 to delete user.')
print()

choose = int(input('Enter the no.:'))

if choose == 1:
    db.fetchAll()

elif choose == 2:
    a = int(input('Enter the userId: '))
    b = input('Enter the userName: ')
    c = int(input('Enter the phone no.: '))
    db.insertUser(a, b, c)

elif choose == 3:
    a = int(input('Enter the userId :'))
    db.fetchId(a)

elif choose == 4:
    c = int(input('Enter the userId for which need to update : '))
    a = input('Enter the updated userName : ')
    b = int(input('ENter the updated phone no : '))
    db.updateUser(a, b, c)

elif choose == 5:
    a = int(input('Enter the userId need to del :'))
    db.delUser(a)

else:
    print('Enter from the given input')
