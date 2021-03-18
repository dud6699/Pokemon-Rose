import pokemon
import poke_func
import sys
import save
import ast
import pygame
import moves
import random
from pygame.locals import*

#ex P.party["Litwick"] = [5,random.randint(0,1),62,"Ember",25,"Astonish",15,"Minimize",10,"Smog",20,None,None,0,"pokeball"]

class Poke:
    def __init__(self, name, data):
        self.name = name
        self.actual_name = name
        self.code = name
        self.lvl = data[0]
        self.gen = data[1]
        self.ch = data[2]
        self.m1 = data[3]
        self.m2 = data[5]
        self.m3 = data[7]
        self.m4 = data[9]
        self.p1 = data[4]
        self.p2 = data[6]
        self.p3 = data[8]
        self.p4 = data[10]
        if self.p1 == -1:
            self.p1 = self.get_pp(self.m1)
        if self.p2 == -1:
            self.p2 = self.get_pp(self.m2)
        if self.p3 == -1:
            self.p3 = self.get_pp(self.m3)
        if self.p4 == -1:
            self.p4 = self.get_pp(self.m4)
        self.item = data[11]
        self.status = data[12]
        self.exp = data[13]
        if self.exp > self.get_exp():
            self.exp = self.get_exp()
        self.ball = data[14]
        if len(data) >= 16:
            self.friend = data[15]
        else:
            self.friend = 0
        if len(data) >= 17:
            self.ability = data[16]
        else:
            self.ability = None
        if len(data) >= 18:
            self.player = True
        else:
            self.player = False
        if len(data) >= 19:
            if data[18] != None:
                self.name = data[18]
        if len(data) >= 20:
            self.nurse = data[19]
        else:
            self.nurse = False
        self.icon = pygame.transform.scale(pygame.image.load("p/poke/"+self.code+"_ico.png"),(70,70))
        #self.full = pygame.image.load("p/poke/"+self.code+"_full.png")
        self.get_stats(True)
        self.flinch = False
        self.idf = False
        self.dc = False
        self.protect = False
        self.spikyshield = False
        self.minimize = False
        self.pursuit = False
        self.charge = None
        self.inf = False
        self.explode = False
        self.endure = False
        self.nightmare = False
        self.bugbite = False
        self.rest = False
        self.bellydrum = False
        self.trapped = [None,0]
        self.type_hit = None
        self.child_hit = False
        self.magic_coat = False
        self.can_sucker = False
        self.chrg = 0
        self.fury_count = 0
        self.damage_taken = 0
        self.yawn = 0
        self.taunt = 0
        self.roost = 0
        self.procount = 0
        self.rollcount = 0
        self.cont_move = [None,0]
        self.stockpile = [0,0,0]
        self.cfs = 0
        self.slptim = 0
        self.turn_count = 0
        self.magnet_rise = 0
        self.bide = [0,0]
        self.bps = 1
        self.akm = 0
        self.sakm = 0
        self.dfm = 0
        self.sdfm = 0
        self.spdm = 0
        self.accm = 0
        self.evam = 0
        self.critm = 0
        self.ff = 0

    def code_nos(self):
        if self.code[-2:] == '_S':
            return self.code[:-2]
        return self.code

    def grounded(self):
        if self.ability != 'Levitate' and 'Flying' not in self.type and self.magnet_rise == 0:
            return True
        return False

    def get_spd(self,P):
        ans = self.spd*moves.modifier(self.spdm)
        if self.status != None and self.ability == 'Quick Feet':
            ans *= 1.5
        elif self.status == 'Par':
            ans *= 0.25
        if P.battle_weather != None and P.battle_weather[0] == 'Rain' and self.ability == 'Swift Swim':
            ans *= 2
        return ans

    def take_damage(self,P,amount):
        print(amount)
        if P.tourney_battle and self.bellydrum == False and self.explode == False:
            amount /= 4
        if amount > 0 and amount < 1:
            amount = 1
        if amount > self.ch:
            amount = self.ch
        self.ch -= int(amount)
        self.damage_taken += int(amount)

    def reset_stats(self) -> None:
        self.flinch = False
        self.idf = False
        self.dc = False
        self.protect = False
        self.spikyshield = False
        self.minimize = False
        self.pursuit = False
        self.charge = None
        self.inf = False
        self.explode = False
        self.rest = False
        self.nightmare = False
        self.bellydrum = False
        self.trapped = [None,0]
        self.type_hit = None
        self.magic_coat = False
        self.can_sucker = False
        self.child_hit = False
        self.chrg = 0
        self.taunt = 0
        self.yawn = 0
        self.roost = 0
        self.fury_count = 0
        self.procount = 0
        self.cfs = 0
        self.turn_count = 0
        self.magnet_rise = 0
        self.cont_move = [None,0]
        self.bide = [0,0]
        self.bps = 1
        self.akm = 0
        self.sakm = 0
        self.dfm = 0
        self.sdfm = 0
        self.spdm = 0
        self.accm = 0
        self.evam = 0
        self.critm = 0
        self.ff = 0
        self.rollcount = 0
        self.stockpile = [0,0,0]
        self.turn_count = -1
        if self.ability == 'Natural Cure' and self.status != 'Faint':
            self.status = None
        self.get_stats(True)

    def get_pp(self,move):
        m = moves.Move(move)
        return m.pp

    def equals(self, poke) -> bool:
        return self.code == poke.code and self.name == poke.name and self.lvl == poke.lvl and self.gen == poke.gen and self.ch == poke.ch and self.m1 == poke.m1 and self.m2 == poke.m2 and self.m3 == poke.m3 and self.m4 == poke.m4 and self.p1 == poke.p1 and self.p2 == poke.p2 and self.p3 == poke.p3 and self.p4 == poke.p4 and self.status == poke.status and self.akm == poke.akm and self.sakm == poke.sakm and self.dfm == poke.dfm and self.sdfm == poke.sdfm and self.spdm == poke.spdm and self.accm == poke.accm and self.evam == poke.evam and self.idf == poke.idf and self.inf == poke.inf and self.cfs == poke.cfs
        #return (and self.item == poke.item and self.exp == poke.exp and self.ball == poke.ball and self.icon == poke.icon and self.full == poke.full and self.flinch == poke.flinch and self.ability == poke.ability and self.hp == poke.hp and self.ak == poke.ak and self.sak == poke.sak and self.df == poke.df and self.sdf == poke.sdf and self.spd == poke.spd and self.type == poke.type)

    def same(self, poke):
        return self.name == poke.name and self.ability == poke.ability and self.lvl == poke.lvl and self.exp == poke.exp and self.gen == poke.gen and self.m1 == poke.m1 and self.m2 == poke.m2 and self.m3 == poke.m3 and self.m4 == poke.m4

    def gain_friend(self,amount,P = None):
        if self.ball == 'Luxury Ball':
            amount *= 2
        if self.ball == 'Nursery Ball' and amount < 1:
            amount *= 14+P.prog[8][1][0]
        if self.friend + amount > 300:
            amount -= max(0,300-self.friend)
            if self.friend < 300:
                self.friend = 300
            amount = amount/3
        self.friend += amount
        if self.friend > 400:
            self.friend = 400
        # if update:
        thp = self.hp
        self.update_stats()
        if self.status != 'Faint':
            self.ch += self.hp-thp

    def lvlup(self,P,battle = True,candy = False):
        self.lvl += 1
        self.exp = 0
        if candy == False:
            self.gain_friend((self.lvl/5)+10)
        thp = self.hp
        self.get_stats()
        if self.lvl in self.moveset and self.nurse == False:
            if type(self.moveset[self.lvl]) == list:
                for mv in self.moveset[self.lvl]:
                    self.learn(P,moves.Move(mv),battle)
            else:
                self.learn(P,moves.Move(self.moveset[self.lvl]),battle)
        if candy:
            if self.status != 'Faint':
                self.ch += self.hp-thp

    def has_move(self,move):
        if self.m1 == move or self.m2 == move or self.m3 == move or self.m4 == move:
            return True
        return False

    def learn(self,P,move,battle = True):
        if self.has_move(move.name):
            return -1
        chg = False
        if self.m2 == None:
            self.m2 = move.name
            self.p2 = move.pp
            chg = True
        elif self.m3 == None:
            self.m3 = move.name
            self.p3 = move.pp
            chg = True
        elif self.m4 == None:
            self.m4 = move.name
            self.p4 = move.pp
            chg = True
        else:
            end = True
            new = ""
            while end:
                if battle:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,f'{self.name} is trying',f'to learn {move.name}.')
                    poke_func.cont(P)
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,f'But {self.name} can\'t learn','more than four moves.')
                    poke_func.cont(P)
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,'Delete a move to make',f'room for {move.name}?')
                else:
                    poke_func.txt(P,f'{self.name} is trying',f'to learn {move.name}.')
                    poke_func.txt(P,f'But {self.name} can\'t learn','more than four moves.')
                    poke_func.new_txt(P)
                    poke_func.write(P,'Delete a move to make',f'room for {move.name}?')
                if poke_func.choice(P,550,600):
                    t = P.surface.copy()
                    poke_func.fade_out(P)
                    new = self.new_move_summ(P,move)
                    P.surface.blit(t,(0,0))
                    poke_func.fade_in(P)
                    if new != "":
                        end = False
                        if battle:
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,'1, 2 and...')
                            poke_func.cont(P)
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,'Poof!')
                            poke_func.cont(P)
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,f'{self.name} forgot {new}.')
                            poke_func.cont(P)
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,'And...')
                            poke_func.cont(P)
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,f'{self.name} learned',f'{move.name}!')
                            poke_func.cont(P)
                        else:
                            poke_func.txt(P,'1, 2 and...')
                            poke_func.txt(P,'Poof!')
                            poke_func.txt(P,f'{self.name} forgot {new}.')
                            poke_func.txt(P,'And...')
                            poke_func.txt(P,f'{self.name} learned',f'{move.name}!')
                        return True
                if new == "":
                    if battle:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,'Give up on learning',f'{move.name}?')
                    else:
                        poke_func.new_txt(P)
                        poke_func.write(P,'Give up on learning',f'{move.name}?')
                    if poke_func.choice(P,550,600):
                        if battle:
                            poke_func.new_battle_txt(P)
                            poke_func.battle_write(P,f'{self.name} didn\'t learn',f'{move.name}.')
                            poke_func.cont(P)
                        else:
                            poke_func.txt(P,f'{self.name} didn\'t learn',f'{move.name}.')
                        end = False
                    else:
                        pass         
        if chg:
            if battle:
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,f'{self.name} learned',f'{move.name}!')
                poke_func.cont(P)
            else:
                poke_func.txt(P,f'{self.name} learned',f'{move.name}!')
            return True
        return False

    def new_move_summ(self,P,move):
        back = pygame.image.load("p/new_move_summ.png")
        if self.code[-2:] == '_S':
            back = pygame.image.load("p/new_move_summ_S.png")
        ball = pygame.transform.scale(poke_func.load("p/"+self.ball+".png"),(30,30))
        name = P.font.render(self.name,True,(255,255,255))
        name_size = P.font.size(self.name)[0]
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        exp = pygame.image.load("p/summ_exp.png")
        high = pygame.image.load("p/high_move.png")
        desc = pygame.image.load("p/move_desc.png")
        if self.gen == 0:
            gen_i = pygame.image.load("p/boy_ico.png")
        if self.gen == 1:
            gen_i = pygame.image.load("p/girl_ico.png")
        if self.gen == 2:
            gen_i = pygame.image.load("p/blank.png")
        lvl = P.font.render("Lv."+str(self.lvl),True,(255,255,255))
        mn = 1
        m1 = P.font.render(str(self.m1),True,(0,0,0))
        mt1 = pygame.image.load("p/"+moves.Move(self.m1).type+"_ico.png")
        mp1 = P.font.render("PP "+str(moves.Move(self.m1).pp),True,(0,0,0))
        m2 = P.font.render(str(self.m2),True,(0,0,0))
        mt2 = pygame.image.load("p/"+moves.Move(self.m2).type+"_ico.png")
        mp2 = P.font.render("PP "+str(moves.Move(self.m2).pp),True,(0,0,0))
        m3 = P.font.render(str(self.m3),True,(0,0,0))
        mt3 = pygame.image.load("p/"+moves.Move(self.m3).type+"_ico.png")
        mp3 = P.font.render("PP "+str(moves.Move(self.m3).pp),True,(0,0,0))
        m4 = P.font.render(str(self.m4),True,(0,0,0))
        mt4 = pygame.image.load("p/"+moves.Move(self.m4).type+"_ico.png")
        mp4 = P.font.render("PP "+str(moves.Move(self.m4).pp),True,(0,0,0))
        m5 = P.font.render(str(move.name),True,(0,0,0))
        mt5 = pygame.image.load("p/"+move.type+"_ico.png")
        mp5 = P.font.render("PP "+str(move.pp),True,(0,0,0))
        move_list = [self.m1,self.m2,self.m3,self.m4]
        type1 = pygame.image.load("p/"+self.type[0]+"_ico.png")
        if self.type[1] != None:
            type2 = pygame.image.load("p/"+self.type[1]+"_ico.png")
        P.surface.blit(back,(0,0))
        if self.lvl != 100:
            P.surface.fill((0,0,255), Rect(64,110,int(320*(self.exp/self.get_exp())),10))
        else:
            P.surface.fill((0,0,255), Rect(64,110,320,10))
        P.surface.blit(exp,(10,105))
        P.surface.blit(ball,(18,18))
        P.surface.blit(name,(60,10))
        if self.code[:5] == 'Mega_':
            P.surface.blit(mega,(65+name_size,20))
        P.surface.blit(gen_i,(350,10))
        P.surface.blit(lvl,(20,50))
        P.surface.blit(m1,(430,115))
        P.surface.blit(mt1,(425,155))
        P.surface.blit(mp1,(550,150))
        P.surface.blit(m2,(430,210))
        P.surface.blit(mt2,(425,250))
        P.surface.blit(mp2,(550,245))
        P.surface.blit(m3,(430,305))
        P.surface.blit(mt3,(425,345))
        P.surface.blit(mp3,(550,340))
        P.surface.blit(m4,(430,400))
        P.surface.blit(mt4,(425,440))
        P.surface.blit(mp4,(550,435))
        P.surface.blit(m5,(430,505))
        P.surface.blit(mt5,(425,545))
        P.surface.blit(mp5,(550,540))
        P.surface.blit(type1,(170,55))
        if self.type[1] != None:
            P.surface.blit(type2,(280,55))
        poke_func.fade_in(P)
        a = 0
        end = True
        ans = ""
        while end:
            if mn == 5:
                mv = move
            else:
                mv = moves.Move(move_list[mn-1])
            P.surface.blit(back,(0,0))
            if self.lvl != 100:
                P.surface.fill((0,0,255), Rect(64,110,int(320*(self.exp/self.get_exp())),10))
            else:
                P.surface.fill((0,0,255), Rect(64,110,320,10))
            P.surface.blit(exp,(10,105))
            P.surface.blit(ball,(18,18))
            P.surface.blit(name,(60,10))
            if self.code[:5] == 'Mega_':
                P.surface.blit(name,(65+name_size,20))
            P.surface.blit(gen_i,(350,10))
            P.surface.blit(lvl,(20,50))
            if mv.cat == '0':
                cat_ico = pygame.image.load("p/phy_ico.png")
            elif mv.cat == '1':
                cat_ico = pygame.image.load("p/spe_ico.png")
            else:
                cat_ico = pygame.image.load("p/sta_ico.png")
            if mn == 5:
                mod = 25
            else:
                mod = 15
            P.surface.blit(high,(410,mod+(95*mn)))
            P.surface.blit(desc,(5,130))
            cat = P.font.render("Category",True,(0,0,0))
            power = P.font.render("Power     "+mv.pow,True,(0,0,0))
            if int(float(mv.acc)*100) > 100:
                acc = P.font.render("Accuracy  ---",True,(0,0,0))
            else:
                acc = P.font.render("Accuracy  "+str(int(float(mv.acc)*100)),True,(0,0,0))
            descr = []
            cngy = 0
            for x in mv.desc:
                descr.append(P.font_s.render(x,True,(0,0,0)))
            for x in descr:
                P.surface.blit(x,(20,285+cngy))
                cngy += 34
            P.surface.blit(cat,(20,135))
            P.surface.blit(cat_ico,(270,140))
            P.surface.blit(power,(20,185))
            P.surface.blit(acc,(20,235))
            P.surface.blit(m1,(430,115))
            P.surface.blit(mt1,(425,155))
            P.surface.blit(mp1,(550,150))
            P.surface.blit(m2,(430,210))
            P.surface.blit(mt2,(425,250))
            P.surface.blit(mp2,(550,245))
            P.surface.blit(m3,(430,305))
            P.surface.blit(mt3,(425,345))
            P.surface.blit(mp3,(550,340))
            P.surface.blit(m4,(430,400))
            P.surface.blit(mt4,(425,440))
            P.surface.blit(mp4,(550,435))
            P.surface.blit(m5,(430,505))
            P.surface.blit(mt5,(425,545))
            P.surface.blit(mp5,(550,540))
            P.surface.blit(type1,(170,55))
            if self.type[1] != None:
                P.surface.blit(type2,(280,55))
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[0]):
                    if mn > 1:
                        mn -= 1
                elif event.key == pygame.key.key_code(P.controls[1]):
                    if mn < 5:
                        mn += 1
                elif event.key == pygame.key.key_code(P.controls[5]) and a > 15:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[4]) and a > 20:
                    if mn == 5:
                        end = False
                    else:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,f'Forget {move_list[mn-1]}?')
                        if poke_func.choice(P,550,600):
                            if mn == 1:
                                ans = self.m1
                                self.m1 = move.name
                                self.p1 = move.pp
                            elif mn == 2:
                                ans = self.m2
                                self.m2 = move.name
                                self.p2 = move.pp
                            elif mn == 3:
                                ans = self.m3
                                self.m3 = move.name
                                self.p3 = move.pp
                            else:
                                ans = self.m4
                                self.m4 = move.name
                                self.p4 = move.pp
                            end = False
                        P.surface.set_clip((0,0,800,600))
            a += 1
            P.clock.tick(P.ani_spd)
            poke_func.update_screen(P)
        poke_func.fade_out(P)
        return ans

    def get_name(self,lower = False):
        if self.player:
            return self.name
        if lower:
            return 'the foe '+self.name
        return 'The foe '+self.name

    def heal(self):
        self.ch = self.hp
        self.status = None
        if self.m1 != None:
            self.p1 = self.get_pp(self.m1)
        if self.m2 != None:
            self.p2 = self.get_pp(self.m2)
        if self.m3 != None:
            self.p3 = self.get_pp(self.m3)
        if self.m4 != None:
            self.p4 = self.get_pp(self.m4)
    
    def copy(self):
        copy = Poke(self.code,[self.lvl,self.gen,self.ch,self.m1,self.p1,self.m2,self.p2,self.m3,self.p3,self.m4,self.p4,self.item,self.status,self.exp,self.ball,self.friend,self.ability,self.player,self.name,self.nurse])
        copy.flinch = self.flinch
        copy.idf = self.idf
        copy.cfs = self.cfs
        copy.inf = self.inf
        copy.pursuit = self.pursuit
        copy.minimize = self.minimize
        copy.protect = self.protect
        copy.rest = self.rest
        copy.spikyshield = self.spikyshield
        copy.child_hit = self.child_hit
        copy.cont_move = self.cont_move
        copy.procount = self.procount
        copy.nightmare = self.nightmare
        copy.can_sucker = self.can_sucker
        copy.charge = self.charge
        copy.magic_coat = self.magic_coat
        copy.bellydrum = self.bellydrum
        copy.trapped = self.trapped
        copy.type_hit = self.type_hit
        copy.chrg = self.chrg
        copy.explode = self.explode
        copy.taunt = self.taunt
        copy.yawn = self.yawn
        copy.roost = self.roost
        copy.dc = self.dc
        copy.slptim = self.slptim
        copy.turn_count = self.turn_count
        copy.magnet_rise = self.magnet_rise
        copy.bide = self.bide
        copy.bps = self.bps
        copy.akm = self.akm
        copy.sakm = self.sakm
        copy.fury_count = self.fury_count
        copy.dfm = self.dfm
        copy.sdfm = self.sdfm
        copy.spdm = self.spdm
        copy.accm = self.accm
        copy.evam = self.evam
        copy.critm = self.critm
        copy.ff = self.ff
        copy.rollcount = self.rollcount
        copy.stockpile = self.stockpile
        return copy

    def update_stats(self):
        stats = self.orig_stats.copy()
        if self.friend > 300:
            for s in range(len(stats)):
                stats[s] += (self.friend-300)*0.002
        mod = .9+(min(300,self.friend)*0.0002)
        self.hp = int((10+stats[0]*self.lvl)*mod)+self.lvl
        if self.ch > self.hp:
            self.ch = self.hp
        self.ak = int((5+stats[1]*self.lvl)*mod)
        if self.ability == "Huge Power":
            self.ak *= 2
        if self.ability == 'Hustle':
            self.ak *= 1.5
        self.sak = int((5+stats[2]*self.lvl)*mod)
        self.df = int((5+stats[3]*self.lvl)*mod)
        self.sdf = int((5+stats[4]*self.lvl)*mod)
        self.spd = int((5+stats[5]*self.lvl)*mod)


    def get_stats(self,weight = False) -> None:
        if self.code[-2:] == '_S':
            file = open("poke/"+self.code[:-2]+".txt","r")
        else:
            file = open("poke/"+self.code+".txt","r")
        if self.name[-2:] == '_S':
            self.name = self.name[:-2]
        if self.name == 'Pineapple_Oddish':
            self.name = 'Oddish'
        if self.name[:5] == 'Mega_':
            self.name = self.name[5:]
        if self.name[-2:] == '_M':
            self.name = self.name[:-2]
        if self.name[-2:] == '_F':
            self.name = self.name[:-2]
        if self.name[-2:] == '_T':
            self.name = self.name[:-2]
        if self.name == 'Mime Jr':
            self.name = 'Mime Jr.'
        if self.name == 'Mr Mime':
            self.name = 'Mr. Mime'
        if self.actual_name[-2:] == '_S':
            self.actual_name = self.actual_name[:-2]
        if self.actual_name == 'Pineapple_Oddish':
            self.actual_name = 'Oddish'
        if self.actual_name[:5] == 'Mega_':
            self.actual_name = self.actual_name[5:]
        if self.actual_name[-2:] == '_M':
            self.actual_name = self.actual_name[:-2]
        if self.actual_name == 'Mime Jr':
            self.actual_name = 'Mime Jr.'
        if self.actual_name == 'Mr. Mime':
            self.actual_name = 'Mr. Mime'
        if self.actual_name[-2:] == '_F':
            self.actual_name = self.actual_name[:-2]
        if self.actual_name[-2:] == '_T':
            self.actual_name = self.actual_name[:-2]
        data = file.readlines()
        abilist = ast.literal_eval(data[0])
        no_hidden = abilist.copy()
        for a in range(len(abilist)):
            if abilist[a][0] == '*':
                no_hidden.remove(abilist[a])
                abilist[a] = abilist[a][1:]
        if self.ability == None or self.ability not in abilist:
            self.ability = no_hidden[random.randint(0,len(no_hidden)-1)]
        #check ability
        abis = open("info/abilities.txt","r")
        abidata = [line[:-1] for line in abis]
        if self.ability not in abidata:
            print(self.ability)
        #
        self.orig_stats = ast.literal_eval(data[1])
        self.update_stats()
        self.type = ast.literal_eval(data[2])
        self.evo = ast.literal_eval(data[3])
        self.moveset = ast.literal_eval(data[4])
        #check moves and images
        for x in self.moveset:
            if x == 1:
                for a in self.moveset[x]:
                    m = moves.Move(a)
            elif type(self.moveset[x]) == list:
                for a in self.moveset[x]:
                    m = moves.Move(a)
            else:
                m = moves.Move(self.moveset[x])
        #
        bf = pygame.image.load("p/poke/"+self.code+"_bf.png")
        bfw = pygame.image.load("p/poke/" + self.code + "_bfw.png")
        bb = pygame.image.load("p/poke/" + self.code + "_bb.png")
        bbw = pygame.image.load("p/poke/" + self.code + "_bbw.png")
        ico = pygame.image.load("p/poke/" + self.code + "_ico.png")
        full = pygame.image.load("p/poke/" + self.code + "_full.png")
        #check end
        self.cr = int(data[5])
        if weight:
            self.weight = float(data[6])
        if len(data) > 7:
            self.height = float(data[7])
            self.dex = int(data[8])
            self.locs = ast.literal_eval(data[9])
            if len(data) > 10:
                self.desc = ast.literal_eval(data[10])
            # if len(data) > 9:
            #     self.locs = ast.literal_eval(data[9])
            # else:
            #     file.close()
            #     file = open("poke/"+self.code+".txt","a")
            #     file.write("\n")
            #     file.write("[]")
            #     file.close()
        file.close()
        if self.ch == 334:
            self.ch = self.hp

    def get_exp(self) -> int:
        l = self.lvl
        return int((4*(l+1)*(l+1)*(l+1)/5)-(4*l*l*l/5))

    def to_list(self):
        ret = [self.lvl,self.gen,self.ch,self.m1,self.p1,self.m2,self.p2,self.m3,self.p3,self.m4,self.p4,self.item,self.status,self.exp,self.ball,self.friend,self.ability,self.player,self.name,self.nurse]
        return ret
        
