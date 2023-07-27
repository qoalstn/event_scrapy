import sqlite3
import datetime


def deleteAllGSDatas():
    # 데이터베이스 연결
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()

    # 모든 레코드 삭제
    cursor.execute('''DELETE FROM item_gs25''')
    conn.commit()
    conn.close()

# 크롤링 데이터 저장


def saveGSCrawlDatas(item_idx, name, price, img):
    # 데이터베이스 연결
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()

    now = datetime.datetime.now()  # 현재 날짜와 시간
    last_day = datetime.datetime(
        now.year, now.month + 1, 1) - datetime.timedelta(days=1)  # 이번 달의 마지막 날

    cursor.execute('INSERT INTO item_gs25 (item_idx, name, price, img, created_at ,updated_at ,expired_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (item_idx, name, price, img, now, now, last_day))
    conn.commit()

    conn.close()

# 크롤링한 모든 데이터


def selectAllGSDatas():
    # 데이터베이스 연결
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM item_gs25''')
    rows = cursor.fetchall()

    list = []
    for row in rows:
        list.append(
            {'item_idx': row[0], 'title': row[1], 'price': row[2], 'img': row[3]})

    conn.close()

    return list


def searchKeyword(keyword):
    # 데이터베이스 연결
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()

    # 쿼리 실행
    cursor.execute(f"SELECT * FROM item_gs25 WHERE name LIKE '%{keyword}%'")

    # 결과 가져오기
    rows = cursor.fetchall()

    list = []
    for row in rows:
        list.append(
            {'item_idx': row[0], 'title': row[1], 'price': row[2], 'img': row[3]})

    conn.close()

    return list
