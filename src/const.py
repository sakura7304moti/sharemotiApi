import os
import pandas as pd
import yaml
import glob
import json

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
