import pyodbc

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESKTOP-R7LHLUR;'
                               'Database=f19_sql;'
                               'trusted_Connection=yes;'
                               )

print('Connected Successfully')

cursor = connection.cursor()

create_sql = 'drop table if exists Roster create table Roster (Name varchar(30), Species varchar(30), Age int)'
insert_sql = "insert into Roster values ('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)"
select_sql = 'select * from Roster'

cursor.execute(create_sql)
cursor.execute(insert_sql)

data = cursor.execute(select_sql)
print(data.fetchall())

update_sql = "update Roster set Name = 'Ezri Dax' where Name = 'Jadzia Dax' "
cursor.execute(update_sql)
cursor.execute(select_sql)
print(data.fetchall())

second_select_sql = "select Name, Age from Roster where Species = 'Bajoran'"
cursor.execute(second_select_sql)
data2 = cursor.execute(second_select_sql)
print(data2.fetchall())

connection.commit()
cursor.close()
connection.close()