import mysql.connector

cnx = mysql.connector.connect(user='iiot', password='pass',
                              host='10.128.10.234',
                              database='Test')
cnx.close()