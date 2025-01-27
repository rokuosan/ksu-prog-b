# プログラミング演習B 最終課題
# author: Koki Matsumoto (454575)

# == 実行例
#   $ python ./src/last/main.py ./assets/score4train.csv ./assets/score4test.csv
#   ### 通常 ####################
#   モデルの評価
#   	OK 線形回帰 学習対象
#   	OK 線形回帰 テスト対象
#   	OK ランダムフォレスト 学習対象
#   	OK ランダムフォレスト テスト対象
#   線形回帰の結果
#   	- MAE: 3.06
#   	- MSE: 24.40
#   	- R2 : 0.96
#   ランダムフォレストの結果
#   	- MAE: 3.21
#   	- MSE: 40.30
#   	- R2 : 0.93
#   **以下省略**

# == 利用するアルゴリズム
#   - 線形回帰
#   - ランダムフォレスト

# == アルゴリズムに対するパラメータ
#   ランダムフォレストのみパラメータを指定している．
#       - ランダムフォレストの決定木の数: 100
#       - ランダムフォレストの乱数のシード: 42

# == データの前処理
#   - データの標準化を行っている．

# == 目的変数
#   - 最終成績の点数(Target.score)

# == 予測精度の検証
#   - 予測精度の検証は，R2値を用いて行う．
#   - R2値が0.9以上であれば，良いモデルと判定する．

# == 考察
# 目的変数として点数を選択した．
# レポートの提出率や点数，小テストの点数がその目的変数に十分に寄与していると考えたため，これらを特徴量として選択した．
# また，これらは線形的な関係を持つと考えられるため，線形回帰を用いて学習を行った．

import sys
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor


class TargetRow:
    """学習対象のデータを表すクラス"""

    def __init__(self, id: int, eval: str, score: int, exam: float, report: float, submit: float, test: float):
        self.id = id
        self.eval = eval
        self.score = score
        self.exam = exam
        self.report = report
        self.submit = submit
        self.test = test

    @staticmethod
    def from_csv_line(line: str) -> "TargetRow":
        c = line.strip().split(",")
        return TargetRow(int(c[0]), c[1], int(c[2]), float(c[3]), float(c[4]), float(c[5]), float(c[6]))

class Target:
    """学習対象のデータを表すクラス"""

    def __init__(self, rows: list[TargetRow]):
        self.rows = rows

    @staticmethod
    def from_csv(filename: str) -> "Target":
        rows = []
        with open(filename, "r") as f:
            f.readline()
            for line in f:
                rows.append(TargetRow.from_csv_line(line))
        return Target(rows)


    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int) -> TargetRow:
        return self.rows[index]

    def __iter__(self):
        return iter(self.rows)

    def ids(self) -> list[int]:
        return [row.id for row in self.rows]

    def evals(self) -> list[str]:
        return [row.eval for row in self.rows]

    def scores(self) -> list[int]:
        return [row.score for row in self.rows]

    def exams(self) -> list[float]:
        return [row.exam for row in self.rows]

    def reports(self) -> list[float]:
        return [row.report for row in self.rows]

    def submits(self) -> list[float]:
        return [row.submit for row in self.rows]

    def tests(self) -> list[float]:
        return [row.test for row in self.rows]

# 線形回帰がこのデータに対して良いモデルかどうかを判定する
# 寄与率(R2)が0.9以上であれば良いモデルと判定する
def is_match_linear_regression(target: Target):
    x = list(zip(target.exams(), target.reports(), target.submits(), target.tests()))
    y = target.scores()

    # データの標準化と分割．学習とテストを8:2に分割するが，再現のために random_state は万物の答えである 42 に固定する．
    x_scaled = StandardScaler().fit_transform(x)
    x_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    return r2 >= 0.9

def is_match_random_forest(target: Target):
    x = list(zip(target.exams(), target.reports(), target.submits(), target.tests()))
    y = target.scores()

    # データの標準化と分割．学習とテストを8:2に分割するが，再現のために random_state は万物の答えである 42 に固定する．
    x_scaled = StandardScaler().fit_transform(x)
    x_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    return r2 >= 0.9


def perform_models_match(train: Target, test: Target):
    """モデルが適合しているかどうかを評価する

    Args:
        train (Target): 訓練用データ
        test (Target): テスト用データ
    """
    # データの一部を学習してモデルの評価を行う関数
    def evaluate_model(model_name, model_func, data, data_name):
        if model_func(data):
            print(f"\tOK {model_name} {data_name}")
        else:
            print(f"\tNOT OK {model_name} {data_name}")

    # 学習対象とテスト対象のデータに対して線形回帰とランダムフォレストが適しているかどうかを判定する
    print("モデルの評価")
    for model_name, model_func in [("線形回帰", is_match_linear_regression), ("ランダムフォレスト", is_match_random_forest)]:
        for data, data_name in [(train, "学習対象"), (test, "テスト対象")]:
            evaluate_model(model_name, model_func, data, data_name)

def perform_models(train: Target, test: Target):
    """モデルの学習と評価を行う

    Args:
        train (Target): 訓練用データ
        test (Target): テスト用データ
    """
    x_train = list(zip(train.exams(), train.reports(), train.submits(), train.tests()))
    x_train_scaled = StandardScaler().fit_transform(x_train)
    y = train.scores()

    # モデルの学習
    model_linear = linear_model.LinearRegression()
    model_linear.fit(x_train_scaled, y)
    model_forest = RandomForestRegressor(n_estimators=100, random_state=42)
    model_forest.fit(x_train_scaled, y)

    # テストデータの予測
    x_test = list(zip(test.exams(), test.reports(), test.submits(), test.tests()))
    x_test_scaled = StandardScaler().fit_transform(x_test)
    y_pred_linear = model_linear.predict(x_test_scaled)
    y_pred_forest = model_forest.predict(x_test_scaled)

    # テストデータの評価
    result = []
    y_test = test.scores()
    result.append(("線形回帰", mean_absolute_error(y_test, y_pred_linear), mean_squared_error(y_test, y_pred_linear), r2_score(y_test, y_pred_linear)))
    result.append(("ランダムフォレスト", mean_absolute_error(y_test, y_pred_forest), mean_squared_error(y_test, y_pred_forest), r2_score(y_test, y_pred_forest)))
    # 結果の表示
    for name, mae, mse, r2 in result:
        print(f"{name}の結果")
        print(f"\t- MAE: {mae:.2f}")
        print(f"\t- MSE: {mse:.2f}")
        print(f"\t- R2 : {r2:.2f}")

def main(args: list[str] = []):
    if not args:
        print("Usage: python main.py <learning_target>")
        return 1

    training_target = args[0]
    if not training_target:
        print("学習対象のファイルを指定してください")
        return 1

    test_target = args[1]
    if not test_target:
        print("テスト対象のファイルを指定してください")
        return 1

    # ひとまずファイルを読み込んでおく
    print("### 通常 ####################")
    train = Target.from_csv(training_target)
    test = Target.from_csv(test_target)

    # モデルの評価
    perform_models_match(train, test)
    perform_models(train, test)
    print()

    # target の要素数を減らしてみる
    print("### データを減らしてみる ####################")
    train_small = Target(train.rows[:10])
    test_small = Target(test.rows[:10])

    # モデルの評価
    perform_models_match(train_small, test_small)
    perform_models(train_small, test_small)
    print()

    # データの一部を削除してみる
    print("### 優のデータを削除してみる ####################")
    train_small = Target([row for row in train.rows if row.eval != "優"])
    test_small = Target([row for row in test.rows if row.eval != "優"])

    # モデルの評価
    perform_models_match(train_small, test_small)
    perform_models(train_small, test_small)
    print()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
