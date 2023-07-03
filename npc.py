import pokemon
import poke_func
import sys
import save
import ast
import pygame
import random
from pygame.locals import*

class NPC:
    def __init__(self,P,type,name,xy,motion,text,lose_text = None, trainer = False,vision = [0,0,0,0],team = None,tid = 0,spd = 2,tim = None,curr = None,extra_walk = None,loc = None, y_offset = 0,stationary = False):
        self.P = P
        self.trainer = trainer
        self.tid = tid
        #[u,d,l,r]
        self.vision = vision
        if team != None:
            self.team = team.copy()
            self.team.insert(0,type+" "+name)
        else:
            self.team = None
        self.type = type
        gender = ""
        if self.type == "Rival" and P.save_data.gen == 0:
            gender = "g"
        if self.type == "Rival" and P.save_data.gen == 1:
            gender = "b"
        if self.type == 'Rocket Admin':
            gender = name
        self.u = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_u1.png"),(54,64))
        self.r = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_r1.png"),(54,64))
        self.d = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_d1.png"),(54,64))
        self.l = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_l1.png"),(54,64))
        if stationary:
            self.u2 = self.u
            self.u3 = self.u
            self.r2 = self.r
            self.r3 = self.r
            self.d2 = self.d
            self.d3 = self.d
            self.l2 = self.l
            self.l3 = self.l
        else:
            self.u2 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_u2.png"),(54,64))
            self.u3 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_u3.png"),(54,64))
            self.r2 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_r2.png"),(54,64))
            self.r3 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_r3.png"),(54,64))
            self.d2 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_d2.png"),(54,64))
            self.d3 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_d3.png"),(54,64))
            self.l2 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_l2.png"),(54,64))
            self.l3 = pygame.transform.scale(poke_func.load("p/spr/"+self.type+gender+"_l3.png"),(54,64))
        self.rect = (P.px+1300,P.py-1350,50,40)
        self.turn = False
        self.trainer_walk = extra_walk
        if self.trainer_walk == None:
            self.turn = True
        self.in_front = False
        self.tempp = None
        self.p = self.u
        self.x = xy[0]
        self.y = xy[1]
        self.yd = 0
        self.bx = self.x
        self.by = self.y
        self.blx = 50
        self.bly = 40
        self.xmod = 0
        self.ymod = 0
        self.movex = 0
        self.movey = 0
        self.spd = spd
        self.walkc = spd-1
        self.mr = 0
        self.ml = 0
        self.md = 0
        self.mu = 0
        self.name = name
        self.text = text
        self.lose_text = lose_text
        self.motion = motion
        if tim == None:
            self.curr = 0
            self.tim = motion[self.curr][1]
        else:
            self.curr = curr
            self.tim = tim
            if self.tim == self.motion[self.curr][1]:
                self.curr -= 1
                self.tim = 0
            if (self.motion[self.curr][0] == 'ml'or self.motion[self.curr][0] == 'mr' or self.motion[self.curr][0] == 'mu' or self.motion[self.curr][0] == 'md') and trainer:
                while self.tim > 0:
                    if self.trainer_walk[1] > 0:
                        self.trainer_walk[1] -= 50
                        if spd == 1:
                            self.tim -= 10
                        else:
                            self.tim -= 20
                    else:
                        break
                if self.trainer_walk[1] == 0:
                    self.trainer_walk = None
                    self.turn = True
        self.extra_walk = None
        if loc == None or P.save_data.loc == loc:
            self.check_in()
        self.y_offset = y_offset

    def set_motion(self,motion):
        self.motion = motion
        self.curr = 0
        self.tim = motion[self.curr][1]

    def get_rect(self):
        return (self.P.px+self.bx+self.xmod,self.P.py+self.by+self.ymod,self.blx,self.bly)

    def blit(self,temppx,temppy,mod,modx):
        mod += self.y_offset
        if self.type == 'Professor':
            mod -= 1
        poke_func.blit_img(self.P,self.P.char_shad,(temppx+self.x+modx,temppy+self.y+13+mod))
        if self.type == 'Manaphy' and self.face() == 'r':
            poke_func.blit_img(self.P,self.p,(temppx+self.x-12+modx,temppy+self.y-12+mod))
        elif self.type == 'Manaphy' and self.face() == 'l':
            poke_func.blit_img(self.P,self.p,(temppx+self.x+8+modx,temppy+self.y-12+mod))
        else:
            poke_func.blit_img(self.P,self.p,(temppx+self.x-2+modx,temppy+self.y-12+mod))

    def face(self):
        if self.p == self.r or self.p == self.r2 or self.p == self.r3:
            return 'r'
        if self.p == self.l or self.p == self.l2 or self.p == self.l3:
            return 'l'
        if self.p == self.d or self.p == self.d2 or self.p == self.d3:
            return 'd'
        if self.p == self.u or self.p == self.u2 or self.p == self.u3:
            return 'u'

    def x_dist(self):
        return 375-self.P.px-self.x

    def y_dist(self):
        return 275-self.P.py-self.y

    def trainer_check(self,rects = [],not_trainer = True):
        if self.trainer == False and not_trainer:
            return False
        if self.trainer_walk == None and (self.P.px-25)%50 == 0 and (self.P.py-25)%50 == 0 and self.x % 50 == 0 and self.y % 50 == 0:
            if self.face() == 'd' and self.y_dist() <= self.vision[1] and self.y_dist() >= 50 and self.x_dist() == 0 and self.check_trainer('d',rects):
                self.trainer_walk = ['d',self.y_dist()-50,20]
                self.extra_walk = ['u',self.y_dist()-50,0]
                if self.y_dist()-50 == 0:
                    self.P.p = self.P.u1
                return True
            elif self.face() == 'u' and self.y_dist() >= -self.vision[0] and self.y_dist() <= 0 and self.x_dist() == 0 and self.check_trainer('u',rects):
                self.trainer_walk = ['u',abs(self.y_dist())-50,20]
                self.extra_walk = ['d',abs(self.y_dist())-50,0]
                if abs(self.y_dist())-50 == 0:
                    self.P.p = self.P.d1
                return True
            elif self.face() == 'r' and self.x_dist() <= self.vision[3] and self.x_dist() >= 50 and self.y_dist() == 0 and self.check_trainer('r',rects):
                self.trainer_walk = ['r',self.x_dist()-50,20]
                self.extra_walk = ['l',self.x_dist()-50,0]
                if self.x_dist()-50 == 0:
                    self.P.p = self.P.l1
                return True
            elif self.face() == 'l' and self.x_dist() >= -self.vision[2] and self.x_dist() <= 0 and self.y_dist() == 0 and self.check_trainer('l',rects):
                self.trainer_walk = ['l',abs(self.x_dist())-50,20]
                self.extra_walk = ['r',abs(self.x_dist())-50,0]
                if abs(self.x_dist())-50== 0:
                    self.P.p = self.P.r1
                return True
        return False

    def check_time(self):
        if self.tim == 0:
            if self.curr == len(self.motion)-1:
                self.curr = 0
            else:
                self.curr += 1
            self.tim = self.motion[self.curr][1]


    def npc_move(self,dir = None):
        # if (self.movex == 1 or self.mr != 0):
        if self.trainer_walk != None and self.trainer_walk[1] == 0:
            return
        if self.walkc == 0:
            if self.trainer_walk != None:
                self.trainer_walk[1] -= 5
            if dir == 'r':
                self.x += 5
                if self.x % 50 == 0:
                    self.p = self.r
                elif self.x % 25 == 0:
                    if self.x % 100 >= 50:
                        self.p = self.r2
                    else:
                        self.p = self.r3
            # if (self.movex == -1 or self.ml != 0):
            elif dir == 'l':
                self.x -= 5
                if self.x % 50 == 0:
                    self.p = self.l
                elif self.x % 25 == 0:
                    if self.x % 100 >= 50:
                        self.p = self.l2
                    else:
                        self.p = self.l3
            # if (self.movey == 1 or self.mu != 0):
            elif dir == 'u':
                self.y -= 5
                if self.y % 50 == 0:
                    self.p = self.u
                elif self.y % 25 == 0:
                    if self.y % 100 >= 50:
                        self.p = self.u2
                    else:
                        self.p = self.u3
            # if (self.movey == -1 or self.md != 0):
            elif dir == 'd':
                self.y += 5
                if self.y % 50 == 0:
                    self.p = self.d
                elif self.y % 25 == 0:
                    if self.y % 100 >= 50:
                        self.p = self.d2
                    else:
                        self.p = self.d3
            self.walkc = self.spd
        self.walkc -= 1

    def talk(self):
        if 375-self.P.px-self.x == 50 and 275-self.P.py == self.y and poke_func.face_l(self.P):
            self.tempp = self.r
            self.P.p = self.P.l1
            if self.trainer:
                self.trainer_walk = ['r',0,20]
            return True
        elif 375-self.P.px-self.x == -50 and 275-self.P.py == self.y and poke_func.face_r(self.P):
            self.tempp = self.l
            self.P.p = self.P.r1
            if self.trainer:
                self.trainer_walk = ['l',0,20]
            return True
        elif 275-self.P.py-self.y == 50 and 375-self.P.px == self.x and poke_func.face_u(self.P):
            self.tempp = self.d
            self.P.p = self.P.u1
            if self.trainer:
                self.trainer_walk = ['d',0,20]
            return True
        elif 275-self.P.py-self.y == -50 and 375-self.P.px == self.x and poke_func.face_d(self.P):
            self.tempp = self.u
            self.P.p = self.P.d1
            if self.trainer:
                self.trainer_walk = ['u',0,20]
            return True
        return False

    def reset_box(self):
        self.blx = 50
        self.bly = 40
        self.xmod = 0
        self.ymod = 0
        self.bx = self.x
        self.by = self.y

    def check_in(self):
        if 375-self.P.px == self.x and 275-self.P.py == self.y:
            # self.x += self.default_move[0]
            # self.y += self.default_move[1]
            # self.bx = self.x
            # self.by = self.y
            temp_curr = self.curr
            temp_tim = self.tim
            end = True
            con = False
            for movement in self.motion:
                if movement[0] in ['mr','ml','md','mu']:
                    con = True
            if con:
                while end:
                    if self.motion[temp_curr][0][0] == 'm':
                        if self.spd == 1:
                            temp_tim -= 10
                        else:
                            temp_tim -= 20
                        x = 0
                        y = 0
                        if self.motion[temp_curr][0] == 'mr':
                            x = 50
                        elif self.motion[temp_curr][0] == 'ml':
                            x = -50
                        elif self.motion[temp_curr][0] == 'md':
                            y += 50
                        else:
                            y -= 50
                        self.x += x
                        self.y += y
                        self.bx = self.x
                        self.by = self.y
                        if temp_tim == 0:
                            temp_curr += 1
                            if temp_curr >= len(self.motion):
                                temp_curr = 0
                            temp_tim = self.motion[temp_curr][1]
                        end = False
                    else:
                        temp_curr += 1
                        if temp_curr >= len(self.motion):
                            temp_curr = 0
                        temp_tim = self.motion[temp_curr][1]
            else:
                self.x += 50
                self.bx = self.x
            self.curr = temp_curr
            self.tim = temp_tim
            print(self.curr,self.tim)

    def write(self):
        c = 0
        while len(self.text) > c:
            poke_func.new_txt(self.P)
            poke_func.write(self.P,self.text[c],self.text[c+1],self.text[c+2])
            poke_func.cont(self.P)
            c += 3

    def lose_write(self):
        poke_func.new_txt(self.P)
        poke_func.write(self.P,self.lose_text[0],self.lose_text[1],self.lose_text[2])
        poke_func.cont(self.P)
        if len(self.lose_text) > 3:
            poke_func.new_txt(self.P)
            poke_func.write(self.P,self.lose_text[3],self.lose_text[4],self.lose_text[5])
            poke_func.cont(self.P)
        if len(self.lose_text) > 6:
            poke_func.new_txt(self.P)
            poke_func.write(self.P,self.lose_text[6],self.lose_text[7],self.lose_text[8])
            poke_func.cont(self.P)

    def check_trainer(self,dir,rects):
        for tup in rects:
            if dir == 'u':
                return tup[1]-self.by < -100 or tup[1]-self.by > -50 or tup[0] <= self.x-50 or tup[0] >= self.x+50
            elif dir == 'd':
                return tup[1]-self.by > 100 or tup[1]-self.by < 50 or tup[0] <= self.x-50 or tup[0] >= self.x+50
            elif dir == 'l':
                return tup[0]-self.bx < -100 or tup[0]-self.bx > -50 or tup[1] <= self.by-50 or tup[1] >= self.by+50
            else:
                return tup[0]-self.bx > 100 or tup[0]-self.bx < 50 or tup[1] <= self.by-50 or tup[1] >= self.by+50
        return True

    def check_rects(self,dir,rects):
        for tup in rects:
            if dir == 'u':
                return tup[1]-self.by <= -100 or tup[1]-self.by > -50 or tup[0] <= self.x-50 or tup[0] >= self.x+50
            elif dir == 'd':
                return tup[1]-self.by >= 100 or tup[1]-self.by < 50 or tup[0] <= self.x-50 or tup[0] >= self.x+50
            elif dir == 'l':
                return tup[0]-self.bx <= -100 or tup[0]-self.bx > -50 or tup[1] <= self.by-50 or tup[1] >= self.by+50
            else:
                return tup[0]-self.bx >= 100 or tup[0]-self.bx < 50 or tup[1] <= self.by-50 or tup[1] >= self.by+50
        return True

    def skip_move(self):
        while self.x%50 != 0 or self.y%50 != 0:
            self.move(blit = False)
        self.reset_box()

    def move(self,temppx = None, temppy = None,rects = [],cam_mod = 0,cam_modx = 0,blit = True,mov = False):
        if temppx == None and temppy == None:
            self.yd = self.y_dist()
        if (self.yd > 0 and temppx == None and temppy == None) or (self.yd <= 0 and temppx != None and temppy != None) or mov:
            if self.x % 50 == 0 and self.y % 50 == 0:
                self.reset_box()
            self.in_front = False
            if self.tim == 0:
                self.check_time()
            if self.trainer_walk != None:
                if self.trainer_walk[2] > 0:
                    mod = 0
                    if self.trainer_walk[2] > 15:
                        mod = 10*(self.trainer_walk[2]-15)
                    poke_func.blit_img(self.P,self.P.exclaim,(self.P.px+self.x,self.P.py+self.y-60+mod))
                    self.trainer_walk[2] -= 1
                else:
                    self.npc_move(self.trainer_walk[0])
                    if self.trainer_walk[1] <= 5 and self.turn:
                        if self.trainer_walk[0] == 'u':
                            self.P.p = self.P.d1
                        elif self.trainer_walk[0] == 'd':
                            self.P.p = self.P.u1
                        elif self.trainer_walk[0] == 'r':
                            self.P.p = self.P.l1
                        else:
                            self.P.p = self.P.r1
                    if self.trainer_walk[1] == 0:
                        self.turn = True
                        self.trainer_walk = None
                        if self.trainer:
                            self.in_front = True
            elif self.motion[self.curr][0] == 'l':
                self.p = self.l
                self.tim -= 1
                self.check_time()
            elif self.motion[self.curr][0] == 'r':
                self.p = self.r
                self.tim -= 1
                self.check_time()
            elif self.motion[self.curr][0] == 'u':
                self.p = self.u
                self.tim -= 1
                self.check_time()
            elif self.motion[self.curr][0] == 'd':
                self.p = self.d
                self.tim -= 1
                self.check_time()
            elif self.motion[self.curr][0] == 'ml':
                if self.x % 50 == 0 and self.y % 50 == 0:
                    self.p = self.l
                if (375-self.P.px-self.bx <= -100 or 375-self.P.px-self.bx > -50 or 275-self.P.py <= self.by-50 or 275-self.P.py >= self.by+50) and self.check_rects('l',rects):
                    if self.x%50 == 0:
                        self.blx += 50
                        self.xmod = -50
                    self.npc_move('l')
                    #if self.x%50 == 0:
                    #    self.reset_box()
                    self.tim -= 1
                    self.check_time()
            elif self.motion[self.curr][0] == 'mr':
                if self.x % 50 == 0 and self.y % 50 == 0:
                    self.p = self.r
                if (375-self.P.px-self.bx >= 100 or 375-self.P.px-self.bx < 50 or 275-self.P.py <= self.by-50 or 275-self.P.py >= self.by+50) and self.check_rects('r',rects):
                    if self.x%50 == 0:
                        self.blx += 50
                    self.npc_move('r')
                    #if self.x%50 == 0:
                    #    self.reset_box()
                    self.tim -= 1
                    self.check_time()
            elif self.motion[self.curr][0] == 'mu':
                if self.x % 50 == 0 and self.y % 50 == 0:
                    self.p = self.u
                if (275-self.P.py-self.by <= -100 or 275-self.P.py-self.by > -50 or 375-self.P.px <= self.x-50 or 375-self.P.px >= self.x+50) and self.check_rects('u',rects):
                    if self.y%50 == 0:
                        self.bly += 50
                        self.ymod = -50
                    self.npc_move('u')
                    #if self.y%50 == 0:
                    #    self.reset_box()
                    self.tim -= 1
                    self.check_time()
            elif self.motion[self.curr][0] == 'md':
                if self.x % 50 == 0 and self.y % 50 == 0:
                    self.p = self.d
                if (275-self.P.py-self.by >= 100 or 275-self.P.py-self.by < 50 or 375-self.P.px <= self.x-50 or 375-self.P.px >= self.x+50) and self.check_rects('d',rects):
                    if self.y%50 == 0:
                        self.bly += 50
                    self.npc_move('d')
                    #if self.y%50 == 0:
                    #    self.reset_box()
                    self.tim -= 1
                    self.check_time()
        #print(375-self.P.px-self.bx)
            #print(self.y)
            if self.tempp != None:
                self.p = self.tempp
            if temppx == None and temppy == None:
                temppx = self.P.px
                temppy = self.P.py
            if blit:
                self.blit(temppx,temppy,cam_mod,cam_modx)
            self.tempp = None
            return True
        else:
            return False

