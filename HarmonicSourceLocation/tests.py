# from django.test import TestCase

#
# DATA_INFO={"HOST":"127.0.0.1",
#            "USER":'sa',
#            "PASSWORD":'123456',
#            "DATABASE":'test',
#            "TABLE":"DayLoadRate"
# }

DATA_INFO={"HOST":"127.0.0.1",
           "USER":'sa',
           "PASSWORD":'fenghanyu',
           "DATABASE":'PQES',
           "TABLE":"Site"
}
import pymssql
connection=pymssql.connect("127.0.0.1","sa","fenghanyu","PQES",charset="UTF-8");
cursor=connection.cursor();
param="'' or 1=1"
cursor.execute("select * from Site ");

print(cursor.fetchall())