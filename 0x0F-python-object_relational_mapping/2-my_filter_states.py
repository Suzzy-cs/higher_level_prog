#!/usr/bin/python3
"""
display all values in the states table where name matches the argument
take 4 arguments ie <mysql username>, <mysql password>, <database name> and
<state name searched>
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(user=argv[1], passwd=argv[2],
                 db=argv[3], host="localhost", port=3306)
    c = db.cursor()
    st = argv[4]
    sech = "SELECT * FROM states WHERE name='{}' ORDER BY states.id".format(st)
    c.execute(sech)
    [print(state) for state in c.fetchall()]

    c.close()
    db.close()
