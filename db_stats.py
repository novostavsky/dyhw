import pyodbc

DB = '[SMARTBench]'
TABLE = '[dbo].[BenchLog]'
COLUMN = '[Primary Skill]'
#COLUMN = '[id]'

CONNECTION = 'DRIVER={SQL Server};SERVER=localhost;UID=;PWD='

#check for duplicates
def check_if_unique(cursor):
    query = 'select {} from {}.{} group by {} having count(*) >1'.format(COLUMN,DB,TABLE,COLUMN)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#check stats on numerical fields
def check_stats_on_numerical(cursor):
    query = 'select min({}), max({}), avg({}) from {}.{}'.format(COLUMN,COLUMN,COLUMN,DB,TABLE)
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)

#check stats on a string fields
def check_stats_on_string(cursor):
    all_query = 'select count(*) from {}.{}'.format(DB,TABLE)
    cursor.execute(all_query)
    all = float(cursor.fetchone()[0])

    column_query = 'select {}, count(*) from {}.{} group by {}'.format(COLUMN,DB,TABLE,COLUMN)
    cursor.execute(column_query)
    rows = cursor.fetchall()
    for row in rows:
        print( "{} - {}".format(row[0],(float(row[1]/all) )))

#check length on a max string field
def check_max_min_length_on_string(cursor):
    query = 'select max(len({})),min(len({})),avg(len({})) from {}.{}'.format(COLUMN,COLUMN,COLUMN,DB,TABLE)
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)

# Specifying the ODBC driver, server name, database, etc. directly
# Create a cursor from the connection
cnxn = pyodbc.connect(CONNECTION)
cursor = cnxn.cursor()

check_if_unique(cursor)
#check_stats_on_numerical(cursor)
check_stats_on_string(cursor)
check_max_min_length_on_string(cursor)

