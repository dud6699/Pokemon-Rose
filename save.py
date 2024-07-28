import sys
import pygame
import poke_func
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
        self.update_trees()
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
        self.pokedex = ast.literal_eval(data[13][:-1])
        self.fix_old_files()
        self.start_time = datetime.datetime.now()
        #
        if self.gen == 0:
            self.rival = "May"
        else:
            self.rival = "Hugh"

    def update_trees(self):
        while(len(self.prog[10]) < 40):
            self.prog[10].append([0,0,0,0])
        for index,l in enumerate(get_trees()):
            if self.prog[10][index] == [0,0,0,0]:
                self.prog[10][index] = l

    def fix_old_files(self):
        #v1.1.1?
        if len(self.prog) == 16:
            self.prog.append(0)
        #v1.1.4
        if len(self.prog) == 17:
            self.prog.append([[3,1,0,0,0,1,1,1,2,2,2,3,3,3,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0]])
        if len(self.prog[5]) < 80:
            for i in range(40):
                self.prog[5].append(0)
        if len(self.prog[11]) == 7:
            self.prog[11].append([None,[],{}])
        if len(self.prog[12]) == 2:
            for x in range(18):
                self.prog[12].append(0)
        #v1.1.5
        if type(self.prog[8][0][2]) == list:
            if type(self.prog[8][0][2][0]) == str:
                self.prog[8][0][2][0] = None
            for i in range(8):
                self.prog[8][i][2] = self.prog[8][i][2][0]
        if len(self.prog[11]) == 8:
            self.prog[11].append([None,[]])
        if self.prog[11][2] == None or len(self.prog[11][2]) == 3:
            self.prog[11][2] = [None,None]
        #v1.1.6
        if len(self.prog) == 18:
            self.prog.append(0)
        #v1.1.7
        if len(self.prog[11]) == 9:
            self.prog[11].append([0,0,None])
        #v1.1.8
        if len(self.prog[11]) == 10:
            self.prog[11].append(None)
        #v1.1.9 alolan marowak
        if len(self.prog) == 19:
            self.prog.append([0,[0,0,0,0,0]])
        #v1.2.1 journals
        if len(self.prog) == 20:
            self.prog.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        #v1.2.2
        if len(self.prog) == 21:
            self.prog.append([0,0,0,0])
        #v1.2.3
        if len(self.prog[11]) == 11:
            self.prog[11].append([None,[],{}])
        if len(self.prog[11]) == 12:
            self.prog[11].append([0,None])
        #v1.2.6
        if len(self.prog[6]) < 150:
            for i in range(150-len(self.prog[6])):
                self.prog[6].append(0)
        #fix pokedex
        to_del = []
        for pok in self.pokedex:
            if pok[-2:] == '_S':
                to_del.append(pok)
        for x in to_del:
            del self.pokedex[x]
        # fix missing pokedex
        # for pok in self.party:
        #     if pok[0] not in self.pokedex:
        #         self.pokedex[pok[0]] = [1,[]]
        # for box in self.box:
        #     for pok in box:
        #         if pok != 0 and pok[0] not in self.pokedex:
        #             self.pokedex[pok[0]] = [1,[]]


def get_trees():
    return [[0,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,1,0,0],[1,0,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
