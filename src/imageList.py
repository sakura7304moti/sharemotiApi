"""
画像一覧
"""
from . import const
import sqlite3
import datetime

# sns.dbを作成する
# すでに存在していれば、それにアスセスする。
output = const.Output()
dbname = output.sqlite_db()


"""
IMAGE PATH
"""
def get_image_path(id:int):
    file_name = str(id).zfill(8) + '.jpg'
    path = os.path.join(const.img_dir(),file_name)
    return path

"""
CREATE DB
"""
def init():
    conn = sqlite3.connect(dbname)
    # データベースへのコネクションを閉じる。(必須)
    conn.close()
    """
    CREATE TABLE
    """
    conn = sqlite3.connect(dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()
    
    # テーブル作成
    cur.execute(
    """create table if not exists imageList(
        id INTEGER PRIMARY KEY,
        title STRING,
        create_at STRING,
        update_at STRING
    )
    """
    )
    # データベースへコミット。これで変更が反映される。
    conn.commit()
    conn.close()
    print('create table imageList')
    
    #todo DBとフォルダーの画像で一致しないのがあれば更新する
    
"""
INSERT
"""
def insert(title:str,path:str):
    try:
        # 現在の日時を取得
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # データベースに接続する
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()

        query = """
        INSERT INTO imageList (title, createAt, updateAt) VALUES 
        (:title, :file_name, :current_time, :current_time)
        """
        args = {"title":title,"current_time":current_time}
        cursor.execute(query, args)

        # データベースへコミット。これで変更が反映される。
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'insert err -> {e}')
        return False
    
"""
UPDATE
更新できるのは画像名のみ
"""
def update(id:int,title:str):
    try:
        # 現在の日時を取得
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # データベースに接続する
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        
        query = """
        UPDATE imageList SET title = :title , update_at = :current_time WHERE id = :id
        """
        
        args={
            'id':id,
            'title':title,
            'current_time':current_time
        }
        cursor.execute(query, args)

        # データベースへコミット。これで変更が反映される。
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'update err -> {e}')
        return False
    
"""
DELETE
"""
def delete(id:int):
    try:
        path = get_image_path(id)
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file '{path}' was not found.")
            
        query = "DELETE FROM imageList WHERE id = :id"
        args = {"id":id}
        # レコードを削除する
        cursor.execute(query, args)

        # 変更をコミットし、接続を閉じる
        conn.commit()
        conn.close()
        
        #todo　削除が正常に出来たらファイルも削除
        os.remove(path)
        
    except Exception as e:
        print(f'delete err -> {e}')
        return False
    
"""
SEARCH COUNT
検索条件
・タイトル名
・作成日の月
・更新日の月
・更新日順にする?(未指定なら作成順)
"""
def search_count(title:str,create_month:int,update_month:int,order_update:int):
    return 0

def search_query(title:str,create_month:int,update_month:int,order_update:int):
    query = "SELECT * FROM imageList where 1 = 1 "
    args = {}
    if title != '':
        query = query + "and title like :title "
        args['title'] = f'%{title}%'
    if create_month != 0:
        query = query + "and strftime('%m', create_at) = :create_month"