#!/usr/bin/env python

from subprocess import Popen, PIPE
import time
import datetime
from gtp import parse_vertex, gtp_move, gtp_color
from gtp import BLACK, WHITE, PASS


class GTPSubProcess(object):

    def __init__(self, label, args):
        self.label = label
        self.subprocess = Popen(args, stdin=PIPE, stdout=PIPE)
        time.sleep(8)
        print("===================FAN============={} subprocess created".format(label))

    def send(self, data):
        print("sending {}: {}".format(self.label, data))
        self.subprocess.stdin.write(data)
        result = ""
        while True:
            data = self.subprocess.stdout.readline()
            print("=====the data is {}======".format(data))
            if not data.strip():
                break
            result += data
        print("got: {}".format(result))
        return result

    def send1(self, data):
        print("sending {}: {}".format(self.label, data))
        self.subprocess.stdin.write(data)
        data = self.subprocess.stdout.readline()
        print("=====the data is {}======".format(data))
        return data

    def waitUntilEnd(self):
        while True:
            oneline = self.subprocess.stdout.readline()
            if not oneline.strip():
                break

    def close(self):
        print("quitting {} subprocess".format(self.label))
        self.subprocess.communicate("quit\n")


class GTPFacade(object):

    def __init__(self, label, args):
        self.label = label
        self.moves = []
        self.gtp_subprocess = GTPSubProcess(label, args)

    def name(self):
        self.gtp_subprocess.send("name\n")

    def version(self):
        self.gtp_subprocess.send("version\n")

    def boardsize(self, boardsize):
        self.gtp_subprocess.send("boardsize {}\n".format(boardsize))

    def komi(self, komi):
        self.gtp_subprocess.send("komi {}\n".format(komi))

    def clear_board(self):
        self.gtp_subprocess.send("clear_board\n")

    def genmove(self, color):
        self.gtp_subprocess.send(
            "genmove {}\n".format(gtp_color(color)))
        # while True:
        #     isRunning = self.gtp_subprocess.send("check_running\n")
        #     print("=====================The running result is {}===========".format(isRunning))
        #     if not isRunning:
        #         print("============get out!!!!================")
        #         break
        # message = self.gtp_subprocess.send("lastmove\n")

        # print("genmove result is {}".format(message))
        # assert message[0] == "="
        # return parse_vertex(message[1:].strip())

    def genmove1(self, color):
        self.gtp_subprocess.send1(
            "genmove {}\n".format(gtp_color(color)))
        time.sleep(5)
        # while True:
        #     isRunning = self.gtp_subprocess.send("check_running\n")
        #     print("=====================The running result is {}===========".format(isRunning))
        #     if not isRunning:
        #         print("============get out!!!!================")
        #         break
        # message = self.gtp_subprocess.send("lastmove\n")

        # print("genmove result is {}".format(message))
        # assert message[0] == "="
        # return parse_vertex(message[1:].strip())

    def checkRunning(self):
        isRunning = self.gtp_subprocess.send("check_running\n")
        return isRunning

    def setHandicap(self,stoneNumber):
        self.gtp_subprocess.send1("fixed_handicap "+str(stoneNumber)+"\n")

    def getLastMove(self):
        lastMove = self.gtp_subprocess.send1("lastmove\n")
        return lastMove.strip()

    def printSgf(self):
        return self.gtp_subprocess.send("printsgf\n")

    def lastwinrate(self):
        return self.gtp_subprocess.send1("winrate\n")        

    def showboard(self):
        print("========================show board========================")
        self.gtp_subprocess.send("showboard\n")

    def play(self, color, vertex):
        self.gtp_subprocess.send("play {}\n".format(gtp_move(color, vertex)))

    def final_score(self):
        self.gtp_subprocess.send("final_score\n")

    def close(self):
        self.gtp_subprocess.close()

    def waitUntilEnd(self):
        self.gtp_subprocess.waitUntilEnd()

def saveSGF(str,winner):
    now = datetime.datetime.now()
    timestamp = now.strftime("v2_08_%Y%m%d%H%M%S")
    with open(timestamp+"W="+winner+".sgf", "w") as file:
        file.write(str)
    saveWinrate(timestamp,winrates)

def saveWinrate(filename,ar):
    with open(filename+".log","w") as file:
        file.write(str(ar))                

RAYGO = ["/home/ikeda-05444/users/fan/GoProjects/Ray/ray", "--playout", "60000","--size","13"]
LEELAZ_tekake = ["/home/ikeda-05444/users/fan/GoProjects/laalaz13E/build/leelaz13_c_param25_cp_10", "--gtp", "-w", "/home/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
GNUGO_MONTE_CARLO = ["gnugo", "--mode", "gtp", "--monte-carlo"]
LEELAZ = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_08", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_NORMAL = ["/home/ikeda-05444/users/fan/GoProjects/leela13_normal", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_NORMAL_NORMAL = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_normal_normal", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_15 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_15", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_0126_01 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_0126_01", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_0126_v2 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_0126_v2", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_0126_v3 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_0126_v3", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_0126_v4 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_0126_v4", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","1600","--noponder"]
LEELAZ_NORMAL_NORMAL_8 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_normal_normal", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13.txt","-p","128","--noponder"]
LEELAZ_NORMAL_v2 = ["/home/ikeda-05444/users/fan/GoProjects/leela13_normal", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/leelaz-model-v2-7236000.txt","-p","1600","--noponder"]
LEELAZ_v2_08 = ["/home/ikeda-05444/users/fan/GoProjects/leelaz_v2_08", "--gtp", "-w", "/home/ikeda-05444/users/fan/GoProjects/13x13_backup.txt","-p","1600","--noponder"]

# black = GTPFacade("black", LEELAZ_tekake)
# # white = GTPFacade("white", GNUGO_LEVEL_ONE)
# white = GTPFacade("white", RAYGO)

# make sure black is ready
# black.waitUntilEnd()

# print("=======black is ready!!!==============")

white = GTPFacade("white", LEELAZ)
 # white = GTPFacade("white", GNUGO_LEVEL_ONE)
black = GTPFacade("black", RAYGO)

firstPass = False
whiteLastMove = ""
winrates = []

# handicap
#black.play(BLACK,'D4')
#black.play(BLACK,'K10')

#white.play(BLACK,'D4')
#white.play(BLACK,'K10')

while True:
    black.genmove1(BLACK)

    lastBlackMove = black.getLastMove()
    lastwinrate = black.lastwinrate()
    winrates.append(lastwinrate)

    if "resign" in lastBlackMove:
        saveSGF(white.printSgf(), "W")
        break

# if lastBlackMove == "pass":
#     if not firstPass:
#         firstPass = True
#     else:
#         saveSGF(black.printSgf())
#         breakgi t

    white.play(BLACK, lastBlackMove)

    whiteLastMove = lastBlackMove

# white.showboard()
    white.genmove(WHITE)

    lastWhiteMove = white.getLastMove()

    if lastWhiteMove == whiteLastMove:
        saveSGF(white.printSgf(), "B")
        break

    if lastWhiteMove == "" or "pass" in lastWhiteMove or "resign" in lastWhiteMove or "illegal" in lastWhiteMove:
        saveSGF(white.printSgf(), "B")
        break

# if lastWhiteMove == "pass":
#     if not firstPass:
#         firstPass = True
#     else:
#         saveSGF(black.printSgf())
#         break
    black.play(WHITE, lastWhiteMove)
    black.showboard()

    # time.sleep(3)
#
#
#
# white.waitUntilEnd()

# print("=======white is ready!!!==============")


# black.name()
# black.version()
#
# white.name()
# white.version()
#
# black.boardsize(9)
# white.boardsize(9)
#
# black.komi(5.5)
# white.komi(5.5)
#
# black.clear_board()
# white.clear_board()
#
# first_pass = False
#

# black.showboard()
#
# while True:
#     vertex = black.genmove(BLACK)
#
#     if vertex == PASS:
#         if first_pass:
#             break
#         else:
#             first_pass = True
#     else:
#         first_pass = False
#
#     black.showboard()
#
#
#     white.play(BLACK, vertex)
#     white.showboard()
#
#     vertex = white.genmove(WHITE)
#     if vertex == PASS:
#         if first_pass:
#             break
#         else:
#             first_pass = True
#     else:
#         first_pass = False
#
#     white.showboard()
#
#     black.play(WHITE, vertex)
#     black.showboard()
#
# black.final_score()
# white.final_score()
#
# black.close()
# white.close()
