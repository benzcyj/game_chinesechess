import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/home/tarena/PycharmProjects/")))

from unit1.project.game_chinesechess.game_view import GameView



if __name__ == "__main__":
    view = GameView()
    # view.background()
    view.start()
    view.update()
