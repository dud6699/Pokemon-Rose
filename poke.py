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
    def __init__(self, name, data, petals = None, over_ability = None, legendary = False):
        self.debug = False
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
            if over_ability != None:
                self.ability = over_ability
            else:
                self.ability = data[16]
            self.true_ability = data[16]
        else:
            self.ability = None
            self.true_ability = None
        if len(data) >= 18:
            self.player = True
        else:
            self.player = False
        if len(data) >= 19:
            if data[18] != None:
                self.name = data[18]
        if len(data) >= 20:
            self.nurse = data[19]
            #v1.2.8
            if self.nurse == True:
                self.nurse = 1
            elif self.nurse == False:
                self.nurse = 0
        else:
            self.nurse = 0
        if len(data) >= 21:
            self.petals = data[20]
        elif petals:
            self.petals = petals
        else:
            self.petals = []
        self.icon = pygame.transform.scale(pygame.image.load("p/poke/"+self.code+"_ico.png"),(70,70))
        #self.full = pygame.image.load("p/poke/"+self.code+"_full.png")
        self.mega_debuff = 0
        self.stat_swap = [None,None,None,None,None,None]
        self.get_stats(True)
        self.flinch = False
        self.idf = False
        self.dc = False
        self.protect = False
        self.spikyshield = [False,False] #spiky shield, baneful bunker
        self.minimize = False
        self.pursuit = False
        self.charge = None
        self.inf = False
        self.leech = False
        self.explode = False
        self.exit = False
        self.drag = False
        self.endure = False
        self.gastro = False
        self.nightmare = False
        self.curse = False
        self.bugbite = False
        self.rest = False
        self.bellydrum = False
        self.trapped = [None,0]
        self.beat_up = []
        self.type_hit = None
        self.child_hit = False
        self.magic_coat = False
        self.can_sucker = False
        self.chrg = 0
        self.fury_count = 0
        self.damage_taken = 0
        self.yawn = 0
        self.last_resort = [0,0,0,0]
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
        self.legendary = legendary

    def reload_icon(self):
        self.icon = pygame.transform.scale(pygame.image.load("p/poke/"+self.code+"_ico.png"),(70,70))

    def code_nos(self):
        if self.code[-2:] == '_S':
            return self.code[:-2]
        return self.code

    def check_last(self,P,type):
        if type == 1:
            if self.player:
                if poke_func.last_poke(P.party):
                    self.exit = False
            else:
                if poke_func.last_poke(P.opponent):
                    self.exit = False


    def grounded(self):
        if self.ability != 'Levitate' and 'Flying' not in self.type and self.magnet_rise == 0:
            return True
        return False

    def get_spd(self,P):
        ans = self.spd*poke_func.pokestar_mod(P,self.player,self.spdm,moves.modifier(self.spdm))
        if (P.player_buffs[0] > 0 and self.player) or (P.enemy_buffs[0] > 0 and not self.player):
            ans *= 2
        if self.status != None and self.ability == 'Quick Feet':
            ans *= 1.5
        elif self.status == 'Par':
            ans *= 0.25
        if P.battle_weather != None and P.battle_weather[0] == 'Rain' and self.ability == 'Swift Swim':
            ans *= 2
        if P.battle_weather != None and P.battle_weather[0] == 'Sunny' and self.ability == 'Chlorophyll':
            ans *= 2
        return ans

    def get_num_buffs(self):
        return self.akm+self.sakm+self.dfm+self.sdfm+self.spdm+self.accm+self.evam+self.critm

    def get_df(self):
        df = self.df
        if self.item == 'Eviolite' and self.evo != [] and self.evo[0] != 'Mega':
            df *= 1.5
        if self.get_ability() == 'Marvel Scale' and self.status != None:
            df *= 1.5
        return df

    def take_damage(self,P,amount,recoil = False,dot = False):
        print(amount)
        can_exit = False
        if self.get_ability() in ['Wimp Out','Emergency Exit'] and self.ch > self.hp/2:
            can_exit = True
        if (P.tourney_battle or self.legendary) and self.bellydrum == False and self.explode == False and recoil == False:
            amount /= 4
        elif P.pokestar_battle != 0 and self.bellydrum == False and self.explode == False and recoil == False:
            amount /= 2
        if P.pokestar_battle != 0 and not dot and recoil == False and P.turn_count == 5 and not self.player:
            print("finishing move:"+str(1+(P.pokestar_skills[0]/100)))
            amount *= 1+(P.pokestar_skills[0]/100)
        if P.pokestar_battle != 0 and not dot and recoil == False and self.player:
            print("defense buff:"+str(1+(P.pokestar_skills[4]/100)))
            amount *= 1-(P.pokestar_skills[4]/400)
            poke_func.pokestar_gain(P,4,amount/self.hp*8)
        if amount > 0 and amount < 1:
            amount = 1
        if amount > self.ch:
            amount = self.ch
        if amount < 0 and amount > -1:
            amount = -1
        if amount < 0 and amount < self.ch-self.hp:
            amount = self.ch-self.hp
        self.ch -= int(amount)
        if amount > 0 and not dot:
            self.damage_taken += int(amount)
        if can_exit and self.ch < self.hp/2 and self.ch > 0:
            if type(P.opponent[0]) != str and self.player == False and P.legendary_battle == False and P.tourney_battle == False and P.pokestar_battle == 0:
                P.end_battle = self
            self.exit = True

    def gain_hp(self,amount):
        self.ch += amount
        if self.ch > self.hp:
            self.ch = self.hp

    def get_ability(self):
        if self.gastro:
            return ""
        return self.ability

    def set_ability(self,ability):
        if ability == '':
            self.gasto = True
            if self.true_ability == "Huge Power":
                self.ak /= 2
            if self.true_ability == "Hustle":
                self.ak /= 1.5
        else:
            self.ability = ability
            if self.stat_swap[1] == None:
                if self.true_ability == "Huge Power":
                    self.ak /= 2
                if self.true_ability == "Hustle":
                    self.ak /= 1.5
                if self.ability == "Huge Power":
                    self.ak *= 2
                if self.ability == 'Hustle':
                    self.ak *= 1.5

    def reset_stats(self) -> None:
        self.flinch = False
        self.idf = False
        self.dc = False
        self.protect = False
        self.spikyshield = [False,False]
        self.minimize = False
        self.pursuit = False
        self.charge = None
        self.inf = False
        self.leech = False
        self.explode = False
        self.exit = False
        self.drag = False
        self.endure = False
        self.gastro = False
        self.rest = False
        self.nightmare = False
        self.curse = False
        self.stat_swap = [None,None,None,None,None,None]
        self.bellydrum = False
        self.trapped = [None,0]
        self.beat_up = []
        self.type_hit = None
        self.magic_coat = False
        self.can_sucker = False
        self.child_hit = False
        self.chrg = 0
        self.taunt = 0
        self.yawn = 0
        self.last_resort = [0,0,0,0]
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
        self.mega_debuff = 0
        self.rollcount = 0
        self.stockpile = [0,0,0]
        self.turn_count = 0
        if self.ability == 'Natural Cure' and self.status != 'Faint':
            self.status = None
        self.ability = self.true_ability
        self.get_stats(True)

    def get_pp(self,move):
        m = moves.Move(move)
        return m.pp

    def equals(self, poke) -> bool:
        return self.code == poke.code and self.name == poke.name and self.lvl == poke.lvl and self.gen == poke.gen and self.ch == poke.ch and self.m1 == poke.m1 and self.m2 == poke.m2 and self.m3 == poke.m3 and self.m4 == poke.m4 and self.p1 == poke.p1 and self.p2 == poke.p2 and self.p3 == poke.p3 and self.p4 == poke.p4 and self.status == poke.status and self.akm == poke.akm and self.sakm == poke.sakm and self.dfm == poke.dfm and self.sdfm == poke.sdfm and self.spdm == poke.spdm and self.accm == poke.accm and self.evam == poke.evam and self.idf == poke.idf and self.leech == poke.leech and self.cfs == poke.cfs and self.mega_debuff == poke.mega_debuff
        #return (and self.item == poke.item and self.exp == poke.exp and self.ball == poke.ball and self.icon == poke.icon and self.full == poke.full and self.flinch == poke.flinch and self.ability == poke.ability and self.hp == poke.hp and self.ak == poke.ak and self.sak == poke.sak and self.df == poke.df and self.sdf == poke.sdf and self.spd == poke.spd and self.type == poke.type)

    def same(self, poke):
        return self.name == poke.name and self.ability == poke.ability and self.true_ability == poke.true_ability and self.lvl == poke.lvl and self.exp == poke.exp and self.gen == poke.gen and self.m1 == poke.m1 and self.m2 == poke.m2 and self.m3 == poke.m3 and self.m4 == poke.m4

    def gain_friend(self,amount,P = None):
        if self.ball == 'Luxury Ball':
            amount *= 2
        if self.nurse == 1 and amount < 1:
            amount *= 2*(14+P.prog[8][1][0])
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
            gain = (self.lvl/5)+10
            if self.nurse in [2,5]:
                 self.gain_friend(gain*(3+(P.prog[8][1][0]/2)))
            else:
                self.gain_friend(gain)
        thp = self.hp
        self.get_stats()
        if self.lvl in self.moveset and self.nurse == 0:
            if type(self.moveset[self.lvl]) == list:
                for mv in self.moveset[self.lvl]:
                    self.learn(P,moves.Move(mv),battle)
            else:
                self.learn(P,moves.Move(self.moveset[self.lvl]),battle)
        if candy:
            if self.status != 'Faint':
                self.ch += self.hp-thp

    def can_status(self,P,status,cat = ""):
        if cat != '2' and poke_func.in_terrain(P,'Misty',self):
            return False
        if status in ['Psn','BPs']:
            if 'Poison' in self.type or 'Steel' in self.type or (cat != '2' and self.ability == 'Immunity') or self.status != None:
                return False
        elif status == 'Brn':
            if 'Fire' in self.type or self.get_ability() == 'Water Bubble' or self.status != None:
                return False
        elif status == 'Frz':
            if 'Ice' in self.type or self.status != None:
                return False
        elif status == 'Par':
            if 'Electric' in self.type  or (cat != '2' and self.ability == 'Limber') or self.status != None:
                return False
        elif status == 'Slp':
            if (cat != '2' and self.ability == 'Insomnia') or (cat != '2' and poke_func.in_terrain(P,'Electric',self)) or self.status != None:
                return False
        return True

    def can_poison(self,P,cat = ""):

        return True

    def can_burn(self,P,cat = ""):

        return True

    def can_freeze(self,P,cat = ""):

        return True

    def can_paralze(self,P,cat = ""):

        return True

    def can_sleep(self,P,cat = ""):

        return True

    def has_move(self,move,change_move = None):
        if change_move:
            if self.m1 == move:
                self.m1 = change_move
                self.p1 = self.get_pp(self.m1)
            elif self.m2 == move:
                self.m2 = change_move
                self.p2 = self.get_pp(self.m2)
            elif self.m3 == move:
                self.m3 = change_move
                self.p3 = self.get_pp(self.m3)
            elif self.m4 == move:
                self.m4 = change_move
                self.p4 = self.get_pp(self.m4)
            else:
                return False
            return True
        if self.m1 == move or self.m2 == move or self.m3 == move or self.m4 == move:
            return True
        return False

    def learn(self,P,move,battle = True,pokestar = False):
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
                    new = self.new_move_summ(P,move,pokestar)
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

    def new_move_summ(self,P,move,pokestar = False):
        back = pygame.image.load("p/ui/new_move_summ.png")
        if self.code[-2:] == '_S':
            back = pygame.image.load("p/ui/new_move_summ_S.png")
        exp_back = pygame.image.load("p/ui/hs_exp.png")
        ball = pygame.transform.scale(poke_func.load("p/ui/"+self.ball+".png"),(30,30))
        name = P.font.render(self.name,True,(255,255,255))
        name_size = P.font.size(self.name)[0]
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        exp = pygame.image.load("p/summ_exp.png")
        high = pygame.image.load("p/high_move.png")
        desc = pygame.image.load("p/move_desc.png")
        if self.gen == 0:
            gen_i = pygame.image.load("p/ui/boy_ico.png")
        if self.gen == 1:
            gen_i = pygame.image.load("p/ui/girl_ico.png")
        if self.gen == 2:
            gen_i = pygame.image.load("p/blank.png")
        lvl = P.font.render("Lv."+str(self.lvl),True,(255,255,255))
        mn = 1
        m1 = P.font.render(str(self.m1),True,(0,0,0))
        mt1 = pygame.image.load("p/ui/"+moves.Move(self.m1).type+"_ico.png")
        mp1 = P.font.render("PP "+str(moves.Move(self.m1).pp),True,(0,0,0))
        m2 = P.font.render(str(self.m2),True,(0,0,0))
        mt2 = pygame.image.load("p/ui/"+moves.Move(self.m2).type+"_ico.png")
        mp2 = P.font.render("PP "+str(moves.Move(self.m2).pp),True,(0,0,0))
        m3 = P.font.render(str(self.m3),True,(0,0,0))
        mt3 = pygame.image.load("p/ui/"+moves.Move(self.m3).type+"_ico.png")
        mp3 = P.font.render("PP "+str(moves.Move(self.m3).pp),True,(0,0,0))
        m4 = P.font.render(str(self.m4),True,(0,0,0))
        mt4 = pygame.image.load("p/ui/"+moves.Move(self.m4).type+"_ico.png")
        mp4 = P.font.render("PP "+str(moves.Move(self.m4).pp),True,(0,0,0))
        m5 = P.font.render(str(move.name),True,(0,0,0))
        mt5 = pygame.image.load("p/ui/"+move.type+"_ico.png")
        mp5 = P.font.render("PP "+str(move.pp),True,(0,0,0))
        move_list = [self.m1,self.m2,self.m3,self.m4]
        type1 = pygame.image.load("p/ui/"+self.type[0]+"_ico.png")
        if self.type[1] != None:
            type2 = pygame.image.load("p/ui/"+self.type[1]+"_ico.png")
        P.surface.blit(back,(0,0))

        P.surface.blit(ball,(18,18))
        P.surface.blit(name,(60,10))
        if self.code[:5] == 'Mega_':
            P.surface.blit(mega,(65+name_size,20))
        P.surface.blit(gen_i,(350,10))
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
        if not pokestar:
            P.surface.blit(exp_back,(38,107))
            if self.lvl != 100:
                P.surface.fill((0,0,255), Rect(64,110,int(320*(self.exp/self.get_exp())),10))
            else:
                P.surface.fill((0,0,255), Rect(64,110,320,10))
            P.surface.blit(exp,(10,105))
            P.surface.blit(lvl,(20,50))
            P.surface.blit(type1,(170,55))
            if self.type[1] != None:
                P.surface.blit(type2,(280,55))
        else:
            if self.type[1] != None:
                P.surface.blit(type1,(90,55))
                P.surface.blit(type2,(210,55))
            else:
                P.surface.blit(type1,(150,55))
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
            P.surface.blit(ball,(18,18))
            P.surface.blit(name,(60,10))
            if self.code[:5] == 'Mega_':
                P.surface.blit(mega,(65+name_size,20))
            P.surface.blit(gen_i,(350,10))
            if mv.cat == '0':
                cat_ico = pygame.image.load("p/ui/phy_ico.png")
            elif mv.cat == '1':
                cat_ico = pygame.image.load("p/ui/spe_ico.png")
            else:
                cat_ico = pygame.image.load("p/ui/sta_ico.png")
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
            if not pokestar:
                P.surface.blit(exp_back,(38,107))
                if self.lvl != 100:
                    P.surface.fill((0,0,255), Rect(64,110,int(320*(self.exp/self.get_exp())),10))
                else:
                    P.surface.fill((0,0,255), Rect(64,110,320,10))
                P.surface.blit(exp,(10,105))
                P.surface.blit(lvl,(20,50))
                P.surface.blit(type1,(170,55))
                if self.type[1] != None:
                    P.surface.blit(type2,(280,55))
            else:
                if self.type[1] != None:
                    P.surface.blit(type1,(90,55))
                    P.surface.blit(type2,(210,55))
                else:
                    P.surface.blit(type1,(150,55))
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
        copy = Poke(self.code,[self.lvl,self.gen,self.ch,self.m1,self.p1,self.m2,self.p2,self.m3,self.p3,self.m4,self.p4,self.item,self.status,self.exp,self.ball,self.friend,self.true_ability,self.player,self.name,self.nurse,self.petals],over_ability=self.ability,legendary = self.legendary)
        copy.flinch = self.flinch
        copy.idf = self.idf
        copy.cfs = self.cfs
        copy.inf = self.inf
        copy.leech = self.leech
        copy.pursuit = self.pursuit
        copy.minimize = self.minimize
        copy.protect = self.protect
        copy.rest = self.rest
        copy.spikyshield = self.spikyshield
        copy.child_hit = self.child_hit
        copy.cont_move = self.cont_move
        copy.procount = self.procount
        copy.nightmare = self.nightmare
        copy.curse = self.curse
        copy.stat_swap = self.stat_swap
        copy.can_sucker = self.can_sucker
        copy.charge = self.charge
        copy.magic_coat = self.magic_coat
        copy.bellydrum = self.bellydrum
        copy.trapped = self.trapped
        copy.beat_up = self.beat_up
        copy.type_hit = self.type_hit
        copy.chrg = self.chrg
        copy.explode = self.explode
        copy.exit = self.exit
        copy.drag = self.drag
        copy.endure = self.endure
        copy.gastro = self.gastro
        copy.taunt = self.taunt
        copy.yawn = self.yawn
        copy.last_resort = copy.last_resort
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
        copy.mega_debuff = self.mega_debuff
        copy.rollcount = self.rollcount
        copy.stockpile = self.stockpile
        return copy

    def update_stats(self):
        stats = self.orig_stats.copy()
        if self.friend > 300:
            for s in range(len(stats)):
                stats[s] += (self.friend-300)*0.002
        mod = .9+(min(300,self.friend)*0.0002)
        if self.stat_swap[0] == None:
            self.hp = int((10+stats[0]*self.lvl)*mod)+self.lvl
        if self.stat_swap[1] == None:
            self.ak = int((5+stats[1]*self.lvl)*mod)
        if self.stat_swap[2] == None:
            self.sak = int((5+stats[2]*self.lvl)*mod)
        if self.stat_swap[3] == None:
            self.df = int((5+stats[3]*self.lvl)*mod)
        if self.stat_swap[4] == None:
            self.sdf = int((5+stats[4]*self.lvl)*mod)
        if self.stat_swap[5] == None:
            self.spd = int((5+stats[5]*self.lvl)*mod)
        p_mod = self.lvl * 0.2
        if p_mod < 1:
            p_mod = 1
        else:
            p_mod = int(p_mod)
        for petal in self.petals:
            if petal == 'hp' and self.stat_swap[0] == None:
                self.hp += p_mod
            elif petal == 'ak' and self.stat_swap[1] == None:
                self.ak += p_mod
            elif petal == 'sak' and self.stat_swap[2] == None:
                self.sak += p_mod
            elif petal == 'df' and self.stat_swap[3] == None:
                self.df += p_mod
            elif petal == 'sdf' and self.stat_swap[4] == None:
                self.sdf += p_mod
            elif self.stat_swap[5] == None:
                self.spd += p_mod
        if self.ability == "Huge Power" and self.stat_swap[1] == None:
            self.ak *= 2
        if self.ability == 'Hustle' and self.stat_swap[1] == None:
            self.ak *= 1.5
        if self.mega_debuff > 0:
            if self.stat_swap[1] == None:
                self.ak = int(self.ak*self.mega_debuff)
            if self.stat_swap[2] == None:
                self.sak = int(self.sak*self.mega_debuff)
            if self.stat_swap[3] == None:
                self.df = int(self.df*self.mega_debuff)
            if self.stat_swap[4] == None:
                self.sdf = int(self.sdf*self.mega_debuff)
            if self.stat_swap[5] == None:
                self.spd = int(self.spd*self.mega_debuff)
        if self.ch == 787:
            self.ch = self.hp
        if self.ch == 737:
            self.ch = int(self.hp/2)
        if self.ch > self.hp:
            self.ch = self.hp


    def get_stats(self,weight = False) -> None:
        if self.code[-2:] == '_S':
            file = open("poke/"+self.code[:-2]+".txt","r")
        else:
            file = open("poke/"+self.code+".txt","r")
        if self.name[-2:] == '_S':
            self.name = self.name[:-2]
        if self.name == 'Pineapple_Oddish':
            self.name = 'Oddish'
        elif self.name == 'Spooky_Wobbuffet':
            self.name = 'Wobbuffet'
        elif self.name == 'Icy_Gigalith':
            self.name = 'Gigalith'
        if self.name[:5] == 'Mega_':
            self.name = self.name[5:]
        if self.name[:7] == 'Alolan_':
            self.name = self.name[7:]
        if self.name[-5:-1] == '_rot':
            self.name = self.name[:-5]
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
        elif self.actual_name == 'Spooky_Wobbuffet':
            self.actual_name = 'Wobbuffet'
        elif self.actual_name == 'Icy_Gigalith':
            self.actual_name = 'Gigalith'
        if self.actual_name[:7] == 'Alolan_':
            self.actual_name = self.actual_name[7:]
        if self.actual_name[:5] == 'Mega_':
            self.actual_name = self.actual_name[5:]
        if self.actual_name[-5:-1] == '_rot':
            self.actual_name = self.actual_name[:-5]
        if self.actual_name[-2:] == '_M':
            self.actual_name = self.actual_name[:-2]
        if self.actual_name == 'Mime Jr':
            self.actual_name = 'Mime Jr.'
        if self.actual_name == 'Mr Mime':
            self.actual_name = 'Mr. Mime'
        if self.actual_name[-2:] == '_F':
            self.actual_name = self.actual_name[:-2]
        if self.actual_name[-2:] == '_T':
            self.actual_name = self.actual_name[:-2]
        data = file.readlines()
        #fix ability
        abilist = ast.literal_eval(data[0])
        no_hidden = abilist.copy()
        for a in range(len(abilist)):
            if abilist[a][0] == '*':
                no_hidden.remove(abilist[a])
                abilist[a] = abilist[a][1:]
        if self.true_ability == None or self.true_ability not in abilist:
            new_ability = no_hidden[random.randint(0,len(no_hidden)-1)]
            if self.ability == self.true_ability:
                self.ability = new_ability
            self.true_ability = new_ability
        #check ability
        # abis = open("info/abilities.txt","r")
        # abidata = [line[:-1] for line in abis]
        # if self.ability not in abidata:
        #     print(self.ability)
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
        if self.debug:
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

    def ability_list(self):
        if self.code[-2:] == '_S':
            file = open("poke/"+self.code[:-2]+".txt","r")
        else:
            file = open("poke/"+self.code+".txt","r")
        data = file.readlines()
        abilist = ast.literal_eval(data[0])
        no_hidden = abilist.copy()
        hidden = []
        for a in range(len(abilist)):
            if abilist[a][0] == '*':
                no_hidden.remove(abilist[a])
                hidden.append(abilist[a])
                abilist[a] = abilist[a][1:]
        return [no_hidden,hidden,abilist]

    def switch_ability(self):
        abilist = self.ability_list()
        if len(abilist[0]) == 2:
            pos = 0
            if abilist[0][0] == self.true_ability:
                pos = 1
            if self.ability == self.true_ability:
                self.ability = abilist[0][pos]
            self.true_ability = abilist[0][pos]
        else:
            print("Switch Ability Failed: "+len(abilist[0]))
        return self.true_ability

    def get_exp(self) -> int:
        l = self.lvl
        return int((4*(l+1)*(l+1)*(l+1)/5)-(4*l*l*l/5))

    def to_list(self):
        ret = [self.lvl,self.gen,self.ch,self.m1,self.p1,self.m2,self.p2,self.m3,self.p3,self.m4,self.p4,self.item,self.status,self.exp,self.ball,self.friend,self.ability,self.player,self.name,self.nurse,self.petals]
        return ret

    def known_moves(self):
        known = 0
        if self.m1 != None:
            known += 1
        if self.m2 != None:
            known += 1
        if self.m3 != None:
            known += 1
        if self.m4 != None:
            known += 1
        return known

        
