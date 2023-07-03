import sys
import poke
import pygame
import npc
import random
import save
import os
import ast
import poke_func
import map_func
import threading
import items
from pygame.locals import *

class Pokemon:
    def __init__(self):
        pygame.display.set_mode((800,600),DOUBLEBUF)
        #self.poke_tester()
        self.running = True
        self.state = 1
        #1
        f = open("save_files/Sett!ngs.txt","r")
        data = f.readlines()
        self.txt_spd = ast.literal_eval(data[0][:-1])
        self.ani_on = ast.literal_eval(data[1][:-1])
        self.walk_spd = ast.literal_eval(data[2][:-1])
        self.graphic = ast.literal_eval(data[3][:-1])
        self.lighting = data[4][:-1]
        self.vol = ast.literal_eval(data[5][:-1])
        self.sfx_vol = ast.literal_eval(data[6][:-1])
        self.controls = ast.literal_eval(data[7][:-1])
        self.load_images()
        self.song = "music/title.wav"
        self.ocean = -10
        self.f2 = 0
        self.f3 = 0
        self.clock = pygame.time.Clock()
        self.font_l = pygame.font.SysFont("courier", 50, bold = True)
        self.font = pygame.font.SysFont("courier", 40, bold = True)
        self.font_s = pygame.font.SysFont("courier", 30, bold = True)
        self.font_vs = pygame.font.SysFont("courier", 20, bold = True)
        self.leveled_up = []
        self.ani_spd = 60
        #60
        self.bat_spd = 1.25
        #1.5
        self.moving = False
        self.ledge = 0
        self.foam = 0
        self.echoed = [0,0]
        self.buffer_talk = None
        self.new_location = True
        self.loc_in_txt = None
        self.loc_txt = None
        self.ion_deluge = False
        self.grass_prob = 0.01
        self.gem_active = False
        self.use_key_item = None
        self.register_click = 0
        self.move_out_dir = None
        self.turncount = 0
        self.double_money = False
        self.haze_active = 0
        self.loc = ""
        self.habitat = None
        self.fishing = None
        self.camx = 0
        self.camy = 0
        self.legendary_battle = False
        self.tourney_battle = False
        self.garden_timer = False
        self.behind_object = False
        self.future_sight = [0,0,None,None] # fs cast by ally/enemy (ally poke, enemy poke)
        self.prog = [0]
        self.using_repel = False
        self.repel_out = False
        self.ff_dark = self.lantern_dark
        self.metronome = None
        self.txt_sound = pygame.mixer.Sound('music/sfx/text_sfx.wav')
        self.new_memo = None
        self.memo_queue = []
        self.memo_default = self.font_vs.render("Memo Pad updated:",True,(0,0,0))
        self.jour_default = self.font_vs.render("Journal updated:",True,(0,0,0))
        print(self.memo_default.get_width())
        self.memo_default_comp = self.font_vs.render("Entry completed:",True,(0,0,0))
        self.end_battle = 0

    def poke_tester(self):
        no_shiny = []
        shiny = []
        problem = []
        for file in os.listdir("poke"):
            if file.endswith(".txt") and file.startswith("OUTLINE") == False:
                try:
                    bf = pygame.image.load("p/poke/"+file[:-4]+"_S_bf.png")
                    problem.append(file[:-4])
                    bfw = pygame.image.load("p/poke/" + file[:-4] + "_S_bfw.png")
                    bb = pygame.image.load("p/poke/" + file[:-4] + "_S_bb.png")
                    bbw = pygame.image.load("p/poke/" + file[:-4] + "_S_bbw.png")
                    ico = pygame.image.load("p/poke/" + file[:-4] + "_S_ico.png")
                    full = pygame.image.load("p/poke/" + file[:-4] + "_S_full.png")
                    shiny.append(file[:-4])
                except:
                    no_shiny.append(file[:-4])
        for x in shiny:
            problem.remove(x)
        print("has shiny: " + str(shiny))
        print("has problem: " + str(problem))
        print("no shiny: " + str(no_shiny))

    def switch_locations(self):
        while self.running:
            if self.state == 1:
                poke_func.title_screen(self)
                self.state = 2
            if self.state == 2:
                save_r = open("save_files/S@ves.txt","r")
                save_files = save_r.readlines()
                save_r.close()
                self.state = 3
                if save_files == []:
                    poke_func.new_save(self)
                else:
                    poke_func.load_save(save_files, self)
                if self.state == 3:
                    self.load_npcs()
            if self.state == 3:
                self.xl = 0
                self.xr = 0
                self.yu = 0
                self.yd = 0
                self.x = 0
                self.y = 0
                poke_func.update_locs(self)
                if self.loc == "route_1":
                    map_func.route_1(self)
                elif self.loc == 'beedrill':
                    map_func.bee_zone(self)
                elif self.loc == "route_2":
                    map_func.route_2(self)
                elif self.loc == "echo_cave":
                    map_func.echo_cave(self)
                elif self.loc == "aron_cave":
                    map_func.aron_cave(self)
                elif self.loc == "vigore":
                    map_func.vigore_dam(self)
                elif self.loc == "cruise_1":
                    map_func.cruise_1(self)
                elif self.loc == "cruise_2":
                    map_func.cruise_2(self)
                elif self.loc == "dock_1":
                    map_func.dock_1(self)
                elif self.loc == "am_square":
                    map_func.am_square(self)
                elif self.loc == "square_1":
                    map_func.square_1(self)
                elif self.loc == "north_am":
                    map_func.north_am(self)
                elif self.loc == "egida":
                    map_func.egida(self)
                elif self.loc == "egida_under":
                    map_func.egida_under(self)
                elif self.loc == 'egida_mine':
                    map_func.egida_mine(self)
                elif self.loc == 'egida_lab':
                    map_func.egida_lab(self)
                elif self.loc == "egi_gym":
                    map_func.egida_gym_main(self)
                elif self.loc == "egi_gym_l":
                    map_func.egida_gym_l(self)
                elif self.loc == "egi_gym_r":
                    map_func.egida_gym_r(self)
                elif self.loc == "egi_gym_b":
                    map_func.egida_gym_b(self)
                elif self.loc == "power_plant_1":
                    map_func.power_plant_1(self)
                elif self.loc == "power_plant_b":
                    map_func.power_plant_b(self)
                elif self.loc == "power_plant_2":
                    map_func.power_plant_2(self)
                elif self.loc == 'route_3':
                    map_func.route_3(self)
                elif self.loc == 'scarab_l':
                    map_func.scarab_l(self)
                elif self.loc == 'scarab_r':
                    map_func.scarab_r(self)
                elif self.loc == 'fiore':
                    map_func.fiore(self)
                elif self.loc == 'garden_fiore':
                    map_func.gardening(self,1)
                elif self.loc == 'fiore_garden':
                    map_func.fiore_garden(self)
                elif self.loc == 'pianura':
                    map_func.pianura(self)
                elif self.loc == 'pianura_nursery':
                    map_func.pianura_nursery(self)
                elif self.loc == 'pianura_bakery':
                    map_func.pianura_bakery(self)
                elif self.loc == 'mirror_cave':
                    map_func.mirror_cave(self)
                elif self.loc == 'pia_gym':
                    map_func.pia_gym_main(self)
                elif self.loc == 'pia_gymb':
                    map_func.pia_gymb(self)
                elif self.loc == 'route_4':
                    map_func.route_4(self)
                elif self.loc == 'isola':
                    map_func.isola(self)
                elif self.loc == 'route_5':
                    map_func.route_5(self)
                elif self.loc == 'verde':
                    map_func.verde(self)
                elif self.loc == 'verde_garden':
                    map_func.verde_garden(self)
                elif self.loc == 'garden_verde':
                    map_func.gardening(self,0)
                elif self.loc == 'verde_gym':
                    map_func.verde_gym(self)
                elif self.loc == 'verde_gymb':
                    map_func.verde_gymb(self)
                elif self.loc == 'forbidden_1':
                    map_func.forbidden_1(self)
                elif self.loc == 'forbidden_2':
                    map_func.forbidden_2(self)
                elif self.loc == 'forbidden_3':
                    map_func.forbidden_3(self)
                elif self.loc == 'forbidden_4':
                    map_func.forbidden_4(self)
                elif self.loc == 'forbidden_5':
                    map_func.forbidden_5(self)
                elif self.loc == 'forbidden_6':
                    map_func.forbidden_6(self)
                elif self.loc == 'forbidden_7':
                    map_func.forbidden_7(self)
                elif self.loc == 'forbidden_8':
                    map_func.forbidden_8(self)
                elif self.loc == 'forbidden_r':
                    map_func.forbidden_r(self)
                elif self.loc == 'rotom_shed':
                    map_func.rotom_shed(self)
                elif self.loc == 'ombra':
                    map_func.ombra(self)
                elif self.loc == 'ombra_lab':
                    map_func.ombra_lab(self)
                elif self.loc == 'route_6':
                    map_func.route_6(self)
                elif self.loc == 'cascata':
                    map_func.cascata(self)
                elif self.loc == 'cascata_mine':
                    map_func.cascata_mine(self)
                elif self.loc == 'cascata_bakery':
                    map_func.cascata_bakery(self)
                elif self.loc == 'cascata_gym_00':
                    map_func.cascata_gymb(self)
                elif self.loc == 'sunken_cave':
                    map_func.sunken_cave(self)
                elif self.loc == "ralts_cave":
                    map_func.ralts_cave(self)
                elif self.loc == 'mossy':
                    map_func.mossy(self)
                elif self.loc == 'silfide':
                    map_func.silfide(self)
                elif self.loc[:3] == "pc_":
                    self.save_data.pc = self.loc
                    map_func.poke_center(self,self.loc[3:])
                elif self.loc[:7] == "house_1":
                    map_func.house_1(self,int(self.loc[8:]))
                elif self.loc[:8] == "house_21":
                    map_func.house_2_1(self,int(self.loc[9:]))
                elif self.loc[:8] == "house_22":
                    map_func.house_2_2(self,int(self.loc[9:]))
                elif self.loc[:7] == "house_3":
                    map_func.house_3(self,int(self.loc[8:]))
                elif self.loc[:7] == "pia_gym":
                    map_func.pia_gym(self,int(self.loc[8:]))
                elif self.loc[:11] == 'cascata_gym':
                    map_func.cascata_gym(self,int(self.loc[12:]))
            poke_func.update_screen(self)
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def run(self) -> None:
        pygame.display.set_caption("Pokemon Rose")
        pygame.display.set_mode((800,600),DOUBLEBUF)
        #self.surface = pygame.Surface((800,600))
        #self.screen = pygame.display.get_surface()
        self.surface = pygame.display.get_surface()
        t1 = threading.Thread(target = self.close_window)
        t1.start()
        self.switch_locations()
        t1.join()
        #self.switch_locations()

    def close_window(self):
        end = True
        while end:
            if self.running == False:
                end = False
            # if pygame.event.peek(eventtype = pygame.QUIT,pump = True):
            #     self.running = False
            for event in pygame.event.get(eventtype = pygame.QUIT):
                self.running = False
            self.clock.tick(self.ani_spd)

    def load_npcs(self):
        #npcs:
        self.r1_sci = npc.NPC(self,'Scientistm','Nerd',[2500,-1500],[['mr',60],['r',60],['ml',60],['l',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""])
        self.egi_pre = npc.NPC(self,'Preschoolerg','Creep',[1400,-600],[['d',60]],["Sometimes I like to just stare","at the people walking around","down there.","They're so small it makes me","feel like a grown up!",""])
        self.egi_sciu = npc.NPC(self,'Scientistf','Nerd',[1700,-680],[['md',60],['d',60],['mu',60],['u',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""])
        self.egi_sci = npc.NPC(self,'Scientistm','Nerd',[1500,-150],[['mr',60],['r',60],['ml',60],['l',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""])
        self.egi_robb1 = npc.NPC(self,'Bug Catcher','Robb',[500,150],[['d',60],['r',80],['l',90],['u',40]],["","",""])
        self.egi_robb2 = npc.NPC(self,'Bug Catcher','Robb',[500,150],[['u',100]],["","",""])
        self.egi_colress_npc = npc.NPC(self,'Colress','',[1150,-800],[['u',40]],["Were you able to track down","the one that ran away?","","I would imagine he is still","pretty close to the Power", "Plant."])
        self.r2_tree1 = poke_func.cut_tree(self,1200,-1600,16)
        self.pia_gymdoor = poke_func.load("p/pianura/gym_door.png")
        self.pia_mom = npc.NPC(self,'Healer','Cherry',[1300,500],[['d',20]],["Ahh, I'm glad she's so full of","energy, but I don't think I","can keep up with her..."])
        self.pia_kid = npc.NPC(self,'Preschoolerg','Cherry',[1350,850],[['u',120],['mr',40],['u',200],['mr',30],['mu',30],['u',300],['md',30],['ml',30],['u',150],['ml',40]],["I'm playing hide-and-seek with","my mom! Don't tell her where","I'm hiding!"],spd = 1)
        self.pia_hiker = npc.NPC(self,'Hiker','Cherry',[2250,500],[['l',20]],["Oof! I took one step in that","cave, and I couldn't see a","damn thing!","People always said it was","risky to wander in there. I","guess now I know why!"])
        self.pia_lass = npc.NPC(self,'Lass','Cherry',[2000,-450],[['u',20]],["They all look so yummy! But I","only have enough money to buy","one of them!"])
        self.pia_beauty = npc.NPC(self,'Beauty','Cherry',[500,1100],[['d',20]],["Sometimes you just have to","take a break and admire nature","for a bit.","Then when you're well rested","you can get back to the rush","of life!","Or you can be like me and keep","taking it easy!",""])
        self.pia_ace = npc.NPC(self,'Ace Trainerf','Cherry',[650,450],[['mr',40],['ml',40]],["I just left my Pokemon at the","nursery, but I miss it so much","already!","I wanna run back in there and","take it back, but then the","money I spent will go to waste!"])
        self.pia_bea = npc.NPC(self,'Beauty','Cherry',[1950,-850],[['l',20]],["The breeze up here is so nice","and cool!","","Coupled with this delicious","sundae, I feel so refreshed!",""])
        self.pia_rich = npc.NPC(self,'Rich Boy','Cherry',[1850,-850],[['r',20]],["Would you just look at the","size of this sundae!","","I don't think I'll be able to","fit all of this in my stomach","without it hurting!"])
        self.r4_tree1 = poke_func.cut_tree(self,1350,300,17)
        self.r4_tree2 = poke_func.cut_tree(self,1300,350,18)
        self.r4_expf_npc = npc.NPC(self,'Expertf','Timmy',[1500,1200],[['l',80]],["People say this is a scorch","mark left by a lightning","strike from Thundurus.","It could just be a myth, but","it's exhilarating to think","about isn't it?"])

        self.isola_host = npc.NPC(self,'Hostess','Harper',[600,-500],[['d',40]],["","",""])
        self.isola_seed = npc.NPC(self,'Seedot','Harper',[1550,-100],[['d',40]],["SEEDOT!!!","",""])
        self.isola_fish = npc.NPC(self,'Fisherman','Harper',[1550,-150],[['r',40]],["Hey, thanks again for the","Seedot! It's nice to have a","little friend to travel with!","If you ever find the time, you","should come meet me in Alto","Mare Square on Sundays!","I'll have some nice items that","I've collected throughout the","week for you to buy!"])
        self.r5_tree1 = poke_func.cut_tree(self,2150,-300,20)
        self.r5_tree2 = poke_func.cut_tree(self,2200,-250,21)
        self.r5_tree3 = poke_func.cut_tree(self,2150,-200,19)
        self.r5_sci = npc.NPC(self,'Scizor','Dude',[1200,-300],[['d',20]],["","",""])
        self.verde_beauty = npc.NPC(self,'Beauty','Harper',[3200,-150],[['u',180],['md',80],['d',240],['mu',80]],["Whenever I go on a walk, I","love stopping by this area to","relax.","The musician that lives here","plays such beautiful music, I","could listen to it all day!"])
        self.verde_gentle = npc.NPC(self,'Gentleman','Tourney Guy',[3000,-250],[['d',40]],["Are you here to compete in","the Verde Tournament?","","Oh, you don't appear to be a","registered trainer.",""])
        self.verde_fan = npc.NPC(self,'Poke Fan','Harper',[1750,-150],[['u',80],['d',40],['r',60],['l',20]],["Rumors say there's a haunted","storage in the middle of the","forest!","Some say you can hear a","rattling sound inside if you","listen closely!"])

        self.cascata_tri = npc.NPC(self,'Triathelete','Harper',[850,650],[['mr',130],['md',80],['ml',10],['mu',70],['ml',110],['md',220],['ml',10],['mu',230]],["Living on a mountain means","you've got a great workout","spot in your front yard!","I could punt a Geodude across","the city with the amount of","leg strength I've built up!","Probably.","Not that I would actually do","that of course!"],spd = 1)
        self.cascata_beauty = npc.NPC(self,'Beauty','Harper',[500,600],[['u',100]],["Omigosh! The desserts here","look so perfect! I'm dying to","get a taste of them!","But my reservation isn't until","next week! I don't know if I","can wait that long!"])
        self.cascata_fish = npc.NPC(self,'Sailor','Harper',[700,1750],[['u',40]],["You know, there's something","about waterfalls that makes","them so mesmerizing.","I feel like I've been here for","hours, just staring at the","water flow down."])
        self.cascata_bug = npc.NPC(self,'Bug Catcher','Harper',[1500,1400],[['d',40]],["One of these days, a Pokemon","is going to carelessly ride","down this waterfall.","Then BAM!!!","I'll strike from the shadows","and catch it with my net!"])
        self.cascata_gentle = npc.NPC(self,'Gentleman','Harper',[550,300],[['r',40]],["Sitting here, enjoying some","cake, listening to the soft","rumbling of the waterfall...","This is what true bliss feels","like!",""])
        self.r6_rock1 = npc.NPC(self,'Team Rocketf','Grunt',[2450,3600],[['d',20]],["Haha! You'll never get past","this Snorlax!","","We'll complete our master plan","and there's nothing you can do","about it!"])
        self.r6_rock2 = npc.NPC(self,'Team Rocketm','Grunt',[2700,3600],[['d',20]],["This road is closed for","maintenance. Feel free to rest","up in Cascata City.","Why a Snorlax?","Well we couldn't find any","spare construction signs.","Move along now, or you're","going to have a talk with my","superior!"])
        self.r6_healer = None
        self.r6_pre = None
        self.r6_rock3 = None
        self.r6_rock6 = npc.NPC(self,'Team Rocketm','Grunt',[1500,-2100],[['r',20]],["I've still got a Beedrill","left, but he plowed through", "the other guys so fast!","It's probably better if I just","stay here and pretend like I","got beat up."])
        self.r6_rock7 = npc.NPC(self,'Team Rocketm','Grunt',[1900,-2050],[['l',20]],["When I signed up for this","mission, no one told me I'd","have to fight the Elite Four!"])
        self.r6_rock8 = npc.NPC(self,'Team Rocketm','Grunt',[1800,-1950],[['u',20]],["One blast from his Milotic","demolished my Mightyena. He", "didn't even look at me!"])

        self.r6_proton = npc.NPC(self,'Rocket Admin','Proton',[1800,-2200],[['l',20]],["Haha! You'll never get past","this Snorlax!","","We'll complete our master plan","and there's nothing you can do","about it!"])
        self.r6_wallace = npc.NPC(self,'Wallace','Grunt',[1600,-2200],[['r',20]],["Move along now, or you're","going to have a talk with my","superior!"])
        self.r6_lisia = npc.NPC(self,'Lisia','Grunt',[1700,-2850],[['d',40]],["Move along now, or you're","going to have a talk with my","superior!"])
        self.r6_tree1 = poke_func.cut_tree(self,3100,-1000,33)
        self.r6_tree2 = poke_func.cut_tree(self,3050,-950,34)
        pre = 'Preschoolerb'
        she = 'he'
        if self.save_data.gen == 1:
            pre = 'Preschoolerg'
            she = 'she'
        if self.prog[12][7] == 0:
            self.r6_healer = npc.NPC(self,'Healer','Cherry',[4500,2100],[['u',100],['d',80],['l',60],['r',80]],["Please hurry! I don't know","what I would do if something","happened to my child!"])
        elif self.prog[12][7] == 1:
            self.r6_pre = npc.NPC(self,pre,'Cherry',[4400,1250],[['r',20]],["Help! I thought she was my","mom, and now I don't know","where she is!"])
            self.r6_rock3 = npc.NPC(self,'Team Rocketf','Grunt',[4450,1250],[['l',80]],["", "",""])
            self.r6_healer = npc.NPC(self,'Healer','Cherry',[4500,2100],[['u',100],['d',80],['l',60],['r',80]],["Please hurry! I don't know","what I would do if something","happened to my child!"])
        elif self.prog[12][7] == 2:
            self.r6_pre = npc.NPC(self,pre,'Cherry',[4500,2150],[['u',20]],["Poor mommy. You should've seen","how much she was shaking when","I found her.","Thank goodness I got back to","her in time!",""])
            self.r6_healer = npc.NPC(self,'Healer','Cherry',[4500,2100],[['d',80]],["Please hurry! I don't know","what I would do if something","happened to my child!"])
        elif self.prog[12][7] == 3:
            self.r6_pre = npc.NPC(self,pre,'Cherry',[2200,1800],[['u',100],['d',80],['l',60],['r',80]],["You should get a move on. My","mom gets scared pretty easily.",""])
        elif self.prog[12][7] == 4:
            self.r6_pre = npc.NPC(self,pre,'Cherry',[2200,1800],[['u',100],['d',80],['l',60],['r',80]],["You should get a move on. My","mom gets scared pretty easily.",""])
            self.r6_healer = npc.NPC(self,'Healer','Cherry',[2300,650],[['d',80]],["Oh the look on her face is so", "sinister! I don't know what","she wants with me!"])
            self.r6_rock3 = npc.NPC(self,'Team Rocketf','Grunt',[2300,700],[['u',80]],["", "",""])
        elif self.prog[12][7] == 5:
            self.r6_pre = npc.NPC(self,pre,'Cherry',[2200,1800],[['l',80]],["You should get a move on. My","mom gets scared pretty easily.",""])
            self.r6_healer = npc.NPC(self,'Healer','Cherry',[2150,1800],[['r',80]],["We really need to head home,","but "+she+" insisted on waiting","for you to come back."])

        #trainers
        if self.prog[5][0] == 0:
            self.r1_timmy = npc.NPC(self,'Youngster','Timmy',[1200,-450],[['d',100]],["Stop right there!","","","You're gonna have to get past","me if you wanna mess around in", "my field!"],["Ack! Not again...","",""],True,[0,200,0,0],[poke.Poke('Bellsprout',[7,random.randint(0,1),787,"Growth",1,"Vine Whip",0,None,None,None,None,None,None,0,"Poke Ball",0,"Chlorophyll"])],0,loc = "route_1")
        else:
            self.r1_timmy = npc.NPC(self,'Youngster','Timmy',[1200,-450],[['d',100]],["Just you wait!","I'm gonna get you back for","beating me!"],loc = "route_1")
        if self.prog[5][1] == 0:
            self.r1_amy = npc.NPC(self,'Lass','Amy',[1600,-850],[['d',100],['r',100]],["Hey wanna see what I learned","today?",""],["Oh, I guess it wasn't very","useful.",""],True,[0,250,0,300],[poke.Poke('Oddish',[5,random.randint(0,1),787,"Absorb",-1,"Growth",-1,"Sweet Scent",-1,None,None,None,None,0,"Poke Ball"]),poke.Poke('Skitty',[6,random.randint(0,1),787,"Fake Out",-1,"Tackle",-1,"Tail Whip",-1,"Growl",-1,None,None,0,"Poke Ball",0,"Cute Charm"])],1,loc = "route_1")
        else:
            self.r1_amy = npc.NPC(self,'Lass','Amy',[1600,-850],[['d',100]],["My teacher could learn a thing ","or two from you.",""],loc = "route_1")
        if self.prog[5][2] == 0:
            self.r1_robb = npc.NPC(self,'Bug Catcher','Robb',[1500,-1200],[['d',60],['r',80],['l',90],['u',40]],["You there!","Check out this cool Pokemon I","just found!"],["Your Pokemon are pretty cool","too I guess...",""],True,[50,200,100,200],[poke.Poke('Weedle',[5,random.randint(0,1),787,"String Shot",-1,"Poison Sting",-1,None,None,None,None,None,None,0,"Poke Ball"]),poke.Poke('Caterpie',[5,random.randint(0,1),787,"Tackle",-1,"String Shot",-1,None,None,None,None,None,None,0,"Poke Ball"]),poke.Poke('Scyther',[6,random.randint(0,1),787,"Quick Attack",-1,"Leer",-1,"Focus Energy",-1,"Vacuum Wave",-1,None,None,0,"Poke Ball",0,"Swarm"])],2,loc = "route_1")
        else:
            self.r1_robb = npc.NPC(self,'Bug Catcher','Robb',[1500,-1200],[['u',100]],["I bet there's an even cooler","Pokemon hiding in this grass!",""],loc = "route_1")
        if self.prog[5][3] == 0:
            self.r1_noland = npc.NPC(self,'Gentleman','Noland',[2850,-500],[['r',100]],["It's not often I see a new","adventurer around here.","","Perhaps you would be willing", "to entertain this old man with","a battle?"],["Hmmph!","That certainly brought back","old memories!","It's been ages since I got","this heated over a Pokemon","battle!","Who knows, maybe you have what", "it takes to beat the champion!","Ha!"],True,[50,150,50,200],[poke.Poke('Nidorino',[16,0,787,"Focus Energy",-1,"Leer",-1,"Double Kick",-1,"Poison Sting",-1,'Eviolite',None,0,"Luxury Ball",400,"Rivalry"]),poke.Poke('Nidorina',[16,1,787,"Growl",-1,"Scratch",-1,"Poison Sting",-1,"Double Kick",-1,'Eviolite',None,0,"Luxury Ball",400,"Rivalry"])],3,loc = "route_1")
        else:
            self.r1_noland = npc.NPC(self,'Gentleman','Noland',[1500,-550],[['l',100]],["I still remember when this was","a statue of Cynthia back when","she oversaw the city.","I heard you can still find","that statue standing in the", "Alto Mare gym."],loc = "route_1")
        if self.prog[5][4] == 0:
            self.r2_ayla = npc.NPC(self,'Battle Girl','Ayla',[950,-1100],[['d',40],['r',20],['l',20],['md',20],['u',40],['r',20],['l',20],['mu',20]],["Hey you look pretty strong!","Beating you will be part of my","training!"],["Ha ha! Just kidding!","You're way too strong...",""],True,[100,100,50,100],[poke.Poke('Machop',[9,random.randint(0,1),787,"Low Kick",-1,"Leer",-1,"Focus Energy",-1,"Karate Chop",-1,None,None,0,"Poke Ball",0,"Guts"]),poke.Poke('Timburr',[9,random.randint(0,1),787,"Pound",-1,"Leer",-1,"Bide",-1,"Focus Energy",-1,None,None,0,"Poke Ball",0,"Sheer Force"])],4,loc = "route_2")
        else:
            self.r2_ayla = npc.NPC(self,'Battle Girl','Ayla',[950,-1100],[['d',40],['r',20],['l',20],['md',20],['u',40],['r',20],['l',20],['mu',20]],["I'm gonna beat the next","trainer I see as part of my","training!","Not you of course!","",""],loc = "route_2")
        if self.prog[5][5] == 0:
            self.r2_robby = npc.NPC(self,'Hiker','Robby',[800,-1450],[['mr',140],['ml',140]],["The road ahead is pretty", "dangerous.", "","You're gonna have to beat me", "in a battle if you wanna", "survive in there!"],["Ha! You're a lot stronger than","you look! I don't know what I","was so worried about."],True,[0,0,150,150],[poke.Poke('Spearow',[7,random.randint(0,1),787,"Peck",-1,"Growl",-1,"Leer",-1,None,None,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Aron',[8,random.randint(0,1),787,"Harden",-1,"Mud-Slap",-1,"Headbutt",-1,"Tackle",-1,None,None,0,"Poke Ball",0,"Sturdy"]),poke.Poke('Trapinch',[10,random.randint(0,1),787,"Mud-Slap",-1,"Bite",-1,"Bulldoze",-1,"Bide",-1,None,None,0,"Premier Ball",0,"Arena Trap"])],5,loc = "route_2")
        else:
            self.r2_robby = npc.NPC(self,'Hiker','Robby',[800,-1450],[['mr',140],['ml',140]],["Heh.", "I've never actually gone into", "the caves.","I'm too scared of the creepy","sounds you hear just standing", "at the entrance..."],loc = "route_2")
        if self.prog[5][6] == 0:
            self.echo_carlos = npc.NPC(self,'Preschoolerb','Carlos',[550,-600],[['mr',60],['md',40],['ml',60],['mu',40]],["E C H O O O O O ! ! ! ! ! !","",""],["Ehehe...","That was pretty cool though","wasn't it?"],True,[100,100,100,100],[poke.Poke('Whismur',[8,random.randint(0,1),787,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"]),poke.Poke('Whismur',[9,random.randint(0,1),787,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"]),poke.Poke('Whismur',[10,random.randint(0,1),787,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"])],6,spd = 1,loc = "echo_cave")
        else:
            self.echo_carlos = npc.NPC(self,'Preschoolerb','Carlos',[550,-600],[['mr',60],['md',40],['ml',60],['mu',40]],["This place is awesome!!!","I can yell as much as I want","and Mom won't get mad at me!"],spd = 1,loc = "echo_cave")
        if self.prog[5][7] == 0:
            self.echo_vivi = npc.NPC(self,'Ace Trainerf','Vivian',[1300,-1700],[['d',100]],["Ha! What a shame!","Climbing all the way up here","just to get crushed by me!"],["Yikes!","Maybe I spoke a little too", "soon..."],True,[0,150,0,0],[poke.Poke('Nidoran_F',[10,random.randint(0,1),787,"Growl",-1,"Scratch",-1,"Tail Whip",-1,"Double Kick",-1,None,None,0,"Ultra Ball",0,"Rivalry"]),poke.Poke('Noibat',[10,random.randint(0,1),787,"Screech",-1,"Supersonic",-1,"Absorb",-1,"Tackle",-1,None,None,0,"Ultra Ball",0,"Infiltrator"]),poke.Poke('Roggenrola',[10,random.randint(0,1),787,"Tackle",-1,"Sand Attack",-1,"Harden",-1,"Headbutt",-1,None,None,0,"Ultra Ball",0,"Sturdy"]),poke.Poke('Butterfree',[11,random.randint(0,1),787,"Gust",-1,"Confusion",-1,"String Shot",-1,"Tackle",-1,None,None,0,"Ultra Ball",0,"Compound Eyes"])],7,loc = "echo_cave")
        else:
            self.echo_vivi = npc.NPC(self,'Ace Trainerf','Vivian',[1300,-1700],[['d',100]],["Huh, looks like I was the one","who got crushed...",""],loc = "echo_cave")
        if self.prog[5][8] == 0:
            self.vigore_troy = npc.NPC(self,'Triathelete','Troy',[1800,-1300],[['md',20],['mr',250],['mu',20],['ml',250]],["*Huff* *puff*","I can't...last...much...","longer..."],["*Huff* *puff*","I think...this is...the end...","for me..."],True,[100,100,100,100],[poke.Poke('Joltik',[12,random.randint(0,1),787,"Fury Cutter",-1,"Absorb",-1,"Thunder Wave",-1,"Screech",-1,None,None,0,"Poke Ball",0,"Compound Eyes"]),poke.Poke('Electrike',[12,random.randint(0,1),787,"Tackle",-1,"Howl",-1,"Thunder Wave",-1,"Quick Attack",-1,None,None,0,"Poke Ball",0,"Static"]),poke.Poke('Elekid',[12,random.randint(0,1),787,"Quick Attack",-1,"Thunder Shock",-1,"Low Kick",-1,"Swift",-1,None,None,0,"Poke Ball",0,"Static"])],8,spd = 1,loc = "vigore")
        else:
            self.vigore_troy = npc.NPC(self,'Triathelete','Troy',[1800,-1300],[['md',20],['mr',250],['mu',20],['ml',250]],["*Huff* *puff*","I can't...feel...my legs...","anymore..."],spd = 1,loc = "echo_cave")
        if self.prog[5][9] == 0:
            self.vigore_genos = npc.NPC(self,'Expertm','Chuck',[1800,-1200],[['mr',250],['mu',20],['ml',250],['md',20]],["Allow me to give you a taste","of the wonders of running!",""],["Hmph! If I were younger, I","would've run circles around","you!"],True,[100,100,100,100],[poke.Poke('Pidgey',[12,random.randint(0,1),787,"Tackle",-1,"Sand Attack",-1,"Gust",-1,None,None,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Spearow',[12,random.randint(0,1),787,"Peck",-1,"Leer",-1,"Pursuit",-1,"Fury Attack",-1,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Scyther',[12,random.randint(0,1),787,"Vacuum Wave",-1,"Quick Attack",-1,"Pursuit",-1,"Focus Energy",-1,None,None,0,"Poke Ball",0,"Technician"])],9,spd = 1,loc = "echo_cave")
        else:
            self.vigore_genos = npc.NPC(self,'Expertm','Chuck',[1800,-1200],[['mr',250],['mu',20],['ml',250],['md',20]],["No breaks allowed!","Stopping to rest is admitting","defeat!"],spd = 1,loc = "echo_cave")
        if self.prog[5][10] == 0:
            self.vigore_victor = npc.NPC(self,'Ace Trainerm','Victor',[3600,-1000],[['l',20]],["Hey! You look like a suitable","trainer to test my Pokemon","against."],["Well, my dad always said that","losing is just another step in","getting stronger."],True,[0,0,100,0],[poke.Poke('Nidoran_M',[12,random.randint(0,1),787,"Leer",-1,"Peck",-1,"Focus Energy",-1,"Double Kick",-1,None,None,0,"Ultra Ball",0,"Rivalry"]),poke.Poke('Togedemaru',[12,random.randint(0,1),787,"Tackle",-1,"Thunder Shock",-1,"Defense Curl",-1,"Rollout",-1,None,None,0,"Ultra Ball",0,"Iron Barbs"]),poke.Poke('Sandile',[13,random.randint(0,1),787,"Bite",-1,"Sand Attack",-1,"Torment",-1,"Sand Tomb",-1,None,None,0,"Ultra Ball",0,"Moxie"]),poke.Poke('Beedrill',[13,random.randint(0,1),787,"Twineedle",-1,"Fury Attack",-1,"Harden",-1,"Poison Sting",-1,None,None,0,"Ultra Ball",0,"Swarm"])],10,loc = "echo_cave")
        else:
            self.vigore_victor = npc.NPC(self,'Ace Trainerm','Victor',[3600,-1000],[['l',20]],["There's an Electrike down that","trail that keeps snarling when","you approach him."],loc = "echo_cave")
        if self.prog[5][11] == 0:
            self.egi_gyml_sci = npc.NPC(self,'Scientistf','Sandy',[50,350],[['u',20]],["Sorry I didn't see you enter.","Perhaps there's something you","need assistance with?","Well, you're not getting","anything out of me unless you","beat me in a battle!"],["The main gate?","Yeah I've got the controller","for it right here!","...","...","...","Well, that's awkward. It looks","like I accidentally dropped","the controller somewhere."],True,[0,0,0,0],[poke.Poke('Klink',[14,2,787,"Vice Grip",-1,"Charge",-1,"Thunder Shock",-1,None,None,None,None,0,"Poke Ball",0,"Minus"]),poke.Poke('Togedemaru',[15,random.randint(0,1),787,"Defense Curl",-1,"Rollout",-1,"Charge",-1,"Thunder Shock",-1,None,None,0,"Poke Ball",0,"Iron Barbs"])],11,loc = "egi_gym_l")
        else:
            self.egi_gyml_sci = npc.NPC(self,'Scientistf','Sandy',[50,350],[['u',20]],["Very sorry about that. I'm","usually not so clumsy.",""],loc = "egi_gym_l")
        if self.prog[5][12] == 0:
            self.egi_gymr_sci = npc.NPC(self,'Scientistm','George',[150,300],[['d',20]],["Our research has almost hit","the stage where we can revive","Pokemon fossils!", "Imagine all those extinct","Pokemon walking the streets", "again!"],["I apologize if I scared you.","Sometimes I can't help but", "express my love for research.","*BEEP*","That should take care of the","gate outside."],True,[0,0,0,0],[poke.Poke('Klink',[13,2,787,"Vice Grip",-1,"Charge",-1,"Thunder Shock",-1,None,None,None,None,0,"Poke Ball",0,"Plus"]),poke.Poke('Aron',[14,random.randint(0,1),787,"Mud-Slap",-1,"Headbutt",-1,"Metal Claw",-1,"Rock Tomb",-1,None,None,0,"Poke Ball",0,"Sturdy"]),poke.Poke('Magnemite',[14,2,787,"Supersonic",-1,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,None,None,0,"Poke Ball",0,"Magnet Pull"])],12,loc = "egi_gym_r")
        else:
            self.egi_gymr_sci = npc.NPC(self,'Scientistm','George',[150,300],[['d',20]],["Let me know if you ever want","to dabble in research. I would", "love to give you some tips."],loc = "egi_gym_r")
        if self.prog[5][13] == 0:
            self.r3_bug = npc.NPC(self,'Bug Catcher','Charlie',[2100,100],[['md',60],['d',20],['mr',40],['r',80],['mu',60],['u',60],['ml',40],['l',20]],["Are you here to find new bugs","with me? If not, you'd better","buzz off!"],["Hmph! Fine, you can play here","too. Just don't forget that I", "was here first!"],True,[100,100,100,100],[poke.Poke('Joltik',[14,random.randint(0,1),787,"Thunder Wave",-1,"Screech",-1,"Fury Cutter",-1,"Spider Web",-1,None,None,0,"Poke Ball",100,"Compound Eyes"]),poke.Poke('Venipede',[14,random.randint(0,1),787,"Defense Curl",-1,"Rollout",-1,"Screech",-1,"Pursuit",-1,None,None,0,"Poke Ball",100,"Poison Point"]),poke.Poke('Beedrill',[14,random.randint(0,1),787,"Twineedle",-1,"Fury Attack",-1,"Poison Sting",-1,"Rage",-1,None,None,0,"Poke Ball",50,"Swarm"]),poke.Poke('Butterfree',[14,random.randint(0,1),787,"Gust",-1,"Confusion",-1,"Sleep Powder",-1,"Stun Spore",-1,None,None,0,"Poke Ball",50,"Compound Eyes"])],13,loc = "route_3")
        else:
            self.r3_bug = npc.NPC(self,'Bug Catcher','Charlie',[2100,100],[['md',60],['d',20],['mr',40],['r',80],['mu',60],['u',60],['ml',40],['l',20]],["Hurry up and leave already!","I only said you could stay for", "a little while!","I can't have you finding all","the Pokemon here before I get","the chance to!"],loc = "route_3")
        if self.prog[5][14] == 0:
            self.r3_hika = npc.NPC(self,'Hiker','Bryson',[1500,200],[['u',20]],["Hey! These crystals are mine!","No one's getting their hands","on them, not even you!"],["Oh, you're not here to mine","them? Well I just wanted to", "look at them anyways..."],True,[50,0,0,0],[poke.Poke('Roggenrola',[16,random.randint(0,1),787,"Headbutt",-1,"Harden",-1,"Sand Attack",-1,"Rock Blast",-1,None,None,0,"Poke Ball",50,"Weak Armor"]),poke.Poke('Dwebble',[17,random.randint(0,1),787,"Fury Cutter",-1,"Smack Down",-1,"Rock Blast",-1,"Feint Attack",-1,None,None,0,"Poke Ball",50,"Shell Armor"])],14,loc = "route_3")
        else:
            self.r3_hika = npc.NPC(self,'Hiker','Bryson',[1500,200],[['u',20]],["Despite all the expeditions","I've been on, I've never seen", "crystals like these.","The way they're glowing...It's","almost as if they're alive!",""],loc = "route_3")
        if self.prog[5][15] == 0:
            self.r3_sci = npc.NPC(self,'Scientistf','Rosa',[1650,100],[['l',100],['mu',40],['ml',60],['d',140],['mr',60],['md',40]],["I've been analyzing this rock","for so long, I'm starting to","feel really sleepy!", "I think it's about time I had","a break from this crystal!", ""],["Woo! That was refreshing!","Now I can get right back to my", "research!"],True,[100,100,100,100],[poke.Poke('Voltorb',[15,2,787,"Sonic Boom",-1,"Eerie Impulse",-1,"Screech",-1,"Rollout",-1,'Poke Ball',None,50,"Poke Ball",0,"Soundproof"]),poke.Poke('Aron',[15,random.randint(0,1),787,"Mud-Slap",-1,"Headbutt",-1,"Metal Claw",-1,"Harden",-1,None,None,0,"Poke Ball",50,"Sturdy"]),poke.Poke('Carbink',[16,2,787,"Sharpen",-1,"Tackle",-1,"Smack Down",-1,"Harden",-1,None,None,0,"Poke Ball",0,"Clear Body"])],15,loc = "route_3")
        else:
            self.r3_sci = npc.NPC(self,'Scientistf','Rosa',[1650,100],[['l',100],['mu',40],['ml',60],['d',140],['mr',60],['md',40]],["Ugh! I'm already tired again!","How important could a little", "pink crystal possibly be?"],loc = "route_3")
        if self.prog[5][16] == 0:
            self.sl_psy = npc.NPC(self,'Psychic','Hugo',[2250,-550],[['mr',60],['r',200],['md',60],['d',140],['ml',60],['l',260],['mu',60],['u',160]],["","",""],["That's not possible! I had the","power of knowledge! You never", "should have stood a chance!"],True,[100,200,100,200],[poke.Poke('Drowzee',[18,random.randint(0,1),787,"Poison Gas",-1,"Headbutt",-1,"Confusion",-1,"Disable",-1,None,None,0,"Poke Ball",100,"Insomnia"]),poke.Poke('Chimecho',[19,random.randint(0,1),787,"Astonish",-1,"Yawn",-1,"Psywave",-1,"Take Down",-1,None,None,0,"Poke Ball",150,"Levitate"])],16,loc = "scarab_l")
        else:
            self.sl_psy = npc.NPC(self,'Psychic','Hugo',[2250,-550],[['mr',60],['r',200],['md',60],['d',140],['ml',60],['l',260],['mu',60],['u',160]],["I haven't given up! Soon I'll","be able to predict everything", "a trainer could possibly do!","Then I'll be able to take on","anyone that strolls through","here!"],loc = "scarab_l")
        if self.prog[5][17] == 0:
            self.sl_rich = npc.NPC(self,'Rich Boy','Leonard',[1300,400],[['l',60],['u',40],['d',100],['r',60]],["There is so much filth and","muck everwhere! I don't even","know where I am anymore!"],["Ugh, and on top of everything,","I can't even win a battle", "against some random trainer!","This has got to be the worst","day of my life!",""],True,[100,100,100,100],[poke.Poke('Electrike',[17,random.randint(0,1),787,"Leer",-1,"Thunder Wave",-1,"Quick Attack",-1,"Spark",-1,None,None,0,"Poke Ball",100,"Static"]),poke.Poke('Nidorino',[17,0,787,"Poison Sting",-1,"Double Kick",-1,"Peck",-1,"Focus Energy",-1,None,None,0,"Poke Ball",50,"Rivalry"]),poke.Poke('Luxio',[18,random.randint(0,1),787,"Leer",-1,"Spark",-1,"Charge",-1,"Bite",-1,None,None,0,"Poke Ball",50,"Intimidate"])],17,loc = "scarab_l")
        else:
            self.sl_rich = npc.NPC(self,'Rich Boy','Leonard',[1300,400],[['d',60]],["Why did I even bother stepping","inside here? It's just been ","disasters one after another!","I followed the directions that","stupid girl gave me, and just", "look at the result!"],loc = "scarab_l")
        if self.prog[5][18] == 0:
            self.sl_ace = npc.NPC(self,'Ace Trainerf','Jesse',[3300,350],[['l',100]],["I've been training for days in","these woods. Get ready to see","the fruits of my labor!"],["No way! I lost even after all","that training? Maybe I'm not", "cut out for this..."],True,[0,0,150,0],[poke.Poke('Skitty',[17,random.randint(0,1),787,"Attract",-1,"Fake Out",-1,"Disarming Voice",-1,"Double Slap",-1,None,None,0,"Ultra Ball",150,"Normalize"]),poke.Poke('Dunsparce',[18,random.randint(0,1),787,"Screech",-1,"Mud-Slap",-1,"Yawn",-1,"Rollout",-1,None,None,0,"Ultra Ball",50,"Serene Grace"]),poke.Poke('Zubat',[17,random.randint(0,1),787,"Supersonic",-1,"Bite",-1,"Wing Attack",-1,"Confuse Ray",-1,None,None,0,"Ultra Ball",100,"Inner Focus"]),poke.Poke('Nuzleaf',[18,random.randint(0,1),787,"Razor Leaf",-1,"Fake Out",-1,"Nature Power",-1,"Growth",-1,None,None,0,"Ultra Ball",100,"Early Bird"]),poke.Poke('Heracross',[18,random.randint(0,1),787,"Endure",-1,"Aerial Ace",-1,"Chip Away",-1,"Feint",-1,None,None,0,"Ultra Ball",50,"Guts"])],18,loc = "scarab_l")
        else:
            self.sl_ace = npc.NPC(self,'Ace Trainerf','Jesse',[3300,350],[['l',100]],["I won't give up! I'll just","keep training until I can beat","even you in a battle!"],loc = "scarab_l")
        if self.prog[5][19] == 0:
            self.sr_beauty = npc.NPC(self,'Beauty','Lucille',[1100,600],[['l',60],['u',100],['r',60],['u',60]],["Hee hee! He'll never be able","to find me hiding all the way","out here!"],["Hee hee! Well that was pretty","fun, wasn't it?", ""],True,[100,100,100,100],[poke.Poke('Psyduck',[19,random.randint(0,1),787,"Confusion",-1,"Fury Swipes",-1,"Water Pulse",-1,"Disable",-1,None,None,0,"Poke Ball",100,"Damp"]),poke.Poke('Nidorina',[19,1,787,"Poison Sting",-1,"Scratch",-1,"Double Kick",-1,"Growl",-1,None,None,0,"Poke Ball",100,"Rivalry"]),poke.Poke('Maractus',[19,random.randint(0,1),787,"Cotton Spore",-1,"Mega Drain",-1,"Pin Missile",-1,"Synthesis",-1,None,None,0,"Poke Ball",150,"Water Absorb"])],19,loc = "scarab_r")
        else:
            self.sr_beauty = npc.NPC(self,'Beauty','Lucille',[1100,600],[['u',60]],["Do you think he's okay?","He hasn't texted me anything","for a while...","I mean, what's the worst that","could happen?",""],loc = "scarab_r")
        if self.prog[5][20] == 0:
            self.sr_ace = npc.NPC(self,'Ace Trainerm','James',[3000,50],[['d',100]],["You're not gonna get past me","like all those other bastards","did!"],["I don't think I can do this","any longer...", ""],True,[0,50,0,0],[poke.Poke('Mightyena',[19,random.randint(0,1),787,"Tackle",-1,"Sand Attack",-1,"Bite",-1,"Swagger",-1,None,None,0,"Ultra Ball",100,"Intimidate"]),poke.Poke('Furret',[19,random.randint(0,1),787,"Focus Energy",-1,"Fury Swipes",-1,"Quick Attack",-1,"Agility",-1,None,None,0,"Ultra Ball",100,"Keen Eye"]),poke.Poke('Murkrow',[19,random.randint(0,1),787,"Wing Attack",-1,"Haze",-1,"Pursuit",-1,"Astonish",-1,None,None,0,"Ultra Ball",100,"Super Luck"]),poke.Poke('Lombre',[20,random.randint(0,1),787,"Mega Drain",-1,"Mist",-1,"Bubble",-1,"Natural Gift",-1,None,None,0,"Ultra Ball",150,"Rain Dish"]),poke.Poke('Pinsir',[20,random.randint(0,1),787,"Vital Throw",-1,"Revenge",-1,"Seismic Toss",-1,"Bind",-1,None,None,0,"Ultra Ball",100,"Hyper Cutter"])],20,loc = "scarab_r")
        else:
            self.sr_ace = npc.NPC(self,'Ace Trainerm','James',[3000,50],[['d',100]],["That green haired guy was so","cool though! I mean he beat me","pretty badly, but still!","I want to be just like that","when I grow up! Super strong","and in charge of people!"],loc = "scarab_r")
        if self.prog[5][21] == 0:
            self.r3_battle = npc.NPC(self,'Battle Girl','Harper',[5900,200],[['mr',80],['r',100],['ml',80],['l',60]],["I've been training here all", "day! I'm so warmed up, you'll","never stand a chance!"],["*Huff* *Puff*","Maybe I'm a little too", "exhausted for this..."],True,[0,0,200,100],[poke.Poke('Machop',[21,random.randint(0,1),787,"Low Sweep",-1,"Seismic Toss",-1,"Revenge",-1,"Knock Off",-1,None,None,0,"Poke Ball",150,"Guts"]),poke.Poke('Nuzleaf',[21,random.randint(0,1),787,"Torment",-1,"Razor Leaf",-1,"Fake Out",-1,"Razor Wind",-1,None,None,0,"Poke Ball",200,"Early Bird"]),poke.Poke('Zangoose',[21,random.randint(0,1),787,"Hone Claws",-1,"Quick Attack",-1,"Pursuit",-1,"Slash",-1,None,None,0,"Poke Ball",120,"Immunity"])],21,loc = "route_3")
        else:
            self.r3_battle = npc.NPC(self,'Battle Girl','Harper',[5900,200],[['mr',80],['r',100],['ml',80],['l',60]],["I can't remember if I turned","off the oven before I left...",""],loc = "route_3")
        #just pokemon
        self.r3_fishteam = [poke.Poke('Magikarp',[19,random.randint(0,1),787,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[20,random.randint(0,1),787,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[21,random.randint(0,1),787,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[22,random.randint(0,1),787,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[23,random.randint(0,1),787,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",400,"Swift Swim"]),poke.Poke('Gyarados',[24,random.randint(0,1),787,"Bite",-1,"Leer",-1,"Twister",-1,"Taunt",-1,None,None,0,"Net Ball",100,"Intimidate"])]
        self.r3_fishteam2 = [poke.Poke('Shellder',[22,random.randint(0,1),787,"Icicle Spear",-1,"Withdraw",-1,"Protect",-1,"Water Gun",-1,None,None,0,"Poke Ball",100,"Skill Link"]),poke.Poke('Krabby',[23,random.randint(0,1),787,"Metal Claw",-1,"Mud Shot",-1,"Bubble Beam",-1,"Vice Grip",-1,None,None,0,"Poke Ball",150,"Hyper Cutter"]),poke.Poke('Psyduck',[24,random.randint(0,1),787,"Screech",-1,"Confusion",-1,"Water Pulse",-1,"Disable",-1,None,None,0,"Poke Ball",150,"Cloud Nine"])]
        self.r3_triteam = [poke.Poke('Ponyta',[23,random.randint(0,1),787,"Flame Charge",-1,"Stomp",-1,"Flame Wheel",-1,"Tail Whip",-1,None,None,0,"Poke Ball",150,"Flash Fire"]),poke.Poke('Pidgeotto',[23,random.randint(0,1),787,"Twister",-1,"Quick Attack",-1,"Gust",-1,"Whirlwind",-1,None,None,0,"Poke Ball",250,"Tangled Feet"]),poke.Poke('Seviper',[23,random.randint(0,1),787,"Poison Fang",-1,"Glare",-1,"Screech",-1,"Wrap",-1,None,None,0,"Poke Ball",150,"Shed Skin"])]
        self.piag_team1 = [poke.Poke('Jigglypuff',[25,random.randint(0,1),787,"Disarming Voice",-1,"Stockpile",-1,"Swallow",-1,"Spit Up",-1,None,None,0,"Poke Ball",350,"Cute Charm"]),poke.Poke('Lopunny',[25,random.randint(0,1),787,"Jump Kick",-1,"Quick Attack",-1,"Baby-Doll Eyes",-1,"Foresight",-1,None,None,0,"Poke Ball",250,"Cute Charm"])]
        self.piag_team2 = [poke.Poke('Loudred',[25,random.randint(0,1),787,"Screech",-1,"Stomp",-1,"Bite",-1,"Echoed Voice",-1,None,None,0,"Poke Ball",200,"Soundproof"]),poke.Poke('Zangoose',[25,random.randint(0,1),787,"Revenge",-1,"Slash",-1,"Hone Claws",-1,"Quick Attack",-1,None,None,0,"Poke Ball",150,"Immunity"])]
        self.piag_team3 = [poke.Poke('Dunsparce',[24,random.randint(0,1),787,"Drill Run",-1,"Ancient Power",-1,"Yawn",-1,"Mud-Slap",-1,None,None,0,"Poke Ball",100,"Serene Grace"]),poke.Poke('Pidgeotto',[24,random.randint(0,1),787,"Twister",-1,"Quick Attack",-1,"Gust",-1,"Whirlwind",-1,None,None,0,"Poke Ball",300,"Keen Eye"]),poke.Poke('Noctowl',[25,random.randint(0,1),787,"Extrasensory",-1,"Psycho Shift",-1,"Echoed Voice",-1,"Hypnosis",-1,None,None,0,"Poke Ball",150,"Insomnia"])]
        self.piag_team4 = [poke.Poke('Happiny',[25,random.randint(0,1),787,"Pound",-1,"Charm",-1,"Sweet Kiss",-1,"Refresh",-1,None,None,0,"Poke Ball",400,"Natural Cure"]),poke.Poke('Azurill',[25,random.randint(0,1),787,"Bounce",-1,"Slam",-1,"Bubble Beam",-1,"Charm",-1,None,None,0,"Poke Ball",400,"Huge Power"]),poke.Poke('Igglybuff',[25,random.randint(0,1),787,"Sing",-1,"Charm",-1,"Pound",-1,"Sweet Kiss",-1,None,None,0,"Poke Ball",400,"Cute Charm"]),poke.Poke('Munchlax',[25,random.randint(0,1),787,"Screech",-1,"Body Slam",-1,"Amnesia",-1,"Lick",-1,None,None,0,"Poke Ball",400,"Thick Fat"])]
        if self.prog[5][29] == 0:
            self.mc_hex = npc.NPC(self,'Hex Maniac','Scarlett',[2250,250],[['md',80],['d',100],['mr',80],['r',60],['ml',80],['l',60],['mu',80],['u',60]],["It's cold. It's dark. You see", "creepy reflections of yourself","everywhere!","I love this place!","",""],["Spooking trainers that walk in","here is pretty fun too!", ""],True,[150,150,150,150],[poke.Poke('Misdreavus',[26,random.randint(0,1),787,"Hex",-1,"Confuse Ray",-1,"Toxic",-1,"Mean Look",-1,None,None,300,"Poke Ball",120,"Levitate"]),poke.Poke('Mightyena',[27,random.randint(0,1),787,"Swagger",-1,"Snarl",-1,"Fire Fang",-1,"Thunder Fang",-1,None,None,0,"Poke Ball",200,"Intimidate"]),poke.Poke('Hypno',[28,random.randint(0,1),787,"Psybeam",-1,"Poison Gas",-1,"Hypnosis",-1,"Nightmare",-1,None,None,0,"Poke Ball",200,"Insomnia"])],29,loc = "mirror_cave")
        else:
            self.mc_hex = npc.NPC(self,'Hex Maniac','Harper',[2250,250],[['md',80],['d',100],['mr',80],['r',60],['ml',80],['l',60],['mu',80],['u',60]],["Sometimes I like to think that","there's a Pokemon hiding","inside these mirrors!"],loc = "mirror_cave")
        if self.prog[5][30] == 0:
            self.mc_hiker = npc.NPC(self,'Hiker','Ben',[2600,-600],[['mr',120],['r',100],['ml',120],['l',80]],["I only took a quick peek in", "here, and now I've lost the","entrance!","I need something to help me","deal with this stress!",""],["Well that wasn't very stress","relieving...",""],True,[0,0,150,150],[poke.Poke('Geodude',[28,random.randint(0,1),787,"Self-Destruct",-1,"Magnitude",-1,"Smack Down",-1,"Stealth Rock",-1,None,None,0,"Poke Ball",200,"Sturdy"]),poke.Poke('Onix',[28,random.randint(0,1),787,"Slam",-1,"Smack Down",-1,"Gyro Ball",-1,"Curse",-1,None,None,200,"Poke Ball",120,"Sturdy"]),poke.Poke('Sudowoodo',[28,random.randint(0,1),787,"Rock Tomb",-1,"Low Kick",-1,"Slam",-1,"Flail",-1,None,None,0,"Poke Ball",300,"Sturdy"])],30,loc = "mirror_cave")
        else:
            self.mc_hiker = npc.NPC(self,'Hiker','Harper',[2600,-600],[['mr',120],['r',100],['ml',120],['l',80]],["Now that I think about it,","maybe it's not all that bad in","here...","Now I don't have to deal with","the stress of life!",""],loc = "mirror_cave")
        if self.prog[5][31] == 0:
            self.r4_expert = npc.NPC(self,'Expertm','Owen',[700,350],[['mr',100],['r',120],['ml',100],['l',100]],["If you've come all the way out", "here, you must be a developing","trainer!","Allow me to help you refine","your Pokemon!",""],["Hmm...perhaps you're the one","refining my Pokemon...",""],True,[0,0,150,150],[poke.Poke('Machoke',[31,random.randint(0,1),787,"Wake-Up Slap",-1,"Knock Off",-1,"Seismic Toss",-1,"Focus Energy",-1,None,None,0,"Poke Ball",300,"Guts"]),poke.Poke('Hitmonlee',[31,random.randint(0,1),787,"High Jump Kick",-1,"Focus Energy",-1,"Rolling Kick",-1,"Mega Kick",-1,None,None,0,"Poke Ball",300,"Reckless"])],31,loc = "route_4")
        else:
            self.r4_expert = npc.NPC(self,'Expertm','Harper',[700,350],[['mr',100],['r',120],['ml',100],['l',100]],["If you're looking for a place","to rest, keep heading east to","reach Isola Town!"],loc = "route_4")
        if self.prog[5][32] == 0:
            self.r4_battle = npc.NPC(self,'Battle Girl','Lily',[2150,100],[['l',80]],["I'm going to demolish this", "rock right after I've finished","demolishing you!"],["How am I supposed to crack","open this rock if I can't even","beat you?"],True,[0,0,0,0],[poke.Poke('Gurdurr',[32,random.randint(0,1),787,"Rock Throw",-1,"Chip Away",-1,"Wake-Up Slap",-1,"Bulk Up",-1,None,None,0,"Poke Ball",300,"Guts"]),poke.Poke('Hitmonchan',[32,random.randint(0,1),787,"Vacuum Wave",-1,"Bullet Punch",-1,"Mach Punch",-1,"Revenge",-1,None,None,0,"Poke Ball",400,"Iron Fist"])],32,loc = "route_4")
        else:
            self.r4_battle = npc.NPC(self,'Battle Girl','Harper',[2150,100],[['l',80]],["Considering how long I've been","swinging at this rock, I'm","sure I'll break it someday."],loc = "route_4")
        if self.prog[5][33] == 0:
            self.r4_fish = npc.NPC(self,'Fisherman','Richard',[2600,700],[['r',80]],["You know what shellfish are", "great for?","","Beating down all the trainers","passing by!",""],["Huh, I guess you proved me","wrong today!",""],True,[0,0,0,0],[poke.Poke('Kingler',[30,random.randint(0,1),787,"Stomp",-1,"Metal Claw",-1,"Mud Shot",-1,"Bubble Beam",-1,None,None,0,"Poke Ball",300,"Shell Armor"]),poke.Poke('Crawdaunt',[30,random.randint(0,1),787,"Night Slash",-1,"Bubble Beam",-1,"Protect",-1,"Double Hit",-1,None,None,0,"Poke Ball",300,"Shell Armor"]),poke.Poke('Cloyster',[32,random.randint(0,1),787,"Shell Smash",-1,"Ice Shard",-1,"Clamp",-1,"Razor Shell",-1,None,None,0,"Poke Ball",300,"Shell Armor"])],33,loc = "route_4")
        else:
            self.r4_fish = npc.NPC(self,'Fisherman','Harper',[2600,700],[['r',80]],["Well shellfish are great for","lots of other things!","","Like eating and stuff, you","know?",""],loc = "route_4")
        self.r4_expf_train = npc.NPC(self,'Expertf','Stella',[1500,1200],[['l',80]],["Hello there! Not many people","choose to venture all the way","out here.","Perhaps you're looking for a","thrilling battle?",""],["Well that's quite surprising!","I suppose each new generation","really is more talented!"],True,[0,0,0,0],[poke.Poke('Ferrothorn',[40,random.randint(0,1),787,"Pin Missile",-1,"Iron Defense",-1,"Gyro Ball",-1,"Curse",-1,'Metal Coat',None,0,"Luxury Ball",400,"Iron Barbs"]),poke.Poke('Scizor',[40,random.randint(0,1),787,"Quick Attack",-1,"Iron Defense",-1,"Bullet Punch",-1,"Pursuit",-1,'Metal Coat',None,0,"Luxury Ball",400,"Technician"]),poke.Poke('Steelix',[40,random.randint(0,1),787,"Thunder Fang",-1,"Rock Slide",-1,"Crunch",-1,"Iron Tail",-1,'Metal Coat',None,0,"Luxury Ball",400,"Sturdy"])],34,loc = "route_4")
        if self.prog[5][35] == 0:
            self.r5_psy = npc.NPC(self,'Psychic','Lucas',[600,-300],[['mr',40],['r',60],['md',40],['d',80],['ml',40],['l',100],['mu',40],['u',60]],["You better watch out or you'll", "end up hitting yourself!",""],["Hmm, looks like I should have","been watching out myself!",""],True,[150,150,150,150],[poke.Poke('Mismagius',[34,random.randint(0,1),787,"Confuse Ray",-1,"Pain Split",-1,"Mystical Fire",-1,"Shadow Ball",-1,None,None,0,"Poke Ball",350,"Levitate"]),poke.Poke('Wobbuffet',[35,random.randint(0,1),787,"Counter",-1,"Mirror Coat",-1,None,None,None,None,None,None,0,"Poke Ball",400,"Shadow Tag"])],35,loc = "route_5")
        else:
            self.r5_psy = npc.NPC(self,'Psychic','Lucas',[600,-300],[['mr',40],['r',60],['md',40],['d',80],['ml',40],['l',100],['mu',40],['u',60]],["I'm just keeping you on your","toes! You never know what can", "happen in a Pokemon battle!"],loc = "route_5")
        if self.prog[5][36] == 0:
            self.r5_bug = npc.NPC(self,'Bug Catcher','Oliver',[1800,-450],[['mr',80],['r',120],['ml',80],['l',80]],["Woah!!!", "This one's gigantic!!!",""],["Wait, you're not a Pokemon...","",""],True,[0,0,150,150],[poke.Poke('Joltik',[32,random.randint(0,1),787,"Spider Web",-1,"Thunder Wave",-1,"Screech",-1,"Electroweb",-1,None,None,0,"Poke Ball",400,"Unnerve"]),poke.Poke('Joltik',[32,random.randint(0,1),787,"Agility",-1,"Slash",-1,"Electro Ball",-1,"Bug Bite",-1,None,None,0,"Poke Ball",400,"Compound Eyes"]),poke.Poke('Spinarak',[32,random.randint(0,1),787,"Infestation",-1,"Night Shade",-1,"Shadow Sneak",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",400,"Swarm"]),poke.Poke('Ariados',[34,random.randint(0,1),787,"Fell Stinger",-1,"Swords Dance",-1,"Shadow Sneak",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",300,"Swarm"])],36,loc = "route_5")
        else:
            self.r5_bug = npc.NPC(self,'Bug Catcher','Oliver',[1800,-450],[['mr',80],['r',120],['ml',80],['l',80]],["Sorry about that! You're just","kinda funny looking, so I", "mistook you for a Pokemon!"],loc = "route_5")
        if self.prog[5][37] == 0:
            self.r5_lass = npc.NPC(self,'Lass','Emma',[1900,400],[['mr',80],['r',40],['ml',80],['l',60],['md',40],['d',120],['mu',40],['u',40]],["Hey! Come here and play with", "my Pokemon!",""],["Hehe, that was pretty fun","wasn't it?",""],True,[100,100,100,100],[poke.Poke('Vulpix',[32,random.randint(0,1),787,"Hex",-1,"Will-O-Wisp",-1,"Flame Burst",-1,"Extrasensory",-1,None,None,0,"Poke Ball",400,"Flash Fire"]),poke.Poke('Furret',[33,random.randint(0,1),787,"Quick Attack",-1,"Coil",-1,"Slam",-1,"Rest",-1,None,None,0,"Poke Ball",300,"Keen Eye"]),poke.Poke('Floatzel',[34,random.randint(0,1),787,"Aqua Jet",-1,"Ice Fang",-1,"Double Hit",-1,"Quick Attack",-1,None,None,0,"Poke Ball",300,"Swift Swim"])],37,loc = "route_5")
        else:
            self.r5_lass = npc.NPC(self,'Lass','Emma',[1900,400],[['mr',80],['r',40],['ml',80],['l',60],['md',40],['d',120],['mu',40],['u',40]],["We should play again sometime!","It's boring running around all","by myself!"],loc = "route_5")
        if self.prog[5][38] == 0:
            self.r5_beauty = npc.NPC(self,'Beauty','Aria',[1000,500],[['d',80]],["I'm dying to go for a swim!", "You should come join us!",""],["Actually I take that back.","You take things waaay too","seriously!"],True,[0,50,0,0],[poke.Poke('Bellossom',[34,random.randint(0,1),787,"Sunny Day",-1,"Stun Spore",-1,"Magical Leaf",-1,"Moonlight",-1,None,None,0,"Poke Ball",300,"Chlorophyll"]),poke.Poke('Roserade',[34,random.randint(0,1),787,"Venom Drench",-1,"Giga Drain",-1,"Magical Leaf",-1,"Grass Whistle",-1,None,None,0,"Poke Ball",300,"Poison Point"])],38,loc = "route_5")
        else:
            self.r5_beauty = npc.NPC(self,'Beauty','Aria',[1000,500],[['d',80]],["You could have held back","just a little, you know?", ""],loc = "route_5")
        self.verde_gym_pot0team = [poke.Poke('Cottonee',[34,random.randint(0,1),787,"Leech Seed",-1,"Poison Powder",-1,"Endeavor",-1,"Charm",-1,None,None,0,"Poke Ball",300,"Prankster"]),poke.Poke('Roselia',[34,random.randint(0,1),787,"Magical Leaf",-1,"Grass Whistle",-1,"Giga Drain",-1,"Toxic Spikes",-1,None,None,0,"Poke Ball",400,"Poison Point"]),poke.Poke('Maractus',[35,random.randint(0,1),787,"Needle Arm",-1,"Spiky Shield",-1,"Giga Drain",-1,"Acupressure",-1,None,None,0,"Poke Ball",400,"Water Absorb"])]
        self.verde_gym_pot1team = [poke.Poke('Phantump',[34,random.randint(0,1),787,"Confuse Ray",-1,"Leech Seed",-1,"Curse",-1,"Will-O-Wisp",-1,None,None,0,"Poke Ball",400,"Natural Cure"]),poke.Poke('Amoonguss',[34,random.randint(0,1),787,"Feint Attack",-1,"Ingrain",-1,"Giga Drain",-1,"Toxic",-1,None,None,0,"Poke Ball",300,"Effect Spore"]),poke.Poke('Shiftry',[35,random.randint(0,1),787,"Fake Out",-1,"Nasty Plot",-1,"Leaf Tornado",-1,"Hurricane",-1,None,None,0,"Poke Ball",300,"Chlorophyll"])]
        self.verde_gym_pot2team = [poke.Poke('Lombre',[35,random.randint(0,1),787,"Giga Drain",-1,"Fake Out",-1,"Bubble Beam",-1,"Uproar",-1,None,None,0,"Poke Ball",400,"Rain Dish"]),poke.Poke('Victreebel',[35,random.randint(0,1),787,"Knock Off",-1,"Swallow",-1,"Stockpile",-1,"Leaf Storm",-1,None,None,0,"Poke Ball",400,"Chlorophyll"])]
        self.verde_gym_pot3team = [poke.Poke('Seedot',[35,random.randint(0,1),787,"Sunny Day",-1,"Nature Power",-1,"Synthesis",-1,"Explosion",-1,"Eviolite",None,0,"Poke Ball",400,"Early Bird"]),poke.Poke('Oddish',[35,random.randint(0,1),787,"Sleep Powder",-1,"Moonlight",-1,"Giga Drain",-1,"Toxic",-1,"Eviolite",None,0,"Poke Ball",400,"Chlorophyll"]),poke.Poke('Budew',[35,random.randint(0,1),787,"Growth",-1,"Stun Spore",-1,"Mega Drain",-1,"Worry Seed",-1,"Eviolite",None,0,"Poke Ball",400,"Poison Point"]),poke.Poke('Lotad',[35,random.randint(0,1),787,"Bubble Beam",-1,"Rain Dance",-1,"Giga Drain",-1,"Zen Headbutt",-1,"Eviolite",None,0,"Poke Ball",400,"Swift Swim"]),poke.Poke('Cottonee',[35,random.randint(0,1),787,"Energy Ball",-1,"Giga Drain",-1,"Charm",-1,"Stun Spore",-1,"Eviolite",None,0,"Poke Ball",400,"Effect Spore"]),poke.Poke('Foongus',[35,random.randint(0,1),787,"Bide",-1,"Giga Drain",-1,"Synthesis",-1,"Toxic",-1,"Eviolite",None,0,"Poke Ball",400,"Effect Spore"])]
        self.verde_gym_pot4team = [poke.Poke('Sewaddle',[34,random.randint(0,1),787,"Sticky Web",-1,"String Shot",-1,"Struggle Bug",-1,"Razor Leaf",-1,None,None,0,"Poke Ball",400,"Chlorophyll"]),poke.Poke('Sewaddle',[34,random.randint(0,1),787,"Endure",-1,"String Shot",-1,"Struggle Bug",-1,"Razor Leaf",-1,None,None,0,"Poke Ball",400,"Swarm"]),poke.Poke('Swadloon',[35,random.randint(0,1),787,"Grass Whistle",-1,"Protect",-1,"Bug Bite",-1,"Razor Leaf",-1,None,None,0,"Poke Ball",400,"Leaf Guard"])]
        self.verde_gym_pot5team = [poke.Poke('Chespin',[34,random.randint(0,1),787,"Leech Seed",-1,"Bite",-1,"Take Down",-1,"Seed Bomb",-1,None,None,0,"Poke Ball",400,"Overgrow"]),poke.Poke('Gloom',[34,random.randint(0,1),787,"Poison Powder",-1,"Sleep Powder",-1,"Moonlight",-1,"Giga Drain",-1,None,None,0,"Poke Ball",300,"Chlorophyll"]),poke.Poke('Bellossom',[35,random.randint(0,1),787,"Magical Leaf",-1,"Growth",-1,"Sunny Day",-1,"Solar Beam",-1,None,None,0,"Poke Ball",400,"Chlorophyll"])]
        self.verde_gym_pot6team = [poke.Poke('Bulbasaur',[34,random.randint(0,1),787,"Razor Leaf",-1,"Synthesis",-1,"Worry Seed",-1,"Double-Edge",-1,None,None,400,"Poke Ball",300,"Overgrow"]),poke.Poke('Gloom',[34,random.randint(0,1),787,"Poison Powder",-1,"Sleep Powder",-1,"Moonlight",-1,"Giga Drain",-1,None,None,0,"Poke Ball",300,"Chlorophyll"]),poke.Poke('Vileplume',[35,random.randint(0,1),787,"Poison Powder",-1,"Moonlight",-1,"Aromatherapy",-1,"Giga Drain",-1,None,None,0,"Poke Ball",400,"Chlorophyll"])]
        if self.prog[5][46] == 0:
            self.ff1_psy = npc.NPC(self,'Psychic','Herbert',[900,750],[['mr',20],['r',120],['ml',20],['l',100]],["You must be a brave adventurer", "to be wandering in here on","your own.","Or are you also part of that","impudent group that marched","their way in here?"],["Your strength is commendable.","May the spirit's blessings be","with you."],True,[0,0,100,100],[poke.Poke('Hypno',[34,random.randint(0,1),787,"Hypnosis",-1,"Meditate",-1,"Psybeam",-1,"Wake-Up Slap",-1,None,None,0,"Poke Ball",300,"Insomnia"]),poke.Poke('Mr Mime',[34,random.randint(0,1),787,"Magical Leaf",-1,"Reflect",-1,"Light Screen",-1,"Psybeam",-1,None,None,0,"Poke Ball",400,"Filter"]),poke.Poke('Kadabra',[34,random.randint(0,1),787,"Psybeam",-1,"Disable",-1,"Recover",-1,"Psycho Cut",-1,None,None,0,"Poke Ball",300,"Synchronize"])],46,loc = "forbidden_1")
        else:
            self.ff1_psy = npc.NPC(self,'Psychic','Herbert',[900,750],[['mr',20],['r',120],['ml',20],['l',100]],["There was a large gang that","walked through here a couple","moments ago.","I'm not quite sure what they","were up to, but they seemed","to have ill intentions."],loc = "forbidden_1")
        if self.prog[5][47] == 0:
            self.ff2_rock1 = npc.NPC(self,'Team Rocketf','Grunt',[600,1100],[['d',40],['l',80],['r',60],['u',80]],["Ahh! There you are! I've been", "looking everywhere for you!","","Wait, who are you?","",""],["Are you going to leave me all","alone out here too?",""],True,[100,100,100,100],[poke.Poke('Ariados',[35,random.randint(0,1),787,"Fell Stinger",-1,"Swords Dance",-1,"Sucker Punch",-1,"Spider Web",-1,None,None,0,"Poke Ball",0,"Swarm"],petals=['spd','spd','spd']),poke.Poke('Seviper',[36,random.randint(0,1),787,"Glare",-1,"Night Slash",-1,"Poison Jab",-1,"Swords Dance",-1,None,None,0,"Poke Ball",0,"Shed Skin"],petals=['ak','ak','ak'])],47,loc = "forbidden_2")
        else:
            self.ff2_rock1 = npc.NPC(self,'Team Rocketf','Grunt',[600,1100],[['d',40],['l',80],['r',60],['u',80]],["Go ahead! Leave me to fend for","myself! See if I care!", ""],loc = "forbidden_2")
        if self.prog[5][48] == 0:
            self.ff2_rock2 = npc.NPC(self,'Team Rocketm','Grunt',[1300,700],[['mr',40],['r',120],['ml',40],['l',100]],["Am I going the right way?", "You better tell me, or I'm","gonna beat it out of you!"],["Man, why do we keep having","meetings in the middle of","these stupid forests?","My heart can't take this","anymore!",""],True,[0,0,100,100],[poke.Poke('Mightyena',[35,random.randint(0,1),787,"Fire Fang",-1,"Ice Fang",-1,"Thunder Fang",-1,"Swagger",-1,None,None,0,"Poke Ball",0,"Intimidate"],petals=['hp','hp','hp']),poke.Poke('Zangoose',[36,random.randint(0,1),787,"Pursuit",-1,"Revenge",-1,"Crush Claw",-1,"Detect",-1,None,None,0,"Poke Ball",0,"Immunity"],petals=['ak','ak','ak'])],48,loc = "forbidden_2")
        else:
            self.ff2_rock2 = npc.NPC(self,'Team Rocketm','Grunt',[1300,700],[['mr',40],['r',120],['ml',40],['l',100]],["Have you seen my partner","anywhere? She looks exactly", "like me!","Well, I mean she's dressed","exactly like me!",""],loc = "forbidden_2")
        if self.prog[5][49] == 0:
            self.ff3_rock1 = npc.NPC(self,'Team Rocketm','Grunt',[500,1000],[['l',20]],["Ahh! Stay away from me!","",""],["Can't you just leave me alone?","I've got enough problems to","deal with here!"],True,[0,0,0,0],[poke.Poke('Dusclops',[36,random.randint(0,1),787,"Will-O-Wisp",-1,"Curse",-1,"Confuse Ray",-1,"Shadow Punch",-1,None,None,0,"Poke Ball",0,"Pressure"],petals=['hp','hp','hp']),poke.Poke('Golbat',[36,random.randint(0,1),787,"Confuse Ray",-1,"Air Cutter",-1,"Poison Fang",-1,"Leech Life",-1,None,None,0,"Poke Ball",0,"Inner Focus"],petals=['ak','ak','ak']),poke.Poke('Victreebel',[37,random.randint(0,1),787,"Stockpile",-1,"Spit Up",-1,"Swallow",-1,"Leaf Storm",-1,None,None,0,"Poke Ball",0,"Chlorophyll"],petals=['spd','spd','spd'])],49,loc = "forbidden_3")
        else:
            self.ff3_rock1 = npc.NPC(self,'Team Rocketm','Grunt',[500,1000],[['l',20]],["You're heartless! What do you", "not get about leaving someone", "alone?"],loc = "forbidden_3")
        if self.prog[5][50] == 0:
            self.ff4_hex = npc.NPC(self,'Hex Maniac','Isabella',[1250,700],[['d',20]],["You dare disrupt my sacred","domain? You'll pay dearly for","this offense!"],["You're a lot stronger than I","anticipated. You may come and","go as you please."],True,[0,50,0,0],[poke.Poke('Golett',[36,2,787,"Magnitude",-1,"Mega Punch",-1,"Dynamic Punch",-1,"Shadow Punch",-1,None,None,0,"Poke Ball",400,"Iron Fist"]),poke.Poke('Spiritomb',[36,random.randint(0,1),787,"Shadow Sneak",-1,"Dream Eater",-1,"Hypnosis",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",300,"Pressure"]),poke.Poke('Haunter',[38,random.randint(0,1),787,"Curse",-1,"Sucker Punch",-1,"Payback",-1,"Shadow Ball",-1,None,None,0,"Poke Ball",300,"Levitate"])],50,loc = "forbidden_4")
        else:
            self.ff4_hex = npc.NPC(self,'Hex Maniac','Isabella',[1250,700],[['d',20]],["I am no longer protected from", "the outside world by my", "fortress of trees.","It makes me feel so exposed,","and it's all your fault!",""],loc = "forbidden_4")
        if self.prog[5][51] == 0:
            self.ff6_sci = npc.NPC(self,'Scientistf','Olivia',[1150,950],[['u',20]],["Eep! A ghost!!!","",""],["Oh, you're just a trainer.","You gave me a real jump scare","there!"],True,[0,0,0,0],[poke.Poke('Togedemaru',[38,random.randint(0,1),787,"Electric Terrain",-1,"Zing Zap",-1,"Nuzzle",-1,"Protect",-1,None,None,0,"Poke Ball",400,"Iron Barbs"]),poke.Poke('Electrode',[39,2,787,"Light Screen",-1,"Eerie Impulse",-1,"Electro Ball",-1,"Self-Destruct",-1,None,None,0,"Poke Ball",300,"Static"]),poke.Poke('Klinklang',[40,2,787,"Screech",-1,"Autotomize",-1,"Charge Beam",-1,"Gear Grind",-1,None,None,0,"Poke Ball",300,"Plus"])],51,loc = "forbidden_6")
        else:
            self.ff6_sci = npc.NPC(self,'Scientistf','Olivia',[1150,950],[['u',20]],["We rolled dice to distribute", "our research locations.", "","Guess who rolled a one?","",""],loc = "forbidden_6")
        if self.prog[5][52] == 0:
            self.ff8_psy = npc.NPC(self,'Psychic','Eli',[1200,950],[['l',200],['u',150]],["You think you can stand up to","me? I'll make you reconsider","that decision!"],["Wow! I don't remember the last","time I ran into a trainer as","strong as you around here!"],True,[0,0,0,0],[poke.Poke('Mega_Gengar',[50,random.randint(0,1),787,"Shadow Ball",-1,"Dark Pulse",-1,"Dream Eater",-1,"Hypnosis",-1,None,None,0,"Poke Ball",200,"Shadow Tag"]),poke.Poke('Mega_Alakazam',[50,random.randint(0,1),787,"Psychic",-1,"Recover",-1,"Reflect",-1,"Focus Blast",-1,None,None,0,"Poke Ball",200,"Trace"]),poke.Poke('Dusknoir',[52,random.randint(0,1),787,"Shadow Punch",-1,"Ice Punch",-1,"Fire Punch",-1,"Thunder Punch",-1,None,None,0,"Poke Ball",400,"Pressure"],petals=['ak','ak','ak','spd','spd'])],52,loc = "forbidden_8")
        else:
            self.ff8_psy = npc.NPC(self,'Psychic','Eli',[1200,950],[['l',200],['u',150]],["You had better keep your","focus, or your skills will","start to deteriorate.","And it would be embarassing if","I lost to a slacker!",""],loc = "forbidden_8")
        if self.prog[5][53] == 0:
            self.r6_bug = npc.NPC(self,'Bug Catcher','Ian',[2650,4250],[['md',40],['d',150],['mr',100],['r',100],['mu',40],['u',120],['ml',100],['l',80]],["Hey, this is my territory!","Go find your own patch of", "grass to sneak around in!"],["Just stay outta my way, will","you? You're scaring all the", "Pokemon away!"],True,[100,100,100,100],[poke.Poke('Galvantula',[42,1,787,"Electro Ball",-1,"Signal Beam",-1,"Sticky Web",-1,"Thunder Wave",-1,None,None,0,"Poke Ball",200,"Compound Eyes"],petals=['spd','spd','spd']),poke.Poke('Crustle',[42,0,787,"Stealth Rock",-1,"X-Scissor",-1,"Shell Smash",-1,"Rock Slide",-1,None,None,0,"Poke Ball",300,"Shell Armor"],petals=['hp','hp','hp']),poke.Poke('Leavanny',[43,1,787,"Entrainment",-1,"Grass Whistle",-1,"Leaf Blade",-1,"X-Scissor",-1,None,None,0,"Poke Ball",400,"Swarm"],petals=['ak','ak','ak'])],53,loc = "route_6")
        else:
            self.r6_bug = npc.NPC(self,'Bug Catcher','Ian',[2650,4250],[['md',40],['d',150],['mr',100],['r',100],['mu',40],['u',120],['ml',100],['l',80]],["Hey, didn't I tell you not to","get in my way?","","Now you're just trying to rile","me up, aren't you?",""],loc = "route_6")
        self.casg_team1 = [poke.Poke('Kingler',[43,1,787,"Mud Shot",-1,"Metal Claw",-1,"Bubble Beam",-1,"Guillotine",-1,None,None,0,"Poke Ball",200,"Hyper Cutter"]),poke.Poke('Ludicolo',[43,0,787,"Zen Headbutt",-1,"Bubble Beam",-1,"Mega Drain",-1,"Knock Off",-1,None,None,0,"Poke Ball",200,"Swift Swim"]),poke.Poke('Floatzel',[44,0,787,"Ice Fang",-1,"Crunch",-1,"Aqua Jet",-1,"Double Hit",-1,None,None,0,"Poke Ball",400,"Swift Swim"])]
        self.casg_team2 = [poke.Poke('Starmie',[43,0,787,"Psychic",-1,"Brine",-1,"Minimize",-1,"Confuse Ray",-1,None,None,0,"Poke Ball",0,"Natural Cure"],petals=['hp','hp','hp']),poke.Poke('Crawdaunt',[44,1,787,"Crunch",-1,"Swords Dance",-1,"Razor Shell",-1,"Protect",-1,None,None,0,"Poke Ball",0,"Hyper Cutter"],petals=['ak','ak','ak']),poke.Poke('Golduck',[44,0,787,"Zen Headbutt",-1,"Aqua Tail",-1,"Screech",-1,"Amnesia",-1,None,None,0,"Poke Ball",0,"Damp"],petals=['spd','spd','spd'])]
        self.casg_team3 = [poke.Poke('Tentacruel',[45,1,787,"Toxic Spikes",-1,"Poison Jab",-1,"Brine",-1,"Barrier",-1,None,None,0,"Poke Ball",200,"Liquid Ooze"]),poke.Poke('Gyarados',[45,0,787,"Dragon Dance",-1,"Crunch",-1,"Ice Fang",-1,"Hydro Pump",-1,None,None,0,"Poke Ball",200,"Intimidate"])]
        self.casg_team4 = [poke.Poke('Huntail',[44,0,787,"Aqua Tail",-1,"Crunch",-1,"Ice Fang",-1,"Screech",-1,None,None,0,"Ultra Ball",300,"Swift Swim"]),poke.Poke('Barbaracle',[44,0,787,"Night Slash",-1,"Hone Claws",-1,"Stone Edge",-1,"Rock Polish",-1,None,None,0,"Ultra Ball",400,"Tough Claws"]),poke.Poke('Jellicent_M',[45,0,787,"Night Shade",-1,"Recover",-1,"Ominous Wind",-1,"Water Pulse",-1,None,None,0,"Ultra Ball",300,"Water Absorb"])]
        self.casg_team5 = [poke.Poke('Gorebyss',[44,0,787,"Aqua Tail",-1,"Crunch",-1,"Ice Fang",-1,"Screech",-1,None,None,0,"Ultra Ball",300,"Swift Swim"]),poke.Poke('Vaporeon',[44,0,787,"Muddy Water",-1,"Aurora Beam",-1,"Acid Armor",-1,"Haze",-1,None,None,0,"Ultra Ball",400,"Water Absorb"]),poke.Poke('Jellicent_F',[45,0,787,"Night Shade",-1,"Recover",-1,"Ominous Wind",-1,"Water Pulse",-1,None,None,0,"Ultra Ball",300,"Water Absorb"])]
        if self.prog[5][60] == 0:
            self.sunken_pre = npc.NPC(self,'Preschoolerg','Lucy',[1300,800],[['md',40],['mr',70],['mu',70],['ml',20],['md',30],['ml',50]],["Hee hee! My shoes are all wet","and muddy! My mom's going to", "yell at me again!"],["You should run around too!","It's so much fun!", ""],True,[100,100,100,100],[poke.Poke('Clefairy',[45,1,787,"Moonlight",-1,"Metronome",-1,None,None,None,None,None,None,0,"Poke Ball",300,"Cute Charm"],petals=['spd','spd','spd']),poke.Poke('Jigglypuff',[45,0,787,"Hyper Voice",-1,"Wake-Up Slap",-1,"Rollout",-1,"Sing",-1,None,None,0,"Poke Ball",300,"Cute Charm"]),poke.Poke('Togetic',[45,1,787,"Ancient Power",-1,"Metronome",-1,"Yawn",-1,"Fairy Wind",-1,None,None,0,"Poke Ball",300,"Serene Grace"])],60,spd = 1,loc = "sunken_cave")
        else:
            self.sunken_pre = npc.NPC(self,'Preschoolerg','Lucy',[1300,800],[['md',40],['mr',70],['mu',70],['ml',20],['md',30],['ml',50]],["Splish Splash! Splish Splash!","Come on, move those legs!",""],spd = 1, loc = "sunken_cave")
        if self.prog[5][61] == 0:
            self.sunken_hiker = npc.NPC(self,'Hiker','Wyatt',[2050,450],[['u',80],['r',60]],["Hey! Why are you busting up my","hidey-hole? I'm busy hunting", "for gems here!"],["Look what you did! Now people","are gonna come by and steal my", "gems!"],True,[0,0,0,0],[poke.Poke('Carbink',[45,2,787,"Skill Swap",-1,"Ancient Power",-1,"Reflect",-1,"Stealth Rock",-1,None,None,0,"Poke Ball",200,"Clear Body"]),poke.Poke('Seismitoad',[45,1,787,"Aqua Ring",-1,"Uproar",-1,"Muddy Water",-1,"Drain Punch",-1,None,None,0,"Poke Ball",200,"Poison Touch"]),poke.Poke('Steelix',[46,1,787,"Rock Slide",-1,"Dig",-1,"Crunch",-1,"Iron Tail",-1,None,None,0,"Poke Ball",100,"Sturdy"])],61,loc = "sunken_cave")
        else:
            self.sunken_hiker = npc.NPC(self,'Hiker','Wyatt',[2050,450],[['u',80],['r',60]],["Hey! Stop looking this way!","There's nothing to see here!",""],loc = "sunken_cave")
        if self.prog[5][62] == 0:
            self.sunken_sci = npc.NPC(self,'Scientistm','Dillon',[2250,1200],[['r',80]],["I've heard of mutations like","this, but I've never seen a", "real life example of it!"],["I guess it doesn't seem much","stronger than your average", "Quagsire, does it?"],True,[0,0,0,0],[poke.Poke('Magnezone',[46,2,787,"Discharge",-1,"Magnet Rise",-1,"Light Screen",-1,"Eerie Impulse",-1,None,None,0,"Poke Ball",200,"Soundproof"]),poke.Poke('Quagsire_S',[47,0,787,"Yawn",-1,"Earthquake",-1,"Amnesia",-1,"Slam",-1,None,None,0,"Poke Ball",300,"Water Absorb"])],62,loc = "sunken_cave")
        elif self.prog[5][62] == 1:
            self.sunken_sci = npc.NPC(self,'Scientistm','Dillon',[2250,1200],[['r',80]],["Interesting...it looks so","different, but it seems the","mutation is just cosmetic.","Maybe it's trying to adapt to","living in a different kind of", "environment?","What's up? I'm in your way?","Oh, I'm very sorry. I guess","I'll just move down this way."],loc = "sunken_cave")
        else:
            self.sunken_sci = npc.NPC(self,'Scientistm','Dillon',[2500,950],[['mu',60],['u',100],['md',60],['d',180]],["Quite fascinating, isn't it?","It's like a regional variant,","but with less variance."],loc = "sunken_cave")
        if self.prog[5][63] == 0:
            self.r6_tri = npc.NPC(self,'Triathelete','Chase',[2100,2100],[['mr',300],['ml',300]],["Phew! I think you'll make a","great addition to my training","regime!"],["Oh man, I think I'm starting","to run out of steam...", "","But that's exactly when you've","gotta pick yourself up and","keep running!"],True,[0,0,200,200],[poke.Poke('Electrode',[46,2,787,"Mirror Coat",-1,"Thunder Wave",-1,"Flash Cannon",-1,"Discharge",-1,None,None,0,"Poke Ball",200,"Magnet Pull"]),poke.Poke('Hitmontop',[46,0,787,"Triple Kick",-1,"Counter",-1,"Rapid Spin",-1,"Rolling Kick",-1,None,None,0,"Poke Ball",200,"Technician"]),poke.Poke('Rapidash',[46,1,787,"Fire Blast",-1,"Inferno",-1,"Flame Wheel",-1,"Megahorn",-1,None,None,0,"Poke Ball",200,"Flash Fire"]),poke.Poke('Jolteon',[46,0,787,"Discharge",-1,"Last Resort",-1,"Thunder Wave",-1,"Baby-Doll Eyes",-1,None,None,0,"Poke Ball",300,"Volt Absorb"])],63,loc = "route_6",spd = 1)
        else:
            self.r6_tri = npc.NPC(self,'Triathelete','Chase',[2100,2100],[['mr',300],['ml',300]],["I think...I'm about to...pass","out...just one more...mile...",""],loc = "route_6",spd = 1)
        if self.prog[5][64] == 0:
            self.r6_aroma = npc.NPC(self,'Aroma Lady','Iris',[4300,2550],[['mr',60],['r',60],['md',40],['d',80],['mu',40],['u',100],['ml',60],['l',60]],["I love bringing my Pokemon out","here to play in the fields!", "","Would you help me burn all the","energy they've gotten from","relaxing the whole day?"],["Well I guess it's time for","them to go back to resting for", "a while."],True,[100,100,100,100],[poke.Poke('Whimsicott',[47,0,787,"Dazzling Gleam",-1,"Tailwind",-1,"Cotton Guard",-1,"Energy Ball",-1,None,None,0,"Poke Ball",200,"Prankster"],petals=['sdf','sdf','sdf']),poke.Poke('Ribombee',[47,1,787,"Dazzling Gleam",-1,"Pollen Puff",-1,"Aromatherapy",-1,"Stun Spore",-1,None,None,0,"Poke Ball",200,"Shield Dust"],petals=['sdf','sdf','sdf']),poke.Poke('Leafeon',[47,1,787,"Synthesis",-1,"Swords Dance",-1,"Leaf Blade",-1,"Last Resort",-1,None,None,0,"Poke Ball",200,"Leaf Guard"],petals=['sdf','sdf','sdf'])],64,loc = "route_6")
        else:
            self.r6_aroma = npc.NPC(self,'Aroma Lady','Iris',[4300,2550],[['mr',60],['r',60],['md',40],['d',80],['mu',40],['u',100],['ml',60],['l',60]],["Why don't you join us? Lay in","the grass, stare at the lake,","and forget all your problems!"],loc = "route_6")
        if self.prog[5][65] == 0:
            self.r6_bug2 = npc.NPC(self,'Bug Catcher','Max',[1350,50],[['md',40],['d',80],['md',40],['d',140],['mu',80],['u',80]],["Hey! Watch where you're","stepping! I haven't checked", "that spot yet!"],["Hmm, I guess I'll forgive you","since you showed me some", "pretty cool Pokemon..."],True,[100,100,0,0],[poke.Poke('Pinsir',[48,1,787,"Swords Dance",-1,"Thrash",-1,"X-Scissor",-1,"Brick Break",-1,None,None,0,"Poke Ball",300,"Hyper Cutter"]),poke.Poke('Accelgor',[48,0,787,"Bug Buzz",-1,"U-turn",-1,"Giga Drain",-1,"Double Team",-1,None,None,0,"Poke Ball",300,"Hydration"]),poke.Poke('Araquanid',[48,0,787,"Lunge",-1,"Crunch",-1,"Bubble Beam",-1,"Leech Life",-1,None,None,0,"Poke Ball",300,"Water Bubble"])],65,loc = "route_6")
        else:
            self.r6_bug2 = npc.NPC(self,'Bug Catcher','Max',[1350,50],[['md',40],['d',80],['md',40],['d',140],['mu',80],['u',80]],["Some of these Pokemon are","getting way too big for me to","catch with this net."],loc = "route_6")
        if self.prog[5][66] == 0:
            self.r6_fish1 = npc.NPC(self,'Fisherman','Dean',[3250,1800],[['r',20]],["Freshly caught Pokemon, ready","for their debut battle!", ""],["Seems like they need a bit of","training before they're ready", "for battling."],True,[0,0,0,0],[poke.Poke('Kingler',[50,1,787,"Slam",-1,"Guillotine",-1,"Metal Claw",-1,"Bubble Beam",-1,None,None,0,"Poke Ball",0,"Hyper Cutter"]),poke.Poke('Octillery',[50,0,787,"Gunk Shot",-1,"Signal Beam",-1,"Ice Beam",-1,"Octazooka",-1,None,None,0,"Poke Ball",0,"Sniper"]),poke.Poke('Kingdra',[50,0,787,"Dragon Pulse",-1,"Brine",-1,"Focus Energy",-1,"Hydro Pump",-1,None,None,0,"Poke Ball",0,"Sniper"])],66,loc = "route_6")
        else:
            self.r6_fish1 = npc.NPC(self,'Fisherman','Dean',[3250,1800],[['r',20]],["I guess it makes sense that","these Pokemon didn't warm up","to me immediately.","I did just yank them out of","the water after all...",""],loc = "route_6")
        if self.prog[5][67] == 0:
            self.r6_fish2 = npc.NPC(self,'Fisherman','Tucker',[3450,1450],[['u',20]],["Behold!!!", "The untamed wrath of the sea!",""],["Okay, I guess this is more of","a lake than a sea...", ""],True,[0,0,0,0],[poke.Poke('Milotic',[48,1,787,"Hydro Pump",-1,"Attract",-1,"Dragon Tail",-1,"Recover",-1,None,None,0,"Poke Ball",400,"Marvel Scale"]),poke.Poke('Sharpedo',[48,0,787,"Crunch",-1,"Poison Fang",-1,"Ice Fang",-1,"Aqua Jet",-1,None,None,0,"Poke Ball",400,"Rough Skin"])],67,loc = "route_6")
        else:
            self.r6_fish2 = npc.NPC(self,'Fisherman','Tucker',[3450,1450],[['u',20]],["When I come out here, I like","to pretend I'm at war with the","mighty ocean!"],loc = "route_6")
        if self.prog[5][68] == 0:
            self.r6_fish3_npc = npc.NPC(self,'Fisherman','David',[2950,1500],[['l',60]],["It's a nice day out! Why don't","I show you some of the amazing","Pokemon I've fished up?"],["Seems like you handled those","Pokemon pretty well. Why don't","you try fishing yourself?"],True,[0,0,0,0],[poke.Poke('Golisopod',[55,0,787,"First Impression",-1,"Liquidation",-1,"Swords Dance",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",300,"Emergency Exit"]),poke.Poke('Whiscash',[55,1,787,"Snore",-1,"Rest",-1,"Muddy Water",-1,"Earthquake",-1,None,None,0,"Poke Ball",300,"Oblivious"]),poke.Poke('Clawitzer',[55,1,787,"Aura Sphere",-1,"Dark Pulse",-1,"Dragon Pulse",-1,"Aqua Jet",-1,None,None,0,"Poke Ball",300,"Mega Launch"]),poke.Poke('Malamar',[55,0,787,"Superpower",-1,"Night Slash",-1,"Psycho Cut",-1,"Light Screen",-1,None,None,0,"Poke Ball",300,"Suction Cups"]),poke.Poke('Kingdra',[55,1,787,"Dragon Pulse",-1,"Brine",-1,"Agility",-1,"Focus Energy",-1,None,None,0,"Poke Ball",300,"Sniper"]),poke.Poke('Lapras',[55,0,787,"Hydro Pump",-1,"Ice Beam",-1,"Rain Dance",-1,"Safeguard",-1,None,None,0,"Poke Ball",300,"Shell Armor"])],68,loc = "route_6")
        else:
            self.r6_fish3_npc = npc.NPC(self,'Fisherman','David',[2950,1500],[['l',60]],["Have you had any luck using","the rod I gave you?","","Just make sure to keep your","hands steady and reel in when","the fish bites!"],loc = "route_6")
        if self.prog[5][69] == 0:
            self.r6_hiker = npc.NPC(self,'Hiker','Brooks',[3300,-900],[['u',80],['l',80],['r',100]],["I'm sure there's something","valuable in those woods, but","I'm too scared to explore it!"],["How about you take a look in", "there? After all you seem to","be pretty competent!"],True,[150,0,150,150],[poke.Poke('Crustle',[48,1,787,"X-Scissor",-1,"Shell Smash",-1,"Rock Slide",-1,"Stealth Rock",-1,None,None,0,"Poke Ball",300,"Shell Armor"]),poke.Poke('Golurk',[48,1,787,"Dynamic Punch",-1,"Magnitude",-1,"Shadow Punch",-1,"Iron Defense",-1,None,None,0,"Poke Ball",300,"Iron Fist"]),poke.Poke('Aggron',[50,0,787,"Iron Defense",-1,"Rock Slide",-1,"Iron Tail",-1,"Double-Edge",-1,None,None,0,"Poke Ball",300,"Sturdy"])],69,loc = "route_6")
        else:
            self.r6_hiker = npc.NPC(self,'Hiker','Brooks',[3300,-900],[['u',80],['l',80],['r',100]],["So did you get a chance to","take a stroll in there? Find","any gold? Or diamonds?"],loc = "route_6")
        if self.prog[5][70] == 0:
            self.r6_rock4 = npc.NPC(self,'Team Rocketf','Grunt',[2350,-1050],[['d',20]],["Halt! You're not allowed to", "go past here! We've got some","important business to do.","Wait...Did you already get","past me? Either way I'm not","letting you get away!"],["Let's pretend you just snuck","past me without me noticing.", "Sound good?"],True,[0,100,0,0],[poke.Poke('Vileplume',[50,1,787,"Moonlight",-1,"Giga Drain",-1,"Toxic",-1,"Petal Blizzard",-1,None,None,0,"Poke Ball",200,"Chlorophyll"],petals=['hp','hp','hp']),poke.Poke('Yanmega',[50,0,787,"U-turn",-1,"Bug Buzz",-1,"Air Slash",-1,"Ancient Power",-1,None,None,0,"Poke Ball",200,"Speed Boost"],petals=['spd','spd','spd']),poke.Poke('Honchkrow',[50,0,787,"Taunt",-1,"Wing Attack",-1,"Sucker Punch",-1,"Night Slash",-1,None,None,0,"Poke Ball",200,"Super Luck"],petals=['ak','ak','ak'])],70,loc = "route_6")
        else:
            self.r6_rock4 = npc.NPC(self,'Team Rocketf','Grunt',[2350,-1050],[['d',20]],["Hey, I already let you go!","No need to gloat your victory","in my face!"],loc = "route_6")
        if self.prog[5][71] == 0:
            self.r6_rock5 = npc.NPC(self,'Team Rocketm','Grunt',[1900,-1450],[['u',20]],["Stop right there! I've got", "orders to stop any passerbys","from continuing forward!","That means you! And if you","resist, I'll have to force you","to leave!"],["Hold on, this isn't how this", "was supposed to go...",""],True,[150,0,0,0],[poke.Poke('Magneton',[50,2,787,"Electric Terrain",-1,"Discharge",-1,"Flash Cannon",-1,"Metal Sound",-1,None,None,0,"Poke Ball",200,"Magnet Pull"],petals=['hp','hp','hp']),poke.Poke('Toxicroak',[50,1,787,"Poison Jab",-1,"Sucker Punch",-1,"Swagger",-1,"Revenge",-1,None,None,0,"Poke Ball",200,"Dry Skin"],petals=['ak','ak','ak']),poke.Poke('Golem',[50,0,787,"Double-Edge",-1,"Earthquake",-1,"Rock Blast",-1,"Explosion",-1,None,None,0,"Poke Ball",200,"Rock Head"],petals=['spd','spd','spd']),poke.Poke('Malamar',[50,0,787,"Topsy-Turvy",-1,"Psycho Cut",-1,"Night Slash",-1,"Superpower",-1,None,None,0,"Poke Ball",200,"Contrary"],petals=['hp','hp','hp'])],71,loc = "route_6")
        else:
            self.r6_rock5 = npc.NPC(self,'Team Rocketm','Grunt',[1900,-1450],[['u',20]],["What do I do? Proton didn't","give me instructions for if","I lost..."],loc = "route_6")



    def load_images(self,graphics_change = False) -> None:
        if self.graphic == 1:
            self.r_flair = poke_func.load("p/red_flair.png")
            self.g_flair = poke_func.load("p/green_flair.png")
            self.wave = poke_func.load("p/waves.png")
        else:
            self.r_flair = poke_func.load("p/transparent.png")
            self.g_flair = poke_func.load("p/green_flair_low.png")
            self.wave = poke_func.load("p/waves_low.png")
        if graphics_change == False:
            self.nurse_box = pygame.transform.scale(poke_func.load("p/nurse_icon.png"),(25,25))
            self.item_box = pygame.transform.scale(poke_func.load("p/item_icon.png"),(16,20))
            self.rain_img = poke_func.load("p/terrain/rain.png")
            self.wind_img = poke_func.load("p/terrain/wind.png")
            self.sun_img = poke_func.load("p/terrain/sunny.png")
            self.char_shad = poke_func.load("p/char_shadow.png")
            self.ss_d2 = poke_func.load("p/stair_shadow_d2.png")
            self.ss_d1 = poke_func.load("p/stair_shadow_d1.png")
            self.ss_u1 = poke_func.load("p/stair_shadow_u1.png")
            self.ss_u2 = poke_func.load("p/stair_shadow_u2.png")
            self.shadow_u = poke_func.load("p/shadow_u.png")
            self.shadow_d = poke_func.load("p/shadow_d.png")
            self.shadow_l = poke_func.load("p/shadow_l.png")
            self.shadow_r = poke_func.load("p/shadow_r.png")
            self.textbox = poke_func.load("p/textbox.png")
            self.exclaim = poke_func.load("p/exclaim.png")
            self.battlebox = poke_func.load("p/battle_txtbox.png")
            self.choicebox = poke_func.load("p/2_box.png")
            self.arrow = poke_func.load("p/arrow.png")
            self.pokeball = poke_func.load("p/Poke Ball.png")
            self.item_cave = poke_func.load("p/item_cave.png")
            self.item_out = poke_func.load("p/item.png")
            self.dwebble_rock = poke_func.load("p/dwebble.png")
            self.lamp = poke_func.load("p/am/street_lamp.png")
            self.light = poke_func.load("p/am/lamp_light.png")
            self.grass = poke_func.load("p/am/grass_bot.png")
            self.dark_grass = poke_func.load("p/am/dark_grass_bot.png")
            self.small_door = poke_func.load("p/am/house_1_door.png")
            self.traffic_cone = poke_func.load("p/egida/traffic_cone.png")
            self.black_back = poke_func.load("p/black_back.png")
            self.pc_black = poke_func.load("p/am/pc_black.png")
            self.mine_door = poke_func.load("p/egida/mine_door.png")
            self.gondolier = pygame.transform.scale(poke_func.load("p/spr/gondolier_d.png"),(45,54))
            self.gondola_1 = poke_func.load("p/am/gondola_1.png")
            self.gondola_2 = poke_func.load("p/am/gondola_2.png")
            self.gondola = self.gondola_1
            self.pcdr = poke_func.load("p/am/pc_door_r.png")
            self.pcdl = poke_func.load("p/am/pc_door_l.png")
            self.pc_light = poke_func.load("p/am/poke_center_light.png")
            self.falls = poke_func.load("p/waterfall.png")
            self.cave_out_u = poke_func.load("p/cave_out_u.png")
            self.cave_in_d = poke_func.load("p/cave_in_d.png")
            self.cave_in_r = poke_func.load("p/cave_in_r.png")
            self.cave_out_r = poke_func.load("p/cave_out_r.png")
            self.caught_icon = pygame.transform.scale(poke_func.load("p/Poke Ball.png"),(25,25))
            self.garden_bin = poke_func.load("p/gardening/bin.png")
            self.garden_water_bin = poke_func.load("p/gardening/water_bucket.png")
            self.garden_fertilizer = poke_func.load("p/gardening/fertilizer.png")
            self.lantern_dark = poke_func.load("p/pianura/cave_darkness.png")
            self.lantern_light = poke_func.load("p/pianura/lantern.png")
            self.ff_bell = poke_func.load("p/ombra/bell.png")
            self.repel_img = poke_func.load("p/item/Repel.png")
            self.repel_bar = poke_func.load("p/repel_bar.png")
            self.beadr = poke_func.load("p/silfide/beauty_door_r.png")
            self.beadl = poke_func.load("p/silfide/beauty_door_l.png")
            #route 1
            self.route_1 = poke_func.load("p/am/Route_1.png")
            self.r1_trees = poke_func.load("p/am/route_1_trees.png")
            self.r1_foam = poke_func.load("p/am/route_1_foam.png")
            self.r1_statue = poke_func.load("p/am/route_1_statue.png")
            self.r1_bridge_l = poke_func.load("p/am/bridge_r.png")
            self.r1_grass = poke_func.load("p/am/route_1_grass.png")
            self.r1_path = poke_func.load("p/am/route_1_path.png")
            self.r1_fence = poke_func.load("p/am/route_1_fence.png")
            #Egida
            self.egida = poke_func.load("p/egida/Egida_City.png")
            self.egi_f = poke_func.load("p/egida/egida_front.png")
            self.egi_gen = poke_func.load("p/egida/generators.png")
            self.egi_lift = poke_func.load("p/egida/lift.png")
            self.egi_back = poke_func.load("p/egida/Egida_Alt.png")
            self.egi_clip = poke_func.load("p/egida/Egida_clip.png")
            #route 2
            self.route_2 = poke_func.load("p/egida/Route_2.png")
            self.r2_f = poke_func.load("p/egida/Route_2_f.png")
            #route 3
            self.r3_back = poke_func.load("p/egida/Route_3.png")
            self.r3_foam = poke_func.load("p/egida/route_3_foam.png")
            self.r3_grass = poke_func.load("p/am/route_1_grass.png")
            self.r3_grass2 = poke_func.load("p/egida/route_3_grass.png")
            self.r3_grass3 = poke_func.load("p/egida/route_3_grass_bot.png")
            self.r3_beach = poke_func.load("p/pianura/route_3_beach.png")
            self.r3_f = poke_func.load("p/egida/route_3_f.png")
            self.r3_fence = poke_func.load("p/egida/route_3_fence2.png")
            self.r3_cloud = poke_func.load("p/pianura/thundurus_cloud.png")
            self.r3_shad = pygame.transform.scale(poke_func.load("p/pianura/Thundurus_shadow.png"),(150,150))
            self.r3_thun = pygame.transform.scale(poke_func.load("p/pianura/Thundurus.png"),(150,150))
            self.r3_lights = poke_func.load("p/egida/shrine_lights.png")
            self.r3_poke_shad = poke_func.load("p/egida/poke_shadow.png")
            self.r3_slow1 = pygame.transform.scale(poke_func.load("p/spr/Slowpoke_sleep1.png"),(80,50))
            self.r3_slow2 = pygame.transform.scale(poke_func.load("p/spr/Slowpoke_sleep2.png"),(80,50))
            self.r3_slow3 = pygame.transform.scale(poke_func.load("p/spr/Slowpoke_d1.png"),(80,60))
            self.r3_slow0 = poke_func.load("p/blank.png")
            self.r3_slow = self.r3_slow1
            #pianura
            self.pia_back = poke_func.load("p/pianura/Pianura_City.png")
            self.pia_f = poke_func.load("p/pianura/pianura_f.png")
            self.pia_foam = poke_func.load("p/pianura/pianura_foam.png")
            self.pia_light = poke_func.load("p/pianura/Lighthouse_light.png")
            self.d1_door = poke_func.load("p/am/house_2_door.png")
            #sableye
            self.sableye_u1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u1.png"),(50,60))
            self.sableye_u2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u2.png"),(50,60))
            self.sableye_u3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u3.png"),(50,60))
            self.sableye_d1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d1.png"),(50,60))
            self.sableye_d2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d2.png"),(50,60))
            self.sableye_d3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d3.png"),(50,60))
            self.sableye_l1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l1.png"),(50,60))
            self.sableye_l2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l2.png"),(50,60))
            self.sableye_l3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l3.png"),(50,60))
            self.sableye_r1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r1.png"),(50,60))
            self.sableye_r2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r2.png"),(50,60))
            self.sableye_r3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r3.png"),(50,60))
            #route 4
            self.r4_back = poke_func.load("p/isola/route_4.png")
            self.r4_foam = poke_func.load("p/isola/route_4_foam.png")
            self.r4_f = poke_func.load("p/isola/route_4_f.png")
            self.r4_kang = pygame.transform.scale(poke_func.load("p/spr/Kangaskhan_r1.png"),(75,90))
            self.r4_cave = poke_func.load("p/isola/cave_out_r.png")
            self.r4_shad = poke_func.load("p/isola/poke_shadow_side.png")
            #isola
            self.isola_back = poke_func.load("p/isola/Isola_Town.png")
            self.isola_f = poke_func.load("p/isola/Isola_f.png")
            self.isola_foam = poke_func.load("p/isola/Isola_foam.png")
            #route 5
            self.r5_back = poke_func.load("p/isola/route_5.png")
            self.r5_beach = poke_func.load("p/isola/route_5_beach.png")
            self.r5_f = poke_func.load("p/isola/route_5_f.png")
            self.r5_foam = poke_func.load("p/isola/route_5_foam.png")
            #verde
            self.verde_back = poke_func.load("p/verde/Verde_City.png")
            self.verde_foam = poke_func.load("p/verde/verde_foam.png")
            self.verde_f = poke_func.load("p/verde/verde_f.png")
            self.verde_gym = poke_func.load("p/verde/gym_door.png")
            self.verde_berry1 = pygame.transform.scale(poke_func.load("p/spr/berry_trees/Iapapa_tree_1.png"),(60,75))
            self.verde_berry2 = pygame.transform.scale(poke_func.load("p/spr/berry_trees/Lum_tree_1.png"),(60,75))
            self.verde_berry3 = pygame.transform.scale(poke_func.load("p/spr/berry_trees/Wiki_tree_1.png"),(60,75))
            self.verde_berry4 = pygame.transform.scale(poke_func.load("p/spr/berry_trees/Persim_tree_1.png"),(60,75))
            #route 6
            self.r6_back = poke_func.load("p/cascata/Route_6.png")
            self.r6_f = poke_func.load("p/cascata/Route_6_f.png")
            self.r6_lf = poke_func.load("p/cascata/Route_6_lake_f.png")
            self.r6_tf = poke_func.load("p/cascata/Route_6_top_f.png")
            self.r6_rc = poke_func.load("p/cascata/Route_6_river_cover.png")
            self.r6_foam = poke_func.load("p/cascata/Route_6_foam.png")
            self.r6_lfoam = poke_func.load("p/cascata/Route_6_lake_foam.png")
            self.r6_tfoam = poke_func.load("p/cascata/Route_6_top_foam.png")
            self.r6_stair = poke_func.load("p/cascata/route_6_stair.png")
            self.r6_foam_1 = poke_func.load("p/cascata/route_6_f1.png")
            self.r6_foam_2 = poke_func.load("p/cascata/route_6_f2.png")
            self.r6_foam_3 = poke_func.load("p/cascata/route_6_f3.png")
            self.r6_snor1 = pygame.transform.scale(poke_func.load("p/spr/Snorlax_sleep1.png"),(200,200))
            self.r6_snor2 = pygame.transform.scale(poke_func.load("p/spr/Snorlax_sleep2.png"),(200,200))
            self.r6_audino = pygame.transform.scale(poke_func.load("p/spr/Audino_r1.png"),(60,72))
            self.r6_torn1 = pygame.transform.scale(poke_func.load("p/cascata/Tornadus_b.png"),(150,150))
            self.r6_torn2 = pygame.transform.scale(poke_func.load("p/cascata/Tornadus.png"),(150,150))
            self.r6_torn = self.r6_torn1
            self.r6_weez = pygame.transform.scale(poke_func.load("p/spr/Weezing_l1.png"),(100,100))
            self.r6_milo = pygame.transform.scale(poke_func.load("p/spr/Milotic_r1.png"),(100,120))
            self.r6_alt = pygame.transform.scale(poke_func.load("p/spr/Altaria_d1.png"),(50,66))
            self.r6_silf = poke_func.load("p/cascata/r6_silfide.png")
            self.r6_cloud = poke_func.load("p/cascata/r6_clouds.png")
            #cascata
            self.cascata_back = poke_func.load("p/cascata/Cascata_City.png")
            self.cascata_f = poke_func.load("p/cascata/Cascata_f.png")
            self.cascata_fen = poke_func.load("p/cascata/Cascata_fen.png")
            self.cascata_foam = poke_func.load("p/cascata/Cascata_foam.png")
            self.cascata_foam_1 = poke_func.load("p/cascata/cascata_foam_1.png")
            self.cascata_foam_2 = poke_func.load("p/cascata/cascata_foam_2.png")
            self.cascata_foam_3 = poke_func.load("p/cascata/cascata_foam_3.png")
            #fishing
            self.fishing_hud = poke_func.load("p/fishing/hud.png")
            self.old_rod = poke_func.load("p/fishing/Old Rod.png")
            self.good_rod = poke_func.load("p/fishing/Good Rod.png")
            self.super_rod = poke_func.load("p/fishing/Super Rod.png")
            self.fishing_dot = poke_func.load("p/fishing/dot.png")
            self.fishing_dark = poke_func.load("p/fishing/dark.png")
            #silfide
            self.silfide_back = poke_func.load("p/silfide/Silfide_City.png")
            self.silfide_f = poke_func.load("p/silfide/Silfide_f.png")
            self.silfide_wind = poke_func.load("p/silfide/windmill.png")
            self.silfide_foam = poke_func.load("p/silfide/Silfide_foam.png")
            self.silfide_foamf = poke_func.load("p/silfide/Silfide_foamf.png")

if __name__ == '__main__':
    pygame.init()
    Pokemon().run()
