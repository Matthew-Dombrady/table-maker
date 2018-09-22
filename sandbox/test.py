from table_maker import Table

t = Table.Table('Test table', ['Student name', 'GPA', "Jobs", "GFs"], '#')
t.addEntry(["Ardhendu", "12", "20", "100"])
t.addEntry(["Sagar", "12", "6", "5"])
t.addEntry(["Matthew", "1", "0", "0"])
t.addEntry(["Giannis Antentekounpo", "12", "1", "1"])
t.addEntries([["Venushan", "5", "0", "-1"],["John", "12", "0", "0"]])
t.print()




#t = Table(table_title, labels, '=')
#t.addEntry('bargea', 12)

'''
t.addEntry()
t.addEntries()
t.removeEntry()
t.sort()
t.print()

'''
