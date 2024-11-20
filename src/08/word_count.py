import os
import sys


class Counts:
    def __init__(self):
        # 文字数(chars)，行数(lines)，ファイル数(files)を初期化する．
        self.chars = 0
        self.lines = 0
        self.files = 0

    def parse(self, file):
        with open(file, "r") as f:
            # ファイルの内容を読み込んで，文字数と行数を数える．
            self.chars += len(f.read())
            f.seek(0)
            self.lines += len(f.readlines())
        # ファイル数を1増やす．
        self.files += 1

    def str(self):
        return f"chars: {self.chars}, lines: {self.lines}, files: {self.files}"


class WordCounts:
    def __init__(self):
        self.types = {}

    def traverse(self, path):
        if os.path.isdir(path):  # ディレクトリかどうかを判定する．
            for p in os.listdir(
                path
            ):  # ディレクトリ内のファイル，ディレクトリを列挙する．
                new_path = os.path.join(
                    path, p
                )  # ディレクトリ名とファイル名を結合する．
                self.traverse(new_path)  # ディレクトリを再帰的に探索する．
        else:  # ディレクトリではない場合（ファイルの場合）
            ext = self._find_ext(path)  # 拡張子を取得する（_find_ext を呼び出す）．
            if (
                ext not in self.types
            ):  # ディクショナリに拡張子に対応する Counts が存在するか．
                self.types[ext] = Counts() # 存在しなければ，新たに作成して，types に追加する．
            # バイナリファイルを読み込むとエラーが発生するため，try-except でエラーを回避する．
            try:
                self.types[ext].parse(path)  # ファイルを解析する．
            except:
                pass

    def _find_ext(self, path):  # ファイル名を受け取り，拡張子を返す．
        ext = os.path.splitext(path)[
            -1
        ]  # 拡張子を取得する（一番最後の要素を取得する）．
        if ext == "":  # 拡張子が存在しない場合
            return os.path.basename(path)  # ファイル名を返す．
        return ext  # 拡張子を返す．

    def print(self):
        for ext, counts in self.types.items():  # 拡張子と Counts のペアを取り出す．
            print(f"{ext}: {counts.str()}")  # 結果を出力する．


wc = WordCounts()
for arg in sys.argv[1:]:
    wc.traverse(arg)
wc.print()
