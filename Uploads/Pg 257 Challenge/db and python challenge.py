import sqlite3


# I need some information to put in database

livingValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))




##name = ("Jean-Baptiste Zorg", "Korben Dallas", "Ak\'not")
##species = ('Human', 'Meat Popsicle', 'Mangalore')
##iq = 122, 100, -5


# connect and create a conect to modify data within 
with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
##    i = 0
    c.execute("DROP TABLE IF EXISTS livingThings")
    c.execute("CREATE TABLE livingThings(Name TEXT, Species TEXT, Iq INT)")
    c.executemany("INSERT INTO livingThings VALUES(?, ?, ?)",
                    livingValues)
    c.execute("UPDATE livingThings SET Species=? WHERE Name=? AND Iq=?",
            ('Human', 'Korben Dallas', 100))
    c.execute("SELECT Name, Iq FROM livingThings WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)


#c.execute('UPDATE livingThings SET  = Human WHERE Name = Korben Dallas')

                  
##    if i < len(name):
##        for each in name:
##            line = "INSERT INTO People VALUES ('"+ name[i] +"', '"+ species[i] +"', "+str(iq[i]) +")"
##            c.execute(line)
##            print(line)
##            i+=1
        
