import sqlite3
import pandas as pd
import numpy as np

connection = sqlite3.connect('bank.db')
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS clients (
             "index" SMALLINT PRIMARY KEY,
             age TINYINT,
             job VARCHAR(15),
             marital VARCHAR(10),
             education VARCHAR(10),
             "default" VARCHAR(3),
             balance BIGINT,
             housing VARCHAR(3),
             loan VARCHAR(3),
             contact VARCHAR(10),
             day TINYINT,
             month VARCHAR(3),
             duration SMALLINT,
             campaign TINYINT,
             pdays SMALLINT,
             previous TINYINT,
             poutcome VARCHAR(10),
             y VARCHAR(3)
             )""")

pd.set_option('display.max_columns', 500)
df = pd.read_csv('bank.csv', delimiter=';')

for row in range(len(df)):
    row_tuple = (row,)
    for col in range(len(df.columns)):
        val = df.iloc[row, col]
        if isinstance(val, np.int64):
            val = int(val)
        row_tuple += (val,)
    with connection:
        c.execute(
            """INSERT INTO clients ("index", age, job, marital, education, "default", balance, housing, loan, contact, day, 
            month, duration, campaign, pdays, previous, poutcome, y) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            row_tuple)

connection.close()
