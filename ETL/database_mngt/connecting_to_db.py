import pyodbc

server = '.\sqlexpress' 
database = 'test' 
username = 'sa'  
password  = 'marfa'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

sql_statement = "select 1"
response = cursor.execute(sql_statement).fetchone()
print(response[0])