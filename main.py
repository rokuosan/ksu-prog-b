#!./.venv/bin/python
import re
import sys

def make_header(section: int, number: int)->str:
    """ヘッダーを作成する

    Parameters:
        section (int): セクション番号
        number (int): 課題番号

    Returns:
        str: 作成したヘッダー

    Examples:
        >>> make_header(1, 3)
        '# 第1回 課題3: 課題名\\n# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=課題ID\\n# 教材: https://ksubpb.github.io/2024/\\n# 作成: 2454575 / 松本 紘輝'
    """

    return f"""
# 第{section}回 課題{number}: 課題名
# 提出: https://cclms.kyoto-su.ac.jp/mod/assign/view.php?id=課題ID
# 教材: https://ksubpb.github.io/2024/
# 作成: 2454575 / 松本 紘輝
    """.strip()

def test():
    import doctest
    doctest.testmod()

def main():
    if len(sys.argv) != 4:
        print("Usage: ./main.py <section> <number> <name>")
        return

    section = sys.argv[1]
    number = sys.argv[2]
    name = sys.argv[3]
    print (f"section: {section}, number: {number}, name: {name}")
    if not re.compile(r"^[a-zA-Z0-9-_]+$").match(name):
        print("課題コードは制約/^[a-zA-Z0-9-_]+$/を満たすようにしてください")
        return

    filename = f"./src/{name}.py"
    with open(filename, "w") as f:
        f.write(make_header(section, number))


if __name__ == "__main__":
    test()
    main()
