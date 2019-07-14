import sqlite3
import pandas as pd

connection = sqlite3.connect('bank.db')
pd.set_option('display.max_columns', None)

sql = "SELECT * FROM clients"
df = pd.read_sql(sql, connection)
print(df.head(3))