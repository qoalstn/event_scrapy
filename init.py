import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS item_cu (
    item_idx TEXT PRIMARY KEY,
    name TEXT,
    price INTEGER,
    img TEXT,
    created_at TEXT,
    updated_at TEXT,
    expired_at TEXT
)
''')


cursor.execute(
'''CREATE TABLE IF NOT EXISTS item_gs25 (
  item_idx TEXT PRIMARY KEY,
  name TEXT,
  price INTEGER,
  img TEXT ,
  created_at TEXT ,
  updated_at TEXT ,
  expired_at TEXT
)
''')


cursor.execute(
'''CREATE TABLE IF NOT EXISTS like (
  idx INTEGER PRIMARY KEY,
  uid INTEGER ,
  item_idx INTEGER ,
  is_like TEXT CHECK (is_like IN ('Y','N')),
  created_at TEXT ,
  updated_at TEXT
) 
''')


cursor.execute(
'''CREATE TABLE IF NOT EXISTS user (
  uid INTEGER PRIMARY KEY,
  id TEXT ,
  password TEXT,
  is_auth  TEXT CHECK (is_auth IN ('Y','N')),
  created_at TEX
) 
''')

# 커밋 및 연결 종료
conn.commit()
conn.close()