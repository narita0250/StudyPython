"""
10章：ハングマン

編集元：https://github.com/calthoff/self_taught/blob/master/python_ex239.py/
"""

from typing import Final
import random

# 人の絵
STAGE: Final= ["",
            "________        ",
            "|               ",
            "|        |      ",
            "|        0      ",
            "|       /|\     ",
            "|       / \     ",
            "|               "
            ]

WORDS: Final = [
    "cat", "dog", "apple", "book", "chair",
    "table", "house", "water", "music", "train",
    "cloud", "river", "green", "light", "phone",
    "bread", "plant", "mouse", "clock", "beach",
    "dream", "stone", "tiger", "horse", "piano",
    "world", "happy", "magic", "robot",
]

def hangman(word):
    """
    メイン関数
    :param word:str 答えとなる文字列
    """
    # 初期変数
    wrong = 0
    rletters = list(word)
    board = ["_"] * len(word)
    win = False

    # ゲーム開始
    print("Welcome to Hangman")
    print((" ".join(board)))
    while wrong < len(STAGE) - 1:
        print("\n")

        # 文字の入力
        msg = "Guess a letter > "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(STAGE[0 : wrong + 1]))

        # プレイヤー勝利
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    
    # プレイヤー敗北
    if not win:
        print("\n".join(STAGE[0 : wrong]))
        print("You lose! It was {}.".format(word))

# 答えの単語をリストからランダムに選んでゲーム開始
hangman(random.choice(WORDS))
