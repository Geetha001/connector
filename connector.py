import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='9894',
    port='3306',
    database='userform'
)
mycursor = mydb.cursor()
mycursor.execute('select * from geetha')
geetha = mycursor.fetchall()
for geetha in geetha:
    print(geetha)
    print('userid :' + geetha[1])
    print('first name : ' + geetha[2])
    print('last name : ' + geetha[3])
    print('mailid : 3' + geetha[4])