import sys
import pygame
import ast
import datetime
from pygame.locals import *

class Save:
    def __init__(self,data):
        self.name = ast.literal_eval(data[0][:-1])[0]
        self.starter = ast.literal_eval(data[0][:-1])[1]
        self.gen = int(data[1])
        self.x = int(data[2])
        self.y = int(data[3])
        self.dir = data[4]
        self.loc = ast.literal_eval(data[5])[0]
        self.pc = ast.literal_eval(data[5])[1]
        self.prog = ast.literal_eval(data[6])
        #new trees
        if len(self.prog[10]) == 20:
            self.prog[10].append([0,1,0,0])
            self.prog[10].append([0,0,0,1])
            for x in range(18):
                self.prog[10].append([0,0,0,0])
        if len(self.prog) == 16:
            self.prog.append(0)
        if len(self.prog[11]) == 7:
            self.prog[11].append([None,[],{}])
        if len(self.prog[12]) == 2:
            for x in range(18):
                self.prog[12].append(0)
        self.party = ast.literal_eval(data[7][:-1])
        self.money = int(data[8])
        self.bag = ast.literal_eval(data[9][:-1])
        self.box = ast.literal_eval(data[10][:-1])
        #change
        # if len(data) >= 12:
        self.time = ast.literal_eval(data[11][:-1])
        # else:
        #     self.time = [0,0,0]
        #urdl
        # if len(data) >= 13:
        self.register = ast.literal_eval(data[12][:-1])
        # else:
        #     self.register = [None,None,None,None]
        # if len(data) >= 14:
        self.pokedex = ast.literal_eval(data[13][:-1])
        # else:
        #     self.pokedex = {}
        #     for pok in self.party:
        #         self.pokedex[pok[0]] = [1,[]]
        #     for b in self.box:
        #         for pok in b:
        #             if pok != 0:
        #                 self.pokedex[pok[0]] = [1,[]]
        #v.1.0.7
        # for p in self.party:
        #     p[1][17] = True
        # for b in self.box:
        #     for pok in b:
        #         if pok != 0 and len(pok[1]) > 17:
        #             pok[1][17] = True
        # if self.prog[4] > 4:
        #     self.prog[4] = 4
        self.start_time = datetime.datetime.now()
        #
        if self.gen == 0:
            self.rival = "May"
        else:
            self.rival = "Hugh"
