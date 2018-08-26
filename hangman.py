#hangman
import random

words = ['cat', 'dog', 'bird', 'turtle', 'rabbit']

def hangman(word=words[random.randint(0, (len(words) - 1))]):
    #プレイヤーが間違えた回数
    wrong = 0
    stages = ['',
              '_____     ',
              '|         ',
              '|    |    ',
              '|    0    ',
              '|   /|\   ',
              '|   / \   ',
              '|         '
              ]
    #変数 word は当ててほしい単語。変数 rletters に1文字ずつに分解してリストにして代入
    rletters = list(word)
    #変数 board にプレイヤーに見せるヒントを記録しておく
    board = ['_'] * len(word)
    #変数 win は勝敗の状況を記録。
    win = False
    print('ハングマンへようこそ！')

    #wrongの数がstages-1未満であればループ
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね'
        char = input(msg)
        #もしcharに入力した1文字がrlettersの中にあれば
        if char in rletters:
            #変数 cind に1文字のindex値を代入
            cind = rletters.index(char)
            #boardのcindの位置に1文字を代入
            board[cind] = char
            #?
            rletters[cind] = '$'
        else:
            #当てはまらなければwrongを1つインクリメント
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は {}.'.format(word))


hangman()
