import os

from unit1.project.game_chinesechess.game_controller import GameController


class GameView:

    # def background(self):
    #     pygame.init()
    #     bg_size = (630, 630)  # 设置背景大小
    #     screen = pygame.display.set_mode(bg_size, 0, 32)  # 创建窗体
    #     pygame.display.set_caption("中国象棋")  # 设置窗体标题
    #     background = pygame.image.load('/home/tarena/PycharmProjects/unit1/project/game_chinesechess/image/background.jpeg')
    #     # 游戏开始画面
    #     # begin_image = pygame.image.load("../image/background.jpg").convert_alpha()
    #     # # 开始图片位置
    #     # begin_image_rect = begin_image.get_rect()
    #     # begin_image_rect.left, begin_image_rect.top = (0, 0)
    #     screen.blit(background,(0,0))

    def __init__(self):
        self.__controller = GameController()

    def __print_map(self):
        os.system("clear")

        i = 0
        for line in self.__controller.bord:
            for item in line:
                print(item,end=" ")
            i += 1
            print(i)
            print()

    def start(self):
        print(" １　 ２　 ３　 ４　 ５　 ６　 ７　 ８　 ９")
        self.__print_map()
        print(" １　 ２　 ３　 ４　 ５　 ６　 ７　 ８　 ９")

    def update(self):
        step = 1
        while True:
            try:
                if step % 2 == 1:
                    a = 0
                    print("红(将)方移动")
                    chess = input("请红方输入要移动的棋子：")
                    row = int(input("请输入要放置的棋子的行："))
                    line = int(input("请输入要放置的棋子的列："))
                    otherwin = self.__controller.other_win(row,line,chess)
                    if otherwin == 1:
                        self.__print_map()
                        print("－－－－－－－－－－－")
                        print("！帅被吃了，红方赢了！")
                        print("－－－－－－－－－－－")
                        break
                    jiangwin = self.__controller.shuai_win()
                    if jiangwin == 1:
                        self.__print_map()
                        print("－－－－－－－－－－－")
                        print("！帅被吃了，红方赢了！")
                        print("－－－－－－－－－－－")
                        a += 1
                    if chess == "将０":
                        c = self.__controller.jiang_move(row,line,chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["士１","士２"]:
                        c = self.__controller.jiang_shi_move(row,line,chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["象１","象２"]:
                        c = self.__controller.jiang_xiang_move(row,line,chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["马１","马２"]:
                        c = self.__controller.jiang_ma_move(row,line,chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["車１","車２"]:
                        c = self.__controller.jiang_ju_move(row,line,chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["炮１","炮２"]:
                        c = self.__controller.pao_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["卒１","卒２","卒３","卒４","卒５"]:
                        c = self.__controller.zu_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess not in ["車１","马１","象１","士１","将０","士２","象２","马２",
                                       "車２","炮１","炮２","卒１","卒２","卒３","卒４","卒５"]:
                        raise ValueError
                    if a == 0:
                        raise IndexError
                else:
                    a = 0
                    print("黑(帅)方移动")
                    chess = input("请黑方输入要移动的棋子：")
                    row = int(input("请输入要放置的棋子的行："))
                    line = int(input("请输入要放置的棋子的列："))
                    otherwin = self.__controller.other_win(row,line,chess)
                    if otherwin == 1:
                        self.__print_map()
                        print("－－－－－－－－－－－")
                        print("！将被吃了，黑方赢了！")
                        print("－－－－－－－－－－－")
                        a += 1
                    shuaiwin = self.__controller.jiang_win()
                    if shuaiwin == 1:
                        self.__print_map()
                        print("－－－－－－－－－－－")
                        print("！将被吃了，黑方赢了！")
                        print("－－－－－－－－－－－")
                        a += 1
                    if chess == "帅０":
                        c = self.__controller.shuai_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["仕１", "仕２"]:
                        c = self.__controller.shuai_shi_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["相１", "相２"]:
                        c = self.__controller.shuai_xiang_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["犸１", "犸２"]:
                        c = self.__controller.shuai_ma_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["车１", "车２"]:
                        c = self.__controller.shuai_ju_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["豹１", "豹２"]:
                        c = self.__controller.bao_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess in ["兵１", "兵２", "兵３", "兵４", "兵５"]:
                        c = self.__controller.bing_move(row, line, chess)
                        if c == 1:
                            a += 1
                            step += 1
                    elif chess not in ["车１","犸１","相１","仕１","帅０","仕２","相２","犸２",
                                       "车２","豹１","豹２","兵１","兵２","兵３","兵４","兵５"]:
                        raise ValueError
                    if a == 0:
                        raise IndexError

            except ValueError:
                print("－－－－－－－－－－－－－－－－－")
                print("！该棋子不是己方棋子，请重新选择！")
                print("－－－－－－－－－－－－－－－－－")
                continue
            except IndexError:
                print("－－－－－－－－－－－－－－－－")
                print("！不能放置到该位置，请重新输入！")
                print("－－－－－－－－－－－－－－－－")
                continue
            except KeyboardInterrupt:
                print("－－－－－－")
                print("！游戏结束！")
                print("－－－－－－")
                break
            print(" １　 ２　 ３　 ４　 ５　 ６　 ７　 ８　 ９")
            self.__print_map()
            print(" １　 ２　 ３　 ４　 ５　 ６　 ７　 ８　 ９")
