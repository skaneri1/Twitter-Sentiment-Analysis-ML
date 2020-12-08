import sqlite3
import pandas as pd

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%china%' ORDER BY unix DESC LIMIT 1000", conn)
df.sort_values('unix', inplace=True)

df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
df.dropna(inplace=True)
print(df.tail())
