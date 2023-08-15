import os
import pandas as pd
import yaml
import glob
import json
import datetime

# プロジェクトの相対パス
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 各保存先
class Output:
    def __init__(self):
        self._base_path = base_path

    def sqlite_db(self):
        return os.path.join(self._base_path, "share.db")


"""
options
"""


def ssbu_names():
    df = pd.read_csv(os.path.join(base_path, "option", "ssbu.csv"))
    data = []
    for index, row in df.iterrows():
        d = row["0"]
        data.append(d)
    return data


def ssbu_dict():
    df = pd.read_csv(os.path.join(base_path, "option", "ssbu_dict.csv"))
    return df


"""
Record interface
"""


class WordListRecord:  # 名言集
    def __init__(self, word: str, desc: str):
        self.word = word
        self.desc = desc

    def __dict__(self):
        return {"word": self.word, "desc": self.desc}


class NameListRecord:  # あだ名集
    def __init__(self, key: str, val: str):
        self.key = key
        self.val = val

    def __dict__(self):
        return {"key": self.key, "val": self.val}
    

class YakiListRecord:  # 焼き直し条約
    def __init__(self, word: str, yaki: str):
        self.word = word
        self.yaki = yaki

    def __dict__(self):
        return {"word": self.word, "yaki": self.yaki}
    
class SchoolListRecord:  # 学校一覧
    def __init__(self, word: str):
        self.word = word

    def __dict__(self):
        return {"word": self.word}
    
class MannerListRecord:  # 日本国失礼憲法
    def __init__(self, word: str):
        self.word = word

    def __dict__(self):
        return {"word": self.word}
    
class HaikuListRecord:#俳句一覧
    def __init__(self,id:int,first:str,second:str,third:str,poster:str,detail:str,createAt:str,updateAt:str):
        self.id = id
        self.first = first
        self.second = second
        self.third = third
        self.detail = detail
        self.poster = poster
        self.createAt = datetime.datetime.strptime(createAt,'%Y-%m-%d %H:%M:%S')
        self.updateAt = datetime.datetime.strptime(updateAt,'%Y-%m-%d %H:%M:%S')

    def __dict__(self):
        return {"id":self.id,"first":self.first,"second":self.second,"third":self.third,"poster":self.poster,"detail":self.detail,"createAt":self.createAt.strftime('%Y-%m-%d %H:%M:%S'),"updateAt":self.updateAt.strftime('%Y-%m-%d %H:%M:%S')}

class HaikuListStatusResult:#俳句一覧の追加結果
    def __init__(self,success:bool,errorText:str):
        self.success = success
        self.errorText = errorText
    
    def __dict__(self):
        return {"success":self.success,"errorText":self.errorText}