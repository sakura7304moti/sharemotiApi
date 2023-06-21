"""
名言集のAPI
"""
from . import const
output = const.Output()
"""
CREATE DB
"""
import sqlite3
# sns.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = output.sqlite_db()
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる。(必須)
conn.close()

"""
CREATE TABLE
"""
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# wordlistというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute(
    """CREATE TABLE IF NOT EXISTS wordList(
            word STRING,
            desc STRING
            )
            """)

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()

"""
INSERT
"""
def insert(word:str='',desc:str=''):
    # データベースに接続する
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    # レコードの存在をチェックするためのクエリを作成する
    check_query = f"SELECT * FROM wordList WHERE word = '{word}'"
    # クエリを実行して結果を取得する
    cursor.execute(check_query)
    result = cursor.fetchall()

    #存在しないレコードなら追加する
    if result is None:
        query = "INSERT INTO wordList (word,desc) VALUES (:word,:desc)"
        args = {
            'word':word,
            'desc':desc
        }
        # レコードを追加する
        cursor.execute(query,args)

    # 変更をコミットし、接続を閉じる
    conn.commit()
    conn.close()
    
    #追加したらtrue,すでに存在したらfalse
    return True if result is None else False

"""
SELECT
"""
def search(word:str='',desc:str=''):
    # データベースに接続する
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    # クエリー設定
    query = "SELECT * FROM wordList WHERE 1 = 1 "
    if word != '':
        query = query + "and word like :word "
    if desc != '':
        query = query + "and desc like :desc "

    args = {
        'word' : f'%{word}%',
        'desc' : f'%{desc}%'
    }

    # SELECTクエリを実行
    cursor.execute(query,args)
    results = cursor.fetchall()

    # 結果を表示
    records = []
    for row in results:
        rec = const.WordListRecord(*row)
        records.append(rec)

    # 接続を閉じる
    conn.close()
    return records