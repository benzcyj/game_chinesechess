import random

class GameController:

    def __init__(self):
        self.__jiang = ["車１","马１","象１","士１","将０","士２","象２","马２",
                        "車２","炮１","炮２","卒１","卒２","卒３","卒４","卒５"]
        self.__shuai = ["车１","犸１","相１","仕１","帅０","仕２","相２","犸２",
                        "车２","豹１","豹２","兵１","兵２","兵３","兵４","兵５"]
        self.__bord = [
            # ＃１   ＃２　　＃３   ＃４　　＃５　　＃６   ＃７　　＃８　　＃９
            ["車１","马１","象１","士１","将０","士２","象２","马２","車２"],#1
            ["＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿"],#2
            ["＿＿","炮１","＿＿","＿＿","＿＿","＿＿","＿＿","炮２","＿＿"],#3
            ["卒１","＿＿","卒２","＿＿","卒３","＿＿","卒４","＿＿","卒５"],#4
            ["＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿"],#5
            # ["河河","河河","河河","河河","河河","河河","河河","河河","河河"],
            ["＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿"],#6
            ["兵１","＿＿","兵２","＿＿","兵３","＿＿","兵４","＿＿","兵５"],#7
            ["＿＿","豹１","＿＿","＿＿","＿＿","＿＿","＿＿","豹２","＿＿"],#8
            ["＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿","＿＿"],#9
            ["车１","犸１","相１","仕１","帅０","仕２","相２","犸２","车２"],#10
        ]

    @property
    def bord(self):
        return self.__bord

    def other_win(self, row, line, chess):
        if chess in self.__jiang:
            if self.__bord[row - 1][line - 1] == "帅０":
                self.__bord[row - 1][line - 1] = chess
                return 1
        if chess in self.__shuai:
            if self.__bord[row - 1][line - 1] == "将０":
                self.__bord[row - 1][line - 1] = chess
                return 1

    def jiang_shuai_win(self):
        for i in range(0,3):# 将所在的行
            for j in range(3,6):# 将所在的列
                for k in range(7,10):# 帅所在的行
                    list01 = []
                    for l in range(i+1,k):# 将,帅中间隔的行
                        list01.append(self.__bord[l][j])
                    if self.__bord[i][j] == "将０" and self.__bord[k][j] == "帅０"\
                            and len(set(list01)) == 1:
                        return 1

    def jiang_win(self):
        # 当将走完的下一步发生如下情况则帅赢:
        GameController().jiang_shuai_win()
        if GameController().jiang_shuai_win() == 1:
            return 1

    def shuai_win(self):
        # 当帅走完的下一步发生如下情况则将赢：
        GameController().jiang_shuai_win()
        if GameController().jiang_shuai_win() == 1:
            return 1

    def jiang_move(self,row,line,chess):
        for i in range(len(self.__bord)):
            for j in range(len(self.__bord[i])):
                if row < 4 or 3 < line < 7:
                    if self.__bord[i][j] == chess:
                        if abs(i - (row - 1)) == 1 and j == line - 1 \
                                and self.__bord[row - 1][line - 1]  not in self.__jiang:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1
                        elif i == row - 1 and abs(j - (line - 1)) == 1 \
                                and self.__bord[row - 1][line - 1] not in self.__jiang:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1

    def jiang_shi_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__jiang:
            if row < 4 and 3 < line < 7:
                if self.__bord[row][line - 2] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row][line - 2] = "＿＿"
                    return 1
                elif self.__bord[row][line] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row][line] = "＿＿"
                    return 1
                elif self.__bord[row - 2][line - 2] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 2][line - 2] = "＿＿"
                    return 1
                elif self.__bord[row - 2][line] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 2][line] = "＿＿"
                    return 1

    def jiang_xiang_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__jiang:
            if row in [1,3,5] or line in [1,3,5,7,9]:
                if self.__bord[row - 3][line - 3] == chess and \
                        self.__bord[row - 2][line - 2] == "＿＿":
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 3][line - 3] = "＿＿"
                    return 1
                elif line < 8 and self.__bord[row - 3][line + 1] == chess and \
                        self.__bord[row - 2][line] == "＿＿":
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 3][line + 1] = "＿＿"
                    return 1
                elif self.__bord[row + 1][line - 3] == chess and \
                        self.__bord[row][line - 2] == "＿＿":
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row + 1][line - 3] = "＿＿"
                    return 1
                elif line < 8 and self.__bord[row + 1][line + 1] == chess and \
                        self.__bord[row][line] == "＿＿":
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row + 1][line + 1] = "＿＿"
                    return 1

    def jiang_ma_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__jiang:
            if self.__bord[row + 1][line - 2] == chess:
                if self.__bord[row][line - 2] == "＿＿":
                    if GameController().other_win(row, line, chess) == 1:
                        self.__bord[row + 1][line - 2] = "＿＿"
                        return 1
                    else:
                        self.__bord[row - 1][line - 1] = chess
                        self.__bord[row + 1][line - 2] = "＿＿"
                        return 1
            if line < 9:
                if self.__bord[row + 1][line] == chess:
                    if self.__bord[row][line] == "＿＿":
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[row + 1][line] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[row + 1][line] = "＿＿"
                            return 1
            if self.__bord[row - 3][line - 2] == chess:
                if self.__bord[row - 2][line - 2] == "＿＿":
                    if GameController().other_win(row, line, chess) == 1:
                        self.__bord[row - 3][line - 2] = "＿＿"
                        return 1
                    else:
                        self.__bord[row - 1][line - 1] = chess
                        self.__bord[row - 3][line - 2] = "＿＿"
                        return 1
            if line < 9:
                if self.__bord[row - 3][line] == chess:
                    if self.__bord[row - 2][line] == "＿＿":
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[row - 3][line] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[row - 3][line] = "＿＿"
                            return 1

    def jiang_ju_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__jiang:
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) == 1 and random.choice(list01) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list01)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) == 1 and random.choice(list02) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list02)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) == 1 and random.choice(list03) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list03)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) == 1 and random.choice(list04) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list04)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1

    def pao_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] == "＿＿":
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) == 1 and random.choice(list01) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list01)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) == 1  and random.choice(list02) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list02)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) == 1 and random.choice(list03) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list03)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) == 1 and random.choice(list04) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list04)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
        elif self.__bord[row - 1][line - 1] in self.__shuai:
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) in [1,2]:
                                for y in list01:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) in [1,2]:
                                for y in list02:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) in [1,2]:
                                for y in list03:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) in [1,2]:
                                for y in list04:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1

    def zu_move(self,row,line,chess):
        for i in range(len(self.__bord)):
            for j in range(len(self.__bord[i])):
                if self.__bord[i][j] == chess:
                    if (row - 1) - i == 1 and j == line - 1 \
                            and self.__bord[row - 1][line - 1] not in self.__jiang:
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[i][j] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1
                    elif i == row + 1 and abs(j - (line - 1)) == 1 and i > 4 \
                            and self.__bord[row - 1][line - 1] not in self.__jiang:
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[i][j] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1

    def shuai_move(self,row,line,chess):
        for i in range(len(self.__bord)):
            for j in range(len(self.__bord[i])):
                if row > 7 or 3 < line < 7:
                    if self.__bord[i][j] == chess:
                        if abs(i - (row - 1)) == 1 and j == line - 1 \
                                and self.__bord[row - 1][line - 1]  not in self.__shuai:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1
                        elif i == row - 1 and abs(j - (line - 1)) == 1 \
                                and self.__bord[row - 1][line - 1] not in self.__shuai:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1

    def shuai_shi_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1]  not in self.__shuai:
            if row > 7 and 3 < line < 7:
                if self.__bord[row][line - 2] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row][line - 2] = "＿＿"
                    return 1
                elif self.__bord[row][line] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row][line] = "＿＿"
                    return 1
                elif self.__bord[row - 2][line - 2] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 2][line - 2] = "＿＿"
                    return 1
                elif self.__bord[row - 2][line] == chess:
                    self.__bord[row - 1][line - 1] = chess
                    self.__bord[row - 2][line] = "＿＿"
                    return 1

    def shuai_xiang_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__shuai \
                and row in [6,8,10] or line in [1,3,5,7,9]:
            if self.__bord[row - 3][line - 3] == chess and \
                    self.__bord[row - 2][line - 2] == "＿＿":
                self.__bord[row - 1][line - 1] = chess
                self.__bord[row - 3][line - 3] = "＿＿"
                return 1
            elif self.__bord[row - 3][line + 1] == chess and \
                    self.__bord[row - 2][line] == "＿＿":
                self.__bord[row - 1][line - 1] = chess
                self.__bord[row - 3][line + 1] = "＿＿"
                return 1
            elif self.__bord[row + 1][line - 3] == chess and \
                    self.__bord[row][line - 2] == "＿＿":
                self.__bord[row - 1][line - 1] = chess
                self.__bord[row + 1][line - 3] = "＿＿"
                return 1
            elif self.__bord[row + 1][line + 1] == chess and \
                    self.__bord[row][line] == "＿＿":
                self.__bord[row - 1][line - 1] = chess
                self.__bord[row + 1][line + 1] = "＿＿"
                return 1

    def shuai_ma_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__shuai:
            if self.__bord[row + 1][line - 2] == chess:
                if self.__bord[row][line - 2] == "＿＿":
                    if GameController().other_win(row, line, chess) == 1:
                        self.__bord[row + 1][line - 2] = "＿＿"
                        return 1
                    else:
                        self.__bord[row - 1][line - 1] = chess
                        self.__bord[row + 1][line - 2] = "＿＿"
                        return 1
            if line < 9:
                if self.__bord[row + 1][line] == chess:
                    if self.__bord[row][line] == "＿＿":
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[row + 1][line] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[row + 1][line] = "＿＿"
                            return 1
            if self.__bord[row - 3][line - 2] == chess:
                if self.__bord[row - 2][line - 2] == "＿＿":
                    if GameController().other_win(row, line, chess) == 1:
                        self.__bord[row - 3][line - 2] = "＿＿"
                        return 1
                    else:
                        self.__bord[row - 1][line - 1] = chess
                        self.__bord[row - 3][line - 2] = "＿＿"
                        return 1
            if line < 9:
                if self.__bord[row - 3][line] == chess:
                    if self.__bord[row - 2][line] == "＿＿":
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[row - 3][line] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[row - 3][line] = "＿＿"
                            return 1

    def shuai_ju_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] not in self.__shuai:
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) == 1 and random.choice(list01) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list01)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) == 1 and random.choice(list02) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list02)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) == 1 and random.choice(list03) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list03)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) == 1 and random.choice(list04) == "＿＿":
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                            if len(set(list04)) == 0:
                                if GameController().other_win(row, line, chess) == 1:
                                    self.__bord[i][j] = "＿＿"
                                    return 1
                                else:
                                    self.__bord[row - 1][line - 1] = chess
                                    self.__bord[i][j] = "＿＿"
                                    return 1

    def bao_move(self,row,line,chess):
        if self.__bord[row - 1][line - 1] == "＿＿":
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) == 1 and random.choice(list01) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list01)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) == 1  and random.choice(list02) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list02)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) == 1 and random.choice(list03) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list03)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) == 1 and random.choice(list04) == "＿＿":
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
                            if len(set(list04)) == 0:
                                self.__bord[row - 1][line - 1] = chess
                                self.__bord[i][j] = "＿＿"
                                return 1
        elif self.__bord[row - 1][line - 1] in self.__jiang:
            for i in range(len(self.__bord)):
                for j in range(len(self.__bord[i])):
                    if row - 1 == i and self.__bord[i][j] == chess:
                        if j < line -1:
                            list01 = []
                            for x in range(j + 1,line - 1):
                                list01.append(self.__bord[i][x])
                            if len(set(list01)) in [1,2]:
                                for y in list01:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                        else:
                            list02 = []
                            for x in range(line,j):
                                list02.append(self.__bord[i][x])
                            if len(set(list02)) in [1,2]:
                                for y in list02:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                    elif line - 1 == j and self.__bord[i][j] == chess:
                        if i < row - 1:
                            list03 = []
                            for x in range(i + 1, row - 1):
                                list03.append(self.__bord[x][j])
                            if len(set(list03)) in [1,2]:
                                for y in list03:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                        else:
                            list04 = []
                            for x in range(row,i):
                                list04.append(self.__bord[x][j])
                            if len(set(list04)) in [1,2]:
                                for y in list04:
                                    if y in self.__jiang + self.__shuai:
                                        if GameController().other_win(row, line, chess) == 1:
                                            self.__bord[i][j] = "＿＿"
                                            return 1
                                        else:
                                            self.__bord[row - 1][line - 1] = chess
                                            self.__bord[i][j] = "＿＿"
                                            return 1

    def bing_move(self,row,line,chess):
        for i in range(len(self.__bord)):
            for j in range(len(self.__bord[i])):
                if self.__bord[i][j] == chess:
                    if i - (row - 1) == 1 and j == line - 1 \
                            and self.__bord[row - 1][line - 1]  not in self.__shuai:
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[i][j] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1
                    elif i == row - 1 and abs(j - (line - 1)) == 1 and i < 5 \
                            and self.__bord[row - 1][line - 1] not in self.__shuai:
                        if GameController().other_win(row, line, chess) == 1:
                            self.__bord[i][j] = "＿＿"
                            return 1
                        else:
                            self.__bord[row - 1][line - 1] = chess
                            self.__bord[i][j] = "＿＿"
                            return 1

if __name__ == "__main__":
    controller = GameController()