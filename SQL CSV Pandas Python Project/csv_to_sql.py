import sqlite3
import pandas as pd

connection = sqlite3.connect('bank.db')
df = pd.read_csv('bank.csv', delimiter=';')
df.to_sql('clients', connection)
connection.close()
