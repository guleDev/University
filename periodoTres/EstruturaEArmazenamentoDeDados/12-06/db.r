install.packages("RMySQL")

library("RMySQL")
library("DBI")

user = "ESW2024_E7"
password = "123mudar"
dbname = "ESW2024_E7_AUTOTECH"
host = "167.99.252.245"

mydb = dbConnect(MySQL(), user=user, password=password, dbname=dbname, host=host)

dbListTables(mydb)

dbListFields(mydb, 'InventarioPecas')

query_sql = dbSendQuery(mydb, "SELECT * FROM InventarioPecas;")
lista = fetch(query_sql, n=-1)
lista
