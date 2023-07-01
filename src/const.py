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
Record interface
"""


class WordListRecord:  # 名言集
    def __init__(self, word: str, desc: str):
        self.word = word
        self.desc = desc

    def __dict__(self):
        return {"word": self.word, "desc": self.desc}
