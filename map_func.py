import pokemon
import poke
import sys
import pygame
import save
import random
import moves
import npc
from poke_func import*
from pygame.locals import*



def verde_b(P,wx,wy,pcx,pcy,gy):
    draw_waves(P, wx, wy)
    if P.px == -725 and P.py > 75 and P.py <= 125:
        pcx = (-75 + P.py)
        pcy = ((-75 + P.py)/5)
    P.surface.blit(P.pc_black,(P.px+1080,P.py+130))
    P.surface.blit(P.pcdr, (P.px + 1125 + pcx, P.py + 130 - pcy))
    P.surface.blit(P.pcdl, (P.px + 1088 - pcx, P.py + 130 - pcy))
    P.surface.blit(P.verde_back, (P.px + 100, P.py - 1200))
    if P.px == -775 and P.py > 475 and P.py <= 525:
        blit_small_door(P,525)
    if P.px == -2075 and P.py > 1175 and P.py <= 1225:
        blit_small_door(P,1225)
    if P.px == -2575 and P.py > 75 and P.py <= 125:
        blit_small_door(P,125)
    if P.px == -3025 and P.py > 75 and P.py <= 125:
        blit_small_door(P,125)
    if P.px == -275 and P.py > 475 and P.py <= 525:
        blit_small_door(P,515)
    P.surface.blit(P.gondola, (P.px + 1450, P.py - 650 + abs(P.foam)-gy))
    P.surface.blit(P.char_shad, (P.px + 1461, P.py - 590 + abs(P.foam)-gy))
    P.surface.blit(P.gondolier, (P.px + 1462, P.py - 610 + abs(P.foam)-gy))

    P.surface.blit(P.verde_foam,(P.px+1387,P.py-818+abs(P.foam)))

def verde_p(P,temppx,temppy,move,gond,gy):
    aroma = P.isola_aroma.y_dist() > 0
    if aroma:
        P.isola_aroma.move()
    if P.isola_lat:
        lat = P.isola_lat.y_dist() > 0
        lato = P.isola_lat.y_dist() > 0
        if lat:
            P.isola_lat.move()
        if lato:
            P.isola_lato.move()
    if P.isola_fish:
        fish = P.isola_fish.y_dist() > 0
        if fish:
            P.isola_fish.move()
    if P.isola_seed:
        seed = P.isola_seed.y_dist() > 0
        if seed:
            P.isola_seed.move()
    P.isola_host.move()
    r1 = (P.px+500,P.py+350,300,40)
    r2 = (P.px+900,P.py+350,400,40)
    r3 = (P.px+450,P.py-200,50,540)
    r4 = (P.px+500,P.py-250,150,40)
    r5 = (P.px+650,P.py-300,50,40)
    r6 = (P.px+700,P.py-250,150,40)
    r7 = (P.px+600,P.py,50,40)
    r8 = (P.px+550,P.py+100,50,40)
    r9 = (P.px+700,P.py+50,50,40)
    r10 = (P.px+800,P.py-700,50,440)
    r11 = (P.px+850,P.py-750,450,40)
    r12 = (P.px+1300,P.py-700,50,90)
    r13 = (P.px+1350,P.py-650,100,40)
    r14 = (P.px+1450,P.py-600,50,90)
    r15 = (P.px+1300,P.py-500,150,40)
    r16 = (P.px+1050,P.py-450,250,40)
    r17 = (P.px+1050,P.py-400,50,190)
    r18 = (P.px+1100,P.py-250,50,40)
    r19 = (P.px+1150,P.py-300,50,40)
    r20 = (P.px+1200,P.py-250,450,40)
    r21 = (P.px+950,P.py-100,700,40)
    r22 = (P.px+950,P.py-50,50,240)
    r23 = (P.px+1000,P.py+150,100,40)
    r24 = (P.px+1100,P.py+100,50,40)
    r25 = (P.px+1150,P.py+150,150,40)
    r26 = (P.px+1300,P.py+200,50,140)
    r27 = (P.px+1650,P.py-50,850,40)
    r28 = (P.px+1600,P.py-300,50,40)
    r29 = (P.px+1650,P.py-350,50,40)
    r30 = (P.px+1700,P.py-300,150,40)
    r31 = (P.px+1850,P.py-250,200,40)
    r32 = (P.px+2050,P.py-300,50,40)
    r33 = (P.px+2100,P.py-250,200,40)
    r34 = (P.px+2250,P.py-400,50,140)
    r35 = (P.px+2300,P.py-750,50,340)
    r36 = (P.px+2450,P.py-750,50,340)
    r37 = (P.px+2500,P.py-400,50,140)
    r38 = (P.px+2050,P.py-750,250,40)
    r39 = (P.px+2000,P.py-1100,50,340)
    r40 = (P.px+2050,P.py-1150,150,40)
    r41 = (P.px+2100,P.py-1100,50,40)
    r42 = (P.px+2200,P.py-1100,50,40)
    r43 = (P.px+2200,P.py-1050,150,40)
    r44 = (P.px+2150,P.py-1000,50,40)
    r45 = (P.px+2250,P.py-950,50,40)
    r46 = (P.px+2350,P.py-1000,50,90)
    r47 = (P.px+2400,P.py-950,50,40)
    r48 = (P.px+2450,P.py-1000,50,40)
    r49 = (P.px+2500,P.py-950,50,40)
    r50 = (P.px+2550,P.py-1100,50,190)
    r51 = (P.px+2600,P.py-1150,50,40)
    r52 = (P.px+2650,P.py-1100,50,340)
    r53 = (P.px+2500,P.py-750,150,40)
    r54 = (P.px+2500,P.py-250,400,40)
    r55 = (P.px+2500,P.py-100,350,40)
    r56 = (P.px+2850,P.py-50,250,40)
    r57 = (P.px+3050,P.py,50,190)
    r58 = (P.px+3000,P.py+150,50,40)
    r59 = (P.px+2950,P.py+100,50,40)
    r60 = (P.px+2850,P.py+150,100,40)
    r61 = (P.px+2800,P.py+200,50,140)
    r62 = (P.px+2850,P.py+350,700,40)
    r63 = (P.px+3550,P.py+200,50,140)
    r64 = (P.px+3450,P.py+150,100,40)
    r65 = (P.px+3400,P.py+100,50,40)
    r66 = (P.px+3300,P.py+150,100,40)
    r67 = (P.px+3300,P.py,50,140)
    r68 = (P.px+3300,P.py-50,250,40)
    r69 = (P.px+3550,P.py-450,50,390)
    r70 = (P.px+2850,P.py-450,50,190)
    r71 = (P.px+2900,P.py-500,650,40)
    # if P.isola_seed:
    #     r32 = P.isola_seed.get_rect()
    rects = [r71,r70,r69,r68,r67,r66,r65,r64,r63,r62,r61,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+1461,P.py-537+abs(P.foam)-gy))
        P.surface.blit(P.p,(P.px+1460,P.py-560+abs(P.foam)-gy))
    else:
        if move:
            if P.prog[0] == 89 and P.px in [-625,-725] and P.py == 975 and (face_l(P) or face_r(P)):
                player_move(P,rects,manual_input = 'd')
            else:
                player_move(P,rects)
        else:
            blit_player(P)
    if P.isola_lat:
        if not lat:
            P.isola_lat.move(temppx,temppy)
        if not lato:
            P.isola_lato.move(temppx,temppy)
    if not aroma:
        P.isola_aroma.move(temppx,temppy)
    if P.isola_fish:
        if not fish:
            P.isola_fish.move(temppx,temppy)
    if P.isola_seed:
        if not seed:
            P.isola_seed.move(temppx,temppy)

def verde_f(P,temppx,temppy,tim):
    set_sky(P)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+1065,temppy-51))
    show_location(P, P.loc_txt, tim)

def verde(P,enter = False) -> None:
    #sci_tim = None,sci_curr = None
    if P.song != "music/verde.wav":
        P.song = "music/verde.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] == 98:
        P.prog[0] += 1
    P.isola_host = npc.NPC(P,'Hostess','Harper',[600,-500],[['d',40]],["","",""])
    if P.prog[0] == 89:
        P.isola_lat = npc.NPC(P,'Latias','Harper',[850,-300],[['l',40]],["Where could she have gone?","I've been looking everywhere","for her!","Huh? Sorry I don't think we've","met before...You must have the","wrong person."])
        P.isola_lato = npc.NPC(P,'Latios','Harper',[800,-300],[['r',40]],["I'm sure she'll be okay. I","just hope she comes back to us","soon..."])
        P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-700],[['u',40]],["Hey! I just saw some strange","people making their way down","to Route 4.","They looked like they were up","to something real suspicious.","","You look like someone that can","handle them. Could you go over","and check it out?"])
    else:
        P.isola_lat = None
        P.isola_lato = None
        P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-450],[['md',60],['d',100],['mu',60],['u',140]],["Our town may be small, but","that's part of what makes it","so nice!","It's like we're one big family","living together in our own","little village!"])
    if not (datetime.datetime.today().weekday() == 6 and get_time() >= 6 and P.prog[16] == 2):
        P.isola_fish = npc.NPC(P,'Fisherman','Harper',[1550,-150],[['r',40]],["Hey, thanks again for the","Seedot! It's nice to have a","little friend to travel with!","If you ever find the time, you","should come meet me in Alto","Mare Square on Sundays!","I'll have some nice items that","I've collected throughout the","week for you to buy!"])
        if P.px == -1175 and P.py in [375,425]:
            P.px += 50
        if P.prog[16] == 2:
            P.isola_seed = npc.NPC(P,'Seedot','Harper',[1550,-100],[['d',40]],["SEEDOT!!!","",""])
        else:
            P.isola_seed = None
    else:
        P.isola_fish = None
        P.isola_seed = None
    set_location(P)
    wx = 0
    wy = 0
    gond = 0
    gy = 0
    pcx = 0
    pcy = 0
    fade = None
    move = True
    tim = 0
    if enter == False:
        verde_b(P,wx,wy,pcx,pcy,gy)
        verde_p(P,P.px,P.py,False,gond,gy)
        verde_f(P,P.px,P.py,tim)
        fade_in(P)
    end = True
    m = 0
    while end:
        print(P.px,P.py)
        verde_b(P,wx,wy,pcx,pcy,gy)
        temppx = P.px
        temppy = P.py
        verde_p(P,temppx,temppy,move,gond,gy)
        verde_f(P, temppx, temppy, tim)
        if gond == 1:
            gond = 2
            fade_in(P)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and gond == 0 and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -1025 and P.py == 875 and face_r(P):
                        nxtl = gondolier(P)
                        if nxtl != "Verde City":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.py == 1025 and face_u(P):
                        #change
                        txt(P,"There's some strange barrier","stopping you from continuing.")
                    elif P.px == -225 and P.py == 675 and face_u(P):
                        txt(P,"Hello! Are you here to join","the Isola Town Water Race?")
                        txt(P,"No? Well you're welcome to","come back once you've gotten","certified!")
                    elif P.px == -1175 and P.py in [375,425,475] and face_r(P):
                        txt(P,"There's a gondola tied to the","end of this dock.")
                    elif P.isola_lat and P.isola_lat.talk():
                        verde_b(P,wx,wy,pcx,pcy,gy)
                        verde_p(P,temppx,temppy,False,gond,gy)
                        verde_f(P,temppx,temppy,tim)
                        P.isola_lat.write()
                    elif P.isola_lato and P.isola_lato.talk():
                        verde_b(P,wx,wy,pcx,pcy,gy)
                        verde_p(P,temppx,temppy,False,gond,gy)
                        verde_f(P,temppx,temppy,tim)
                        P.isola_lato.write()
                    elif P.isola_aroma.talk():
                        verde_b(P,wx,wy,pcx,pcy,gy)
                        verde_p(P,temppx,temppy,False,gond,gy)
                        verde_f(P,temppx,temppy,tim)
                        P.isola_aroma.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            end = False
            fade = P.song

        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        # if P.py == -275 and P.px in [-525,-575,-625] and face_d(P):
        #     P.py = 525
        #     P.px -= 1600
        #     P.loc = 'route_4'
        #     route_4(P,True,wx,wy)
        #     end = False
        if P.py == -75 and P.px > -575 and face_d(P):
            P.py = 1275
            P.px -= 500
            P.loc = "route_5"
            route_5(P,True)
            end = False
        if P.px == -825 and P.py == 125 and face_u(P):
            P.loc = "house_3_2"
            P.px = -25
            P.py = -75
            end = False
        if P.py == 125 and P.px == -725 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_verde"
            fade = P.song
            end = False
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def route_5_b(P,wx,wy,beachx,beachy,beach_poke):
    draw_waves(P,wx,wy)
    P.surface.blit(P.r5_back,(P.px-150,P.py-1600))
    if type(beach_poke) == list:
        P.surface.blit(P.r3_poke_shad,(P.px+beachx[beach_poke[0]],P.py+beachy[beach_poke[0]]+abs(P.foam)))
    P.surface.blit(P.r5_beach,(P.px+408,P.py+520+abs(P.foam)))
    #if P.py <= 625:
    #    P.surface.blit(P.r3_fence,(P.px+4397,P.py-374))
    if P.prog[6][51] == 0:
        P.surface.blit(P.item_out,(P.px+2400,P.py-250))
    if P.prog[6][52] == 0:
        P.surface.blit(P.item_out,(P.px+1000,P.py+150))
        P.surface.blit(P.grass,(P.px+1000,P.py+140))

def route_5_p(P,temppx,temppy,move):
    tree1 = P.r5_tree1.y_dist() > 0
    tree2 = P.r5_tree2.y_dist() > 0
    tree3 = P.r5_tree3.y_dist() > 0
    if tree1:
        P.r5_tree1.blit()
    if tree2:
        P.r5_tree2.blit()
    if tree3:
        P.r5_tree3.blit()
    if P.r5_rival:
        rival = P.r5_rival.y_dist() > 0
        if rival:
            P.r5_rival.move()
            draw_grass(P,P.r5_rival.x,P.r5_rival.y,-1675,275,200,100,[P.px,P.py],ignore = [(-1675,275),(-1725,275)])
    psy = P.r5_psy.y_dist() > 0
    bug = P.r5_bug.y_dist() > 0
    lass = P.r5_lass.y_dist() > 0
    beauty = P.r5_beauty.y_dist() > 0
    if psy:
        P.r5_psy.move()
        draw_grass(P,P.r5_psy.x,P.r5_psy.y,-125,675,400,400,[P.px,P.py])
    if bug:
        P.r5_bug.move()
        draw_grass(P,P.r5_bug.x,P.r5_bug.y,-1275,775,600,200,[P.px,P.py])
    if lass:
        P.r5_lass.move()
    if beauty:
        P.r5_beauty.move()
    #rects start
    r1 = (P.px+2750,P.py-100,50,690)
    r2 = (P.px+2250,P.py-150,500,40)
    r3 = (P.px+2550,P.py+100,50,490)
    r4 = (P.px+2000,P.py+100,550,40)
    r5 = (P.px+2250,P.py-200,200,40)
    r6 = (P.px+2450,P.py-250,50,40)
    r7 = (P.px+2250,P.py-300,200,40)
    r8 = (P.px+2250,P.py-500,50,190)
    r9 = (P.px+1650,P.py-550,600,40)
    r10 = (P.px+1750,P.py-300,400,40)
    r11 = (P.px+1750,P.py-250,50,90)
    r12 = (P.px+2100,P.py-250,50,90)
    r13 = (P.px+1750,P.py-150,400,40)
    r14 = (P.px+1600,P.py-500,50,340)
    r15 = (P.px+1250,P.py-150,400,40)
    r16 = (P.px+1300,P.py-300,50,140)
    r17 = (P.px+1150,P.py-350,150,40)
    r18 = (P.px+1100,P.py-300,50,140)
    r19 = (P.px+1000,P.py-150,200,40)
    r20 = (P.px+950,P.py-100,50,340)
    r21 = (P.px+1000,P.py+200,450,90)
    r22 = (P.px+1400,P.py+100,50,90)
    r23 = (P.px+1450,P.py+100,450,40)
    r24 = (P.px+1650,P.py+150,250,40)
    r25 = (P.px+1450,P.py+200,200,40)
    r26 = (P.px+900,P.py-700,50,890)
    r27 = (P.px+2000,P.py+150,150,40)
    r28 = (P.px+2150,P.py+200,100,40)
    r31 = (P.px+2250,P.py+250,50,40)
    r29 = (P.px+2300,P.py+300,50,90)
    r30 = (P.px+2350,P.py+400,50,90)
    r32 = (P.px+2400,P.py+500,50,90)
    r33 = (P.px+650,P.py,50,490)
    r34 = (P.px+500,P.py,150,40)
    r35 = (P.px+450,P.py-400,50,390)
    r36 = (P.px+500,P.py-450,200,40)
    r37 = (P.px+650,P.py-800,50,340)
    r38 = (P.px+700,P.py-850,110,40)
    r39 = r1
    if P.px == -475 and P.py == 1100:
        r39 = (P.px+850,P.py-850,50,15)
    if P.px == -475 and P.py == 1050:
        r39 = (P.px+850,P.py-725,50,50)
    if P.px == -475 and P.py == 975:
        r39 = (P.px+850,P.py-750,50,40)
    r40 = (P.px+900,P.py-900,100,40)
    r41 = (P.px+940,P.py-750,60,90)
    r42 = (P.px+1000,P.py-650,500,40)
    r43 = (P.px+1500,P.py-950,50,290)
    r44 = (P.px+950,P.py-950,50,40)
    r45 = (P.px+1000,P.py-1000,300,40)
    r46 = (P.px+1400,P.py-1000,100,40)
    #beach
    r47 = (P.px+600,P.py+500,50,40)
    r48 = (P.px+650,P.py+550,100,40)
    r49 = (P.px+750,P.py+600,1650,40)
    r50 = P.r5_bug.get_rect()
    r51 = P.r5_psy.get_rect()
    r52 = P.r5_lass.get_rect()
    r53 = P.r5_beauty.get_rect()
    r54 = P.r5_tree1.get_rect()
    r55 = P.r5_tree2.get_rect()
    r56 = P.r5_tree3.get_rect()
    r57 = (P.px+2400,P.py-250,50,40)
    r58 = (P.px+1000,P.py+150,50,40)
    rects = [r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.px >= -450:
            player_move(P,rects,[Rect(P.px+850,P.py-850,50,150)])
        else:
            player_move(P,rects,[Rect(P.px+850,P.py-850,50,140)])
    else:
        if P.prog[15][6] == 1 and P.py < 425:
            player_move(P,rects,manual_input = 'u',spd = 3)
        else:
            blit_player(P)
    draw_grass(P,temppx,temppy,-125,675,400,400)
    draw_grass(P,temppx,temppy,-1025,375,100,200,ignore = [(-1075,325),(-1075,275),(-1075,225),(-1025,275)])
    draw_grass(P,temppx,temppy,-625,375,400,300)
    draw_grass(P,temppx,temppy,-1275,775,600,200)
    draw_grass(P,temppx,temppy,-1675,275,200,100,ignore = [(-1675,275),(-1725,275)])
    draw_grass(P,temppx,temppy,-1875,375,500,200)
    draw_grass(P,temppx,temppy,-625,1225,500,300)
    if not tree1:
        P.r5_tree1.blit(temppx,temppy)
    if not tree2:
        P.r5_tree2.blit(temppx,temppy)
    if not tree3:
        P.r5_tree3.blit(temppx,temppy)
    if not psy:
        P.r5_psy.move(temppx,temppy)
        draw_grass(P,P.r5_psy.x,P.r5_psy.y,-125,675,400,400,[temppx,temppy])
    if not bug:
        P.r5_bug.move(temppx,temppy)
        draw_grass(P,P.r5_bug.x,P.r5_bug.y,-1275,775,600,200,[temppx,temppy])
    if not lass:
        P.r5_lass.move(temppx,temppy)
    if not beauty:
        P.r5_beauty.move(temppx,temppy)
    if P.r5_rival:
        if not rival:
            P.r5_rival.move(temppx,temppy)
            draw_grass(P,P.r5_rival.x,P.r5_rival.y,-1675,275,200,100,[temppx,temppy],ignore = [(-1675,275),(-1725,275)])



def route_5_f(P,temppx,temppy,tim):
    P.surface.blit(P.r5_f,(temppx+401,temppy-657))
    P.surface.blit(P.r5_foam,(temppx+211,temppy+298+abs(P.foam)))
    # if P.py > 625:
    #     P.surface.blit(P.r3_fence,(temppx+4397,temppy-374))
    draw_lamps(P, temppx, temppy, [6438], [550])
    #set_sky(P)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+1565,temppy-1401))
    show_location(P, P.loc_txt, tim)

def route_5(P,enter = False,wx = 0,wy = 0) -> None:
    if P.song != "music/route_5.wav":
        P.song = "music/route_5.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    beachx = [725,775,825,875,925,975,1025,1075,1125,1175,1225,1275,1325,1375,1425,1475,1525,1575,1625,1675,1725,1775,1825,1875,1925,1975,2025,2075,2125,2175]
    beachy = [590,600,605,610,610,615,615,615,610,605,600,595,590,585,580,580,580,580,585,590,595,600,605,610,615,615,615,610,610,605]
    P.r5_tree1 = cut_tree(P,2150,-300,20)
    P.r5_tree2 = cut_tree(P,2200,-250,21)
    P.r5_tree3 = cut_tree(P,2150,-200,19)
    P.habitat = 'grass'
    move = True
    # wx = 0
    # wy = 0
    if P.prog[0] == 99:
        P.r5_rival = npc.NPC(P,'Rival',P.save_data.rival,[2100,-50],[['l',100]],["","",""])
    else:
        P.r5_rival = None
    tim = 0
    beach_poke = 0
    set_location(P)
    if enter == False:
        route_5_b(P,wx,wy,beachx,beachy,beach_poke)
        route_5_p(P,P.px,P.py,False)
        route_5_f(P,P.px,P.py,tim)
        fade_in(P)
    end = True
    m = 0
    while end:
        print(P.px,P.py)
        #print(beach_poke)
        if type(beach_poke) == float and tim%10 == 0:
            if random.random() < beach_poke:
                beach_poke = [random.randint(0,len(beachx)-1),random.randint(20,150)]
        route_5_b(P,wx,wy,beachx,beachy,beach_poke)
        if move == True and P.r5_psy.trainer_check():
            move = False
        if move == True and P.r5_bug.trainer_check():
            move = False
        if move == True and P.r5_lass.trainer_check():
            move = False
        if move == True and P.r5_beauty.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        route_5_p(P,temppx,temppy,move)
        route_5_f(P,temppx,temppy,tim)
        if P.px == -1875 and P.prog[0] == 99:
            if P.py == 375:
                P.r5_rival = npc.NPC(P,'Rival',P.save_data.rival,[2100,-50],[['mu',20],['mr',40],['r',60]],["","",""])
            else:
                P.r5_rival = npc.NPC(P,'Rival',P.save_data.rival,[2100,-50],[['md',P.r5_rival.y_dist()*2/5],['mr',40],['r',60]],["","",""])
            move = False
            P.prog[0] += 1
        if P.prog[0] == 100 and P.r5_rival.x == 2200:
            te = P.surface.copy()
            txt(P,"Hey "+P.save_data.name+"!", "Looks like you have some free","time on your hands.")
            txt(P,"It's been a while since our","last battle. I'm excited to","see how strong you've gotten!")
            txt(P,"You better not go easy on me!","I've been training pretty hard","for this fight!")
            play_music(P,"music/trainer_battle.wav",0)
            battle(P,["Rival "+P.save_data.rival,poke.Poke('Pidgeotto',[31,0,334,"Aerial Ace",-1,"Return",-1,"Feather Dance",-1,"Sand Attack",-1,None,None,0,"Poke Ball",380,'Keen Eye']),get_rival_poke(P,0),get_rival_poke(P,2),get_rival_poke(P,1),poke.Poke('Mega_Manectric',[34,0,334,"Discharge",-1,"Bite",-1,"Thunder Fang",-1,"Quick Attack",-1,None,None,0,"Poke Ball",200,'Intimidate'])])
            play_music(P,"music/route_5.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            txt(P,"Haha, looks like you were just as","strong as I thought you'd be!","")
            txt(P,"You may have beaten me this","time, but I won't give up that","easily!")
            txt(P,"Well I'll be going on ahead!","Good luck out there!")
            #change old rival
            P.r5_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.r5_rival.x,P.r5_rival.y],[['ml',100],['md',160]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 101 and P.r5_rival.y == 350:
            move = True
            P.prog[0] += 1
            P.r5_rival = None
        if P.px == -5525 and P.py == 225 and face_u(P) and P.prog[15][6] == 0:
            if P.prog[15][0] == 0:
                txt(P,"The Lopunny is eyeing you","funny.")
                print_mega_area(P)
            elif P.prog[15][6] == 0:
                txt(P,"The Lopunny is eyeing you","funny.")
                if in_party(P,'Lopunny',True):
                    new_txt(P)
                    write(P,"Approach the Lopunny?")
                    if choice(P):
                        move = False
                        P.prog[15][6] += 1
                else:
                    txt(P,"You should bring a Lopunny","before approaching it.")
        if P.py == 425 and P.prog[15][6] == 1:
            te = P.surface.copy()
            txt(P,"The Lopunny attacked!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Lopunny' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Lopunny',[30,1,334,'Dizzy Punch',-1,None,None,None,None,None,None,None,None,0,"Poke Ball",200,'Dodge'])],no_pc = True)
            play_music(P,"music/route_5.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][6] = 0
                txt(P,"The Lopunny didn't seem very","happy with how quickly you","lost the battle.")
                txt(P,"It drove you away from the","clearing!")
                fade_out(P)
                P.p = P.d1
                P.px = -5525
                P.py = 175
                route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                route_5_p(P,P.px,P.py,False)
                route_5_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][6] += 1
                txt(P,"The Lopunny looks quite happy!","It handed you a mysterious","stone before leaving.")
                add_item(P,'Lopunnite',1)
                fade_out(P)
                P.r3_lop = None
                route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                route_5_p(P,P.px,P.py,False)
                route_5_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
        if trainer_check(P,P.r5_psy,"music/route_5.wav"):
            P.r5_psy = npc.NPC(P,'Psychic','Charlie',[P.r5_psy.x,P.r5_psy.y],[['mr',40],['r',60],['md',40],['d',80],['ml',40],['l',100],['mu',40],['u',60]],["I'm just keeping you on your","toes! You never know what can", "happen in a Pokemon battle!"],tim = P.r5_psy.tim,curr = P.r5_psy.curr,extra_walk = P.r5_psy.extra_walk)
            move = True
        if trainer_check(P,P.r5_bug,"music/route_5.wav"):
            P.r5_bug = npc.NPC(P,'Bug Catcher','Ethan',[P.r5_bug.x,P.r5_bug.y],[['mr',80],['r',120],['ml',80],['l',80]],["Sorry about that! You're just","kinda funny looking, so I", "mistook you for a Pokemon!"],tim = P.r5_bug.tim,curr = P.r5_bug.curr,extra_walk = P.r5_bug.extra_walk)
            move = True
        if trainer_check(P,P.r5_lass,"music/route_5.wav"):
            P.r5_lass = npc.NPC(P,'Lass','Charlie',[P.r5_lass.x,P.r5_lass.y],[['mr',80],['r',40],['ml',80],['l',60],['md',40],['d',120],['mu',40],['u',40]],["We should play again sometime!","It's boring running around all","by myself!"],tim = P.r5_lass.tim,curr = P.r5_lass.curr,extra_walk = P.r5_lass.extra_walk)
            move = True
        if trainer_check(P,P.r5_beauty,"music/route_5.wav"):
            P.r5_beauty = npc.NPC(P,'Beauty','Ethan',[P.r5_beauty.x,P.r5_beauty.y],[['d',80]],["Come on, I just wanted to have","a little fun! Now my Pokemon", "are all beat up."],tim = P.r5_beauty.tim,curr = P.r5_beauty.curr,extra_walk = P.r5_beauty.extra_walk)
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.r5_psy.talk():
                        if P.r5_psy.trainer:
                            move = False
                        else:
                            route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_5_p(P,P.px,P.py,False)
                            route_5_f(P,P.px,P.py,tim)
                            P.r5_psy.write()
                    elif P.r5_bug.talk():
                        if P.r5_bug.trainer:
                            move = False
                        else:
                            route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_5_p(P,P.px,P.py,False)
                            route_5_f(P,P.px,P.py,tim)
                            P.r5_bug.write()
                    elif P.r5_lass.talk():
                        if P.r5_lass.trainer:
                            move = False
                        else:
                            route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_5_p(P,P.px,P.py,False)
                            route_5_f(P,P.px,P.py,tim)
                            P.r5_lass.write()
                    elif P.r5_beauty.talk():
                        if P.r5_beauty.trainer:
                            move = False
                        else:
                            route_5_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_5_p(P,P.px,P.py,False)
                            route_5_f(P,P.px,P.py,tim)
                            P.r5_beauty.write()
                    elif next_to(P,2400,-250) and P.prog[6][51] == 0:
                        txt(P,P.save_data.name + " found a", "Heart Scale!")
                        txt(P,P.save_data.name + " put the Heart Scale","in the Items pocket.")
                        add_item(P,"Heart Scale",1)
                        P.prog[6][51] = 1
                    elif next_to(P,1000,150) and P.prog[6][52] == 0:
                        txt(P,P.save_data.name + " found a", "Heart Scale!")
                        txt(P,P.save_data.name + " put the Heart Scale","in the Items pocket.")
                        add_item(P,"Heart Scale",1)
                        P.prog[6][52] = 1
                    elif type(beach_poke) == list and P.px+beachx[beach_poke[0]] == 350 and P.py == -275 and face_d(P):
                        te = P.surface.copy()
                        txt(P,"The Pokemon came out of the","water!")
                        P.habitat = "beach"
                        P.song = "music/wild_battle.wav"
                        pygame.mixer.music.load(P.song)
                        set_mixer_volume(P,P.vol)
                        pygame.mixer.music.play(0)
                        rando = random.random()
                        if rando < 0.2:
                            r = random.randint(27,32)
                            if r < 29:
                                battle(P,[poke.Poke('Krabby',[r,random.randint(0,1),334,"Bubble Beam",-1,"Stomp",-1,"Harden",-1,"Mud Shot",-1,None,None,0,"Poke Ball"])])
                            elif r < 31:
                                battle(P,[poke.Poke('Krabby',[r,random.randint(0,1),334,"Bubble Beam",-1,"Metal Claw",-1,"Protect",-1,"Mud Shot",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Kingler',[r,random.randint(0,1),334,"Bubble Beam",-1,"Stomp",-1,"Harden",-1,"Mud Shot",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .2 and rando < .35:
                            r = random.randint(30,33)
                            if r < 33:
                                battle(P,[poke.Poke('Mareanie',[r,random.randint(0,1),334,"Toxic Spikes",-1,"Protect",-1,"Venoshock",-1,"Spike Cannon",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Mareanie',[r,random.randint(0,1),334,"Toxic Spikes",-1,"Recover",-1,"Venoshock",-1,"Spike Cannon",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .35 and rando < .55:
                            r = random.randint(27,32)
                            if r < 31:
                                battle(P,[poke.Poke('Corphish',[r,random.randint(0,1),334,"Night Slash",-1,"Double Hit",-1,"Protect",-1,"Bubble Beam",-1,None,None,0,"Poke Ball"])])
                            elif r < 32:
                                battle(P,[poke.Poke('Crawdaunt',[r,random.randint(0,1),334,"Night Slash",-1,"Double Hit",-1,"Protect",-1,"Bubble Beam",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Crawdaunt',[r,random.randint(0,1),334,"Night Slash",-1,"Double Hit",-1,"Protect",-1,"Razor Shell",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .55 and rando < .8:
                            r = random.randint(28,32)
                            g = random.randint(0,1)
                            n = ['Frillish_M','Frillish_F']
                            if r < 32:
                                battle(P,[poke.Poke(n[g],[r,g,334,"Water Pulse",-1,"Ominous Wind",-1,"Recover",-1,"Night Shade",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke(n[g],[r,g,334,"Brine",-1,"Ominous Wind",-1,"Recover",-1,"Night Shade",-1,None,None,0,"Poke Ball"])])
                        else:
                            r = random.randint(28,32)
                            if r < 32:
                                battle(P,[poke.Poke('Binacle',[r,random.randint(0,1),334,"Slash",-1,"Mud-Slap",-1,"Clamp",-1,"Ancient Power",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Binacle',[r,random.randint(0,1),334,"Slash",-1,"Hone Claws",-1,"Clamp",-1,"Ancient Power",-1,None,None,0,"Poke Ball"])])
                        P.song = "music/route_5.wav"
                        P.habitat = "grass"
                        pygame.mixer.music.load(P.song)
                        set_mixer_volume(P,P.vol)
                        pygame.mixer.music.play(-1)
                        P.surface.blit(te,(0,0))
                        fade_in(P)
                        beach_poke = 0
                    elif next_to(P,P.r5_tree1.x,P.r5_tree1.y):
                        P.r5_tree1.cut()
                    elif next_to(P,P.r5_tree2.x,P.r5_tree2.y):
                        P.r5_tree2.cut()
                    elif next_to(P,P.r5_tree3.x,P.r5_tree3.y):
                        P.r5_tree3.cut()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.py == 1325 and face_u(P):
            P.py = -25
            P.px += 500
            P.loc = "verde"
            verde(P,True)
            end = False
        if P.py == -325 and face_d(P):
            P.py = 1275
            P.px += 1600
            P.loc = "isola"
            isola(P,True,wx,wy)
            end = False
        #right
        if move and (wild_grass(P,-625,1225,500,300) or wild_grass(P,-125,675,400,400) or wild_grass(P,-1025,375,100,200,ignore = [(-1075,325),(-1075,275),(-1075,225),(-1025,275)]) or wild_grass(P,-625,375,400,300) or wild_grass(P,-1275,775,600,200) or wild_grass(P,-1675,275,200,100,ignore = [(-1675,275),(-1725,275)]) or wild_grass(P,-1875,375,500,200)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.1:
                r = random.randint(28,32)
                if r < 29:
                    battle(P,[poke.Poke('Scyther',[r,random.randint(0,1),334,"False Swipe",-1,"Agility",-1,"Wing Attack",-1,"Fury Cutter",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Scyther',[r,random.randint(0,1),334,"Slash",-1,"Agility",-1,"Wing Attack",-1,"Fury Cutter",-1,None,None,0,"Poke Ball"])])
            elif rando >= .1 and rando < .25:
                r = random.randint(28,33)
                if r < 31:
                    battle(P,[poke.Poke('Sandile',[r,random.randint(0,1),334,"Mud-Slap",-1,"Swagger",-1,"Crunch",-1,"Sand Tomb",-1,None,None,0,"Poke Ball"])])
                elif r < 32:
                    battle(P,[poke.Poke('Sandile',[r,random.randint(0,1),334,"Mud-Slap",-1,"Swagger",-1,"Crunch",-1,"Dig",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Krokorok',[r,random.randint(0,1),334,"Mud-Slap",-1,"Swagger",-1,"Crunch",-1,"Dig",-1,None,None,0,"Poke Ball"])])
            elif rando >= .25 and rando < .45:
                r = random.randint(28,32)
                if r < 32:
                    battle(P,[poke.Poke('Foongus',[r,random.randint(0,1),334,"Growth",-1,"Bide",-1,"Sweet Scent",-1,"Giga Drain",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Foongus',[r,random.randint(0,1),334,"Growth",-1,"Bide",-1,"Toxic",-1,"Giga Drain",-1,None,None,0,"Poke Ball"])])
            elif rando >= .45 and rando < .6:
                r = random.randint(28,32)
                if r < 31:
                    battle(P,[poke.Poke('Cottonee',[r,random.randint(0,1),334,"Fairy Wind",-1,"Poison Powder",-1,"Giga Drain",-1,"Charm",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Cottonee',[r,random.randint(0,1),334,"Endeavor",-1,"Poison Powder",-1,"Giga Drain",-1,"Charm",-1,None,None,0,"Poke Ball"])])
            elif rando >= .6 and rando < .8:
                r = random.randint(27,33)
                if r < 31:
                    battle(P,[poke.Poke('Buizel',[r,random.randint(0,1),334,"Pursuit",-1,"Aqua Jet",-1,"Double Hit",-1,"Swift",-1,None,None,0,"Poke Ball"])])
                elif r < 32:
                    battle(P,[poke.Poke('Buizel',[r,random.randint(0,1),334,"Pursuit",-1,"Aqua Jet",-1,"Double Hit",-1,"Whirlpool",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Floatzel',[r,random.randint(0,1),334,"Pursuit",-1,"Aqua Jet",-1,"Double Hit",-1,"Swift",-1,None,None,0,"Poke Ball"])])
            else:
                r = random.randint(27,32)
                if r < 29:
                    battle(P,[poke.Poke('Spinarak',[r,random.randint(0,1),334,"Infestation",-1,"Shadow Sneak",-1,"Fury Swipes",-1,"Sucker Punch",-1,None,None,0,"Poke Ball"])])
                elif r < 31:
                    battle(P,[poke.Poke('Spinarak',[r,random.randint(0,1),334,"Spider Web",-1,"Shadow Sneak",-1,"Fury Swipes",-1,"Sucker Punch",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Ariados',[r,random.randint(0,1),334,"Infestation",-1,"Shadow Sneak",-1,"Fury Swipes",-1,"Sucker Punch",-1,None,None,0,"Poke Ball"])])
            P.song = "music/route_5.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if tim%20 == 0:
            if P.r3_slow == P.r3_slow1:
                P.r3_slow = P.r3_slow2
            else:
                P.r3_slow = P.r3_slow1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if type(beach_poke) == list:
                beach_poke[1] -= 1
                if beach_poke[1] == 0:
                    beach_poke = 0
            else:
                beach_poke += 0.001
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def isola_b(P,wx,wy,pcx,pcy,gy):
    draw_waves(P, wx, wy)
    if P.px == -375 and P.py > 75 and P.py <= 125:
        pcx = (-75 + P.py)
        pcy = ((-75 + P.py)/5)
    P.surface.blit(P.pc_black,(P.px+730,P.py+130))
    P.surface.blit(P.pcdr, (P.px + 775 + pcx, P.py + 130 - pcy))
    P.surface.blit(P.pcdl, (P.px + 738 - pcx, P.py + 130 - pcy))
    P.surface.blit(P.isola_back, (P.px + 100, P.py - 1400))
    P.surface.blit(P.isola_foam,(P.px+502,P.py-220+abs(P.foam)))
    if P.px == -825 and P.py > 75 and P.py <= 125:
        blit_small_door(P,115)
    if P.px == -975 and P.py > 475 and P.py <= 525:
        blit_small_door(P,515)
    if P.px == -525 and P.py > 675 and P.py <= 725:
        blit_small_door(P,715)
    P.surface.blit(P.gondola, (P.px + 1600, P.py - 200 + abs(P.foam)))
    P.surface.blit(P.gondola, (P.px + 1600, P.py + 200 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 1611, P.py + 260 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 1612, P.py + 240 + abs(P.foam)+gy))

    #P.surface.blit(P.r5_back,(P.px-150,P.py-1600))
    P.surface.blit(P.r5_beach,(P.px-1192,P.py-1080+abs(P.foam)))
    P.surface.blit(P.r5_f,(P.px-1199,P.py-2257))
    P.surface.blit(P.r5_foam,(P.px-1389,P.py-1302+abs(P.foam)))

def isola_p(P,temppx,temppy,move,gond,gy):
    aroma = P.isola_aroma.y_dist() > 0
    if aroma:
        P.isola_aroma.move()
    if P.isola_lat:
        lat = P.isola_lat.y_dist() > 0
        lato = P.isola_lat.y_dist() > 0
        if lat:
            P.isola_lat.move()
        if lato:
            P.isola_lato.move()
    if P.isola_fish:
        fish = P.isola_fish.y_dist() > 0
        if fish:
            P.isola_fish.move()
    if P.isola_seed:
        seed = P.isola_seed.y_dist() > 0
        if seed:
            P.isola_seed.move()
    P.isola_host.move()
    r1 = (P.px+550,P.py+200,50,140)
    r2 = (P.px+600,P.py+150,150,40)
    r3 = (P.px+750,P.py+100,50,40)
    r4 = (P.px+800,P.py+150,400,40)
    r5 = (P.px+600,P.py+350,300,40)
    r6 = (P.px+850,P.py+400,50,140)
    r7 = (P.px+1050,P.py+400,50,140)
    r8 = (P.px+1050,P.py+350,550,40)
    r9 = (P.px+1200,P.py+100,50,40)
    r10 = (P.px+1250,P.py-50,50,240)
    r11 = (P.px+1450,P.py+150,150,40)
    r12 = (P.px+1600,P.py+200,50,140)
    r13 = (P.px+1450,P.py-50,50,190)
    r14 = (P.px+1500,P.py-50,100,40)
    r15 = (P.px+1600,P.py-200,50,140)
    r16 = (P.px+1400,P.py-250,200,40)
    r17 = (P.px+1350,P.py-300,50,40)
    r18 = (P.px+1150,P.py-250,200,40)
    r19 = (P.px+1000,P.py-50,250,40)
    r20 = (P.px+950,P.py-250,50,190)
    r21 = (P.px+500,P.py-250,450,40)
    r22 = (P.px+450,P.py-400,50,140)
    r23 = (P.px+500,P.py-450,400,40)
    r24 = (P.px+900,P.py-500,50,40)
    r25 = (P.px+950,P.py-1000,50,590)
    r26 = (P.px+1150,P.py-1000,50,740)
    r27,r28 = r1,r1
    if P.isola_lat:
        r27 = P.isola_lat.get_rect()
        r28 = P.isola_lato.get_rect()
    r29 = P.isola_aroma.get_rect()
    #temp
    #r30 = (P.px+1000,P.py-800,150,40)
    r31,r32 = r1,r1
    if P.isola_fish:
        r31 = P.isola_fish.get_rect()
    if P.isola_seed:
        r32 = P.isola_seed.get_rect()
    rects = [r32,r31,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+1611,P.py+313+abs(P.foam)+gy))
        P.surface.blit(P.p,(P.px+1610,P.py+290+abs(P.foam)+gy))
    else:
        if move:
            if P.prog[0] == 89 and P.px in [-625,-725] and P.py == 975 and (face_l(P) or face_r(P)):
                player_move(P,rects,manual_input = 'd')
            else:
                player_move(P,rects)
        else:
            blit_player(P)
    if P.isola_lat:
        if not lat:
            P.isola_lat.move(temppx,temppy)
        if not lato:
            P.isola_lato.move(temppx,temppy)
    if not aroma:
        P.isola_aroma.move(temppx,temppy)
    if P.isola_fish:
        if not fish:
            P.isola_fish.move(temppx,temppy)
    if P.isola_seed:
        if not seed:
            P.isola_seed.move(temppx,temppy)

def isola_f(P,temppx,temppy,tim):
    P.surface.blit(P.isola_f, (temppx + 499, temppy - 499))
    set_sky(P)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+715,temppy-51))
    show_location(P, P.loc_txt, tim)

def isola(P,enter = False,wx = 0,wy = 0) -> None:
    #sci_tim = None,sci_curr = None
    if P.song != "music/isola.wav":
        P.song = "music/isola.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] == 98:
        P.prog[0] += 1
    P.isola_host = npc.NPC(P,'Hostess','Harper',[600,-500],[['d',40]],["","",""])
    if P.prog[0] == 89:
        P.isola_lat = npc.NPC(P,'Latias','Harper',[850,-300],[['l',40]],["Where could she have gone?","I've been looking everywhere","for her!","Huh? Sorry I don't think we've","met before...You must have the","wrong person."])
        P.isola_lato = npc.NPC(P,'Latios','Harper',[800,-300],[['r',40]],["I'm sure she'll be okay. I","just hope she comes back to us","soon..."])
        P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-700],[['u',40]],["Hey! I just saw some strange","people making their way down","to Route 4.","They looked like they were up","to something real suspicious.","","You look like someone that can","handle them. Could you go over","and check it out?"])
    else:
        P.isola_lat = None
        P.isola_lato = None
        P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-450],[['md',60],['d',100],['mu',60],['u',140]],["Our town may be small, but","that's part of what makes it","so nice!","It's like we're one big family","living together in our own","little village!"])
    if not (datetime.datetime.today().weekday() == 6 and get_time() >= 6 and P.prog[16] == 2):
        P.isola_fish = npc.NPC(P,'Fisherman','Harper',[1550,-150],[['r',40]],["Hey, thanks again for the","Seedot! It's nice to have a","little friend to travel with!","If you ever find the time, you","should come meet me in Alto","Mare Square on Sundays!","I'll have some nice items that","I've collected throughout the","week for you to buy!"])
        if P.px == -1175 and P.py in [375,425]:
            P.px += 50
        if P.prog[16] == 2:
            P.isola_seed = npc.NPC(P,'Seedot','Harper',[1550,-100],[['d',40]],["SEEDOT!!!","",""])
        else:
            P.isola_seed = None
    else:
        P.isola_fish = None
        P.isola_seed = None
    set_location(P)
    gond = 0
    gy = 0
    fade = None
    move = True
    tim = 0
    pcx = 0
    pcy = 0
    if enter == False:
        isola_b(P,wx,wy,pcx,pcy,gy)
        isola_p(P,P.px,P.py,False,gond,gy)
        isola_f(P,P.px,P.py,tim)
        fade_in(P)
    end = True
    m = 0
    while end:
        if P.px in [-725,-625] and P.py == 975 and P.prog[0] == 89:
            dir = 'r'
            P.p = P.l1
            if P.px == -625:
                dir = 'l'
                P.p = P.r1
            P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-700],[[dir,40]],["Hey! I just saw some strange","people making their way down","to Route 4.","They looked like they were up","to something real suspicious.","","You look like someone that can","handle them. Could you go over","and check it out?"])
            isola_b(P,wx,wy,pcx,pcy,gy)
            isola_p(P,P.px,P.py,False,gond,gy)
            isola_f(P,P.px,P.py,tim)
            P.isola_aroma.write()
            P.isola_aroma = npc.NPC(P,'Aroma Lady','Harper',[1050,-700],[['u',40]],["Hey! I just saw some strange","people making their way down","to Route 4.","They looked like they were up","to something real suspicious.","","You look like someone that can","handle them. Could you go over","and check it out?"])
        print(P.px,P.py)
        isola_b(P,wx,wy,pcx,pcy,gy)
        temppx = P.px
        temppy = P.py
        isola_p(P,temppx,temppy,move,gond,gy)
        isola_f(P, temppx, temppy, tim)
        if gond == 1:
            gond = 2
            fade_in(P)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and gond == 0 and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -1175 and P.py == 25 and face_r(P):
                        nxtl = gondolier(P)
                        if nxtl != "Isola Town":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.py == 1025 and face_u(P):
                        #change
                        txt(P,"There's some strange barrier","stopping you from continuing.")
                    elif P.px == -225 and P.py == 675 and face_u(P):
                        txt(P,"Hello! Are you here to join","the Isola Town Water Race?")
                        txt(P,"No? Well you're welcome to","come back once you've gotten","certified!")
                    elif P.px == -1175 and P.py in [375,425,475] and face_r(P):
                        txt(P,"There's a gondola tied to the","end of this dock.")
                    elif P.isola_lat and P.isola_lat.talk():
                        isola_b(P,wx,wy,pcx,pcy,gy)
                        isola_p(P,temppx,temppy,False,gond,gy)
                        isola_f(P,temppx,temppy,tim)
                        P.isola_lat.write()
                    elif P.isola_lato and P.isola_lato.talk():
                        isola_b(P,wx,wy,pcx,pcy,gy)
                        isola_p(P,temppx,temppy,False,gond,gy)
                        isola_f(P,temppx,temppy,tim)
                        P.isola_lato.write()
                    elif P.isola_seed and P.isola_seed.talk():
                        isola_b(P,wx,wy,pcx,pcy,gy)
                        isola_p(P,temppx,temppy,False,gond,gy)
                        isola_f(P,temppx,temppy,tim)
                        P.font = pygame.font.SysFont("courier", 40, bold = False, italic = True)
                        P.isola_seed.write()
                        P.font = pygame.font.SysFont("courier", 40, bold = True, italic = False)
                    elif P.isola_fish and P.isola_fish.talk():
                        isola_b(P,wx,wy,pcx,pcy,gy)
                        isola_p(P,temppx,temppy,False,gond,gy)
                        isola_f(P,temppx,temppy,tim)
                        if P.prog[16] == 0:
                            txt(P,"Hey there traveler! I enjoy","searching for rare items out","in the ocean!")
                            txt(P,"Lately though, I've been","feeling kinda lonely all by","myself out there.")
                            txt(P,"Hey! What if you brought me a", "nice Pokemon to accompany me", "on my travels?")
                            txt(P,"I really love Seedots! How","about you bring me one of", "those?")
                            txt(P,"But make sure it's friendly!","I wouldn't want it to get","scared out in the ocean!")
                            P.prog[16] += 1
                        elif P.prog[16] == 1:
                            t = P.surface.copy()
                            new_txt(P)
                            write(P,"Did you get me a Seedot?")
                            if choice(P):
                                fade_out(P)
                                ans = trade_poke(P,"Seedot")
                                P.surface.blit(t,(0,0))
                                fade_in(P)
                                if ans != None:
                                    if ans.friend >= 300:
                                        txt(P,"Wow! You really brought me a","Seedot! And it's so friendly!")
                                        txt(P,"I'll be sure to work really","hard to find all sorts of","amazing items!")
                                        txt(P,"You can catch me in the Alto","Mare Square on Sundays where","I'll be selling what I find!")
                                        txt(P,"I'm sure I'll have some stuff","that you'll find useful!")
                                        P.party.remove(ans)
                                        P.prog[16] += 1
                                    else:
                                        txt(P,"Hmm...that Seedot is really","cute, but I would prefer if","it was a little friendlier.")
                                        txt(P,"I want to be sure it trusts","me to bring it out in the","ocean, you know?")
                                else:
                                    txt(P,"Oh, well I hope you're still","working on getting me one!")
                                    txt(P,"Don't forget I would like it","to be on the friendlier side!")
                            else:
                                txt(P,"Oh, well I hope you're still","working on getting me one!")
                                txt(P,"Don't forget I would like it","to be on the friendlier side!")
                        else:
                            P.isola_fish.write()
                    elif P.isola_aroma.talk():
                        isola_b(P,wx,wy,pcx,pcy,gy)
                        isola_p(P,temppx,temppy,False,gond,gy)
                        isola_f(P,temppx,temppy,tim)
                        P.isola_aroma.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            end = False
            fade = P.song
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.py == -275 and P.px in [-525,-575,-625] and face_d(P):
            P.py = 525
            P.px -= 1600
            P.loc = 'route_4'
            route_4(P,True,wx,wy)
            end = False
        if P.py == 1325 and face_u(P):
            P.py = -275
            P.px -= 1600
            P.loc = 'route_5'
            update_locs(P)
            route_5(P,True,wx,wy)
            end = False
        if P.px == -825 and P.py == 125 and face_u(P):
            P.loc = "house_3_2"
            P.px = -25
            P.py = -75
            end = False
        if P.px == -975 and P.py == 525 and face_u(P):
            P.loc = "house_3_3"
            P.px = -25
            P.py = -75
            end = False
        if P.px == -525 and P.py == 725 and face_u(P):
            P.loc = "house_3_4"
            P.px = -25
            P.py = -75
            end = False
        if P.py == 125 and P.px == -375 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_isola"
            fade = P.song
            end = False
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def route_4_b(P,wx,wy):
    draw_waves(P,wx,wy)
    P.surface.blit(P.r4_back,(P.px+50,P.py-1000))
    P.surface.blit(P.r4_foam,(P.px+2401,P.py+497 + abs(P.foam)))
    P.surface.blit(P.isola_foam,(P.px+2102,P.py-1020+abs(P.foam)))
    if P.prog[6][46] == 0:
        P.surface.blit(P.item_out,(P.px+500,P.py-300))
        P.surface.blit(P.dark_grass,(P.px+500,P.py-310))
    if P.prog[6][47] == 0:
        P.surface.blit(P.item_out,(P.px+2250,P.py+800))
        P.surface.blit(P.dark_grass,(P.px+2250,P.py+790))
    if P.prog[15][10] != 2:
        P.surface.blit(P.char_shad,(P.px+1570,P.py-230))
        P.surface.blit(P.r4_kang,(P.px+1550,P.py-280))

def route_4_p(P,temppx,temppy,move = False):
    tree1 = P.r4_tree1.y_dist() > 0
    tree2 = P.r4_tree2.y_dist() > 0
    if P.r4_expf:
        exp = P.r4_expf.y_dist() > 0
        if exp:
            P.r4_expf.move()
    if tree1:
        P.r4_tree1.blit()
    if tree2:
        P.r4_tree2.blit()
    expert = P.r4_expert.y_dist() > 0
    battle = P.r4_battle.y_dist() > 0
    fish = P.r4_fish.y_dist() > 0
    if expert:
        P.r4_expert.move()
        draw_grass(P,P.r4_expert.x,P.r4_expert.y,-125,-25,700,150,[P.px,P.py],dark = True)
    if battle:
        P.r4_battle.move()
    if fish:
        P.r4_fish.move()
    #rects start
    r1 = (P.px+500,P.py-350,1150,40)
    r2 = (P.px+450,P.py-300,50,240)
    r3 = (P.px+400,P.py-50,50,90)
    r4 = (P.px+450,P.py+50,50,390)
    r5 = (P.px+500,P.py+450,1750,40)
    r6 = (P.px+1650,P.py-300,50,140)
    r7 = (P.px+1000,P.py-150,650,40)
    r8 = (P.px+1000,P.py-100,50,290)
    r9 = (P.px+1000,P.py+200,650,40)
    r10 = (P.px+1600,P.py,50,190)
    r11 = (P.px+1650,P.py-50,800,40)
    r12 = (P.px+2450,P.py-400,50,490)
    r13 = (P.px+2450,P.py+250,50,590)
    r14 = (P.px+2490,P.py+90,10,10)
    if P.px == -2075:
        if P.py == 150:
            r14 = (P.px+2450,P.py+100,50,15)
        elif P.py == 100:
            r14 = (P.px+2450,P.py+225,50,10)
    r15 = (P.px+2450,P.py+240,10,10)
    r16 = (P.px+2650,P.py-400,50,1440)
    r17 = (P.px+2250,P.py+850,250,40)
    r18 = (P.px+2250,P.py+900,50,190)
    r19 = (P.px+2450,P.py+1050,200,40)
    r20 = (P.px+2450,P.py+1100,50,390)
    r21 = (P.px+2200,P.py+500,50,340)
    r22 = (P.px+1300,P.py+1500,1150,40)
    r23 = (P.px+1100,P.py+1050,1150,40)
    r24 = (P.px+1050,P.py+1100,50,40)
    r25 = (P.px+1100,P.py+1150,150,40)
    r26 = (P.px+1250,P.py+1150,50,340)
    r27 = (P.px+1850,P.py,50,40)
    r28 = (P.px+2100,P.py+100,50,40)
    r29 = (P.px+1350,P.py+250,50,40)
    r30 = (P.px+1350,P.py+400,50,40)
    r31 = (P.px+1250,P.py+300,50,40)
    r32 = P.r4_tree1.get_rect()
    r33 = P.r4_tree2.get_rect()
    r34,r35,r36 = r1,r1,r1
    if P.prog[6][46] == 0:
        r34 = (P.px+500,P.py-300,50,40)
    if P.prog[6][47] == 0:
        r35 = (P.px+2250,P.py+800,50,40)
    if P.prog[6][48] == 0:
        r36 = (P.px+1100,P.py+1100,50,40)
    r37 = P.r4_expert.get_rect()
    r38 = P.r4_battle.get_rect()
    r39 = P.r4_fish.get_rect()
    r40 = r1
    if P.r4_expf:
        r40 = P.r4_expf.get_rect()
    rects = [r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.px <= -2100:
            player_move(P,rects,[],[Rect(P.px+2450,P.py+100,50,150)])
        else:
            if P.px == -975 and P.py in [575,525,475] and face_r(P) and P.prog[15][10] == 0:
                player_move(P,rects,[],[Rect(P.px+2450,P.py+100,50,140)],manual_input = 'l')
            else:
                player_move(P,rects,[],[Rect(P.px+2450,P.py+100,50,140)])
    else:
        if P.prog[0] == 91 and P.r4_latias and P.r4_latias.y == 1300:
            if P.py > -975:
                player_move(P,rects,manual_input = 'd',spd = 3)
            elif P.px < -1625:
                player_move(P,rects,manual_input = 'l',spd = 3)
            else:
                blit_player(P)
        elif P.prog[15][10] == 1:
            if P.px > -1125:
                player_move(P,rects,manual_input = 'r',spd = 3)
            elif P.py > 525:
                player_move(P,rects,manual_input = 'd',spd = 3)
            elif P.py < 525:
                player_move(P,rects,manual_input = 'u',spd = 3)
            else:
                blit_player(P)
        else:
            blit_player(P)
    draw_grass(P,temppx,temppy,-125,575,700,150,ignore = [(-725,575),(-775,575)],dark = True)
    draw_grass(P,temppx,temppy,-125,75,300,250,dark = True)
    draw_grass(P,temppx,temppy,-425,25,400,200,ignore = [(-725,25),(-775,25),(-725,-25),(-775,-25)],dark = True)
    draw_grass(P,temppx,temppy,-1125,25,950,200,ignore = [(-1125,-75),(-1175,-75),(-1125,-125),(-1175,-125),(-1225,-125)],dark = True)
    draw_grass(P,temppx,temppy,-1875,-175,200,400,dark = True)
    draw_grass(P,temppx,temppy,-1175,-825,650,150,ignore = [(-1175,-925),(-1225,-925),(-1275,-925),(-1625,-925),(-1675,-925),(-1725,-925),(-1775,-925),(-1725,-875),(-1775,-875)],dark = True)
    draw_grass(P,temppx,temppy,-925,-1025,700,200,ignore = [(-1425,-1025),(-1475,-1025),(-1525,-1025),(-1575,-1025),(-1525,-1075),(-1575,-1075)],dark = True)
    if not tree1:
        P.r4_tree1.blit(temppx,temppy)
    if not tree2:
        P.r4_tree2.blit(temppx,temppy)
    if not expert:
        P.r4_expert.move(temppx,temppy)
        draw_grass(P,P.r4_expert.x,P.r4_expert.y,-125,-25,700,150,[temppx,temppy],dark = True)
    if not battle:
        P.r4_battle.move(temppx,temppy)
    if not fish:
        P.r4_fish.move(temppx,temppy)
    if P.r4_latias:
        P.r4_latias.move(temppx,temppy)
        draw_grass(P,P.r4_latias.x,P.r4_latias.y,-925,-1025,700,200,[temppx,temppy],ignore = [(-1425,-1025),(-1475,-1025),(-1525,-1025),(-1575,-1025),(-1525,-1075),(-1575,-1075)],dark = True)
        P.r4_rock1.move(temppx,temppy)
        draw_grass(P,P.r4_rock1.x,P.r4_rock1.y,-1175,-825,650,150,[temppx,temppy],ignore = [(-1175,-925),(-1225,-925),(-1275,-925),(-1625,-925),(-1675,-925),(-1725,-925),(-1775,-925),(-1725,-875),(-1775,-875)],dark = True)
        P.r4_rock2.move(temppx,temppy)
        P.r4_manaphy.move(temppx,temppy)
        draw_grass(P,P.r4_manaphy.x,P.r4_manaphy.y,-925,-1025,700,200,[temppx,temppy],ignore = [(-1425,-1025),(-1475,-1025),(-1525,-1025),(-1575,-1025),(-1525,-1075),(-1575,-1075)],dark = True)
    if P.r4_expf:
        if not exp:
            P.r4_expf.move(temppx,temppy)
        

def route_4_f(P,temppx,temppy,tim):
    P.surface.blit(P.r4_f,(temppx+900,temppy+1044))
    P.surface.blit(P.r4_cave,(temppx+400,temppy-100))
    set_sky(P)
    show_location(P,P.loc_txt,tim)

def route_4(P,enter = False,wx = 0,wy = 0) -> None:
    if P.song != "music/route_4.wav":
        P.song = "music/route_4.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.r4_tree1 = cut_tree(P,1350,300,17)
    P.r4_tree2 = cut_tree(P,1300,350,18)
    P.habitat = 'mount_grass'
    if P.prog[0] == 89:
        P.r4_latias = npc.NPC(P,'Latias','Harper',[2300,1200],[['l',80]],["","",""])
        P.r4_manaphy = npc.NPC(P,'Manaphy','Harper',[1800,1250],[['r',80]],["","",""])
        P.r4_rock1 = npc.NPC(P,'Team Rocketm','Harper',[1700,1250],[['r',80]],["","",""])
        P.r4_rock2 = npc.NPC(P,'Team Rocketf','Harper',[1900,1250],[['l',80]],["","",""])
    else:
        P.r4_latias = None
        P.r4_manaphy = None
        P.r4_rock1 = None
        P.r4_rock2 = None
    if P.prog[0] >= 99:
        if P.prog[5][34] == 0:
            P.r4_expf = npc.NPC(P,'Expertf','Stella',[1500,1200],[['l',80]],["Hello there! Not many people","choose to venture all the way","out here.","Perhaps you're looking for a","thrilling battle?",""],["Well that's quite surprising!","I suppose each new generation","really is more talented!"],True,[0,0,0,0],P.r4_team1,34,loc = "route_4")
        else:
            P.r4_expf = npc.NPC(P,'Expertf','Timmy',[1500,1200],[['l',80]],["People say this is a scorch","mark left by a lightning","strike from Thundurus.","It could just be a myth, but","it's exhilarating to think","about isn't it?"])
    else:
        P.r4_expf = None
    set_location(P)
    tim = 0
    gran_talk = 50
    if enter == False:
        route_4_b(P,wx,wy)
        route_4_p(P,P.px,P.py)
        route_4_f(P,P.px,P.py,tim)
        fade_in(P)
    end = True
    move = True
    pause = False
    m = 0
    while end:
        print(P.px,P.py)
        if P.prog[0] == 89 and P.py == -775:
            move = False
            P.r4_latias = npc.NPC(P,'Latias','Harper',[2300,1200],[['u',80]],["","",""])
            route_4_b(P,wx,wy)
            route_4_p(P,P.px,P.py,False)
            route_4_f(P,P.px,P.py,tim)
            P.r4_latias = npc.NPC(P,'Latias','Harper',[2300,1200],[['mr',P.r4_latias.x_dist()*2/5],['mu',40],['u',20]],["","",""])
            P.r4_latias.trainer_walk = ['u',0,20]
            P.prog[0] += 1
        if P.prog[0] == 90 and P.r4_latias.y == 1100:
            txt(P,"She frantically tugs at your","arm and points down the path.")
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['md',80],['ml',60+((P.r4_latias.x-2300)*2/5)],['l',200]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 91 and P.px == -1625:
            P.r4_rock2 = npc.NPC(P,'Team Rocketf','Harper',[1900,1250],[['r',80]],["","",""])
            route_4_b(P,wx,wy)
            route_4_p(P,P.px,P.py,False)
            route_4_f(P,P.px,P.py,tim)
            txt(P,"Hey! We're pretty busy here!", "You had better stay back if","you know what's good for you!")
            txt(P,"Or are you just here looking","for trouble?")
            P.r4_rock2 = npc.NPC(P,'Team Rocketf','Harper',[1900,1250],[['mr',20],['r',100]],["","",""])
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['l',80]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 92 and P.r4_rock2.x == 1950:
            te = P.surface.copy()
            txt(P,"Well if you ain't gonna back","off, I'll just have to force","you to!")
            play_music(P,"music/trainer_battle.wav",0)
            P.habitat = 'mount'
            #battle(P,["Team Rocketf Grunt",poke.Poke('Wynaut',[10,random.randint(0,1),21,"Tackle",35,"Lick",30,"Odor Sleuth",40,None,None,None,None,0,"Poke Ball"])])
            battle(P,["Team Rocketf Grunt",poke.Poke('Ariados',[31,random.randint(0,1),334,"Sucker Punch",-1,"Swords Dance",-1,"Shadow Sneak",-1,"Infestation",-1,None,None,0,"Poke Ball",200,"Insomnia"]),poke.Poke('Seviper',[31,random.randint(0,1),334,"Poison Jab",-1,"Night Slash",-1,"Glare",-1,"Wrap",-1,None,None,0,"Poke Ball",200,"Shed Skin"]),poke.Poke('Mismagius',[32,random.randint(0,1),334,"Magical Leaf",-1,"Will-O-Wisp",-1,"Hex",-1,"Psybeam",-1,None,None,0,"Poke Ball",200,"Levitate"])])
            P.habitat = 'mount_grass'
            P.r4_rock2 = npc.NPC(P,'Team Rocketf','Harper',[P.r4_rock2.x,1250],[['ml',20],['r',200]],["","",""])
            P.r4_rock1 = npc.NPC(P,'Team Rocketm','Harper',[1700,1250],[['mu',20],['mr',120],['d',50]],["","",""])
            play_music(P,"music/route_4.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            txt(P,"Ugh. You're way stronger than","I expected!")
            P.prog[0] += 1
        if P.prog[0] == 94 and P.r4_latias.face() == 'u':
            P.p = P.l1
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['u',1000]],["","",""])
            P.r4_manaphy = npc.NPC(P,'Manaphy','Harper',[1800,1250],[['d',20],['mr',10],['md',20],['ml',20],['mu',20],['mr',10],['d',40],['mr',30],['r',100]],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 93 and P.r4_rock1.face() == 'd':
            P.p = P.u1
            route_4_b(P,wx,wy)
            route_4_p(P,P.px,P.py,False)
            route_4_f(P,P.px,P.py,tim)
            te = P.surface.copy()
            txt(P,"Well she was just softening","you up for me anyways!")
            play_music(P,"music/trainer_battle.wav",0)
            P.habitat = 'mount'
            #battle(P,["Team Rocketm Grunt",poke.Poke('Wynaut',[10,random.randint(0,1),21,"Tackle",35,"Lick",30,"Odor Sleuth",40,None,None,None,None,0,"Poke Ball"])])
            battle(P,["Team Rocketm Grunt",poke.Poke('Loudred',[31,random.randint(0,1),334,"Uproar",-1,"Stomp",-1,"Bite",-1,"Screech",-1,None,None,0,"Poke Ball",200,"Soundproof"]),poke.Poke('Zangoose',[31,random.randint(0,1),334,"Pursuit",-1,"Fury Cutter",-1,"Revenge",-1,"Crush Claw",-1,None,None,0,"Poke Ball",200,"Immunity"]),poke.Poke('Victreebel',[32,random.randint(0,1),334,"Leaf Storm",-1,"Knock Off",-1,"Stun Spore",-1,"Leaf Tornado",-1,None,None,0,"Poke Ball",200,"Chlorophyll"])])
            P.habitat = 'mount_grass'
            P.r4_rock2 = npc.NPC(P,'Team Rocketf','Harper',[P.r4_rock2.x,1250],[['md',10],['mr',30],['mu',20],['mr',50],['mu',100]],["","",""],spd = 1)
            P.r4_rock1 = npc.NPC(P,'Team Rocketm','Harper',[P.r4_rock1.x,P.r4_rock1.y],[['mr',70],['mu',100]],["","",""],spd = 1)
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['l',60],['ml',140],['u',100]],["","",""])
            play_music(P,"music/route_4.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            txt(P,"No way! You beat both of us?","Man, we're gonna get in so","much trouble!")
            txt(P,"I'm gonna get you back for","this! Just you wait!")
            P.prog[0] += 1
        if P.prog[0] == 95 and P.r4_manaphy.x == 1950:
            txt(P,"Manaphy handed you a Mystic","Water!")
            add_item(P,'Mystic Water',1)
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['mr',20],['r',20]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 96 and P.r4_latias.x == 1850:
            txt(P,"She bowed in appreciation","before leaving.")
            P.r4_latias = npc.NPC(P,'Latias','Harper',[P.r4_latias.x,P.r4_latias.y],[['ml',120]],["","",""])
            P.r4_manaphy = npc.NPC(P,'Manaphy','Harper',[P.r4_manaphy.x,P.r4_manaphy.y],[['r',40],['ml',120]],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 97 and P.r4_manaphy.x == 1500:
            move = True
            P.prog[0] += 1
            P.r4_latias = None
            P.r4_manaphy = None
            P.r4_rock1 = None
            P.r4_rock2 = None
        route_4_b(P,wx,wy)
        if move == True and P.r4_expert.trainer_check():
            move = False
        if move == True and P.r4_battle.trainer_check():
            move = False
        if move == True and P.r4_fish.trainer_check():
            move = False
        if move == True and gran_talk > 50 and P.r4_expf and P.r4_expf.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        route_4_p(P,temppx,temppy,move)
        route_4_f(P,temppx,temppy,tim)
        if P.px == -975 and P.py in [575,525,475] and face_r(P):
            if P.prog[15][0] == 0:
                txt(P,"A Kangaskhan is gazing at the","ocean.")
                print_mega_area(P)
            elif P.prog[15][10] == 0:
                txt(P,"A Kangaskhan is gazing at the","ocean.")
                if in_party(P,'Kangaskhan',True):
                    new_txt(P)
                    write(P,"Approach the Kangaskhan?")
                    if choice(P):
                        move = False
                        P.prog[15][10] += 1
                else:
                    txt(P,"If you brought a Kangaskhan","you could probably approach it","safely.")
        if P.prog[15][10] == 1 and P.px == -1125 and P.py == 525:
            P.r4_kang = pygame.transform.scale(load("p/spr/Kangaskhan_l1.png"),(75,90))
            P.p = P.r1
            route_4_b(P,wx,wy)
            route_4_p(P,P.px,P.py,False)
            route_4_f(P,P.px,P.py,tim)
            te = P.surface.copy()
            txt(P,"The Kangaskhan attacked!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.habitat = 'mount'
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Kangaskhan' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            P.party.insert(0,poke.Poke('Kangaskhan_M',[20,1,334,'Tackle',-1,'Baby-Doll Eyes',-1,'Endure',-1,None,None,None,None,0,"Nest Ball",300,'Guts',True]))
            battle(P,[poke.Poke('Kangaskhan',[32,1,334,'Fake Out',-1,'Bite',-1,'Mega Punch',-1,'Chip Away',-1,None,None,0,"Poke Ball",400,'Scrappy'])],no_pc = True)
            play_music(P,"music/route_4.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[1].status = None
                P.party[1].ch = P.party[1].hp
                P.prog[15][10] = 0
                txt(P,"The Kangaskhan roared in","triumph and drove you away!")
                fade_out(P)
                P.p = P.l1
                P.px = -875
                P.r4_kang = pygame.transform.scale(load("p/spr/Kangaskhan_r1.png"),(75,90))
                route_4_b(P,wx,wy)
                route_4_p(P,P.px,P.py,False)
                route_4_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][10] += 1
                txt(P,"The Kangaskhan looks content.","It hands you a mysterious","stone before leaving.")
                add_item(P,'Kangaskhanite',1)
                fade_out(P)
                route_4_b(P,wx,wy)
                route_4_p(P,P.px,P.py,False)
                route_4_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
            P.habitat = 'mount_grass'
        if P.prog[0] == 18 and P.r1_rival.y == -1600:
            P.r1_rival = None
            P.prog[0] += 1
            move = True
        if trainer_check(P,P.r4_expert,"music/route_4.wav"):
            P.r4_expert = npc.NPC(P,'Expertm','Timmy',[P.r4_expert.x,P.r4_expert.y],[['mr',100],['r',120],['ml',100],['l',100]],["If you're looking for a place","to rest, keep heading east to","reach Isola Town!"],tim = P.r4_expert.tim,curr = P.r4_expert.curr,extra_walk = P.r4_expert.extra_walk)
            move = True
        if trainer_check(P,P.r4_battle,"music/route_4.wav"):
            P.r4_battle = npc.NPC(P,'Battle Girl','Timmy',[P.r4_battle.x,P.r4_battle.y],[['l',100]],["Considering how long I've been","swinging at this rock, I'm","sure I'll break it someday."])
            move = True
        if trainer_check(P,P.r4_fish,"music/route_4.wav"):
            P.r4_fish = npc.NPC(P,'Fisherman','Timmy',[P.r4_fish.x,P.r4_fish.y],[['r',100]],["Well shellfish are great for","lots of other things!","","Like eating and stuff, you","know?",""])
            move = True
        if gran_talk > 50 and trainer_check(P,P.r4_expf,"music/route_4.wav"):
            if P.prog[5][34] == 0:
                P.r4_expf = npc.NPC(P,'Expertf','Stella',[1500,1200],[['l',80]],["Hello there! Not many people","choose to venture all the way","out here.","Perhaps you're looking for a","thrilling battle?",""],["Well that's quite surprising!","I suppose each new generation","really is more talented!"],True,[0,0,0,0],P.r4_team1,34,loc = "route_4")
                gran_talk = 0
                move = True
            else:
                P.r4_expf = npc.NPC(P,'Expertf','Timmy',[1500,1200],[['l',80]],["People say this is a scorch","mark left by a lightning","strike from Thundurus.","It could just be a myth, but","it's exhilarating to think","about isn't it?"])
                move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.r4_expert.talk():
                        if P.r4_expert.trainer:
                            move = False
                        else:
                            route_4_b(P,wx,wy)
                            route_4_p(P,P.px,P.py,False)
                            route_4_f(P,P.px,P.py,tim)
                            P.r4_expert.write()
                    elif P.r4_battle.talk():
                        if P.r4_battle.trainer:
                            move = False
                        else:
                            route_4_b(P,wx,wy)
                            route_4_p(P,P.px,P.py,False)
                            route_4_f(P,P.px,P.py,tim)
                            P.r4_battle.write()
                    elif P.r4_fish.talk():
                        if P.r4_fish.trainer:
                            move = False
                        else:
                            route_4_b(P,wx,wy)
                            route_4_p(P,P.px,P.py,False)
                            route_4_f(P,P.px,P.py,tim)
                            P.r4_fish.write()
                    elif gran_talk > 50 and P.r4_expf and P.r4_expf.talk():
                        if P.r4_expf.trainer:
                            move = False
                        else:
                            route_4_b(P,wx,wy)
                            route_4_p(P,P.px,P.py,False)
                            route_4_f(P,P.px,P.py,tim)
                            P.r4_expf.write()
                    elif next_to(P,500,-300) and P.prog[6][46] == 0:
                        txt(P,P.save_data.name + " found a Rare Candy!")
                        txt(P,P.save_data.name + " put the Rare Candy","in the Medicine pocket.")
                        add_item(P,"Rare Candy",1)
                        P.prog[6][46] = 1
                    elif next_to(P,1100,1100) and P.prog[6][48] == 0:
                        txt(P,P.save_data.name + " found a Luxury", "Ball!")
                        txt(P,P.save_data.name + " put the Luxury Ball","in the Balls pocket.")
                        add_item(P,"Luxury Ball",1)
                        P.prog[6][48] = 1
                    elif next_to(P,2250,800) and P.prog[6][47] == 0:
                        txt(P,P.save_data.name + " found a TM69 Rock", "Polish!")
                        txt(P,P.save_data.name + " put the TM69 in","the TMs pocket.")
                        add_item(P,"TM69 Rock Polish",1)
                        P.prog[6][47] = 1
                    elif P.px == -1925 and P.py == -625 and face_u(P):
                        txt(P,"It's a fishing sign.")
                    elif (P.py >= -675 and P.py <= -275 and P.px == -2225 and face_r(P)) or (P.px >= -2225 and P.px <= -2075 and P.py == -725 and face_d(P)) or (P.px == -2025 and P.py <= -775 and P.py >= -1175 and face_r(P)):
                        txt(P,"You could probably fish here","if you had a fishing rod.")
                    elif next_to(P,P.r4_tree1.x,P.r4_tree1.y):
                        P.r4_tree1.cut()
                    elif next_to(P,P.r4_tree2.x,P.r4_tree2.y):
                        P.r4_tree2.cut()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.py in [275,325] and P.px == -75 and face_l(P):
            P.px = -2925
            P.py += 350
            P.move_out_dir = 'l'
            P.loc = "mirror_cave"
            end = False
        if P.px in [-2125,-2225,-2175] and P.py == 575 and face_u(P):
            P.py = -225
            P.px += 1600
            P.loc = "isola"
            update_locs(P)
            isola(P,True,wx,wy)
            end = False
        if move and (wild_grass(P,-1175,-825,650,150,ignore = [(-1175,-925),(-1225,-925),(-1275,-925),(-1625,-925),(-1675,-925),(-1725,-925),(-1775,-925),(-1725,-875),(-1775,-875)]) or wild_grass(P,-925,-1025,700,200,ignore = [(-1425,-1025),(-1475,-1025),(-1525,-1025),(-1575,-1025),(-1525,-1075),(-1575,-1075)]) or wild_grass(P,-1875,-175,200,400) or wild_grass(P,-1125,25,950,200,ignore = [(-1125,-75),(-1175,-75),(-1125,-125),(-1175,-125),(-1225,-125)]) or wild_grass(P,-425,25,400,200,ignore = [(-725,25),(-775,25),(-725,-25),(-775,-25)]) or wild_grass(P,-125,575,700,150,ignore = [(-725,575),(-775,575)]) or wild_grass(P,-125,75,300,250)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < .07:
                r = random.randint(25,27)
                if r < 26:
                    battle(P,[poke.Poke('Vulpix',[r,random.randint(0,1),334,"Fire Spin",-1,"Confuse Ray",-1,"Will-O-Wisp",-1,"Payback",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Vulpix',[r,random.randint(0,1),334,"Fire Spin",-1,"Hex",-1,"Will-O-Wisp",-1,"Payback",-1,None,None,0,"Poke Ball"])])
            elif rando >= .07 and rando < .25:
                battle(P,[poke.Poke('Ponyta',[random.randint(25,28),random.randint(0,1),334,"Fire Spin",-1,"Flame Wheel",-1,"Flame Charge",-1,"Stomp",-1,None,None,0,"Poke Ball"])])
            elif rando >= .25 and rando < .4:
                battle(P,[poke.Poke('Kangaskhan',[random.randint(26,28),1,334,"Mega Punch",-1,"Fake Out",-1,"Comet Punch",-1,"Bite",-1,None,None,0,"Poke Ball"])])
            elif rando >= .4 and rando < .65:
                r = random.randint(23,27)
                if r < 25:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Assurance",-1,"Mirror Move",-1,"Fury Attack",-1,"Aerial Ace",-1,None,None,0,"Poke Ball"])])
                elif r < 27:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Assurance",-1,"Agility",-1,"Fury Attack",-1,"Aerial Ace",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Fearow',[r,random.randint(0,1),334,"Assurance",-1,"Agility",-1,"Fury Attack",-1,"Aerial Ace",-1,None,None,0,"Poke Ball"])])
            elif rando >= .65 and rando < .8:
                r = random.randint(24,28)
                if r < 28:
                    battle(P,[poke.Poke('Timburr',[r,random.randint(0,1),334,"Chip Away",-1,"Wake-Up Slap",-1,"Rock Throw",-1,"Bide",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Gurdurr',[r,random.randint(0,1),334,"Chip Away",-1,"Wake-Up Slap",-1,"Rock Throw",-1,"Bulk Up",-1,None,None,0,"Poke Ball"])])
            else:
                r = random.randint(23,27)
                if r < 24:
                    battle(P,[poke.Poke('Dwebble',[r,random.randint(0,1),334,"Bug Bite",-1,"Rock Polish",-1,"Feint Attack",-1,"Smack Down",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Dwebble',[r,random.randint(0,1),334,"Bug Bite",-1,"Rock Polish",-1,"Stealth Rock",-1,"Smack Down",-1,None,None,0,"Poke Ball"])])
            P.song = "music/route_4.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        gran_talk += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
        if pause:
            P.clock.tick(P.ani_spd/30)
            pause = False
    fade_out(P,P.song)

def pia_gymb_b(P,cam_mod = 0):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pia_gymb_back,(P.px,P.py+cam_mod))

def pia_gymb_p(P,temppx,temppy,move,cam_mod = 0):
    if P.pia_gymb_cheryl:
        cheryl = P.pia_gymb_cheryl.y_dist()
        if cheryl > 0:
            P.pia_gymb_cheryl.move(cam_mod = cam_mod)
    #rects start
    r1 = (P.px+100,P.py+50,100,40)
    r2 = (P.px+250,P.py+50,100,40)
    r3 = (P.px+50,P.py+100,50,340)
    r4 = (P.px+350,P.py+100,50,340)
    r5 = (P.px,P.py+250,50,40)
    r6 = (P.px+400,P.py+250,50,40)
    r7 = (P.px+100,P.py+400,100,40)
    r8 = (P.px+250,P.py+400,100,40)
    r9 = (P.px-50,P.py+300,50,490)
    r10 = (P.px+450,P.py+300,50,490)
    r11 = (P.px,P.py+800,450,40)
    r12 = (P.px+200,P.py,50,40)
    r13,r14,r20 = r1,r1,r1
    if P.px == 175 and P.py == -175:
        r13 = (P.px+150,P.py+450,50,40)
        r14 = (P.px+250,P.py+450,50,40)
    elif P.px != 175:
        r13 = (P.px+200,P.py+450,50,40)
    if P.pia_gymb_cheryl:
        r20 = P.pia_gymb_cheryl.get_rect()
    rects = [r20,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.prog[0] == 83 and P.py > -125:
            player_move(P,rects,manual_input = 'd',spd = 3)
        else:
            player_move(P,rects,mod = cam_mod)
    else:
        blit_player(P,mod = cam_mod)
    # if P.egi_gymb_colress:
    #     if colress <= 0:
    #         P.egi_gymb_colress.move(temppx,temppy)

def pia_gymb_f(P,temppx,temppy,tim,cam_mod = 0):
    show_location(P, P.loc_txt, tim)

def pia_gymb(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.pia_gymb_back = load("p/pianura/Pianura_Gym_Back.png")
    P.pia_gymb_cheryl = None
    if P.prog[0] <= 86:
        P.pia_gymb_cheryl = npc.NPC(P,'Cheryl','',[200,50],[['d',40]],["","",""])
    P.habitat = 'indoor'
    move = True
    cam_mod = 0
    tim = 0
    set_location(P)
    pia_gymb_b(P)
    pia_gymb_p(P,P.px,P.py,False)
    pia_gymb_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        if P.prog[0] == 83 and P.py == -125:
            P.p = P.u1
            P.prog[0] += 1
            move = False
        pia_gymb_b(P,cam_mod)
        temppx = P.px
        temppy = P.py
        pia_gymb_p(P,temppx,temppy,move,cam_mod)
        pia_gymb_f(P,temppx,temppy,tim,cam_mod)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 175 and P.py == 175 and face_u(P):
                        if P.prog[0] == 82:
                            txt(P,"Good to see you "+P.save_data.name+"!","I hope you didn't have too","much trouble getting here.")
                            txt(P,"Go ahead and take your spot on", "the other side and we'll begin","your challenge.")
                            P.prog[0] += 1
                        elif P.prog[0] == 86:
                            txt(P,"I had a lot of fun during our","battle! I hope you'll continue","to train your Pokemon well.")
                            txt(P,"If you ever want to talk to","me, you can catch me wandering","around the city.")
                            txt(P,"Don't forget to help out at","the nursery. I'm sure you'll","find it worthwhile.")
                    elif P.py == -25 and P.px in [375,-25] and face_u(P):
                        txt(P,"It's a statue with a colorful","orb on the top.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 175 and P.py == -475 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = 75
            P.py = 225
            P.loc = "pia_gym_3"
            end = False
        if P.prog[0] == 84:
            if cam_mod == 150:
                t = P.surface.copy()
                txt(P,"Any capable trainer must have","a tight bond with each of","their Pokemon.")
                txt(P,"You had better not give me a","poor showing of your Pokemon!","")
                play_music(P,"music/cheryl_battle.wav",0)
                #battle(P,["Leader Cheryl",poke.Poke('Mega_Audino',[15,0,334,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,"Light Screen",-1,None,None,0,"Poke Ball",0,'Magnet Pull'])])
                battle(P,["Leader Cheryl",poke.Poke('Wigglytuff',[25,0,334,"Disarming Voice",-1,"Swallow",-1,"Return",-1,"Stockpile",-1,None,None,0,"Poke Ball",300,'Cute Charm']),poke.Poke('Delcatty',[25,0,334,"Fake Out",-1,"Charm",-1,"Wake-Up Slap",-1,"Return",-1,None,None,0,"Poke Ball",300,'Cute Charm']),poke.Poke('Noctowl',[25,0,334,"Extrasensory",-1,"Echoed Voice",-1,"Steel Wing",-1,"Calm Mind",-1,None,None,0,"Poke Ball",300,'Insomnia']),poke.Poke('Chansey',[25,0,334,"Soft-Boiled",-1,"Minimize",-1,"Return",-1,"Grass Knot",-1,'Eviolite',None,0,"Poke Ball",400,'Serene Grace']),poke.Poke('Mega_Audino',[25,0,334,"Secret Power",-1,"Return",-1,"Disarming Voice",-1,"Attract",-1,None,None,0,"Premier Ball",400,'Healer'])])
                play_music(P,"music/gym.wav")
                P.surface.blit(t,(0,0))
                fade_in(P)
                txt(P,"Well you definitely showed me","your expertise in raising your","Pokemon!")
                txt(P,"Here's the Affinity Badge!","With it, your Pokemon will be","able to reach level 35.")
                txt(P,"It also serves as proof of","your ability as a trainer, so","you can help at the nursery.")
                txt(P,"They'll let you care for","Pokemon in exchange for money","and some other perks.")
                txt(P,"Take this TM27 Return.","You can use it to teach your","Pokemon Return.")
                txt(P,"It's a normal type attack that","becomes stronger if your","Pokemon are friendlier.")
                txt(P,"If you're looking for the","closest gym, you should head","towards Verde City.")
                txt(P,"You can take this lantern.","It'll help you find your way","through Mirror Cave.")
                txt(P,"I wish you luck in the rest of","your journey!","")
                add_item(P,"Lantern",1)
                add_item(P,"TM27 Return",1)
                P.prog[0] += 1
                P.prog[8][1][0] = 1
            else:
                cam_mod += 2
        if P.prog[0] == 85:
            cam_mod -= 2
            if cam_mod == 0:
                move = True
                P.prog[0] += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)


def pia_gym_b(P,num):
    P.surface.fill((0,0,0))
    P.surface.blit(P.piag_back, (P.px, P.py))
    if num == 5 and P.prog[6][41] == 0:
        P.surface.blit(P.item_out,(P.px,P.py+100))
    if num == 3 and P.px == 75 and P.py > 175 and P.py <= 225:
        P.surface.blit(P.piag_black,(P.px+301,P.py+35))

def pia_gym_p(P,temppx,temppy,move,num):
    if P.piag_npc1:
        one = P.piag_npc1.y_dist() > 0
        if one:
            P.piag_npc1.move()
    #rects start
    r0 = (P.px,P.py+50,300,40)
    r1 = (P.px,P.py+350,50,40)
    r2 = (P.px+250,P.py+100,100,40)
    if num == 3 and P.prog[0] >= 82:
        r2 = (P.px+200,P.py+100,100,40)
    r3 = (P.px-50,P.py+100,50,290)
    r4 = (P.px,P.py+400,350,40)
    r5 = (P.px+350,P.py+50,50,340)
    r6 = (P.px+50,P.py+100,100,90)
    r7,r8 = r0,r0
    if P.piag_npc1:
        r7 = P.piag_npc1.get_rect()
    if P.prog[6][41] == 0 and num == 5:
        r8 = (P.px,P.py+100,50,40)
    r9 = (P.px+300,P.py,50,40)
    rects = [r9,r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.piag_npc1:
        if not one:
            P.piag_npc1.move(temppx,temppy)

def pia_gym_f(P,temppx,temppy,tim):
    show_location(P, P.loc_txt, tim)

def pia_gym(P,num) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    set_location(P)
    P.piag_back = load("p/pianura/Pianura_Gym_Room.png")
    P.piag_black = load("p/egida/black_door.png")
    if P.prog[0] >= 82 and num == 3:
        P.piag_back = load("p/pianura/Pianura_Gym_Room_h.png")
    P.habitat = 'indoor'
    P.piag_npc1 = None
    if num == 1:
        if P.prog[5][25] == 0:
            P.piag_npc1 = npc.NPC(P,'Lass','Sophie',[150,250],[['d',40]],["Ha! Bet you didn't expect to","find me here!",""],["Or maybe you were expecting","me, I don't know...",""],True,[0,150,0,0],P.piag_team1,25)
        else:
            P.piag_npc1 = npc.NPC(P,'Lass','Harper',[150,250],[['d',40]],["Where's Cheryl?","As if I'm going to tell","you that!"])
    elif num == 2:
        if P.prog[5][26] == 0:
            P.piag_npc1 = npc.NPC(P,'Youngster','Lucas',[150,250],[['d',40]],["Hey I have a hint to help you","find Cheryl, but you're gonna","have to beat me to get it!"],["What! I actually lost?","Whatever, I'm not going to","break my promise.","If you look hard enough, there","are clues hidden in each of","the rooms."],True,[0,150,0,0],P.piag_team2,26)
        else:
            P.piag_npc1 = npc.NPC(P,'Youngster','Harper',[150,250],[['d',40]],["Did you forget already?","Just explore the rooms some","more and you'll find hints."])
    elif num == 3:
        if P.prog[5][27] == 0:
            if P.prog[0] >= 82:
                P.piag_npc1 = npc.NPC(P,'Gentleman','Anderson',[250,150],[['u',40]],["I wouldn't know where you","could find Cheryl. Or maybe I","might?"],["Well that door right there is","looking quite suspicious if","you ask me."],True,[0,0,0,0],P.piag_team3,27)
            else:
                P.piag_npc1 = npc.NPC(P,'Gentleman','Anderson',[250,150],[['u',40]],["I wouldn't know where you","could find Cheryl. Or maybe I","might?"],["Well you can keep looking,","I'll just be here reading some","of these books."],True,[0,0,0,0],P.piag_team3,27)
        else:
            P.piag_npc1 = npc.NPC(P,'Gentleman','Harper',[250,150],[['u',40]],["The books here are quite nice.","You should take some time to","browse this bookshelf."])
    elif num == 4:
        if P.prog[5][28] == 0:
            P.piag_npc1 = npc.NPC(P,'Preschoolerg','Ellie',[200,350],[['l',40]],["B O O ! ! !","",""],["Haha!","You should've seen the look on","your face!"],True,[0,0,50,0],P.piag_team4,28)
        else:
            P.piag_npc1 = npc.NPC(P,'Preschoolerg','Harper',[200,350],[['l',40]],["Cheryl? Who's that?","",""])
    move = True
    tim = 0
    pia_gym_b(P,num)
    pia_gym_p(P,P.px,P.py,False,num)
    pia_gym_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        pia_gym_b(P,num)
        if move == True and P.piag_npc1 and P.piag_npc1.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        pia_gym_p(P,temppx,temppy,move,num)
        pia_gym_f(P,temppx,temppy,tim)
        if P.piag_npc1 and trainer_check(P,P.piag_npc1,"music/gym.wav"):
            if num == 1:
                P.piag_npc1 = npc.NPC(P,'Lass','Harper',[P.piag_npc1.x,P.piag_npc1.y],[[P.piag_npc1.face(),20]],["Where's Cheryl?","As if I'm going to tell","you that!"])
            elif num == 2:
                P.piag_npc1 = npc.NPC(P,'Youngster','Harper',[P.piag_npc1.x,P.piag_npc1.y],[[P.piag_npc1.face(),20]],["Did you forget already?","Just explore the rooms some","more and you'll find hints."])
            elif num == 3:
                P.piag_npc1 = npc.NPC(P,'Gentleman','Harper',[P.piag_npc1.x,P.piag_npc1.y],[['u',20]],["The books here are quite nice.","You should take some time to","browse this bookshelf."])
            elif num == 4:
                P.piag_npc1 = npc.NPC(P,'Preschoolerg','Harper',[P.piag_npc1.x,P.piag_npc1.y],[[P.piag_npc1.face(),20]],["Cheryl? Who's that?","",""])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.piag_npc1 and P.piag_npc1.talk():
                        if P.piag_npc1.trainer:
                            move = False
                        else:
                            pia_gym_b(P,num)
                            pia_gym_p(P,P.px,P.py,False,num)
                            pia_gym_f(P,P.px,P.py,tim)
                            P.piag_npc1.write()
                    elif ((P.py == 125 and P.px in [75,125] and (num != 3 or P.prog[0] < 82)) or (P.py == 125 and P.px == 175 and num == 3 and P.prog[0] >= 82)) and face_u(P):
                        if num == 1:
                            new_txt(P)
                            write(P,"Super Secret Diary","Read?")
                            if choice(P):
                                txt(P,"The entrance to Cheryl's gym","stage is on the right of this","room.")
                                txt(P,"Just in case you want to know,","mysterious challenger!")
                        elif num == 2:
                            new_txt(P)
                            write(P,"There's a journal sticking out","of the bookshelf.","Read?")
                            if choice(P):
                                txt(P,"If you're trying to challenge","Cheryl, you'll have better","luck looking upstairs.")
                        elif num == 3:
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.07:","Slowpoke and Shellder","Read?")
                            if choice(P):
                                txt(P,"Slowpoke can evolve when a","Shellder attaches to it by","biting down.")
                                txt(P,"Slowpoke evolve at level 37,","or if given a King's Rock, but","only with Shellder present.")
                                txt(P,"Depending on how it evolves,","Slowpoke will evolve into a","Slowbro or Slowking.")
                                txt(P,"This process will render","Shellder unusable as a Pokemon","for battling.")
                        elif num == 4:
                            new_txt(P)
                            write(P,"A message is written on the","bookshelf in permanent ink.","Read?")
                            if choice(P):
                                txt(P,"I've been circling the rooms","forever, and I still can't","find the gym leader!")
                                txt(P,"I don't even remember where","I've been since every room","looks the same!")
                        else:
                            new_txt(P)
                            write(P,"There's a note poking out of","one of the books.","Read?")
                            if choice(P):
                                txt(P,"There's a bookshelf in front","of the entrance to the gym","stage.")
                                txt(P,"You'll have to pull it out of","the way to get through.")
                    elif P.px == 175 and P.py == 175 and num == 3 and face_r(P):
                        txt(P,"There's something off about","this bookshelf.")
                        new_txt(P)
                        write(P,"Pull it out of the way?")
                        if choice(P):
                            P.px += 50
                            temppx += 50
                            P.prog[0] += 1
                            P.piag_back = load("p/pianura/Pianura_Gym_Room_h.png")
                            if P.prog[5][27] == 0:
                                P.piag_npc1 = npc.NPC(P,'Gentleman','Anderson',[250,150],[['u',40]],["I wouldn't know where you","could find Cheryl. Or maybe I","might?"],["Well that door right there is","looking quite suspicious if","you ask me."],True,[0,0,0,0],P.piag_team3,27)
                            fade_out(P)
                            P.clock.tick(2)
                            pia_gym_b(P,num)
                            pia_gym_p(P,P.px,P.py,False,num)
                            pia_gym_f(P,P.px,P.py,tim)
                            fade_in(P)
                    elif next_to(P,0,100) and P.prog[6][41] == 0 and num == 5:
                        txt(P,P.save_data.name + " found a Luxury","Ball!")
                        txt(P,P.save_data.name + " put the Luxury","Ball in the Balls pocket.")
                        add_item(P,"Luxury Ball",1)
                        P.prog[6][41] = 1
                    elif next_to(P,0,350):
                        if num == 1 and P.prog[6][39] == 0:
                            txt(P,P.save_data.name + " found an Old Candy!")
                            txt(P,P.save_data.name + " put the Old Candy","in the Medicine pocket.")
                            add_item(P,"Old Candy",1)
                            P.prog[6][39] = 1
                        elif num == 4 and P.prog[6][40] == 0:
                            txt(P,P.save_data.name + " found an Old Candy!")
                            txt(P,P.save_data.name + " put the Old Candy","in the Medicine pocket.")
                            add_item(P,"Old Candy",1)
                            P.prog[6][40] = 1
                        else:
                            txt(P,"The trashcan's empty.")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 225 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            if num == 1:
                P.px = 125
                P.py = -125
            elif num == 2:
                P.px = -175
                P.py = -125
            elif num == 3:
                P.px = -275
                P.py = 175
            elif num == 4:
                P.px = -25
                P.py = 175
            else:
                P.px = 225
                P.py = 175
            P.loc = "pia_gym"
            P.move_out_dir = 'd'
            end = False
        if P.px == 75 and P.py == 225 and face_u(P):
            P.px = 175
            P.py = -475
            P.loc = 'pia_gymb'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def pia_gym_main_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pia_gym_back,(P.px,P.py))
    if P.px == 125 and P.py > -175 and P.py <= -125:
        P.surface.blit(P.pia_gym_black,(P.px+251,P.py+385))
    if P.px == -175 and P.py > -175 and P.py <= -125:
        P.surface.blit(P.pia_gym_black,(P.px+551,P.py+385))
    if P.px == -275 and P.py > 125 and P.py <= 175:
        P.surface.blit(P.pia_gym_black,(P.px+651,P.py+85))
    if P.px == -25 and P.py > 125 and P.py <= 175:
        P.surface.blit(P.pia_gym_black,(P.px+401,P.py+85))
    if P.px == 225 and P.py > 125 and P.py <= 175:
        P.surface.blit(P.pia_gym_black,(P.px+151,P.py+85))

def pia_gym_main_p(P,temppx,temppy,move):
    #rects start
    guide = P.pia_gym_guide.y_dist() > 0
    if guide:
        P.pia_gym_guide.move()
    r1 = (P.px,P.py+100,150,40)
    r3 = (P.px+200,P.py+100,200,40)
    r5 = (P.px+450,P.py+100,200,40)
    r7 = (P.px+700,P.py+100,150,40)
    r8 = (P.px+850,P.py+150,50,690)
    r9 = (P.px-50,P.py+150,50,690)
    r10 = (P.px+150,P.py+300,550,40)
    r11 = (P.px+100,P.py+350,50,340)
    if P.px >= 275:
        r11 = (P.px+150,P.py+350,50,340)
    r12 = (P.px+700,P.py+350,50,340)
    if P.px <= -325:
        r12 = (P.px+650,P.py+350,50,340)
    r13 = (P.px,P.py+850,850,40)
    r14 = (P.px+150,P.py+650,50,40)
    r15 = (P.px+650,P.py+650,50,40)
    r16 = (P.px+150,P.py+400,100,40)
    r18 = (P.px+300,P.py+400,250,40)
    r20 = (P.px+600,P.py+400,100,40)
    r21 = P.pia_gym_guide.get_rect()
    #door
    r2 = (P.px+150,P.py+50,50,40)
    r4 = (P.px+400,P.py+50,50,40)
    r6 = (P.px+650,P.py+50,50,40)
    r17 = (P.px+250,P.py+350,50,40)
    r19 = (P.px+550,P.py+350,50,40)
    if P.prog[0] < 81:
        r2 = (P.px+150,P.py+100,50,40)
        r4 = (P.px+400,P.py+100,50,40)
        r6 = (P.px+650,P.py+100,50,40)
        r17 = (P.px+250,P.py+400,50,40)
        r19 = (P.px+550,P.py+400,50,40)
    rects = [r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if not guide:
        P.pia_gym_guide.move(temppx,temppy)

def pia_gym_main_f(P,temppx,temppy,tim):
    P.surface.blit(P.pia_gym_f,(temppx+145,temppy+275))
    show_location(P, P.loc_txt, tim)

def pia_gym_main(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.pia_gym_back = load("p/pianura/Pianura_Gym_Main.png")
    P.pia_gym_black = load("p/egida/black_door.png")
    P.pia_gym_f = load("p/pianura/pia_gym_f.png")
    P.pia_gym_guide = npc.NPC(P,'Officer','Ross',[600,650],[['d',20]],["Welcome to the Pianura City","Gym! Our gym leader Cheryl", "uses Normal-type Pokemon.","Most attacks aren't effective","against Normal-type Pokemon,","but if you have multiple Rock","or Steel-type Pokemon, they","won't hit you very hard","either!"])
    move = True
    tim = 0
    set_location(P)
    pia_gym_main_b(P)
    pia_gym_main_p(P,P.px,P.py,False)
    pia_gym_main_f(P,P.px,P.py,tim)
    fade_in(P)
    fade = None
    end = True
    m = 0
    while end:
        pia_gym_main_b(P)
        #print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        pia_gym_main_p(P,temppx,temppy,move)
        pia_gym_main_f(P,temppx,temppy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.pia_gym_guide.talk():
                        pia_gym_main_b(P)
                        pia_gym_main_p(P,P.px,P.py,False)
                        pia_gym_main_f(P,P.px,P.py,tim)
                        P.pia_gym_guide.write()
                    elif next_to(P,150,650):
                        txt(P,"It's a status in the shape of","Latias' head.")
                    elif next_to(P,650,650):
                        txt(P,"It's a status in the shape of","Latios' head.")
                    elif P.prog[0] < 81 and (next_to(P,550,400) or next_to(P,250,400) or next_to(P,650,100) or next_to(P,400,100) or next_to(P,150,100)):
                        txt(P,"It's locked.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == -25 and P.py == -525 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = -725
            P.py = 775
            fade = P.song
            P.loc = "pianura"
            end = False
        if P.px == 125 and P.py == -125 and face_u(P):
            P.px = 225
            P.py = -75
            P.loc = "pia_gym_1"
            end = False
        if P.px == -175 and P.py == -125 and face_u(P):
            P.px = 225
            P.py = -75
            P.loc = "pia_gym_2"
            end = False
        if P.px == -275 and P.py == 175 and face_u(P):
            P.px = 225
            P.py = -75
            P.loc = "pia_gym_3"
            end = False
        if P.px == -25 and P.py == 175 and face_u(P):
            P.px = 225
            P.py = -75
            P.loc = "pia_gym_4"
            end = False
        if P.px == 225 and P.py == 175 and face_u(P):
            P.px = 225
            P.py = -75
            P.loc = "pia_gym_5"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def mirror_cave_b(P):
    P.surface.blit(P.mc_back,(P.px+50,P.py-1000))
    if P.prog[6][36] == 0:
        P.surface.blit(P.item_cave,(P.px+700,P.py+1200))
    if P.prog[6][37] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+600,P.py+1100))
    if P.prog[6][38] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+1650,P.py+400))
    if P.prog[6][42] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+2450,P.py-200))
    if P.prog[6][43] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+2750,P.py+550))
    if P.prog[6][44] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+3000,P.py+750))
    if P.prog[6][45] == 0:
        P.surface.blit(P.item_cave,(P.px+2700,P.py-150))
    if P.py <= -325 and P.py >= -375 and P.px >= -1025 and P.px <= -925:
        blit_reverse_player(P,'u',-325,1)
    elif P.py <= -740 and P.py >= -925 and P.px >= -675 and P.px <= -575:
        blit_reverse_player(P,'r',-675,2)
    elif P.py <= 60 and P.py >= -125 and P.px >= -2175 and P.px <= -2075:
        blit_reverse_player(P,'r',-2175,4)
    elif P.py <= 475 and P.py >= 425 and P.px >= -2475 and P.px <= -2375:
        blit_reverse_player(P,'u',475,5)
    elif P.py <= 275 and P.py >= 175 and P.px >= -1825 and P.px <= -1725:
        blit_reverse_player(P,'u',275,3)
    P.surface.blit(P.mc_rmirror,(P.px+2750,P.py-300))
    P.surface.blit(P.mc_lmirror,(P.px+1300,P.py+500))
    P.surface.blit(P.mc_mmirror,(P.px+2100,P.py-150))
    P.surface.blit(P.mc_lbmirror,(P.px+1050,P.py+1000))
    P.surface.blit(P.mc_mbmirror,(P.px+2550,P.py+200))
    if P.prog[0] <= 88 and P.mc_sableye and P.mc_sableye.x == 1950:
        P.surface.blit(P.mc_gem,(P.px+1900,P.py+50))
    if P.prog[15][8] != 2:
        P.surface.blit(P.mc_steel,(P.px+2300,P.py+990))
    

def mirror_cave_p(P,temppx,temppy,move):
    hex = P.mc_hex.y_dist() > 0
    if hex:
        P.mc_hex.move()
    hiker = P.mc_hiker.y_dist() > 0
    if hiker:
        P.mc_hiker.move()
    #rects start
    if P.mc_sableye:
        P.mc_sableye.move()
    r1 = (P.px+700,P.py+50,50,90)
    r2 = (P.px+750,P.py,50,40)
    r3 = (P.px+750,P.py+150,50,40)
    r4 = (P.px+800,P.py-50,1600,40)
    r5 = (P.px+800,P.py+200,200,40)
    r6 = r1
    if P.py == 75:
        r6 = (P.px+1000,P.py+250,100,40)
    r7 = (P.px+1100,P.py+200,500,40)
    r8 = (P.px+1100,P.py+250,50,340)
    r9 = (P.px+1550,P.py+250,50,340)
    r10 = (P.px+950,P.py+250,50,640)
    r11 = (P.px+1150,P.py+550,400,40)
    r12 = (P.px+600,P.py+850,350,40)
    r13 = (P.px+550,P.py+900,50,390)
    r14 = (P.px+600,P.py+1300,500,40)
    r15 = (P.px+1100,P.py+700,50,640)
    #rocks
    r16 = (P.px+700,P.py+1250,50,40)
    r17 = (P.px+750,P.py+1200,50,40)
    r18 = (P.px+650,P.py+1150,100,40)
    r19 = (P.px+600,P.py+900,50,40)
    r20 = (P.px+1600,P.py+450,50,40)
    #walls
    r21 = (P.px+1150,P.py+700,550,40)
    r22 = (P.px+1700,P.py+200,50,490)
    r23 = (P.px+1750,P.py+200,450,40)
    #rocks
    r24 = (P.px+1850,P.py+150,50,40)
    r25 = (P.px+1900,P.py+50,50,40)
    r26 = (P.px+1850,P.py,50,40)
    #sabeleye
    r27 = r1
    if P.prog[0] < 89:
        r27 = (P.px+1900,P.py+100,50,40)
    #items
    r28,r29,r30 = r1,r1,r1
    if P.prog[6][36] == 0:
        r28 = (P.px+700,P.py+1200,50,40)
    if P.prog[6][37] == 0:
        r29 = (P.px+600,P.py+1100,50,40)
    if P.prog[6][38] == 0:
        r30 = (P.px+1650,P.py+400,50,40)
    #walls
    r31 = (P.px+2350,P.py-600,50,540)
    r32 = (P.px+2400,P.py-650,850,40)
    r33 = (P.px+2500,P.py-500,600,40)
    r34 = (P.px+2500,P.py-450,50,240)
    r35 = (P.px+2550,P.py-250,550,40)
    r36 = (P.px+3050,P.py-450,50,190)
    r37 = (P.px+3250,P.py-600,50,40)
    r38 = (P.px+3300,P.py-550,50,140)
    r39 = (P.px+3350,P.py-400,50,90)
    r40 = (P.px+3300,P.py-300,50,190)
    r41 = (P.px+2600,P.py-100,700,40)
    r42 = r1
    if P.px == -2275:
        r42 = (P.px+2700,P.py-200,50,90)
    r43 = (P.px+2400,P.py-150,50,40)
    r44 = (P.px+2600,P.py-50,50,540)
    r45 = (P.px+2150,P.py+250,50,290)
    r46 = (P.px+2650,P.py+450,450,40)
    r47 = (P.px+2200,P.py+550,50,40)
    r48 = (P.px+2250,P.py+600,700,40)
    r49 = (P.px+2800,P.py+500,50,40)
    r50 = (P.px+3050,P.py+500,50,540)
    r51 = (P.px+2900,P.py+650,50,340)
    r52 = (P.px+2950,P.py+700,50,40)
    r53 = (P.px+3000,P.py+1050,50,40)
    r54 = (P.px+2300,P.py+950,600,40)
    r55 = (P.px+2300,P.py+1100,700,40)
    r56 = (P.px+2250,P.py+1000,50,90)
    r57,r58,r59,r62 = r1,r1,r1,r1
    if P.prog[6][42] == 0:
        r57 = (P.px+2450,P.py-200,50,40)
    if P.prog[6][43] == 0:
        r58 = (P.px+2750,P.py+550,50,40)
    if P.prog[6][44] == 0:
        r59 = (P.px+3000,P.py+750,50,40)
    r60 = P.mc_hex.get_rect()
    r61 =  P.mc_hiker.get_rect()
    if P.prog[6][45] == 0:
        r62 = (P.px+2700,P.py-150,50,40)
    rects = [r62,r61,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.prog[15][8] == 0 and P.px == -2225 and P.py in [-725,-775] and face_l(P):
            player_move(P,rects,manual_input = 'r')
        else:
            player_move(P,rects)
    else:
        if P.px < -2025 and P.prog[15][8] == 1:
            player_move(P,rects,manual_input = 'l')
        else:
            blit_player(P)
    if not hex:
        P.mc_hex.move(temppx,temppy)
    if not hiker:
        P.mc_hiker.move(temppx,temppy)

def mirror_cave_f(P,temppx,temppy,tim):
    P.surface.blit(P.mc_cavel,(temppx+650,temppy-50))
    P.surface.blit(P.mc_caver,(temppx+3200,temppy-500))
    trans = pygame.Surface((800,600))
    trans.set_alpha(50)
    trans.fill((0,0,20))
    P.surface.blit(trans,(0,0))
    P.surface.blit(P.mc_lightl,(temppx+650,temppy-50))
    P.surface.blit(P.mc_lightr,(temppx+3200,temppy-500))
    P.surface.blit(P.mc_dark,(0,0))
    show_location(P, P.loc_txt, tim)

def mirror_cave(P) -> None:
    if P.song != "music/mirror_cave.wav":
        P.song = "music/mirror_cave.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] == 98:
        P.prog[0] += 1
    P.habitat = 'cave'
    P.mc_back = load("p/pianura/Cave_of_Mirrors.png")
    P.mc_cavel = load("p/pianura/cave_l.png")
    P.mc_lightl = load("p/pianura/light_l.png")
    P.mc_caver = load("p/pianura/cave_r.png")
    P.mc_lightr = load("p/pianura/light_r.png")
    P.mc_rmirror = load("p/pianura/right_mirror.png")
    P.mc_lmirror = load("p/pianura/left_mirror.png")
    P.mc_mmirror = load("p/pianura/mid_mirror.png")
    P.mc_lbmirror = load("p/pianura/leftbot_mirror.png")
    P.mc_mbmirror = load("p/pianura/midbot_mirror.png")
    P.mc_gem = load("p/pianura/Sableye_gem.png")
    P.mc_darkness = load("p/pianura/cave_darkness.png")
    P.mc_light = load("p/pianura/lantern.png")
    P.mc_steel1 = pygame.transform.scale(load("p/pianura/steelix_sleep1.png"),(100,100))
    P.mc_steel2 = pygame.transform.scale(load("p/pianura/steelix_sleep2.png"),(100,100))
    P.mc_steel = P.mc_steel1
    P.mc_dark = P.mc_darkness
    if P.prog[15][9] != 6:
        P.prog[15][9] = 0
    P.mc_sableye = None
    if P.prog[0] <= 88:
        P.mc_sableye = npc.NPC(P,'Sableye','Grunt',[1950,100],[['l',40]],["","",""])
    move = True
    mod = 0
    if P.prog[0] >= 87:
        mod = 3
    tim = 0
    set_location(P)
    mirror_cave_b(P)
    mirror_cave_p(P,P.px,P.py,False)
    mirror_cave_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        print(P.px,P.py)
        mirror_cave_b(P)
        if move == True and P.mc_hex.trainer_check():
            move = False
        if move == True and P.mc_hiker.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        P.ledge = 0
        if (P.px <= -625 and P.px >= -674):
            if P.py > 25 and P.py < 50:
                P.ledge = (25-P.py)/2
            elif P.py >= 50 and P.py < 75:
                P.ledge = -(75-P.py)/2
        elif (P.py <= 475 and P.py >= 425):
            if P.px > -2325 and P.px < -2300:
                P.ledge = -((2325+P.px)/1.5)
            elif P.px >= -2300 and P.px < -2275:
                P.ledge = (2275+P.px)/1.5
        mirror_cave_p(P,temppx,temppy,move)
        mirror_cave_f(P,temppx,temppy,tim)
        if P.prog[0] == 87 and P.mc_dark == P.mc_light and P.px <= -1325:
            move = False
            P.mc_sableye.trainer_walk = ['r',400,20]
            P.prog[0] += 1
        if P.prog[0] == 88 and P.mc_sableye.x == 2250:
            P.mc_sableye = None
            move = True
            P.prog[0] += 1
        if P.px == -2225 and P.py in [-725,-775] and face_l(P) and P.prog[15][8] == 0:
            if P.prog[15][0] == 0:
                txt(P,"There's a Steelix sleeping at","the end of this tunnel.")
                print_mega_area(P)
            else:
                txt(P,"There's a Steelix sleeping at","the end of this tunnel.")
                if in_party(P,'Steelix',True):
                    new_txt(P)
                    write(P,"Approach the Steelix?")
                    if choice(P):
                        move = False
                        P.prog[15][8] += 1
                else:
                    txt(P,"You should bring a Steelix","before approaching it.")
        if P.prog[15][8] == 1 and P.px == -2025:
            te = P.surface.copy()
            txt(P,"You try to take the stone","stuck under the Steelix!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Steelix' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            steel = poke.Poke('Steelix',[42,0,334,'Earthquake',-1,None,None,None,None,None,None,None,'Slp',0,"Poke Ball",400,'Sturdy'])
            steel.slptim = 3
            battle(P,[steel],no_pc = True)
            play_music(P,"music/mirror_cave.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][8] = 0
                txt(P,"The Steelix chased you away","before going back to sleep!")
                fade_out(P)
                P.p = P.r1
                P.px = -2325
                mirror_cave_b(P)
                mirror_cave_p(P,P.px,P.py,False)
                mirror_cave_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][8] += 1
                txt(P,"You got the mysterious stone","and the Steelix disappeared","into the darkness.")
                add_item(P,'Steelixite',1)
                fade_out(P)
                mirror_cave_b(P)
                mirror_cave_p(P,P.px,P.py,False)
                mirror_cave_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
        if trainer_check(P,P.mc_hex,"music/mirror_cave.wav"):
            P.mc_hex = npc.NPC(P,'Hex Maniac','Jesse',[P.mc_hex.x,P.mc_hex.y],[['md',80],['d',100],['mr',80],['r',60],['ml',80],['l',60],['mu',80],['u',60]],["Sometimes I like to think that","there's a Pokemon hiding","inside these mirrors!"],tim = P.mc_hex.tim,curr = P.mc_hex.curr,extra_walk = P.mc_hex.extra_walk)
            move = True
        if trainer_check(P,P.mc_hiker,"music/mirror_cave.wav"):
            P.mc_hiker = npc.NPC(P,'Hiker','Jesse',[P.mc_hiker.x,P.mc_hiker.y],[['mr',120],['r',100],['ml',120],['l',80]],["Now that I think about it,","maybe it's not all that bad in","here...","Now I don't have to deal with","the stress of life!",""])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if next_to(P,1350,550) or next_to(P,1100,1100) or next_to(P,2150,-50) or next_to(P,2600,300) or next_to(P,2800,-250):
                        if next_to(P,1350,550):
                            num = 1
                        elif next_to(P,1100,1100):
                            num = 2
                        elif next_to(P,2150,-50):
                            num = 3
                        elif next_to(P,2600,300):
                            num = 4
                        else:
                            num = 5
                        if in_party(P,'Sableye',True) and P.prog[15][0] != 0 and P.prog[15][9] != num and P.prog[15][9] != 6 and P.prog[0] >= 89:
                            te = P.surface.copy()
                            P.song = "music/wild_battle.wav"
                            pygame.mixer.music.load(P.song)
                            set_mixer_volume(P,P.vol)
                            pygame.mixer.music.play(0)
                            P.legendary_battle = True
                            P.temp_party = P.party.copy()
                            pos = 0
                            while len(P.party) > 1:
                                if P.party[pos].code_nos() != 'Sableye' or P.party[pos].status == 'Faint' or pos == 1:
                                    P.party.remove(P.party[pos])
                                else:
                                    pos += 1
                            battle(P,[poke.Poke('Sableye',[32,1,334,'Confuse Ray',-1,'Shadow Claw',-1,'Punishment',-1,'Shadow Sneak',-1,None,None,0,"Poke Ball",400,'Keen Eye'])],no_pc = True)
                            play_music(P,"music/mirror_cave.wav")
                            P.surface.blit(te,(0,0))
                            fade_in(P)
                            if P.party[0].status == 'Faint':
                                P.party[0].status = None
                                P.party[0].ch = P.party[0].hp
                                txt(P,"The Sableye disappeared from","the reflective surface!")
                                P.prog[15][9] = num
                            else:
                                P.prog[15][9] = 6
                                txt(P,"The Sableye vanishes and you","find a mysterious stone in","your back pocket.")
                                add_item(P,'Sablenite',1)
                                move = True
                            P.party = P.temp_party.copy()
                            P.legendary_battle = False
                        else:
                            txt(P,"Staring at your reflection for","too long makes you a little","uncomfortable.")
                    elif next_to(P,1900,100):
                        txt(P,"There's some sort of crystal","blocking your way.")
                    elif P.mc_hiker.talk():
                        if P.mc_hiker.trainer:
                            move = False
                        else:
                            mirror_cave_b(P)
                            mirror_cave_p(P,P.px,P.py,False)
                            mirror_cave_f(P,P.px,P.py,tim)
                            P.mc_hiker.write()
                    elif P.mc_hex.talk():
                        if P.mc_hex.trainer:
                            move = False
                        else:
                            mirror_cave_b(P)
                            mirror_cave_p(P,P.px,P.py,False)
                            mirror_cave_f(P,P.px,P.py,tim)
                            P.mc_hex.write()
                    elif next_to(P,700,1200) and P.prog[6][36] == 0:
                        txt(P,P.save_data.name + " found a TM78","Bulldoze!")
                        txt(P,P.save_data.name + " put the TM78 in","the TMs pocket.")
                        add_item(P,"TM78 Bulldoze",1)
                        P.prog[6][36] = 1
                    elif next_to(P,2700,-150) and P.px != -2275 and P.prog[6][45] == 0:
                        txt(P,P.save_data.name + " found a Moon Stone!")
                        txt(P,P.save_data.name + " put the Moon Stone","in the Items pocket.")
                        add_item(P,"Moon Stone",1)
                        P.prog[6][45] = 1
                    elif next_to(P,1650,400) and P.prog[6][38] == 0:
                        item_fight(P,"music/mirror_cave.wav",38,20,('Magnitude','Rollout','Smack Down','Rock Polish'),'Geodude','The rock started to move!')
                    elif next_to(P,600,1100) and P.prog[6][37] == 0:
                        item_fight(P,"music/mirror_cave.wav",37,22,('Magnitude','Bulldoze','Smack Down','Rock Polish'),'Geodude','The rock started to move!')
                    elif next_to(P,2450,-200) and P.prog[6][42] == 0:
                        item_fight(P,"music/mirror_cave.wav",42,25,('Magnitude','Bulldoze','Smack Down','Self-Destruct'),'Geodude','The rock started to move!')
                    elif next_to(P,2750,550) and P.prog[6][43] == 0:
                        item_fight(P,"music/mirror_cave.wav",43,25,('Magnitude','Bulldoze','Smack Down','Self-Destruct'),'Geodude','The rock started to move!')
                    elif next_to(P,3000,750) and P.prog[6][44] == 0:
                        item_fight(P,"music/mirror_cave.wav",44,25,('Magnitude','Bulldoze','Smack Down','Self-Destruct'),'Geodude','The rock started to move!')
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == -375 and P.py in [225,175] and face_l(P):
            P.px = -1925
            P.py -= 350
            P.loc = "pianura"
            P.move_out_dir = 'l'
            end = False
        if P.px == -2925 and P.py in [675,625] and face_r(P):
            P.px = -75
            P.py -= 350
            P.loc = "route_4"
            P.move_out_dir = 'r'
            end = False
        #0.7
        if move and wild_grass(P,0,0,0,0,0.7,all = True):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.1:
                r = random.randint(20,22+mod)
                if r < 21:
                    battle(P,[poke.Poke('Sableye',[r,random.randint(0,1),334,"Shadow Sneak",-1,"Night Shade",-1,"Detect",-1,"Feint Attack",-1,None,None,0,"Poke Ball"])])
                elif r < 24:
                    battle(P,[poke.Poke('Sableye',[r,random.randint(0,1),334,"Shadow Sneak",-1,"Night Shade",-1,"Fake Out",-1,"Feint Attack",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Sableye',[r,random.randint(0,1),334,"Shadow Sneak",-1,"Night Shade",-1,"Fake Out",-1,"Punishment",-1,None,None,0,"Poke Ball"])])
            elif rando >= .1 and rando < .25:
                r = random.randint(19,21+mod)
                if r < 20:
                    battle(P,[poke.Poke('Onix',[r,random.randint(0,1),334,"Rock Polish",-1,"Stealth Rock",-1,"Rock Tomb",-1,"Bind",-1,None,None,0,"Poke Ball"])])
                elif r < 22:
                    battle(P,[poke.Poke('Onix',[r,random.randint(0,1),334,"Rock Polish",-1,"Stealth Rock",-1,"Rock Tomb",-1,"Gyro Ball",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Onix',[r,random.randint(0,1),334,"Rock Polish",-1,"Stealth Rock",-1,"Smack Down",-1,"Gyro Ball",-1,None,None,0,"Poke Ball"])])
            elif rando >= .25 and rando < .45:
                r = random.randint(18,21+mod)
                if r < 22:
                    battle(P,[poke.Poke('Aron',[r,random.randint(0,1),334,"Rock Tomb",-1,"Metal Claw",-1,"Headbutt",-1,"Mud-Slap",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Aron',[r,random.randint(0,1),334,"Rock Tomb",-1,"Iron Head",-1,"Headbutt",-1,"Mud-Slap",-1,None,None,0,"Poke Ball"])])
            elif rando >= .45 and rando < .55:
                r = random.randint(19,22+mod)
                if r < 21:
                    battle(P,[poke.Poke('Golett',[r,2,334,"Iron Defense",-1,"Shadow Punch",-1,"Mud-Slap",-1,"Rollout",-1,None,None,0,"Poke Ball"])])
                elif r < 25:
                    battle(P,[poke.Poke('Golett',[r,2,334,"Iron Defense",-1,"Shadow Punch",-1,"Stomping Tantrum",-1,"Rollout",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Golett',[r,2,334,"Iron Defense",-1,"Shadow Punch",-1,"Stomping Tantrum",-1,"Mega Punch",-1,None,None,0,"Poke Ball"])])
            elif rando >= .55 and rando < .8:
                r = random.randint(17,21+mod)
                if r < 19:
                    battle(P,[poke.Poke('Zubat',[r,random.randint(0,1),334,"Wing Attack",-1,"Confuse Ray",-1,"Bite",-1,"Astonish",-1,None,None,0,"Poke Ball"])])
                elif r < 24:
                    battle(P,[poke.Poke('Zubat',[r,random.randint(0,1),334,"Air Cutter",-1,"Confuse Ray",-1,"Bite",-1,"Astonish",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Golbat',[r,random.randint(0,1),334,"Air Cutter",-1,"Confuse Ray",-1,"Bite",-1,"Swift",-1,None,None,0,"Poke Ball"])])
            else:
                r = random.randint(18,21+mod)
                if r < 22:
                    battle(P,[poke.Poke('Whismur',[r,random.randint(0,1),334,"Screech",-1,"Echoed Voice",-1,"Pound",-1,"Supersonic",-1,None,None,0,"Poke Ball"])])
                elif r < 24:
                    battle(P,[poke.Poke('Whismur',[r,random.randint(0,1),334,"Screech",-1,"Echoed Voice",-1,"Stomp",-1,"Supersonic",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Loudred',[r,random.randint(0,1),334,"Screech",-1,"Echoed Voice",-1,"Stomp",-1,"Supersonic",-1,None,None,0,"Poke Ball"])])
            P.song = "music/mirror_cave.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if tim%30 == 0:
            if P.mc_steel == P.mc_steel1:
                P.mc_steel = P.mc_steel2
            else:
                P.mc_steel = P.mc_steel1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def pianura_bakery_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pia_bake_back, (P.px, P.py))
    P.surface.blit(P.char_shad,(P.px+450,P.py+213))
    P.surface.blit(P.pia_bake_clerk,(P.px+448,P.py+184))

def pianura_bakery_p(P,temppx,temppy,move):
    #rects start
    if P.pia_bake_cheryl:
        cheryl = P.pia_bake_cheryl.y_dist() > 0
        if cheryl:
            P.pia_bake_cheryl.move()
    mom = P.pia_bake_mom.y_dist() > 0
    kid = P.pia_bake_kid.y_dist() > 0
    if mom:
        P.pia_bake_mom.move()
    if kid:
        P.pia_bake_kid.move()
    P.pia_bake_hiker.move()
    r0 = (P.px+100,P.py+50,300,40)
    r1 = (P.px,P.py+400,350,40)
    r3 = (P.px-50,P.py+50,50,340)
    r4 = (P.px+400,P.py+100,50,240)
    r2 = (P.px+350,P.py+350,50,40)
    r5 = (P.px+100,P.py+300,50,40)
    r6 = (P.px+100,P.py+200,50,40)
    r7 = (P.px+250,P.py+150,50,40)
    r8 = (P.px+50,P.py+50,50,90)
    r9 = (P.px,P.py,50,40)
    r10 = P.pia_bake_mom.get_rect()
    r11 = P.pia_bake_kid.get_rect()
    r12 = r1
    if P.pia_bake_cheryl:
        r12 = P.pia_bake_cheryl.get_rect()
    rects = [r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if not kid:
        P.pia_bake_kid.move(temppx,temppy)
    if not mom:
        P.pia_bake_mom.move(temppx,temppy)
    if P.pia_bake_cheryl:
        if not cheryl:
            P.pia_bake_cheryl.move(temppx,temppy)

def pianura_bakery_f(P,temppx,temppy):
    P.surface.blit(P.pia_bake_f,(temppx,temppy))

def pianura_bakery(P) -> None:
    set_mixer_volume(P,P.vol)
    if P.song != "music/pianura.wav":
        P.song = "music/pianura.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    box = load("p/3_box.png")
    #23
    if P.prog[0] >= 87 and get_time() >= 19 and get_time() < 23:
        x = 0
        if P.px == 25 and P.py == 25:
            x = 50
        P.pia_bake_cheryl = npc.NPC(P,'Cheryl','Dude',[350,250+x],[['r',20]],["I just love coming here at the","end of the day and trying all","the desserts they have!","Pokemon love them too, but","they tend to enjoy specific","types of foods!"])
    else:
        P.pia_bake_cheryl = None
    P.pia_bake_clerk = pygame.transform.scale(load("p/spr/mart_clerk_l1.png"),(55,66))
    P.pia_bake_back = load("p/pianura/pianura_bakery.png")
    P.pia_bake_f = load("p/pianura/pianura_bakery_f.png")
    P.pia_bake_hiker = npc.NPC(P,'Beauty','Dude',[450,100],[['l',20]],["Man would just you look at all","those gems! I wish I could see","these when I'm out hiking!"])
    P.pia_bake_kid = npc.NPC(P,'Preschoolerg','Dude',[250,100],[['d',20]],["Ahh! There are so many colors,","it must taste amazing!",""])
    P.pia_bake_mom = npc.NPC(P,'Healer','Dude',[250,200],[['u',20]],["It's so delicious, but I can","feel myself getting fatter by","the second!"])
    move = True
    tim = 0
    pianura_bakery_b(P)
    pianura_bakery_p(P,P.px,P.py,False)
    pianura_bakery_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        pianura_bakery_b(P)
        temppx = P.px
        temppy = P.py
        pianura_bakery_p(P,temppx,temppy,move)
        pianura_bakery_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 25 and P.py == 75 and face_r(P):
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Welcome to the Pianura Bakery!","May I help you?")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            poke_mart(P, mt)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"Please come again!")
                    elif P.pia_bake_kid.talk():
                        pianura_bakery_b(P)
                        pianura_bakery_p(P,P.px,P.py,False)
                        pianura_bakery_f(P,P.px,P.py)
                        P.pia_bake_kid.write()
                    elif P.pia_bake_mom.talk():
                        pianura_bakery_b(P)
                        pianura_bakery_p(P,P.px,P.py,False)
                        pianura_bakery_f(P,P.px,P.py)
                        P.pia_bake_mom.write()
                    elif P.pia_bake_cheryl and P.pia_bake_cheryl.talk():
                        pianura_bakery_b(P)
                        pianura_bakery_p(P,P.px,P.py,False)
                        pianura_bakery_f(P,P.px,P.py)
                        P.pia_bake_cheryl.write()
                    elif next_to(P,350,350):
                        txt(P,"The table is covered with all","sorts of tasty treats!")
                    elif P.px == 25 and P.py == 175 and face_r(P):
                        txt(P,"You're looking to help us make", "the treats here?", "")
                        txt(P,"Well I don't think letting a","noive handle our food would be","very wise.")
                        txt(P,"But if you ever get some","experience, you're welcome to","come back and help!")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 125 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -1525
            P.py = 775
            P.loc = 'pianura'
            end = False
        if P.px == 375 and P.py == 225 and face_u(P):
            P.px = -1375
            P.py = 1125
            P.p = P.d1
            P.loc = 'pianura'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def pianura_nursery_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pia_nurse_back, (P.px, P.py))
    P.surface.blit(P.char_shad,(P.px+300,P.py+113))
    P.surface.blit(P.pia_nurse_mom,(P.px+298,P.py+84))
    P.surface.blit(P.char_shad,(P.px+200,P.py+113))
    P.surface.blit(P.pia_nurse_exp,(P.px+198,P.py+84))

def pianura_nursery_p(P,temppx,temppy,move):
    #rects start
    if P.pia_nurse_cheryl:
        cheryl = P.pia_nurse_cheryl.y_dist() > 0
        if cheryl:
            P.pia_nurse_cheryl.move()
    r0 = (P.px,P.py+50,50,40)
    r1 = (P.px,P.py+400,550,40)
    r2 = (P.px+550,P.py+100,50,290)
    r3 = (P.px-50,P.py+100,50,290)
    r4 = (P.px+50,P.py+100,50,40)
    r5 = (P.px+450,P.py+100,50,40)
    r6 = (P.px+100,P.py+150,350,40)
    r8 = (P.px+500,P.py+50,50,40)
    r9 = r1
    if P.pia_nurse_cheryl:
        r9 = P.pia_nurse_cheryl.get_rect()
    rects = [r9,r8,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.pia_nurse_cheryl:
        if not cheryl:
            P.pia_nurse_cheryl.move(temppx,temppy)

def pianura_nursery_f(P,temppx,temppy):
    pass
    #P.surface.blit(P.egi_mine_f,(temppx+5,temppy+325))

def pianura_nursery(P) -> None:
    set_mixer_volume(P,P.vol)
    if P.song != "music/pianura.wav":
        P.song = "music/pianura.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    #19
    if P.prog[0] >= 87 and get_time() >= 15 and get_time() < 19:
        x = 0
        if P.px == 325 and P.py == 125:
            x = 400
        P.pia_nurse_cheryl = npc.NPC(P,'Cheryl','Cherry',[50+x,150],[['u',20]],["Hey "+P.save_data.name+"! Have you been" ,"helping out with nursing the","Pokemon left here?","It's a great way to learn how","to care for your own Pokemon!",""])
    else:
        P.pia_nurse_cheryl = None
    P.pia_nurse_back = load("p/pianura/pianura_nursery.png")
    P.pia_nurse_mom = pygame.transform.scale(load("p/spr/healer_d1.png"),(54,64))
    P.pia_nurse_exp = pygame.transform.scale(load("p/spr/Expertf_d1.png"),(54,64))
    move = True
    tim = 0
    pianura_nursery_b(P)
    pianura_nursery_p(P,P.px,P.py,False)
    pianura_nursery_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        pianura_nursery_b(P)
        temppx = P.px
        temppy = P.py
        pianura_nursery_p(P,temppx,temppy,move)
        pianura_nursery_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.pia_nurse_cheryl and P.pia_nurse_cheryl.talk():
                        pianura_nursery_b(P)
                        pianura_nursery_p(P,P.px,P.py,False)
                        pianura_nursery_f(P,P.px,P.py)
                        P.pia_nurse_cheryl.write()
                    elif P.px == 75 and P.py == 75 and face_u(P):
                        if P.prog[14] == None:
                            temp = P.surface.copy()
                            txt(P,"Would you like to leave one of","your Pokemon to stay here at","the nursery?")
                            txt(P,"If you leave it here with us","for a day, it's friendship","will increase.")
                            new_txt(P)
                            write(P,"It'll cost $800 to leave a","Pokemon here. Is that okay?")
                            if choice(P):
                                if P.save_data.money < 800:
                                    txt(P,"You don't have enough money!")
                                    break
                                txt(P,"Which Pokemon would you like","to leave here?")
                                fade_out(P)
                                ans = trade_poke(P,None,True,nurse_poke = True)
                                P.surface.blit(temp,(0,0))
                                fade_in(P)
                                if ans != None:
                                    if ans.gen == 0:
                                        hh = 'him'
                                    else:
                                        hh = 'her'
                                    txt(P,"Okay, we'll take good care of",ans.name+"! Remember to come","back tomorrow to pick "+hh+" up!")
                                    ans.heal()
                                    P.prog[14] = [[ans.code,ans.to_list()],datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),random.random()]
                                    P.party.remove(ans)
                                    P.save_data.money -= 800
                                else:
                                    txt(P,"Feel free to come back if","you change your mind!")
                            else:
                                txt(P,"Feel free to come back if","you change your mind!")
                        elif date_diff(P.prog[14][1]) < 82800:
                            if P.prog[14][0][1][1] == 0:
                                hh = ['him','his']
                            else:
                                hh = ['her','her']
                            txt(P,P.prog[14][0][1][18]+" isn't ready to","leave. If you take "+hh[0]+" back,",hh[1]+" friendship won't increase.")
                            new_txt(P)
                            write(P,"Are you sure you want to take","back "+P.prog[14][0][1][18]+"?")
                            if choice(P):
                                txt(P,"Okay, here you go!")
                                get_poke(P,poke.Poke(P.prog[14][0][0],P.prog[14][0][1]),False)
                                P.prog[14] = None
                            else:
                                txt(P,"Okay, don't forget to pick",hh[0]+" up!")
                        else:
                            r = P.prog[14][2]
                            if P.prog[14][0][1][1] == 0:
                                p_info = [P.prog[14][0][1][18],'he','He']
                            else:
                                p_info = [P.prog[14][0][1][18],'she','She']
                            if r < 0.15:
                                txt(P,p_info[0]+" seemed like "+p_info[1],"had an amazing time! "+p_info[2]+" got a","lot friendlier!")
                                amount = 150
                            elif r < 0.30:
                                txt(P,p_info[0]+" missed you. "+p_info[2]+" is","a little friendlier, but we","could have done better!")
                                amount = 40
                            else:
                                txt(P,p_info[0]+" had a good time!",p_info[2]+" should be quite a bit","friendlier now!")
                                amount = 80
                            txt(P,"Here you go. Thanks for using","our service!")
                            return_poke = poke.Poke(P.prog[14][0][0],P.prog[14][0][1])
                            return_poke.gain_friend(amount)
                            get_poke(P,return_poke,False)
                            P.prog[14] = None
                    elif P.px == 175 and P.py == 75 and face_u(P):
                        t = P.surface.copy()
                        if P.prog[8][1][0] == -1:
                            txt(P,"Are you interested in helping","us care for the Pokemon we","have kept here?")
                            txt(P,"You don't look ready to help","out yet, but if that changes","we'll gladly accept your help!")
                        elif P.prog[8][1][2][0] != None:
                            new_txt(P)
                            write(P,"Are you done nursing",P.prog[8][1][2][0][1][18]+"?")
                            if choice(P):
                                fade_out(P)
                                ans = trade_poke(P,None,True,return_nurse = True)
                                P.surface.blit(t,(0,0))
                                fade_in(P)
                                if ans != None:
                                    exp = 4*(200 - P.prog[8][1][2][0][1][15])
                                    money = int(800+(exp*(0.9+(0.1*P.prog[8][1][0]))))
                                    lvled = gain_skill(P,1,int((900+exp)/80))
                                    txt(P,"Good work! You can have $"+str(money),"for your trouble!")
                                    P.save_data.money += money
                                    P.party.remove(ans)
                                    P.prog[8][1][2][0] = None
                                    if lvled:
                                        txt(P,"Your nursing skill leveled up!")
                                        txt(P,"The bonus your nursing Pokemon","receive will be a little","higher than before!")
                                        if P.prog[8][1][0] == 2:
                                            gift = poke.Poke('Igglybuff',[1,random.randint(0,1),334,"Sing",-1,"Charm",-1,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 3:
                                            gift = poke.Poke('Mime Jr',[1,random.randint(0,1),334,"Barrier",-1,"Confusion",-1,"Pound",-1,"Tickle",-1,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 4:
                                            gift = poke.Poke('Bonsly',[1,random.randint(0,1),334,"Fake Tears",-1,"Copycat",-1,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 5:
                                            gift = poke.Poke('Wynaut',[1,random.randint(0,1),334,"Splash",-1,"Charm",-1,"Encore",-1,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 6:
                                            gift = poke.Poke('Azurill',[1,random.randint(0,1),334,"Splash",-1,"Water Gun",-1,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 7:
                                            gift = poke.Poke('Chingling',[1,random.randint(0,1),334,"Wrap",-1,None,None,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 8:
                                            gift = poke.Poke('Munchlax',[1,random.randint(0,1),334,"Tackle",-1,"Last Resort",-1,"Lick",-1,"Metronome",-1,None,None,0,"Nest Ball",0,'Ability'])
                                        elif P.prog[8][1][0] == 9:
                                            gift = poke.Poke('Cleffa',[1,random.randint(0,1),334,"Pound",-1,"Charm",-1,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        else:
                                            gift = poke.Poke('Happiny',[1,random.randint(0,1),334,"Pound",-1,"Charm",-1,None,None,None,None,None,None,0,"Nest Ball",0,'Ability'])
                                        txt(P,"Take this gift to commemorate","your improvement!")
                                        txt(P,"You received "+gift.name+"!")
                                        get_poke(P,gift,False)
                                else:
                                    txt(P,"Well come back when you've","maxed out its friendship!")
                            else:
                                txt(P,"Well come back when you've","maxed out its friendship!")
                        elif len(P.party) == 6:
                            txt(P,"If you want to take care of a","Pokemon, clear up a spot in","your team and come back!")
                        else:
                            poke_list = ['Skitty','Poochyena','Oddish','Pidgey','Whismur','Lotad','Joltik','Machop','Aron','Whismur','Electrike','Psyduck','Hoothoot','Karrablast','Shelmet','Ponyta','Seedot']
                            name_listm = ['Daniel','The Boss','Eric','Timmy','Alex','Toby','Jerry','Justin','Ash','Nathan','Latios','Alvin','Pun Pun','Fish','Kevin','David','Josh','Burger']
                            if P.save_data.gen == 0 and len(P.save_data.name) <= 9:
                                name_listm.append(P.save_data.name)
                            name_listf = ['Catherine','Sarah','Glitter','Venice','Latias','Jenny','Chloe','Violet','Rose','Baby','Sky','Jello','Sherbet']
                            if P.save_data.gen == 1 and len(P.save_data.name) <= 9:
                                name_listf.append(P.save_data.name)
                            move_list = ['Confide','Frustration','Return','Facade','Swagger','Round','Rest','Protect','Attract','Captivate','Double Team']
                            moves = []
                            for x in range(4):
                                rm = random.randint(0,len(move_list)-1)
                                moves.append(move_list.pop(rm))
                            gen = random.randint(0,1)
                            if gen == 0:
                                poke_name = name_listm[random.randint(0,len(name_listm)-1)]
                            else:
                                poke_name = name_listf[random.randint(0,len(name_listf)-1)]
                            r = random.randint(0,len(poke_list)-1)
                            txt(P,"Are you interested in helping","us care for the Pokemon we","have kept here?")
                            txt(P,"We'll give you a Pokemon, and","you can return it once you've","gotten it to max frienship.")
                            new_txt(P)
                            write(P,"We have a "+poke_list[r],"here for you to care for.","Would you like to take it?")
                            if choice(P):
                                txt(P,"Here you go! The Pokeball it","has will boost the friendship","it gains from walking!")
                                txt(P,"You can identify the Pokemon","you're nursing by the symbol","next to its name.")
                                txt(P,"Remember that they won't learn","any moves or evolve, and you","can't change their name!")
                                txt(P,"Take good care of "+poke_name+"!")
                                given = poke.Poke(poke_list[r],[random.randint(10,20),gen,334,moves[0],-1,moves[1],-1,moves[2],-1,moves[3],-1,None,None,0,"Nursery Ball",random.randint(50,200),'Random Ability',True,poke_name,True])
                                get_poke(P,given,False)
                                P.prog[8][1][2][0] = [given.code,given.to_list()]
                            else:
                                txt(P,"Well come back when you're","ready!")
                    elif next_to(P,50,100) or next_to(P,450,100):
                        txt(P,"These are some pretty roses!")
                    elif P.px == -25 and P.py == 75 and face_u(P):
                        t = P.surface.copy()
                        txt(P,P.save_data.name+" booted up the", "computer.")
                        fade_out(P)
                        open_cpu(P)
                        P.surface.blit(t,(0,0))
                        fade_in(P)
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 125 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = 25
            P.py = 25
            P.loc = 'pianura'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy):
    draw_waves(P, wx, wy)
    if P.px == -975 and P.py > -1025 and P.py <= -975:
        pcx = (1025 + P.py)
        pcy = ((1025 + P.py)/5)
    P.surface.blit(P.pc_black,(P.px+1330,P.py+1230))
    P.surface.blit(P.pcdr, (P.px + 1375 + pcx, P.py + 1230 - pcy))
    P.surface.blit(P.pcdl, (P.px + 1338 - pcx, P.py + 1230 - pcy))
    P.surface.blit(P.pia_back, (P.px - 450, P.py - 1200))
    if P.px == -1325 and P.py > -1025 and P.py <= -975:
        blit_small_door(P,-975)
    if P.px == -1425 and P.py > -25 and P.py <= 25:
        blit_small_door(P,25)
    if P.px == -1725 and P.py > -25 and P.py <= 25:
        blit_small_door(P,25)
    if P.px == 25 and P.py > -25 and P.py <= 25:
        blit_small_door(P,25)
    if P.px == -1525 and P.py > 725 and P.py <= 775:
        blit_small_door(P,765)
    if P.px == -725 and P.py > 725 and P.py <= 775:
        P.surface.blit(P.pia_gymdoor,(P.px+1099,P.py-526))
    if P.py > -25 and P.py <= 25:
        if P.px == -375:
            P.surface.blit(P.d1_door,(P.px+752,P.py+229))
        elif P.px == -425:
            P.surface.blit(P.d1_door,(P.px+798,P.py+229))
        elif P.px == -1025:
            P.surface.blit(P.d1_door,(P.px+1402,P.py+229))
        elif P.px == -1075:
            P.surface.blit(P.d1_door,(P.px+1448,P.py+229))
    P.surface.blit(P.gondola, (P.px + 826, P.py + 750 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 837, P.py + 810 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 838, P.py + 790 + abs(P.foam)+gy))
    draw_lamps(P,P.px,P.py,listx,listy,"b")

def pianura_p(P,temppx,temppy,move,gond,gy):
    battle = P.r3_battle.y_dist() > 0
    mom = P.pia_mom.y_dist() > 0
    kid = P.pia_kid.y_dist() > 0
    hiker = P.pia_hiker.y_dist() > 0
    ace = P.pia_ace.y_dist() > 0
    lass = P.pia_lass.y_dist() > 0
    beauty = P.pia_beauty.y_dist() > 0
    bea = P.pia_bea.y_dist() > 0
    rich = P.pia_rich.y_dist() > 0
    if battle:
        P.r3_battle.move()
        draw_grass(P,P.r3_battle.x,P.r3_battle.y,575,75,250,50,[P.px,P.py])
    if mom:
        P.pia_mom.move()
    if kid:
        P.pia_kid.move()
    if hiker:
        P.pia_hiker.move()
    if ace:
        P.pia_ace.move()
    if lass:
        P.pia_lass.move()
    if beauty:
        P.pia_beauty.move()
    if bea:
        P.pia_bea.move()
    if rich:
        P.pia_rich.move()
    if P.pia_cheryl:
        cheryl = P.pia_cheryl.y_dist() > 0
        if cheryl:
            P.pia_cheryl.move()
    if P.pia_rival:
        rival = P.pia_rival.y_dist() > 0
        if rival:
            P.pia_rival.move()
    # if aroma:
    #     P.fio_aroma.move()
    #rects start
    # tree1 = P.fio_tree1.y_dist() > 0
    # if tree1:
    #     P.fio_tree1.blit()
    r1 = (P.px+100,P.py+250,250,40)
    r2 = (P.px+350,P.py+200,50,40)
    r3 = (P.px+400,P.py+250,350,40)
    r4 = (P.px+750,P.py+200,100,40)
    r5 = (P.px+850,P.py+250,200,40)
    r6 = (P.px+50,P.py+450,50,690)
    r7 = (P.px+100,P.py+1150,550,40)
    r8 = (P.px+350,P.py+700,50,190)
    r9 = (P.px+400,P.py+950,200,140)
    r10 = (P.px+400,P.py+850,250,40)
    r11 = (P.px+650,P.py+900,50,240)
    r12 = (P.px+400,P.py+700,500,40)
    r13 = (P.px+850,P.py+750,50,240)
    r14 = (P.px+900,P.py+1000,150,40)
    r15 = (P.px+1000,P.py+1050,50,390)
    r16 = (P.px+1050,P.py+1450,850,40)
    r17 = (P.px+1900,P.py+1300,50,140)
    r18 = (P.px+1750,P.py+1250,150,40)
    r19 = (P.px+1700,P.py+1200,50,40)
    r20 = (P.px+1400,P.py+1250,300,40)
    r21 = (P.px+1350,P.py+1200,50,40)
    r22 = (P.px+1200,P.py+1250,150,40)
    r23 = (P.px+1200,P.py+1000,50,240)
    r24 = (P.px+1250,P.py+1000,650,40)
    r25 = (P.px+1900,P.py+650,50,340)
    r26 = (P.px+1950,P.py+650,350,40)
    r27 = (P.px+2300,P.py+500,50,140)
    r28 = (P.px+2300,P.py+300,50,90)
    r29 = (P.px+2350,P.py+400,50,90)
    r30 = (P.px+2150,P.py+250,150,40)
    r31 = (P.px+2100,P.py+200,50,40)
    r32 = (P.px+1850,P.py+250,250,40)
    r33 = (P.px+1800,P.py+200,50,40)
    r34 = (P.px+1500,P.py+250,300,40)
    r35 = (P.px+1400,P.py+200,100,40)
    r36 = (P.px+1200,P.py+250,200,40)
    r37 = (P.px+1300,P.py+450,100,40)
    r38 = (P.px+1550,P.py+450,100,40)
    r39 = (P.px+1400,P.py+550,150,40)
    r40 = (P.px+1350,P.py+600,250,40)
    r41 = (P.px+1400,P.py+650,150,40)
    r42 = (P.px+1200,P.py+650,100,40)
    r43 = (P.px+1650,P.py+650,100,40)
    r44 = (P.px+1300,P.py+800,100,40)
    r45 = (P.px+1550,P.py+800,100,40)
    r46 = (P.px+1200,P.py-250,50,490)
    r47 = (P.px+1000,P.py-250,50,490)
    r48 = (P.px+550,P.py-250,450,40)
    r49 = (P.px+500,P.py-450,50,190)
    r50 = (P.px+550,P.py-500,550,40)
    r51 = (P.px+1100,P.py-550,50,40)
    r52 = (P.px+1150,P.py-500,750,40)
    r53 = (P.px+1900,P.py-550,50,40)
    r54 = (P.px+1950,P.py-500,150,40)
    r55 = (P.px+2100,P.py-450,50,190)
    r56 = (P.px+1250,P.py-250,850,40)
    r57 = P.pia_mom.get_rect()
    r58 = P.pia_kid.get_rect()
    r59 = P.pia_hiker.get_rect()
    r60 = P.pia_ace.get_rect()
    r61 = P.pia_lass.get_rect()
    r62 = P.pia_beauty.get_rect()
    r63,r64,r75 = r1,r1,r1
    if P.pia_fish1:
        r63 = P.pia_fish1.get_rect()
        r64 = P.pia_fish2.get_rect()
    r65 = (P.px+1750,P.py-650,350,40)
    r66 = (P.px+1700,P.py-850,50,190)
    r67 = (P.px+2100,P.py-850,50,190)
    r68 = (P.px+1750,P.py-900,350,40)
    r69 = (P.px+1800,P.py-850,50,90)
    if P.px <= -1425:
        r69 = (P.px+1750,P.py-850,50,90)
    r70 = (P.px+1900,P.py-850,50,40)
    r71 = (P.px+1900,P.py-750,50,40)
    r72 = (P.px+2050,P.py-800,50,40)
    r73 = P.pia_rich.get_rect()
    r74 = P.pia_bea.get_rect()
    if P.pia_cheryl:
        r75 = P.pia_cheryl.get_rect()
    rects = [r75,r74,r73,r72,r71,r70,r69,r68,r67,r66,r65,r64,r63,r62,r61,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+837,P.py+863+abs(P.foam)+gy))
        P.surface.blit(P.p,(P.px+836,P.py+840+abs(P.foam)+gy))
    else:
        if move:
            if P.prog[0] == 65 and P.py == 375:
                if P.px == -675:
                    player_move(P,rects,manual_input = 'r',spd = 3)
                elif P.px == -775:
                    player_move(P,rects,manual_input = 'l',spd = 3)
                else:
                    player_move(P,rects,manual_input = 'u',spd = 3)
            if P.px >= -50:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,200)])
            else:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,190)])
        else:
            blit_player(P)
    if P.pia_cheryl:
        if not cheryl:
            P.pia_cheryl.move(temppx,temppy)
    if P.pia_rival:
        if not rival:
            P.pia_rival.move(temppx,temppy)
    if not battle:
        P.r3_battle.move(temppx,temppy)
        draw_grass(P,P.r3_battle.x,P.r3_battle.y,575,75,250,50,[temppx,temppy])
    if not mom:
        P.pia_mom.move(temppx,temppy)
    if not kid:
        P.pia_kid.move(temppx,temppy)
    if not hiker:
        P.pia_hiker.move(temppx,temppy)
    if not ace:
        P.pia_ace.move(temppx,temppy)
    if not lass:
        P.pia_lass.move(temppx,temppy)
    if not beauty:
        P.pia_beauty.move(temppx,temppy)
    if not bea:
        P.pia_bea.move(temppx,temppy)
    if not rich:
        P.pia_rich.move(temppx,temppy)
    if P.pia_fish1:
        P.pia_fish1.move(temppx,temppy)
        P.pia_fish2.move(temppx,temppy)

def pianura_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.pia_foam, (temppx + 91, temppy + 728 + abs(P.foam)))
    P.surface.blit(P.pia_f, (temppx + 50, temppy - 900))
    # P.surface.blit(P.fio_roof, (temppx + 199, temppy - 300))
    # P.surface.blit(P.fio_roof, (temppx + 1349, temppy - 300))
    # P.surface.blit(P.fio_roof, (temppx + 1799, temppy - 300))
    # P.surface.blit(P.fio_proof, (temppx + 725, temppy - 352))
    draw_lamps(P, temppx, temppy, listx, listy)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+1315,temppy+1049))
        P.surface.blit(P.pia_light,(temppx+240,temppy+512))
    show_location(P, P.loc_txt, tim)

def pianura(P,enter = False,x_pos = -200) -> None:
    #sci_tim = None,sci_curr = None
    if P.song != "music/pianura.wav":
        P.song = "music/pianura.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.r3_battle.x = x_pos
    if P.prog[0] == 86:
        P.prog[0] += 1
    set_location(P)
    gond = 0
    gy = 0
    if P.prog[0] == 80:
        P.prog[0] += 1
    if P.prog[0] >= 87 and get_time() >= 11 and get_time() < 15:
        x = 0
        if P.px == -175 and P.py == -275:
            x = 50
        P.pia_cheryl = npc.NPC(P,'Cheryl','Cherry',[1550+x,550+x],[['l',20]],["It's nice that these flowers","are in bloom all year long!","","That way the park is always","nice and colorful!",""])
        P.pia_rival = None
    elif P.prog[0] == 65:
        P.pia_cheryl = npc.NPC(P,'Cheryl','Cherry',[1100,-350],[['d',20]],["","",""])
        P.pia_rival = npc.NPC(P,'Rival',P.save_data.rival,[1100,-250],[['u',20]],["","",""])
    else:
        P.pia_cheryl = None
        P.pia_rival = None
    if P.prog[0] <= 75:
        P.pia_fish1 = npc.NPC(P,'Fisherman','Cherry',[1100,1400],[['d',20]],["Man, I can't wait until Route","3 opens up again! The fish","here just don't bite!"])
        P.pia_fish2 = npc.NPC(P,'Fisherman','Cherry',[1550,1400],[['d',20]],["Do you think the fish will","still bite if the worms get","soggy?","Do worms even get soggy?","",""])
    else:
        P.pia_fish1 = None
        P.pia_fish2 = None
    pcx = 0
    pcy = 0
    P.pia_mom = npc.NPC(P,'Healer','Cherry',[1300,500],[['d',20]],["Ahh, I'm glad she's so full of","energy, but I don't think I","can keep up with her..."])
    P.pia_kid = npc.NPC(P,'Preschoolerg','Cherry',[1350,850],[['u',120],['mr',40],['u',200],['mr',30],['mu',30],['u',300],['md',30],['ml',30],['u',150],['ml',40]],["I'm playing hide-and-seek with","my mom! Don't tell her where","I'm hiding!"],spd = 1)
    P.pia_hiker = npc.NPC(P,'Hiker','Cherry',[2250,500],[['l',20]],["Oof! I took one step in that","cave, and I couldn't see a","damn thing!","People always said it was","risky to wander in there. I","guess now I know why!"])
    P.pia_lass = npc.NPC(P,'Lass','Cherry',[2000,-450],[['u',20]],["They all look so yummy! But I","only have enough money to buy","one of them!"])
    P.pia_beauty = npc.NPC(P,'Beauty','Cherry',[500,1100],[['d',20]],["Sometimes you just have to","take a break and admire nature","for a bit.","Then when you're well rested","you can get back to the rush","of life!","Or you can be like me and keep","taking it easy!",""])
    P.pia_ace = npc.NPC(P,'Ace Trainerf','Cherry',[650,450],[['mr',40],['ml',40]],["I just left my Pokemon at the","nursery, but I miss it so much","already!","I wanna run back in there and","take it back, but then the","money I spent will go to waste!"])
    P.pia_bea = npc.NPC(P,'Beauty','Cherry',[1950,-850],[['l',20]],["The breeze up here is so nice","and cool!","","Coupled with this delicious","sundae, I feel so refreshed!",""])
    P.pia_rich = npc.NPC(P,'Rich Boy','Cherry',[1850,-850],[['r',20]],["Would you just look at the","size of this sundae!","","I don't think I'll be able to","fit all of this in my stomach","without it hurting!"])
    fade = None
    move = True
    wx = 0
    wy = 0
    tim = 0
    listx = [338,338,638,638,91,1042,1042,1042,1492,1867,1192,1192,1738,1738,545,1038,1192,1650,2085]
    listy = [550,750,750,1000,1000,850,1075,1300,1300,1300,700,300,700,300,-402,-402,-402,-402,-402]
    # listx = [442,715,1088,1289,1565,1838,709,995,1283,1571,715,1565,1838,1838,1434,846,-60]
    # listy = [-1250,-1250,-1250,-1250,-1250,-1250,-1000,-1000,-1000,-1000,-1500,-1500,-1550,-1700,-1745,-1745,-1600]
    if enter == False:
        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
        pianura_p(P,P.px,P.py,False,gond,gy)
        pianura_f(P,P.px,P.py,listx,listy,tim)
        fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        if P.prog[0] == 65 and P.py == 425:
            move = False
            P.pia_rival = npc.NPC(P,'Rival',P.save_data.rival,[1100,-250],[['d',20]],["","",""])
            pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
            pianura_p(P,P.px,P.py,False,gond,gy)
            pianura_f(P,P.px,P.py, listx, listy, tim)
            txt(P,"Hey "+P.save_data.name+"!","You came at just the right", "time!")
            P.pia_cheryl = npc.NPC(P,'Cheryl','Cherry',[1100,-350],[['mr',20],['md',40],['d',20]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 66 and P.pia_cheryl.y == -250:
            txt(P,"I was just talking to "+P.save_data.rival,"about the Pokemon that's been","running amok in Route 3.")
            txt(P,"You must be the one Colress","sent over to assist us with","this situation.")
            txt(P,"I'm afraid we're quite short","on time. When you're prepared,","come meet me at Route 3.")
            P.pia_cheryl = npc.NPC(P,'Cheryl','Cherry',[1150,-250],[['md',20]],["","",""])
            P.pia_rival = npc.NPC(P,'Rival',P.save_data.rival,[1100,-250],[['d',160],['md',20],['d',20]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 67 and P.pia_rival.y == -200:
            txt(P,"You think this is connected to","those shady people we saw in","Scarab Woods?")
            txt(P,"If they started something this","big, it'd be pretty dangerous","to let them run free.")
            txt(P,"Anyways, I'll head on over to","Route 3. Catch you there!")
            P.pia_rival = npc.NPC(P,'Rival',P.save_data.rival,[1100,-200],[['mr',10],['md',100]],["","",""],spd = 1)
            P.p = P.d1
            P.prog[0] += 1
        if P.prog[0] == 68 and P.pia_rival.y == 200:
            move = True
            P.pia_rival = None
            P.pia_cheryl = None
            P.prog[0] += 1
        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
        temppx = P.px
        temppy = P.py
        pianura_p(P,temppx,temppy,move,gond,gy)
        pianura_f(P, temppx, temppy, listx, listy, tim)
        if gond == 1:
            gond = 2
            fade_in(P)
        # show_location(P,loc_txt,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and gond == 0 and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -525 and P.py == -525 and face_l(P):
                        nxtl = gondolier(P)
                        if nxtl != "Pianura City":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.pia_mom.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_mom.write()
                    elif P.pia_kid.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_kid.write()
                    elif P.pia_hiker.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_hiker.write()
                    elif P.pia_ace.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_ace.write()
                    elif P.pia_lass.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_lass.write()
                    elif P.pia_beauty.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_beauty.write()
                    elif P.pia_rich.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_rich.write()
                    elif P.pia_bea.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_bea.write()
                    elif P.pia_fish1 and P.pia_fish1.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_fish1.write()
                    elif P.pia_fish2 and P.pia_fish2.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_fish2.write()
                    elif P.pia_cheryl and P.pia_cheryl.talk():
                        pianura_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        pianura_p(P,P.px,P.py,False,gond,gy)
                        pianura_f(P,P.px,P.py, listx, listy, tim)
                        P.pia_cheryl.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            end = False
            fade = P.song
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == 325 and P.py in [-75,-25,-125] and face_l(P):
            P.px = -5775
            P.loc = 'route_3'
            route_3(P,True,P.r3_battle.x+6100)
            end = False
        if P.px == -1325 and P.py == -975 and face_u(P):
            P.loc = "house_1_12"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -1425 and P.py == 25 and face_u(P):
            P.loc = "house_1_13"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -1725 and P.py == 25 and face_u(P):
            P.loc = "house_1_14"
            P.px = 175
            P.py = -75
            end = False
        if P.py == 25 and face_u(P):
            if P.px == -375 or P.px == -425:
                P.px += 500
                P.py = -125
                P.loc = "house_21_4"
                end = False
            elif P.px == -1025 or P.px == -1075:
                P.px += 1150
                P.py = -125
                P.loc = "house_21_5"
                end = False
        if P.px == 25 and P.py == 25 and face_u(P):
            P.loc = "pianura_nursery"
            P.px = 125
            P.py = -75
            end = False
        if P.px == -1525 and P.py == 775 and face_u(P):
            P.loc = "pianura_bakery"
            P.px = 125
            P.py = -75
            end = False
        if P.px == -1375 and P.py == 1125 and face_u(P):
            P.px = 375
            P.py = 225
            P.p = P.d1
            P.loc = 'pianura_bakery'
            P.move_out_dir = 'd'
            end = False
        if P.py == -975 and P.px == -975 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_pianura"
            fade = P.song
            end = False
        if P.px == -725 and P.py == 775 and face_u(P):
            P.px = -25
            P.py = -525
            P.loc = "pia_gym"
            fade = P.song
            end = False
        if P.py in [-175,-125] and P.px == -1925 and face_r(P):
            P.px = -375
            P.py += 350
            P.loc = "mirror_cave"
            fade = P.song
            P.move_out_dir = 'r'
            end = False
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def scarab_r_b(P,cam_mod = 0):
    P.surface.blit(P.sr_back,(P.px+50+cam_mod,P.py-1000))
    if P.prog[6][28] == 0:
        P.surface.blit(P.item_out,(P.px+1150,P.py-650))
        P.surface.blit(P.grass,(P.px+1150,P.py-660))
    if P.prog[6][29] == 0:
        P.surface.blit(P.item_out,(P.px+1450,P.py-150))
        P.surface.blit(P.grass,(P.px+1450,P.py-160))
    if P.prog[6][30] == 0:
        P.surface.blit(P.item_out,(P.px+1550,P.py+700))
        P.surface.blit(P.grass,(P.px+1550,P.py+690))
    if P.prog[6][31] == 0:
        P.surface.blit(P.item_out,(P.px+2500,P.py))
        P.surface.blit(P.grass,(P.px+2500,P.py-10))

def scarab_r_p(P,temppx,temppy,move,cam_mod = 0):
    #rects start
    beauty = P.sr_beauty.y_dist() > 0
    ace = P.sr_ace.y_dist() > 0
    if P.sr_rival:
        rival = P.sr_rival.y_dist() > 0
        if rival:
            P.sr_rival.move()
            draw_grass(P,P.sr_rival.x,P.sr_rival.y,-625,425,400,100,[P.px,P.py])
            draw_grass(P,P.sr_rival.x,P.sr_rival.y,-1525,-125,200,200,[P.px,P.py])
    if P.sr_proton:
        proton = P.sr_proton.y_dist() > 0
        if proton:
            P.sr_proton.move(cam_modx = cam_mod)
        one = P.sr_rock1.y_dist()> 0
        if one:
            P.sr_rock1.move(cam_modx = cam_mod)
        two = P.sr_rock2.y_dist()> 0
        if two:
            P.sr_rock2.move(cam_modx = cam_mod)
        three = P.sr_rock3.y_dist()> 0
        if three:
            P.sr_rock3.move(cam_modx = cam_mod)
        four = P.sr_rock4.y_dist()> 0
        if four:
            P.sr_rock4.move(cam_modx = cam_mod)
    if beauty:
        P.sr_beauty.move()
    if ace:
        P.sr_ace.move()
    tree1 = P.sr_tree1.y_dist() > 0
    tree2 = P.sr_tree2.y_dist() > 0
    tree3 = P.sr_tree3.y_dist() > 0
    tree4 = P.sr_tree4.y_dist() > 0
    tree5 = P.sr_tree5.y_dist() > 0
    tree6 = P.sr_tree6.y_dist() > 0
    tree7 = P.sr_tree7.y_dist() > 0
    tree8 = P.sr_tree8.y_dist() > 0
    if tree1:
        P.sr_tree1.blit()
    if tree2:
        P.sr_tree2.blit()
    if tree3:
        P.sr_tree3.blit()
    if tree4:
        P.sr_tree4.blit()
    if tree5:
        P.sr_tree5.blit()
    if tree6:
        P.sr_tree6.blit()
    if tree7:
        P.sr_tree7.blit()
    if tree8:
        P.sr_tree8.blit()
    if P.sr_pin1:
        P.sr_pin1.move()
        P.sr_pin2.move()
    r1 = (P.px+650,P.py-250,50,90)
    r2 = (P.px+600,P.py-150,50,90)
    r3 = (P.px+650,P.py-50,50,90)
    r4 = (P.px+700,P.py-300,200,40)
    r5 = (P.px+850,P.py-400,50,90)
    r6 = (P.px+800,P.py-450,100,40)
    r7 = (P.px+750,P.py-650,50,190)
    r8 = (P.px+800,P.py-700,400,40)
    r9 = (P.px+1200,P.py-650,50,90)
    r10 = (P.px+1250,P.py-600,350,40)
    r11 = r1
    if P.prog[15][5] == 0:
        r11 = (P.px+1400,P.py-550,50,40)
    r12 = (P.px+1200,P.py-500,400,40)
    r120 = (P.px+1600,P.py-650,50,40)
    r121 = (P.px+1650,P.py-700,200,40)
    r122 = (P.px+1850,P.py-650,50,40)
    r123 = (P.px+1900,P.py-600,50,140)
    r124 = (P.px+1850,P.py-450,50,40)
    r125 = (P.px+1650,P.py-400,200,40)
    r126 = (P.px+1600,P.py-450,50,40)
    r13 = (P.px+1000,P.py-450,200,40)
    r14 = (P.px+950,P.py-500,50,40)
    r15 = (P.px+1000,P.py-400,50,240)
    r16 = (P.px+1050,P.py-200,450,40)
    r17 = (P.px+1500,P.py-150,50,240)
    r18 = (P.px+700,P.py+50,100,40)
    r19 = (P.px+750,P.py+100,50,540)
    r20 = (P.px+850,P.py+300,50,40)
    r21 = (P.px+1000,P.py+150,450,40)
    r22 = (P.px+1000,P.py+200,50,340)
    r23 = (P.px+800,P.py+650,400,40)
    r24 = (P.px+1050,P.py+500,400,40)
    r25 = (P.px+1150,P.py+700,50,40)
    r26 = (P.px+1200,P.py+750,400,40)
    r27 = (P.px+1600,P.py+550,50,190)
    r28 = (P.px+1500,P.py+500,100,40)
    r29 = (P.px+1500,P.py+150,50,340)
    r30 = (P.px+1400,P.py+200,50,290)
    r31 = (P.px+1550,P.py+150,350,40)
    r32 = (P.px+1550,P.py,550,40)
    r33 = (P.px+1850,P.py+200,50,440)
    r34 = (P.px+2100,P.py+50,50,390)
    r35 = (P.px+2150,P.py+400,100,40)
    r36 = (P.px+1900,P.py+650,400,40)
    r37 = (P.px+2250,P.py+350,50,90)
    r38 = (P.px+2300,P.py+300,500,40)
    r39 = (P.px+2250,P.py+700,50,40)
    r40 = (P.px+2300,P.py+750,500,40)
    r41 = (P.px+2250,P.py+500,50,40)
    r42 = (P.px+2400,P.py+650,50,40)
    r43 = (P.px+2550,P.py+600,50,40)
    r44 = (P.px+2700,P.py+600,50,40)
    r45 = (P.px+2650,P.py+450,50,40)
    r46 = (P.px+2550,P.py+350,50,40)
    r47 = (P.px+2450,P.py+400,50,40)
    r48 = (P.px+2800,P.py+600,50,140)
    r49 = (P.px+2800,P.py+350,50,140)
    r50 = (P.px+2850,P.py+600,250,40)
    r51 = (P.px+2850,P.py+450,150,40)
    r52 = (P.px+2950,P.py+50,50,390)
    r53 = (P.px+3100,P.py-300,50,890)
    r54 = (P.px+3050,P.py+150,50,40)
    r55 = (P.px+2500,P.py+50,450,40)
    r56 = (P.px+2450,P.py-300,50,340)
    r57 = (P.px+2500,P.py-350,100,40)
    r58 = (P.px+2600,P.py-400,100,40)
    r59 = (P.px+2700,P.py-350,400,40)
    r60 = P.sr_tree1.get_rect()
    r61 = P.sr_tree2.get_rect()
    r62 = P.sr_tree3.get_rect()
    r63 = P.sr_tree4.get_rect()
    r64 = P.sr_tree5.get_rect()
    r65 = P.sr_tree6.get_rect()
    r66 = P.sr_tree7.get_rect()
    r67 = P.sr_tree8.get_rect()
    r68 = P.sr_beauty.get_rect()
    r69 = P.sr_ace.get_rect()
    r70,r71,r72,r73 = r1,r1,r1,r1
    if P.prog[6][28] == 0:
        r70 = (P.px+1150,P.py-650,50,40)
    if P.prog[6][29] == 0:
        r71 = (P.px+1450,P.py-150,50,40)    
    if P.prog[6][30] == 0:
        r72 = (P.px+1550,P.py+700,50,40)
    if P.prog[6][31] == 0:
        r73 = (P.px+2500,P.py,50,40)
    rects = [r126,r125,r124,r123,r122,r121,r120,r73,r72,r71,r70,r69,r68,r67,r66,r65,r64,r63,r62,r61,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r48,r49,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if P.prog[0] == 55:
        if P.py > -175:
            player_move(P,rects,manual_input = 'd',spd = 3)
        elif P.px > -1675:
            player_move(P,rects,manual_input = 'r',spd = 3)
        else:
            P.prog[0] += 1
            P.p = P.r1
            blit_player(P)
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['r',50]],["","",""])
    elif P.prog[0] == 58:
        if P.sr_rival.x < 2120:
            blit_player(P)
        elif P.px > -1975:
            player_move(P,rects,manual_input = 'r',spd = 3)
        else:
            P.prog[0] += 1
            blit_player(P)
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.sr_rival.x,P.sr_rival.y],[['r',50]],["","",""])
    elif move:
        if P.px == -975 and P.py == 825 and face_r(P) and P.prog[15][5] == 0:
            player_move(P,rects,manual_input = 'l')
        else:
            player_move(P,rects,modx = cam_mod)
    else:
        if P.prog[15][5] == 1 and P.px > -1225:
            player_move(P,rects,manual_input = 'r',spd = 3)
        else:
            blit_player(P,modx = cam_mod)
    draw_grass(P,temppx,temppy,-2125,575,600,350,ignore = [(-2675,375),(-2625,375),(-2675,325),(-2625,325),(-2575,325),(-2525,325),(-2675,275),(-2625,275),(-2575,275),(-2525,275),(-2475,275),(-2425,275)])
    draw_grass(P,temppx,temppy,-2625,25,100,350,ignore = [(-2625,25)])
    draw_grass(P,temppx,temppy,-2425,-225,200,100)
    draw_grass(P,temppx,temppy,-1525,225,200,600,ignore = [(-1675,-275),(-1675,-325),(-1625,-325),(-1575,-75),(-1525,-75),(-1525,-25)],modx = cam_mod)
    draw_grass(P,temppx,temppy,-1375,225,150,100,ignore = [(-1375,225),(-1425,225)])
    draw_grass(P,temppx,temppy,-825,-275,400,200)
    draw_grass(P,temppx,temppy,-625,-325,50,50)
    draw_grass(P,temppx,temppy,-625,425,500,200)
    draw_grass(P,temppx,temppy,-425,925,400,200)
    draw_grass(P,temppx,temppy,-425,225,200,600,ignore = [(-575,-175),(-575,-125),(-525,175),(-575,175),(-575,225),(-525,225),(-475,225)])
    if not tree1:
        P.sr_tree1.blit(temppx,temppy)
    if not tree2:
        P.sr_tree2.blit(temppx,temppy)
    if not tree3:
        P.sr_tree3.blit(temppx,temppy)
    if not tree4:
        P.sr_tree4.blit(temppx,temppy)
    if not tree5:
        P.sr_tree5.blit(temppx,temppy)
    if not tree6:
        P.sr_tree6.blit(temppx,temppy)
    if not tree7:
        P.sr_tree7.blit(temppx,temppy)
    if not tree8:
        P.sr_tree8.blit(temppx,temppy)
    if P.sr_rival:
        if not rival:
            P.sr_rival.move(temppx,temppy,cam_modx = cam_mod)
            draw_grass(P,P.sr_rival.x,P.sr_rival.y,-625,425,400,100,[temppx,temppy],modx = cam_mod)
            draw_grass(P,P.sr_rival.x,P.sr_rival.y,-1525,-125,200,150,[temppx,temppy],modx = cam_mod)
    if P.sr_proton:
        if not proton:
            P.sr_proton.move(temppx,temppy,cam_modx = cam_mod)
        if not one:
            P.sr_rock1.move(temppx,temppy,cam_modx = cam_mod)
        if not two:
            P.sr_rock2.move(temppx,temppy,cam_modx = cam_mod)
        if not three:
            P.sr_rock3.move(temppx,temppy,cam_modx = cam_mod)
        if not four:
            P.sr_rock4.move(temppx,temppy,cam_modx = cam_mod)
    if not beauty:
        P.sr_beauty.move(temppx,temppy)
    if not ace:
        P.sr_ace.move(temppx,temppy)

def scarab_r_f(P,temppx,temppy,tim,cam_mod = 0):
    P.surface.blit(P.sr_f,(temppx+640+cam_mod,temppy-507))
    set_sky(P)
    show_location(P, P.loc_txt, tim)

def scarab_r(P) -> None:
    if P.song != "music/scarab_woods.wav":
        P.song = "music/scarab_woods.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] == 80:
        P.prog[0] += 1
    P.sr_back = load("p/fiore/Scarab_Woods_r.png")
    P.sr_f = load("p/fiore/Scarab_rf.png")
    P.habitat = 'forest'
    if P.prog[15][5] == 0:
        P.sr_pin1 = npc.NPC(P,'Pinsir','Grunt',[1750,-550],[['l',20]],["","",""])
        P.sr_pin2 = npc.NPC(P,'Pinsir','Grunt',[1700,-550],[['r',20]],["","",""])
    else:
        P.sr_pin1 = None
        P.sr_pin2 = None
    P.sr_tree1 = cut_tree(P,900,-350,8)
    P.sr_tree2 = cut_tree(P,950,-400,9)
    P.sr_tree3 = cut_tree(P,900,-450,10)
    P.sr_tree4 = cut_tree(P,1450,50,13)
    P.sr_tree5 = cut_tree(P,1450,100,12)
    P.sr_tree6 = cut_tree(P,1450,150,11)
    P.sr_tree7 = cut_tree(P,3050,200,14)
    P.sr_tree8 = cut_tree(P,3000,250,15)
    if P.prog[0] == 51:
        P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[850,275-P.py],[['l',100]],["","",""])
    elif P.prog[0] == 54:
        P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['r',50]],["","",""])
    else:
        P.sr_rival = None
    if P.prog[0] <= 54:
        P.sr_proton = npc.NPC(P,'Rocket Admin','Proton',[2650,500],[['l',50]],["","",""])
        P.sr_rock1 = npc.NPC(P,'Team Rocketm','Grunt',[2550,450],[['d',50]],["","",""])
        P.sr_rock2 = npc.NPC(P,'Team Rocketf','Grunt',[2600,550],[['l',50]],["","",""])
        P.sr_rock3 = npc.NPC(P,'Team Rocketm','Grunt',[2500,550],[['r',50]],["","",""])
        P.sr_rock4 = npc.NPC(P,'Team Rocketf','Grunt',[2450,500],[['r',50]],["","",""])
    else:
        P.sr_proton = None
        P.sr_rock1 = None
        P.sr_rock2 = None
        P.sr_rock3 = None
        P.sr_rock4 = None
    move = True
    wx = 0
    wy = 0
    tim = 0
    cam_mod = 0
    set_location(P)
    scarab_r_b(P)
    scarab_r_p(P,P.px,P.py,False)
    scarab_r_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        if P.prog[0] == 56:
            if cam_mod > -300:
                cam_mod -= 3
            else:
                txt(P,"Unfortunately, today's mission","was a complete failure.")
                txt(P,"So much for legends of fierce","thunderstorms wrecking havoc","across the land.")
                txt(P,"We'll just have to resort to","provoking the other one and","hope it's not as pathetic.")
                txt(P,"...............")
                txt(P,"Who's over there!","Stop hiding and come out!")
                P.prog[0] += 1
                P.sr_rock1 = npc.NPC(P,'Team Rocketm','Grunt',[2550,450],[['l',50]],["","",""])
                P.sr_rock3 = npc.NPC(P,'Team Rocketm','Grunt',[2500,550],[['l',50]],["","",""])
                P.sr_rock4 = npc.NPC(P,'Team Rocketf','Grunt',[2450,500],[['l',50]],["","",""])
        if P.prog[0] == 57:
            if cam_mod < 0:
                cam_mod += 5
            else:
                P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['u',50]],["","",""])
                P.p = P.d1
                scarab_r_b(P)
                scarab_r_p(P,P.px,P.py,False)
                scarab_r_f(P,P.px,P.py,tim)
                txt(P,"Shoot! Looks like they caught", "us!")
                P.p = P.r1
                P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['md',20],['mr',120],['r',50]],["","",""])
                P.prog[0] += 1
        if P.prog[0] == 59:
            txt(P,"So you thought it wise to", "eavesdrop on our conversation","here, did you?")
            txt(P,"You two deal with them.","I must be on my way to report","to headquarters.")
            P.sr_proton = npc.NPC(P,'Rocket Admin','Proton',[2650,500],[['mr',100]],["","",""])
            P.sr_rock1 = npc.NPC(P,'Team Rocketm','Grunt',[2550,450],[['md',20],['mr',100]],["","",""])
            P.sr_rock2 = npc.NPC(P,'Team Rocketf','Grunt',[2600,550],[['mu',20],['mr',100]],["","",""])
            P.sr_rock3 = npc.NPC(P,'Team Rocketm','Grunt',[2500,550],[['ml',40],['l',100]],["","",""])
            P.sr_rock4 = npc.NPC(P,'Team Rocketf','Grunt',[2450,500],[['mu',20],['ml',20],['l',100]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 60 and P.sr_rock1.x == 2800:
            te = P.surface.copy()
            txt(P,"Hey, thanks again for the help","earlier, but it looks like our","friendship ends here!")
            play_music(P,"music/trainer_battle.wav",0)
            #battle(P,["Team Rocketf Grunt",poke.Poke('Wynaut',[10,random.randint(0,1),21,"Tackle",35,"Lick",30,"Odor Sleuth",40,None,None,None,None,0,"Poke Ball"])])
            battle(P,["Team Rocketf Grunt",poke.Poke('Fearow',[21,random.randint(0,1),334,"Pursuit",-1,"Mirror Move",-1,"Fury Attack",-1,"Aerial Ace",-1,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Weepinbell',[21,random.randint(0,1),334,"Poison Powder",-1,"Wrap",-1,"Stun Spore",-1,"Vine Whip",-1,None,None,0,"Poke Ball",0,"Chlorophyll"]),poke.Poke('Ariados',[22,random.randint(0,1),334,"Night Shade",-1,"Shadow Sneak",-1,"Infestation",-1,"Scary Face",-1,None,None,0,"Poke Ball",0,"Swarm"])])
            play_music(P,"music/scarab_woods.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            P.sr_rock3 = npc.NPC(P,'Team Rocketm','Grunt',[2400,550],[['l',40],['mr',40],['l',60]],["","",""])
            P.sr_rock4 = npc.NPC(P,'Team Rocketf','Grunt',[2400,450],[['mr',40],['l',100]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 61 and P.sr_rock3.x == 2500 and P.sr_rock3.face() == 'l':
            txt(P,"What? How did you guys beat us","so easily? These Pokemon were","specially trained!")
            txt(P,"Well Proton doesn't go easy on","nosy people, so you guys had","better stay out of this!")
            P.sr_rock3 = npc.NPC(P,'Team Rocketm','Grunt',[2500,550],[['mr',200]],["","",""],spd = 1)
            P.sr_rock4 = npc.NPC(P,'Team Rocketf','Grunt',[2500,450],[['md',10],['mr',160]],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 62 and P.sr_rock3.x == 2800:
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.sr_rival.x,P.sr_rival.y],[['mu',20],['u',50]],["","",""])
            P.p = P.d1
            P.prog[0] += 1
        if P.prog[0] == 63 and P.sr_rival.y == 500:
            txt(P,"I don't think we can catch up","to them but I'll go ahead to","check up on Pianura City.")
            txt(P,"You looked really strong out","there! I hope we can get a","rematch soon!")
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.sr_rival.x,P.sr_rival.y],[['mr',20]],["","",""],spd = 1)
            P.p = P.r1
            P.prog[0] += 1
        if P.prog[0] == 64 and P.sr_rival.x == 2800:
            move = True
            P.prog[0] += 1
            P.sr_proton = None
            P.sr_rock1 = None
            P.sr_rock2 = None
            P.sr_rock3 = None
            P.sr_rock4 = None
            P.sr_rival = None
        if P.prog[0] == 51 and P.px == -325:
            move = False
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[850,275-P.py],[['ml',40],['l',50]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 52 and P.sr_rival.x == 750:
            txt(P,"Hey there "+P.save_data.name+"!","I hope you've been doing well","since I last saw you.")
            txt(P,"I was just training in these","woods when I saw some strange","people heading deeper in.")
            txt(P,"I'm going to sneak back there","to investigate, but I could","use your help as well.")
            txt(P,"Anyways, I'll go there first.","You can join me when you're","more prepared.")
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[750,275-P.py],[['mr',200]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 53 and P.sr_rival.x == 1150:
            move = True
            P.prog[0] += 1
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['r',50]],["","",""])
        if P.prog[0] == 54 and P.py == -125 and P.px <= -1525:
            move = False
            P.sr_rival = npc.NPC(P,'Rival',P.save_data.rival,[2050,500],[['u',50]],["","",""])
            scarab_r_b(P)
            scarab_r_p(P,P.px,P.py,False)
            scarab_r_f(P,P.px,P.py,tim)
            txt(P,"Hey, you can come a little","closer. But be really quiet.")
            P.prog[0] += 1
        scarab_r_b(P,cam_mod)
        if move == True and P.sr_beauty.trainer_check():
            move = False
        if move == True and P.sr_ace.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        scarab_r_p(P,temppx,temppy,move,cam_mod)
        scarab_r_f(P,temppx,temppy,tim,cam_mod)
        if P.px == -975 and P.py == 825 and face_r(P):
            if P.prog[15][0] == 0:
                txt(P,"You see two Pinsir fighting","each other.")
                print_mega_area(P)
            elif P.prog[15][5] == 0:
                txt(P,"You see two Pinsir fighting","each other.")
                if in_party(P,'Pinsir',True):
                    new_txt(P)
                    write(P,"Enter the clearing?")
                    if choice(P):
                        move = False
                        P.prog[15][5] += 1
                        P.sr_pin1 = npc.NPC(P,'Pinsir','Grunt',[1750,-550],[['l',160],['mr',20],['l',500]],["","",""])
                        P.sr_pin2 = npc.NPC(P,'Pinsir','Grunt',[1700,-550],[['r',220],['l',60],['ml',20],['l',500]],["","",""])
                else:
                    txt(P,"You should bring a Pinsir","before trying to enter the","clearing.")
        if P.prog[15][5] == 1 and P.sr_pin2.x == 1650:
            te = P.surface.copy()
            txt(P,"The Pinsir charged straight","into you!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.tourney_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Pinsir' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Pinsir',[35,0,334,'Focus Energy',-1,'Harden',-1,'Bind',-1,'X-Scissor',-1,None,None,0,"Poke Ball",200,'Hyper Cutter'])],no_pc = True)
            play_music(P,"music/scarab_woods.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][5] = 0
                txt(P,"The Pinsir chased you out of","the clearing!")
                fade_out(P)
                P.p = P.l1
                P.px = -875
                P.py = 825
                P.sr_pin1 = npc.NPC(P,'Pinsir','Grunt',[1750,-550],[['l',20]],["","",""])
                P.sr_pin2 = npc.NPC(P,'Pinsir','Grunt',[1700,-550],[['r',20]],["","",""])
                scarab_r_b(P)
                scarab_r_p(P,P.px,P.py,False)
                scarab_r_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][5] += 1
                txt(P,"The Pinsir marched away in","humiliation. It left you with","a mysterious stone.")
                add_item(P,'Pinsirite',1)
                fade_out(P)
                P.sr_pin1 = None
                P.sr_pin2 = None
                scarab_r_b(P)
                scarab_r_p(P,P.px,P.py,False)
                scarab_r_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
            P.tourney_battle = False
        if trainer_check(P,P.sr_beauty,"music/scarab_woods.wav"):
            P.sr_beauty = npc.NPC(P,'Beauty','Lucille',[P.sr_beauty.x,P.sr_beauty.y],[[P.sr_beauty.face(),100]],["Do you think he's okay?","He hasn't texted me anything","for a while...","I mean, what's the worst that","could happen?",""])
            move = True
        if trainer_check(P,P.sr_ace,"music/scarab_woods.wav"):
            P.sr_ace = npc.NPC(P,'Ace Trainerm','James',[P.sr_ace.x,P.sr_ace.y],[[P.sr_ace.face(),100]],["That green haired guy was so","cool though! I mean he beat me","pretty badly, but still!","I want to be just like that","when I grow up! Super strong","and in charge of people!"])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.sr_beauty.talk():
                        if P.sr_beauty.trainer:
                            move = False
                        else:
                            scarab_r_b(P)
                            scarab_r_p(P,P.px,P.py,False)
                            scarab_r_f(P,P.px,P.py,tim)
                            P.sr_beauty.write()
                    elif P.sr_ace.talk():
                        if P.sr_ace.trainer:
                            move = False
                        else:
                            scarab_r_b(P)
                            scarab_r_p(P,P.px,P.py,False)
                            scarab_r_f(P,P.px,P.py,tim)
                            P.sr_ace.write()
                    elif next_to(P,1150,-650) and P.prog[6][28] == 0:
                        txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                        txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                        add_item(P,"Tiny Mushroom",1)
                        P.prog[6][28] = 1
                    elif next_to(P,1550,700) and P.prog[6][30] == 0:
                        txt(P,P.save_data.name + " found a Common", "Candy!")
                        txt(P,P.save_data.name + " put the Common","Candy in the Medicine pocket.")
                        add_item(P,"Common Candy",1)
                        P.prog[6][30] = 1
                    elif next_to(P,1450,-150) and P.prog[6][29] == 0:
                        item_fight(P,"music/scarab_woods.wav",29,20,('Mega Drain','Feint Attack','Ingrain','Bide'),'Foongus')
                    elif next_to(P,2500,0) and P.prog[6][31] == 0:
                        item_fight(P,"music/scarab_woods.wav",31,22,('Mega Drain','Feint Attack','Ingrain','Bide'),'Foongus')
                    elif next_to(P,P.sr_tree1.x,P.sr_tree1.y):
                        P.sr_tree1.cut()
                    elif next_to(P,P.sr_tree2.x,P.sr_tree2.y):
                        P.sr_tree2.cut()
                    elif next_to(P,P.sr_tree3.x,P.sr_tree3.y):
                        P.sr_tree3.cut()
                    elif next_to(P,P.sr_tree4.x,P.sr_tree4.y):
                        P.sr_tree4.cut()
                    elif next_to(P,P.sr_tree5.x,P.sr_tree5.y):
                        P.sr_tree5.cut()
                    elif next_to(P,P.sr_tree6.x,P.sr_tree6.y):
                        P.sr_tree6.cut()
                    elif next_to(P,P.sr_tree7.x,P.sr_tree7.y):
                        P.sr_tree7.cut()
                    elif next_to(P,P.sr_tree8.x,P.sr_tree8.y):
                        P.sr_tree8.cut()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == -275 and P.py in [425,375] and face_l(P):
            P.px = -1925
            P.py += 500
            P.loc = "fiore"
            P.move_out_dir = 'l'
            end = False
        if P.py == 625 and P.px in [-2275,-2225] and face_u(P):
            P.py = -175
            P.px -= 2550
            P.loc = "route_3"
            P.move_out_dir = 'u'
            end = False
        if move and (wild_grass(P,-2125,575,600,350,ignore = [(-2675,375),(-2625,375),(-2675,325),(-2625,325),(-2575,325),(-2525,325),(-2675,275),(-2625,275),(-2575,275),(-2525,275),(-2475,275),(-2425,275)]) or wild_grass(P,-2625,25,100,350,ignore = [(-2625,25)]) or wild_grass(P,-2425,-225,200,100) or wild_grass(P,-1525,225,200,600,ignore = [(-1675,-275),(-1675,-325),(-1625,-325),(-1575,-75),(-1525,-75),(-1525,-25)]) or wild_grass(P,-1375,225,150,100,ignore = [(-1375,225),(-1425,225)]) or wild_grass(P,-825,-275,400,200) or wild_grass(P,-625,-325,50,50) or wild_grass(P,-625,425,500,200) or wild_grass(P,-425,925,400,200) or wild_grass(P,-425,225,200,600,ignore = [(-575,-175),(-575,-125),(-525,175),(-575,175),(-575,225),(-525,225),(-475,225)])):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.2:
                r = random.randint(14,18)
                if r < 17:
                    battle(P,[poke.Poke('Kakuna',[r,random.randint(0,1),334,"Poison Sting",-1,"String Shot",-1,"Harden",-1,"Bug Bite",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Beedrill',[r,random.randint(0,1),334,"Twineedle",-1,"Pursuit",-1,"Fury Attack",-1,"Rage",-1,None,None,0,"Poke Ball"])])
            elif rando >= .2 and rando < .3:
                r = random.randint(15,18)
                if r < 16:
                    battle(P,[poke.Poke('Shelmet',[r,random.randint(0,1),334,"Absorb",-1,"Acid",-1,"Bide",-1,"Curse",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Shelmet',[r,random.randint(0,1),334,"Struggle Bug",-1,"Acid",-1,"Bide",-1,"Curse",-1,None,None,0,"Poke Ball"])])
            elif rando >= .3 and rando < .5:
                battle(P,[poke.Poke('Oddish',[random.randint(15,18),random.randint(0,1),334,"Absorb",-1,"Sleep Powder",-1,"Stun Spore",-1,"Poison Powder",-1,None,None,0,"Poke Ball"])])
            elif rando >= .5 and rando < .6:
                battle(P,[poke.Poke('Seviper',[random.randint(17,19),random.randint(0,1),334,"Wrap",-1,"Venoshock",-1,"Bite",-1,"Screech",-1,None,None,0,"Poke Ball"])])
            elif rando >= .6 and rando < .8:
                r = random.randint(14,18)
                if r < 15:
                    battle(P,[poke.Poke('Lotad',[r,random.randint(0,1),334,"Astonish",-1,"Absorb",-1,"Bubble",-1,"Natural Gift",-1,None,None,0,"Poke Ball"])])
                elif r < 18:
                    battle(P,[poke.Poke('Lotad',[r,random.randint(0,1),334,"Astonish",-1,"Absorb",-1,"Bubble",-1,"Mist",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Lombre',[r,random.randint(0,1),334,"Fake Out",-1,"Bubble",-1,"Absorb",-1,"Natural Gift",-1,None,None,0,"Poke Ball"])])
            else:
                r = random.randint(15,18)
                if get_time() > 19 or get_time() < 6:
                    battle(P,[poke.Poke('Misdreavus',[r,random.randint(0,1),334,"Mean Look",-1,"Confuse Ray",-1,"Astonish",-1,"Psywave",-1,None,None,0,"Poke Ball"])])
                else:
                    if r < 17:
                        battle(P,[poke.Poke('Pidgey',[r,random.randint(0,1),334,"Quick Attack",-1,"Gust",-1,"Sand Attack",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
                    elif r < 18:
                        battle(P,[poke.Poke('Pidgey',[r,random.randint(0,1),334,"Quick Attack",-1,"Gust",-1,"Sand Attack",-1,"Whirlwind",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Pidgeotto',[r,random.randint(0,1),334,"Quick Attack",-1,"Gust",-1,"Sand Attack",-1,"Whirlwind",-1,None,None,0,"Poke Ball"])])
            P.song = "music/scarab_woods.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def fiore_garden_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.fio_gar_back, (P.px, P.py))
    P.surface.blit(P.char_shad,(P.px+450,P.py+163))
    P.surface.blit(P.fio_gar_mom,(P.px+448,P.py+134))

def fiore_garden_p(P,temppx,temppy,move):
    #rects start
    if P.fio_gar_aroma:
        aroma = P.fio_gar_aroma.y_dist() > 0
        if aroma:
            P.fio_gar_aroma.move()
    r0 = (P.px+50,P.py+50,250,40)
    r1 = (P.px,P.py+400,550,40)
    r2 = (P.px+550,P.py+250,50,140)
    r3 = (P.px-50,P.py+150,50,240)
    r4 = (P.px+50,P.py+350,50,40)
    r5 = (P.px+150,P.py+350,50,40)
    r6 = (P.px,P.py+100,50,40)
    r7 = (P.px+300,P.py+100,50,40)
    r8 = (P.px+350,P.py+150,200,90)
    r9 = r1
    if P.fio_gar_aroma:
        r9 = P.fio_gar_aroma.get_rect()
    rects = [r9,r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.fio_gar_aroma:
        if not aroma:
            P.fio_gar_aroma.move(temppx,temppy)

def fiore_garden_f(P,temppx,temppy):
    P.surface.blit(P.fio_gar_tree,(temppx+45,temppy+290))
    P.surface.blit(P.fio_gar_tree,(temppx+145,temppy+290))
    #P.surface.blit(P.egi_mine_f,(temppx+5,temppy+325))

def fiore_garden(P) -> None:
    set_mixer_volume(P,P.vol)
    if P.song != "music/fiore.wav":
        P.song = "music/fiore.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.fio_gar_tree = pygame.transform.scale(load("p/spr/berry_trees/Aguav_tree_1.png"),(60,75))
    P.fio_gar_back = load("p/fiore/fiore_garden.png")
    P.fio_gar_mom = pygame.transform.scale(load("p/spr/healer_d1.png"),(54,64))
    P.fio_gar_aroma = None
    if not (datetime.datetime.today().weekday() == 5 and get_time() >= 6):
        P.fio_gar_aroma = npc.NPC(P,'Aroma Lady','Berry',[50,300],[['d',200],['mu',80],['l',300],['mr',80],['r',200],['md',40],['ml',20],['md',60],['l',300],['mu',20],['ml',60]],["Every weekend, I take some of","the berries grown here to sell","in Alto Mare.","The prices are quite good, so","if you ever have the chance","you should stop by!"])
    move = True
    tim = 0
    fiore_garden_b(P)
    fiore_garden_p(P,P.px,P.py,False)
    fiore_garden_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        fiore_garden_b(P)
        temppx = P.px
        temppy = P.py
        fiore_garden_p(P,temppx,temppy,move)
        fiore_garden_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -75 and P.py == 25 and face_u(P):
                        txt(P,"Are you looking to help out","with growing the berries?")
                        txt(P,"I apologize, but I am a little","hesitant about letting you","care for the plants.")
                        txt(P,"Maybe if you can find someone","to recommend you, I would be","willing to let you work here.")
                    elif next_to(P,0,100) or next_to(P,300,100):
                        txt(P,"These are some pretty roses!")
                    elif next_to(P,50,350) or next_to(P,150,350):
                        txt(P,"It's an Aguav Berry Tree.")
                    elif P.fio_gar_aroma and P.fio_gar_aroma.talk():
                        fiore_garden_b(P)
                        fiore_garden_p(P,P.px,P.py,False)
                        fiore_garden_f(P,P.px,P.py)
                        P.fio_gar_aroma.write()
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 125 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -1125
            P.py = 725
            P.loc = 'fiore'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def fiore_b(P,wx,wy,listx,listy,pcx,pcy,gy):
    draw_waves(P, wx, wy)
    if P.px == -425 and P.py > 275 and P.py <= 325:
        pcx = 50-(325 - P.py)
        pcy = 10-((325 - P.py)/5)
    P.surface.blit(P.pc_black,(P.px+780,P.py-70))
    P.surface.blit(P.pcdr, (P.px + 825 + pcx, P.py - 70 - pcy))
    P.surface.blit(P.pcdl, (P.px + 788 - pcx, P.py - 70 - pcy))
    P.surface.blit(P.fio_back, (P.px - 450, P.py - 1300))
    if P.px == 75 and P.py > 275 and P.py <= 325:
        blit_small_door(P,325)
    if P.px == -1075 and P.py > 275 and P.py <= 325:
        blit_small_door(P,325)
    if P.px == -1525 and P.py > 275 and P.py <= 325:
        blit_small_door(P,325)
    if P.px == -525 and P.py > 675 and P.py <= 725:
        blit_small_door(P,715)
    if P.px == -1125 and P.py > 675 and P.py <= 725:
        blit_small_door(P,715)
    P.surface.blit(P.gondola, (P.px + 1126, P.py - 50 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 1137, P.py + 10 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 1138, P.py - 10 + abs(P.foam)+gy))
    if P.prog[6][25] == 0:
        P.surface.blit(P.item_out,(P.px+950,P.py-900))
    draw_lamps(P,P.px,P.py,listx,listy,"b")

def fiore_p(P,temppx,temppy,move,gond,gy):
    heal = P.fio_healer.y_dist() > 0
    aroma = P.fio_aroma.y_dist() > 0
    if heal:
        P.fio_healer.move()
    if aroma:
        P.fio_aroma.move()
    #rects start
    tree1 = P.fio_tree1.y_dist() > 0
    if tree1:
        P.fio_tree1.blit()
    tree2 = P.fio_tree2.y_dist() > 0
    if tree2:
        P.fio_tree2.blit()
    tree3 = P.fio_tree3.y_dist() > 0
    if tree3:
        P.fio_tree3.blit()
    r1 = (P.px+100,P.py-300,50,440)
    r2 = (P.px+50,P.py-400,50,90)
    r3 = (P.px+100,P.py-500,50,90)
    r4 = (P.px+150,P.py-550,450,40)
    r5 = (P.px+150,P.py+150,850,40)
    r6 = (P.px+1000,P.py-300,50,440)
    r7 = (P.px+550,P.py-900,50,340)
    r8 = (P.px+1050,P.py-300,300,40)
    r9 = P.fio_tree1.get_rect()
    r10 = (P.px+1350,P.py-250,250,190)
    r11 = (P.px+250,P.py-500,50,40)
    r12 = (P.px+400,P.py-450,50,40)
    r13 = (P.px+200,P.py-250,250,190)
    r14 = (P.px+150,P.py-50,150,40)
    r15 = (P.px+350,P.py-50,150,40)
    r16 = (P.px+650,P.py-300,350,240)
    r17 = (P.px+600,P.py-50,200,40)
    r18 = (P.px+850,P.py-50,150,40)
    r19 = (P.px+600,P.py-950,400,40)
    r20 = (P.px+1000,P.py-900,50,40)
    r21 = (P.px+700,P.py-850,300,40)
    r22 = (P.px+700,P.py-800,50,390)
    r23 = (P.px+650,P.py-600,50,40)
    r24 = (P.px+750,P.py-450,150,40)
    r240 = (P.px+950,P.py-450,550,40)
    r241 = (P.px+900,P.py-500,50,40)
    r242 = (P.px+1550,P.py-450,150,40)
    r243 = (P.px+1500,P.py-500,50,40)
    r25 = (P.px+1800,P.py-250,250,190)
    r26 = (P.px+1200,P.py-50,250,40)
    r27 = (P.px+1150,P.py,50,90)
    r28 = (P.px+1200,P.py+100,150,40)
    r29 = (P.px+1350,P.py+150,750,40)
    r30 = (P.px+1500,P.py-50,150,40)
    r31 = (P.px+1750,P.py-50,150,40)
    r32 = (P.px+1950,P.py-50,150,40)
    r33 = (P.px+2100,P.py-200,50,340)
    r34 = (P.px+2150,P.py-200,150,40)
    r35 = (P.px+2100,P.py-350,150,90)
    r36 = (P.px+2100,P.py-500,150,90)
    r37 = (P.px+1900,P.py-500,150,90)
    r38 = (P.px+1900,P.py-350,150,90)
    r39 = (P.px+2300,P.py-300,50,90)
    r40 = (P.px+2350,P.py-300,150,40)
    r41 = (P.px+2500,P.py-350,50,40)
    r42 = (P.px+2300,P.py-400,200,40)
    r43 = (P.px+2300,P.py-550,50,140)
    r44 = (P.px+2350,P.py-650,50,90)
    r45 = (P.px+2300,P.py-700,50,40)
    r46 = (P.px+1700,P.py-750,600,40)
    r47 = (P.px+1650,P.py-700,50,240)
    r48 = P.fio_tree2.get_rect()
    r49 = P.fio_tree3.get_rect()
    r50,r51 = r1,r1
    if P.prog[6][25] == 0:
        r50 = (P.px+950,P.py-900,50,40)
    if P.prog[6][26] == 0:
        r51 = (P.px+2450,P.py-350,50,40)
    r52 = P.fio_healer.get_rect()
    r53 = P.fio_aroma.get_rect()
    rects = [r243,r242,r241,r240,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+1137,P.py+63+abs(P.foam)+gy))
        P.surface.blit(P.p,(P.px+1136,P.py+40+abs(P.foam)+gy))
    else:
        if move:
            if P.px >= -50:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,200)])
            else:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,190)])
        else:
            blit_player(P)
    if not tree1:
        P.fio_tree1.blit(temppx,temppy)
    if not tree2:
        P.fio_tree2.blit(temppx,temppy)
    if not tree3:
        P.fio_tree3.blit(temppx,temppy)
    if not heal:
        P.fio_healer.move(temppx,temppy)
    if not aroma:
        P.fio_aroma.move(temppx,temppy)

def fiore_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.fio_foam, (temppx + 1087, temppy - 272 + abs(P.foam)))
    P.surface.blit(P.fio_f, (temppx + 90, temppy - 700))
    P.surface.blit(P.fio_roof, (temppx + 199, temppy - 300))
    P.surface.blit(P.fio_roof, (temppx + 1349, temppy - 300))
    P.surface.blit(P.fio_roof, (temppx + 1799, temppy - 300))
    P.surface.blit(P.fio_proof, (temppx + 725, temppy - 352))
    x = 0
    y = 0
    for z in range(24):
        if z == 3:
            if P.prog[1] < 2:
                if int(tim/8)%2 == 0 and P.prog[1] == 1:
                    P.surface.blit(P.fio_pine2,(temppx+695+x,temppy-890+y))
                else:
                    P.surface.blit(P.fio_pine1,(temppx+695+x,temppy-890+y))
        else:
            if P.prog[1] == 3:
                P.surface.blit(P.fio_pine1,(temppx+695+x,temppy-890+y))
            else:
                P.surface.blit(P.fio_pine3,(temppx+695+x,temppy-890+y))
        if (z+1)%6 == 0:
            x = 0
            y += 50
        else:
            x += 50
    P.surface.blit(P.fio_berry1,(temppx+1345,temppy-940))
    P.surface.blit(P.fio_berry1,(temppx+1395,temppy-940))
    P.surface.blit(P.fio_berry1,(temppx+1445,temppy-940))
    P.surface.blit(P.fio_berry2,(temppx+1545,temppy-940))
    P.surface.blit(P.fio_berry2,(temppx+1595,temppy-940))
    P.surface.blit(P.fio_berry2,(temppx+1645,temppy-940))
    P.surface.blit(P.fio_berry3,(temppx+1345,temppy-840))
    P.surface.blit(P.fio_berry3,(temppx+1395,temppy-840))
    P.surface.blit(P.fio_berry3,(temppx+1445,temppy-840))
    P.surface.blit(P.fio_berry4,(temppx+1545,temppy-840))
    P.surface.blit(P.fio_berry4,(temppx+1595,temppy-840))
    P.surface.blit(P.fio_berry4,(temppx+1645,temppy-840))
    draw_lamps(P, temppx, temppy, listx, listy)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+765,temppy-249))
    show_location(P, P.loc_txt, tim)

def fiore(P) -> None:
    #change?
    if P.song != "music/fiore.wav":
        P.song = "music/fiore.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.habitat = 'grass'
    P.fio_back = load("p/fiore/Fiore Town.png")
    P.fio_foam = load("p/fiore/Fiore_foam.png")
    P.fio_f = load("p/fiore/Fiore_f.png")
    P.fio_roof = load("p/am/building_3_roof.png")
    P.fio_proof = load("p/am/poke_center_roof.png")
    P.fio_pine1 = pygame.transform.scale(load("p/spr/berry_trees/Pinap_tree_1.png"),(60,75))
    P.fio_pine2 = pygame.transform.scale(load("p/spr/berry_trees/Pinap_tree_2.png"),(60,75))
    P.fio_pine3 = pygame.transform.scale(load("p/spr/berry_trees/Pinap_tree_3.png"),(60,75))
    P.fio_berry1 = pygame.transform.scale(load("p/spr/berry_trees/Nanab_tree_1.png"),(60,75))
    P.fio_berry2 = pygame.transform.scale(load("p/spr/berry_trees/Wacan_tree_1.png"),(60,75))
    P.fio_berry3 = pygame.transform.scale(load("p/spr/berry_trees/Qualot_tree_1.png"),(60,75))
    P.fio_berry4 = pygame.transform.scale(load("p/spr/berry_trees/Chesto_tree_1.png"),(60,75))
    P.fio_tree1 = cut_tree(P,600,-550,5)
    P.fio_tree2 = cut_tree(P,2250,-400,6)
    P.fio_tree3 = cut_tree(P,2250,-350,7)
    if P.prog[12][0] == 5 or P.prog[12][1] == 5:
        P.fio_healer = npc.NPC(P,'Healer','Birb',[800,-400],[['ml',80],['l',100],['mr',80],['r',140]],["Those two boys seemed to have","settled down a little. Is that","your doing?","If so, you have my thanks!","I can finally get some nice","peace and quiet!"])
    else:
        P.fio_healer = npc.NPC(P,'Healer','Birb',[800,-400],[['ml',80],['l',100],['mr',80],['r',140]],["Those two boys won't stop","bickering about which Pokemon","is the coolest.","Someone needs to settle their","constant arguing. Someone like","a nice, capable trainer!"])
    P.fio_aroma = npc.NPC(P,'Aroma Lady','Birb',[2050,-400],[['u',300],['mr',40],['u',80],['ml',40],['l',260],['md',40],['r',100],['mu',40]],["These flowers smell amazing!","They even come in so many","beautiful colors!","I spend my free time taking","care of them, but I don't","really know what I'm doing."])
    set_location(P)
    gond = 0
    gy = 0
    if P.px == -425 and P.py > 275 and P.py <= 325:
        pcx = 50-(325 - P.py)
        pcy = 10-((325 - P.py)/5)
    else:
        pcx = 0
        pcy = 0
    fade = None
    move = True
    wx = 0
    wy = 0
    tim = 0
    listx = []
    listy = []
    # listx = [442,715,1088,1289,1565,1838,709,995,1283,1571,715,1565,1838,1838,1434,846,-60]
    # listy = [-1250,-1250,-1250,-1250,-1250,-1250,-1000,-1000,-1000,-1000,-1500,-1500,-1550,-1700,-1745,-1745,-1600]
    fiore_b(P,wx,wy,listx,listy,pcx,pcy,gy)
    fiore_p(P,P.px,P.py,False,gond,gy)
    fiore_f(P,P.px,P.py,listx,listy,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        fiore_b(P,wx,wy,listx,listy,pcx,pcy,gy)
        temppx = P.px
        temppy = P.py
        fiore_p(P,temppx,temppy,move,gond,gy)
        fiore_f(P, temppx, temppy, listx, listy, tim)
        if gond == 1:
            gond = 2
            fade_in(P)
        # show_location(P,loc_txt,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and gond == 0 and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -825 and P.py == 275 and face_l(P):
                        nxtl = gondolier(P)
                        if nxtl != "Fiore Town":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif next_to(P,P.fio_tree1.x,P.fio_tree1.y):
                        P.fio_tree1.cut()
                    elif next_to(P,P.fio_tree2.x,P.fio_tree2.y):
                        P.fio_tree2.cut()
                    elif next_to(P,P.fio_tree3.x,P.fio_tree3.y):
                        P.fio_tree3.cut()
                    elif next_to(P,950,-900) and P.prog[6][25] == 0:
                        txt(P,P.save_data.name + " found a", "Heart Scale!")
                        txt(P,P.save_data.name + " put the Heart Scale","in the Items pocket.")
                        add_item(P,"Heart Scale",1)
                        P.prog[6][25] = 1
                    elif next_to(P,2450,-350) and P.prog[6][26] == 0:
                        txt(P,P.save_data.name + " found a TM83","Infestation!")
                        txt(P,P.save_data.name + " put the TM83 in","the TMs pocket.")
                        add_item(P,"TM83 Infestation",1)
                        P.prog[6][26] = 1
                    elif P.fio_healer.talk():
                        fiore_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        fiore_p(P,P.px,P.py,False,gond,gy)
                        fiore_f(P,P.px,P.py,listx,listy,tim)
                        P.fio_healer.write()
                    elif next_to(P,950,-850) or next_to(P,700,-700) or next_to(P,700,-750) or next_to(P,700,-800) or next_to(P,700,-850) or next_to(P,750,-850) or next_to(P,800,-850) or next_to(P,850,-850) or next_to(P,900,-850):
                        if next_to(P,850,-850):
                            if P.prog[1] == 1:
                                bag_berry = None
                                for it in P.bag[1]:
                                    if it[0][-6:] == ' Berry':
                                        bag_berry = it[0]
                                        break
                                te = P.surface.copy()
                                if bag_berry == None:
                                    txt(P,"The Pinab Berry bush seems to","be rustling quite a bit.")
                                    txt(P,"You might need something to","bait it out.")
                                else:
                                    new_txt(P)
                                    write(P,"The Pinab Berry bush seems to","be rustling quite a bit.","Take out the "+bag_berry+"?")
                                    if choice(P):
                                        txt(P,"The bush jumped out and","attacked!")
                                        add_item(P,bag_berry,-1)
                                        P.song = "music/wild_battle.wav"
                                        pygame.mixer.music.load(P.song)
                                        set_mixer_volume(P,P.vol)
                                        pygame.mixer.music.play(0)
                                        battle(P,[poke.Poke('Pineapple_Oddish',[20,random.randint(0,1),334,'Needle Arm',-1,'Pin Missile',-1,'Nuzzle',-1,'Acid Armor',-1,None,None,0,"Poke Ball"])])
                                        P.prog[1] = 2
                                        play_music(P,"music/fiore.wav")
                                        P.surface.blit(te,(0,0))
                                        fade_in(P)
                                    else:
                                        txt(P,"You decide to leave it alone.")
                            elif P.prog[1] >= 2:
                                txt(P,"It's a soft patch of soil.")
                            else:
                                txt(P,"The Pinab Berry bush looks","nice and healthy!")
                        else:
                            if P.prog[1] == 3:
                                txt(P,"The Pinab Berry bush looks","nice and healthy!")
                            else:
                                txt(P,"The Pinab Berry bush doesn't","look like it's been getting","enough nutrients.")
                    elif P.fio_aroma.talk():
                        fiore_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        fiore_p(P,P.px,P.py,False,gond,gy)
                        fiore_f(P,P.px,P.py,listx,listy,tim)
                        P.fio_aroma.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            end = False
            fade = P.song
        if P.px == -525 and P.py > 1375 and P.py <= 1425:
            pcx = 50-(1425 - P.py)
            pcy = 10-((1425 - P.py)/5)
        else:
            pcx = 0
            pcy = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 675 or P.py == 625) and P.px == 275 and face_l(P):
            P.px = -2975
            P.py -= 900
            P.move_out_dir = 'l'
            fade = P.song
            P.loc = "scarab_l"
            end = False
        if P.px == -1925 and P.py in [875,925] and face_r(P):
            P.px = -275
            P.py -= 500
            P.move_out_dir = 'r'    
            fade = P.song
            P.loc = "scarab_r"
            end = False
        if P.px == 75 and P.py == 325 and face_u(P):
            P.loc = "house_1_9"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -1075 and P.py == 325 and face_u(P):
            P.loc = "house_1_10"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -1525 and P.py == 325 and face_u(P):
            P.loc = "house_1_11"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -525 and P.py == 725 and face_u(P):
            P.loc = "house_3_1"
            P.px = -25
            P.py = -75
            end = False
        if P.px == -1125 and P.py == 725 and face_u(P):
            P.loc = "fiore_garden"
            P.px = 125
            P.py = -75
            end = False
        if P.py == 325 and P.px == -425 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_fiore"
            fade = P.song
            end = False
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def scarab_l_b(P):
    P.surface.blit(P.sl_back,(P.px+50,P.py-1000))
    if P.prog[6][19] == 0:
        P.surface.blit(P.item_out,(P.px+2550,P.py+300))
    if P.prog[6][20] == 0:
        P.surface.blit(P.item_out,(P.px+1850,P.py+250))
    if P.prog[6][21] == 0:
        P.surface.blit(P.item_out,(P.px+3350,P.py-700))
        P.surface.blit(P.grass,(P.px+3350,P.py-710))

def scarab_l_p(P,temppx,temppy,move):
    #rects start
    if P.sl_hera1:
        P.sl_hera1.move()
        P.sl_hera2.move()
    if P.sl_rocket:
        rocket = P.sl_rocket.y_dist() > 0
        if rocket:
            P.sl_rocket.move()
    rich = P.sl_rich.y_dist() > 0
    psy = P.sl_psy.y_dist() > 0
    ace = P.sl_ace.y_dist() > 0
    if rich:
        P.sl_rich.move()
    if psy:
        P.sl_psy.move()
        draw_grass(P,P.sl_psy.x,P.sl_psy.y,-1775,875,350,450,[P.px,P.py])
    if ace:
        P.sl_ace.move()
    tree1 = P.sl_tree1.y_dist() > 0
    tree2 = P.sl_tree2.y_dist() > 0
    tree3 = P.sl_tree3.y_dist() > 0
    tree4 = P.sl_tree4.y_dist() > 0
    tree5 = P.sl_tree5.y_dist() > 0
    if tree1:
        P.sl_tree1.blit()
    if tree2:
        P.sl_tree2.blit()
    if tree3:
        P.sl_tree3.blit()
    if tree4:
        P.sl_tree4.blit()
    if tree5:
        P.sl_tree5.blit()
    r1 = (P.px+1550,P.py-650,900,40)
    r2 = (P.px+1500,P.py-600,50,90)
    r3 = (P.px+1450,P.py-500,50,90)
    r4 = (P.px+1500,P.py-400,50,90)
    r5 = (P.px+1550,P.py-300,300,190)
    r6 = (P.px+1250,P.py-150,300,40)
    r7 = (P.px+1200,P.py-100,50,890)
    r8 = (P.px+1450,P.py+100,400,590)
    r9 = (P.px+750,P.py+750,450,40)
    r10 = (P.px+750,P.py+850,1950,40)
    r100 = (P.px+700,P.py+700,50,40)
    r101 = (P.px+500,P.py+650,200,40)
    r102 = (P.px+450,P.py+700,50,40)
    r103 = (P.px+400,P.py+750,50,140)
    r104 = (P.px+450,P.py+900,50,40)
    r105 = (P.px+500,P.py+950,200,40)
    r106 = (P.px+700,P.py+900,50,40)
    r11 = (P.px+2150,P.py-150,50,890)
    r12 = (P.px+2200,P.py+700,350,40)
    r13 = (P.px+2550,P.py+450,50,290)
    r14 = (P.px+2700,P.py+450,50,390)
    r15 = (P.px+2500,P.py+250,50,190)
    r16 = (P.px+2750,P.py+250,50,190)
    r17 = (P.px+2550,P.py+200,200,40)
    r18 = (P.px+2600,P.py+300,100,40)
    r19 = (P.px+2550,P.py+350,50,40)
    r20 = (P.px+1350,P.py+100,50,40)
    r21 = (P.px+1850,P.py+200,50,40)
    r22 = r1
    if P.py == -175:
        r22 = (P.px+1850,P.py+500,300,40)
    r23 = (P.px+2200,P.py-150,950,40)
    r24 = (P.px+2000,P.py-750,450,40)
    r25 = (P.px+1950,P.py-700,50,40)
    r26 = (P.px+2450,P.py-800,100,40)
    r27 = (P.px+2550,P.py-750,850,40)
    r28 = (P.px+2500,P.py-650,500,40)
    r29 = (P.px+2500,P.py-600,50,290)
    r30 = (P.px+2500,P.py-300,750,40)
    r31 = (P.px+2950,P.py-250,50,40)
    r32 = (P.px+2950,P.py-600,50,140)
    r33 = (P.px+3000,P.py-450,250,40)
    r34 = (P.px+3200,P.py-400,50,90)
    r35 = (P.px+3400,P.py-700,50,240)
    r36 = (P.px+3350,P.py-450,50,940)
    r37 = (P.px+3100,P.py-100,50,440)
    r38 = (P.px+2950,P.py+300,150,40)
    r39 = (P.px+2900,P.py+350,50,40)
    r40 = (P.px+2950,P.py+400,150,40)
    r41 = (P.px+3200,P.py+300,50,40)
    r42 = (P.px+3100,P.py+400,50,240)
    r43 = (P.px+3150,P.py+650,200,40)
    r44 = (P.px+3350,P.py+600,50,40)
    r45 = (P.px+3400,P.py+500,50,90)
    r46 = P.sl_tree1.get_rect()
    r47 = P.sl_tree2.get_rect()
    r48 = P.sl_tree3.get_rect()
    r49 = P.sl_tree4.get_rect()
    r50 = P.sl_tree5.get_rect()
    r51,r52,r53,r54,r55 = r1,r1,r1,r1,r1
    if P.prog[6][19] == 0:
        r51 = (P.px+2550,P.py+300,50,40)
    if P.prog[6][20] == 0:
        r52 = (P.px+1850,P.py+250,50,40)
    if P.prog[6][21] == 0:
        r53 = (P.px+3350,P.py-700,50,40)
    if P.prog[6][22] == 0:
        r54 = (P.px+2950,P.py+350,50,40)
    if P.prog[6][23] == 0:
        r55 = (P.px+3000,P.py+350,50,40)
    r56 = r1
    if P.sl_rocket:
        r56 = P.sl_rocket.get_rect()
    r57 = P.sl_ace.get_rect()
    r58 = P.sl_rich.get_rect()
    r59 = P.sl_psy.get_rect()
    r60 = r1
    if P.prog[15][4] == 0:
        r60 = (P.px+900,P.py+800,50,40)
    rects = [r106,r105,r104,r103,r102,r101,r100,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.px == -575 and P.py == -525 and face_l(P) and P.prog[15][4] == 0:
            player_move(P,rects,manual_input = 'r')
        else:
            player_move(P,rects)
    else:
        if P.prog[15][4] == 1 and P.px < -325:
            player_move(P,rects,manual_input = 'l',spd = 3)
        else:
            blit_player(P)
    draw_grass(P,temppx,temppy,-2775,425,200,800,ignore = [(-2775,425),(-2825,425),(-2875,425),(-2925,225),(-2925,175),(-2775,125),(-2925,75),(-2825,75),(-2825,25),(-2775,-275),(-2775,-325),(-2825,-325)])
    draw_grass(P,temppx,temppy,-2625,975,400,250)
    draw_grass(P,temppx,temppy,-2125,525,400,100)
    draw_grass(P,temppx,temppy,-1475,175,300,350,ignore = [(-1475,-25),(-1475,25),(-1525,-25),(-1725,-25),(-1725,-75)])
    draw_grass(P,temppx,temppy,-2225,-175,100,400,ignore = [(-2275,-175),(-2225,-225),(-2225,-275),(-2225,-325),(-2275,-325),(-2275,-375)])
    draw_grass(P,temppx,temppy,-1775,-475,450,100,ignore = [(-1925,-525),(-1975,-525),(-1975,-475),(-2025,-475)])
    draw_grass(P,temppx,temppy,-1475,-225,300,350,ignore = [(-1475,-525),(-1525,-525),(-1575,-525)])
    draw_grass(P,temppx,temppy,-1075,-425,200,150,ignore = [(-1075,-525),(-1225,-425),(-1175,-425),(-1125,-425),(-1225,-475)])
    draw_grass(P,temppx,temppy,-875,375,200,950,ignore = [(-875,375),(-875,325),(-925,275),(-1025,275),(-925,225),(-925,25),(-925,-25),(-875,-125),(-925,-125),(-925,-175),(-925,-225),(-1025,-325),(-1025,-375),(-925,-375),(-925,-425),(-875,-425),(-1025,-525)])
    draw_grass(P,temppx,temppy,-1075,375,100,100,ignore = [(-1125,325)])
    draw_grass(P,temppx,temppy,-1775,875,350,450)
    draw_grass(P,temppx,temppy,-1175,675,300,100)
    draw_grass(P,temppx,temppy,-1175,875,300,100)
    if not tree1:
        P.sl_tree1.blit(temppx,temppy)
    if not tree2:
        P.sl_tree2.blit(temppx,temppy)
    if not tree3:
        P.sl_tree3.blit(temppx,temppy)
    if not tree4:
        P.sl_tree4.blit(temppx,temppy)
    if not tree5:
        P.sl_tree5.blit(temppx,temppy)
    if P.sl_rocket:
        if not rocket:
            P.sl_rocket.move(temppx,temppy)
    if not rich:
        P.sl_rich.move(temppx,temppy)
    if not psy:
        P.sl_psy.move(temppx,temppy)
        draw_grass(P,P.sl_psy.x,P.sl_psy.y,-1775,875,350,450,[temppx,temppy])
    if not ace:
        P.sl_ace.move(temppx,temppy)

def scarab_l_f(P,temppx,temppy,tim):
    P.surface.blit(P.sl_f,(temppx+300,temppy-757))
    if item_in_bag(P,"Felling Axe") == 0:
        P.surface.blit(P.sl_axe,((temppx+2600,temppy+250)))
    set_sky(P)
    show_location(P, P.loc_txt, tim)

def scarab_l(P) -> None:
    if P.song != "music/scarab_woods.wav":
        P.song = "music/scarab_woods.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] == 80:
        P.prog[0] += 1
    P.habitat = 'forest'
    P.sl_back = load("p/fiore/Scarab_Woods_l.png")
    P.sl_f = load("p/fiore/Scarab_lf.png")
    P.sl_axe = load("p/fiore/scarab_axe.png")
    P.sl_tree1 = cut_tree(P,2450,-700,0)
    P.sl_tree2 = cut_tree(P,1000,800,1)
    P.sl_tree3 = cut_tree(P,2650,250,2)
    P.sl_tree4 = cut_tree(P,2900,-250,3)
    P.sl_tree5 = cut_tree(P,2900,-200,4)
    if P.prog[15][4] == 0:
        P.sl_hera1 = npc.NPC(P,'Heracross','Grunt',[600,800],[['l',20]],["","",""])
        P.sl_hera2 = npc.NPC(P,'Heracross','Grunt',[550,800],[['r',20]],["","",""])
    else:
        P.sl_hera1 = None
        P.sl_hera2 = None
    if P.prog[0] == 48:
        P.sl_rocket = npc.NPC(P,'Team Rocketf','Grunt',[2800,-250],[['r',20]],["Why is it that every path I","try is blocked off? I'm gonna","be late for the meeting!"])
    else:
        P.sl_rocket = None
    move = True
    wx = 0
    wy = 0
    tim = 0
    set_location(P)
    scarab_l_b(P)
    scarab_l_p(P,P.px,P.py,False)
    scarab_l_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        scarab_l_b(P)
        if move == True and P.sl_ace.trainer_check():
            move = False
        if move == True and P.sl_rich.trainer_check():
            move = False
        if move == True and P.sl_psy.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        P.ledge = 0
        if (P.px <= -1475 and P.px >= -1725):
            if P.py > -225 and P.py < -200:
                P.ledge = (-225-P.py)/2
            elif P.py >= -200 and P.py < -175:
                P.ledge = -(-175-P.py)/2
        scarab_l_p(P,temppx,temppy,move)
        scarab_l_f(P,temppx,temppy,tim)
        if P.px == -575 and P.py == -525 and face_l(P):
            if P.prog[15][0] == 0:
                txt(P,"You see two Heracross fighting","each other.")
                print_mega_area(P)
            elif P.prog[15][4] == 0:
                txt(P,"You see two Heracross fighting","each other.")
                if in_party(P,'Heracross',True):
                    new_txt(P)
                    write(P,"Enter the clearing?")
                    if choice(P):
                        move = False
                        P.prog[15][4] += 1
                        P.sl_hera1 = npc.NPC(P,'Heracross','Grunt',[600,800],[['l',220],['r',60],['mr',20],['r',500]],["","",""])
                        P.sl_hera2 = npc.NPC(P,'Heracross','Grunt',[550,800],[['r',160],['ml',20],['r',500]],["","",""])
                else:
                    txt(P,"You should bring a Heracross","if you want to enter the","clearing.")
        if P.prog[15][4] == 1 and P.sl_hera1.x == 650:
            te = P.surface.copy()
            txt(P,"The Heracross charged straight","at you!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.tourney_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Heracross' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Heracross',[35,1,334,'Leer',-1,'Take Down',-1,'Aerial Ace',-1,'Counter',-1,None,None,0,"Poke Ball",200,'Swarm'])],no_pc = True)
            play_music(P,"music/scarab_woods.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][4] = 0
                txt(P,"The Heracros drove you out of","the clearing!")
                fade_out(P)
                P.p = P.r1
                P.px = -675
                P.py = -525
                P.sl_hera1 = npc.NPC(P,'Heracross','Grunt',[600,800],[['l',20]],["","",""])
                P.sl_hera2 = npc.NPC(P,'Heracross','Grunt',[550,800],[['r',20]],["","",""])
                scarab_l_b(P)
                scarab_l_p(P,P.px,P.py,False)
                scarab_l_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][4] += 1
                txt(P,"The Heracross bowed slightly","before leaving. It left you","with a mysterious stone.")
                add_item(P,'Heracronite',1)
                fade_out(P)
                P.sl_hera1 = None
                P.sl_hera2 = None
                scarab_l_b(P)
                scarab_l_p(P,P.px,P.py,False)
                scarab_l_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
            P.tourney_battle = False
        if P.px == -2525 and P.py == 525 and face_d(P) and P.prog[10][4][0] == -1 and P.prog[0] == 48:
            P.sl_rocket = npc.NPC(P,'Team Rocketf','Grunt',[2800,-250],[['mr',20],['r',20]],["","",""])
            move = False
            P.p = P.l1
            P.prog[0] += 1
        if P.prog[0] == 49 and P.sl_rocket.x == 2850:
            txt(P,"Wow did you just chop down","those trees? I can finally get","to the meeting spot!")
            txt(P,"Thanks a million! Good luck","chugging through the forest!","")
            P.sl_rocket = npc.NPC(P,'Team Rocketf','Grunt',[2850,-250],[['md',10],['mr',70],['md',120]],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 50 and P.sl_rocket.y == 100:
            P.sl_rocket = None
            move = True
            P.prog[0] += 1
        if trainer_check(P,P.sl_ace,"music/scarab_woods.wav"):
            P.sl_ace = npc.NPC(P,'Ace Trainerf','Jesse',[P.sl_ace.x,P.sl_ace.y],[['l',100]],["I won't give up! I'll just","keep training until I can beat","even you in a battle!"])
            move = True
        if trainer_check(P,P.sl_psy,"music/scarab_woods.wav"):
            P.sl_psy = npc.NPC(P,'Psychic','Hugo',[P.sl_psy.x,P.sl_psy.y],[['mr',60],['r',200],['md',60],['d',140],['ml',60],['l',260],['mu',60],['u',160]],["I haven't given up! Soon I'll","be able to predict everything", "a trainer could possibly do!","Then I'll be able to take on","anyone that strolls through","here!"],tim = P.sl_psy.tim,curr = P.sl_psy.curr,extra_walk = P.sl_psy.extra_walk)
            move = True
        if trainer_check(P,P.sl_rich,"music/scarab_woods.wav"):
            P.sl_rich = npc.NPC(P,'Rich Boy','Leonard',[P.sl_rich.x,P.sl_rich.y],[[P.sl_rich.face(),60]],["Why did I even bother stepping","inside here? It's just been ","disasters one after another!","I followed the directions that","stupid girl gave me, and just", "look at the result!"])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if next_to(P,2600,300) or next_to(P,2650,300):
                        if item_in_bag(P,"Felling Axe") == 0:
                            txt(P,P.save_data.name + " found a", "Felling Axe!")
                            txt(P,P.save_data.name + " put the Felling Axe","in the Key Items pocket.")
                            add_item(P,"Felling Axe",1)
                        else:
                            txt(P,"Whoever managed to cut down","this tree must've been really","strong.")
                    elif P.sl_rocket and P.sl_rocket.talk():
                        # if P.r3_bug.trainer:
                        #     move = False
                        # else:
                        scarab_l_b(P)
                        scarab_l_p(P,P.px,P.py,False)
                        scarab_l_f(P,P.px,P.py,tim)
                        P.sl_rocket.write()
                    elif P.sl_psy.talk():
                        if P.sl_psy.trainer:
                            move = False
                        else:
                            scarab_l_b(P)
                            scarab_l_p(P,P.px,P.py,False)
                            scarab_l_f(P,P.px,P.py,tim)
                            P.sl_psy.write()
                    elif P.sl_rich.talk():
                        if P.sl_rich.trainer:
                            move = False
                        else:
                            scarab_l_b(P)
                            scarab_l_p(P,P.px,P.py,False)
                            scarab_l_f(P,P.px,P.py,tim)
                            P.sl_rich.write()
                    elif P.sl_ace.talk():
                        if P.sl_ace.trainer:
                            move = False
                        else:
                            scarab_l_b(P)
                            scarab_l_p(P,P.px,P.py,False)
                            scarab_l_f(P,P.px,P.py,tim)
                            P.sl_ace.write()
                    elif next_to(P,2550,300) and P.prog[6][19] == 0:
                        item_fight(P,"music/scarab_woods.wav",19,17,('Mega Drain','Growth','Astonish','Bide'),'Foongus')
                    elif next_to(P,1850,250) and P.prog[6][20] == 0:
                        txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                        txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                        add_item(P,"Tiny Mushroom",1)
                        P.prog[6][20] = 1
                    elif next_to(P,3350,-700) and P.prog[6][21] == 0:
                        item_fight(P,"music/scarab_woods.wav",21,18,('Mega Drain','Growth','Ingrain','Bide'),'Foongus')
                    elif next_to(P,3000,350) and P.prog[6][23] == 0:
                        item_fight(P,"music/scarab_woods.wav",23,19,('Mega Drain','Growth','Ingrain','Bide'),'Foongus')
                    elif next_to(P,2950,350) and P.prog[6][22] == 0:
                        txt(P,P.save_data.name + " found a", "Big Mushroom!")
                        txt(P,P.save_data.name + " put the Big","Mushroom in the Items pocket.")
                        add_item(P,"Big Mushroom",1)
                        P.prog[6][22] = 1
                    elif next_to(P,P.sl_tree1.x,P.sl_tree1.y):
                        P.sl_tree1.cut()
                    elif next_to(P,P.sl_tree2.x,P.sl_tree2.y):
                        P.sl_tree2.cut()
                    elif next_to(P,P.sl_tree3.x,P.sl_tree3.y):
                        P.sl_tree3.cut()
                    elif next_to(P,P.sl_tree4.x,P.sl_tree4.y):
                        P.sl_tree4.cut()
                    elif next_to(P,P.sl_tree5.x,P.sl_tree5.y):
                        P.sl_tree5.cut()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == -1125 and P.py >= 725 and P.py <= 775 and face_l(P):
            P.px = -1975
            P.py -= 650
            P.loc = "route_3"
            P.move_out_dir = 'l'
            end = False
        if P.px == -1625 and P.py == 975 and face_l(P):
            P.px = -2375
            P.py = 325
            P.move_out_dir = 'l'
            P.loc = "route_3"
            end = False
        if P.px == -2975 and P.py <= -225 and P.py >= -275 and face_r(P):
            P.px = 275
            P.py += 900
            P.move_out_dir = 'r'
            P.loc = "fiore"
            end = False
        if move and (wild_grass(P,-2775,425,200,800,ignore = [(-2775,425),(-2825,425),(-2875,425),(-2925,225),(-2925,175),(-2775,125),(-2925,75),(-2825,75),(-2825,25),(-2775,-275),(-2775,-325),(-2825,-325)]) or wild_grass(P,-2625,975,400,250) or wild_grass(P,-2125,525,400,100) or wild_grass(P,-1475,175,300,350,ignore = [(-1475,-25),(-1475,25),(-1525,-25),(-1725,-25),(-1725,-75)]) or wild_grass(P,-2225,-175,100,400,ignore = [(-2275,-175),(-2225,-225),(-2225,-275),(-2225,-325),(-2275,-325),(-2275,-375)]) or wild_grass(P,-1775,-475,450,100,ignore = [(-1925,-525),(-1975,-525),(-1975,-475),(-2025,-475)]) or wild_grass(P,-1475,-225,300,350,ignore = [(-1475,-525),(-1525,-525),(-1575,-525)]) or wild_grass(P,-1375,-425,100,50) or wild_grass(P,-1075,-425,200,150,ignore =  [(-1075,-525),(-1225,-425),(-1175,-425),(-1125,-425),(-1225,-475)]) or wild_grass(P,-875,375,200,950,ignore = [(-875,375),(-875,325),(-925,275),(-1025,275),(-925,225),(-925,25),(-925,-25),(-875,-125),(-925,-125),(-925,-175),(-925,-225),(-1025,-325),(-1025,-375),(-925,-375),(-925,-425),(-875,-425),(-1025,-525)]) or wild_grass(P,-1075,375,100,100,ignore = [(-1125,325)]) or wild_grass(P,-1775,875,350,450) or wild_grass(P,-1175,675,300,100) or wild_grass(P,-1175,875,300,100)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.2:
                r = random.randint(13,16)
                if r < 16:
                    battle(P,[poke.Poke('Metapod',[r,random.randint(0,1),334,"Tackle",-1,"String Shot",-1,"Harden",-1,"Bug Bite",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Butterfree',[r,random.randint(0,1),334,"Confusion",-1,"Gust",-1,"Poison Powder",-1,"Sleep Powder",-1,None,None,0,"Poke Ball"])])
            elif rando >= .2 and rando < .3:
                r = random.randint(14,16)
                if r < 16:
                    battle(P,[poke.Poke('Karrablast',[r,random.randint(0,1),334,"Leer",-1,"Fury Cutter",-1,"Endure",-1,"Peck",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Karrablast',[r,random.randint(0,1),334,"Fury Attack",-1,"Fury Cutter",-1,"Endure",-1,"Peck",-1,None,None,0,"Poke Ball"])])
            elif rando >= .3 and rando < .5:
                r = random.randint(14,16)
                if r < 15:
                    battle(P,[poke.Poke('Bellsprout',[r,random.randint(0,1),334,"Vine Whip",-1,"Growth",-1,"Wrap",-1,"Sleep Powder",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Bellsprout',[r,random.randint(0,1),334,"Vine Whip",-1,"Sleep Powder",-1,"Wrap",-1,"Poison Powder",-1,None,None,0,"Poke Ball"])])
            elif rando >= .5 and rando < .6:
                battle(P,[poke.Poke('Zangoose',[random.randint(15,17),random.randint(0,1),334,"Hone Claws",-1,"Quick Attack",-1,"Fury Cutter",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
            elif rando >= .6 and rando < .8:
                r = random.randint(13,16)
                if r < 15:
                    battle(P,[poke.Poke('Seedot',[r,random.randint(0,1),334,"Bide",-1,"Harden",-1,"Growth",-1,None,None,None,None,0,"Poke Ball"])])
                elif r < 16:
                    battle(P,[poke.Poke('Seedot',[r,random.randint(0,1),334,"Bide",-1,"Harden",-1,"Growth",-1,"Nature Power",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Nuzleaf',[r,random.randint(0,1),334,"Bide",-1,"Growth",-1,"Nature Power",-1,"Razor Leaf",-1,None,None,0,"Poke Ball"])])
            else:
                if get_time() > 19 or get_time() < 6:
                    r = random.randint(14,16)
                    if r < 15:
                        battle(P,[poke.Poke('Murkrow',[r,random.randint(0,1),334,"Peck",-1,"Astonish",-1,"Haze",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Murkrow',[r,random.randint(0,1),334,"Wing Attack",-1,"Astonish",-1,"Haze",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
                else:
                    r = random.randint(14,16)
                    if r < 16:
                        battle(P,[poke.Poke('Hoothoot',[r,random.randint(0,1),334,"Hypnosis",-1,"Peck",-1,"Confusion",-1,"Echoed Voice",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Hoothoot',[r,random.randint(0,1),334,"Hypnosis",-1,"Peck",-1,"Zen Headbutt",-1,"Echoed Voice",-1,None,None,0,"Poke Ball"])])
            P.song = "music/scarab_woods.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def route_3_b(P,wx,wy,beachx,beachy,beach_poke):
    draw_waves(P,wx,wy)
    P.surface.blit(P.r3_back,(P.px+450,P.py-1200))
    if type(beach_poke) == list:
        P.surface.blit(P.r3_poke_shad,(P.px+beachx[beach_poke[0]],P.py+beachy[beach_poke[0]]+abs(P.foam)))
    P.surface.blit(P.r3_slow,(P.px + 4295,P.py - 1070))
    P.surface.blit(P.r3_foam,(P.px+50,P.py-110+abs(P.foam)))
    P.surface.blit(P.r3_beach,(P.px+4201,P.py-1104+abs(P.foam)))
    P.surface.blit(P.r3_grass,(P.px+706,P.py+267))
    P.surface.blit(P.r3_grass2,(P.px+741,P.py-99))
    P.surface.blit(P.r3_grass3,(P.px+2413,P.py+522))
    if P.prog[0] <= 74:
        P.surface.blit(P.traffic_cone,(P.px+2150,P.py-310))
        P.surface.blit(P.traffic_cone,(P.px+5550,P.py-60))
        P.surface.blit(P.traffic_cone,(P.px+5650,P.py-60))
    if P.py <= 625:
        P.surface.blit(P.r3_fence,(P.px+4397,P.py-374))
    if P.prog[6][13] == 0:
        P.surface.blit(P.item_out,(P.px+1250,P.py-100))
        P.surface.blit(P.grass,(P.px+1250,P.py-110))
    if P.prog[6][35] == 0:
        P.surface.blit(P.item_out,(P.px+4950,P.py+150))
        P.surface.blit(P.grass,(P.px+4950,P.py+140))

def route_3_p(P,temppx,temppy,move):
    #rects start
    if P.r3_noland:
        P.r3_noland.move()
    if P.r3_worker:
        worker = P.r3_worker.y_dist() > 0
        if worker:
            P.r3_worker.move()
    if P.r3_worker2:
        worker2 = P.r3_worker2.y_dist() > 0
        if worker2:
            P.r3_worker2.move()
    if P.r3_cheryl:
        P.r3_cheryl.move()
        P.r3_rival.move()
    hex = P.r3_hex.y_dist() > 0
    if hex:
        P.r3_hex.move()
    if P.r3_fish1:
        fish1 = P.r3_fish1.y_dist() > 0
        if fish1:
            P.r3_fish1.move()
        fish2 = P.r3_fish2.y_dist() > 0
        if fish2:
            P.r3_fish2.move()
        tri2 = P.r3_tri2.y_dist() > 0
        if tri2:
            P.r3_tri2.move()
        beauty = P.r3_beauty.y_dist() > 0
        if beauty:
            P.r3_beauty.move()
        tri = P.r3_tri.y_dist() > 0
        if tri:
            P.r3_tri.move()
        todd = P.r3_todd.y_dist() > 0
        if todd:
            P.r3_todd.move()
        lass = P.r3_lass.y_dist() > 0
        if lass:
            P.r3_lass.move()
    bug = P.r3_bug.y_dist() > 0
    hika = P.r3_hika.y_dist() > 0
    sci = P.r3_sci.y_dist() > 0
    battle = P.r3_battle.y_dist() > 0
    if P.r3_lop:
        P.r3_lop.move()
    if bug:
        P.r3_bug.move()
        draw_grass(P,P.r3_bug.x,P.r3_bug.y,-1625,225,350,350,[P.px,P.py],ignore = [(-1625,25),(-1625,-25),(-1625,-75),(-1675,-75),(-1925,175),(-1925,125),(-1875,125),(-1875,75),(-1925,75),(-1925,25)])
    if hika:
        P.r3_hika.move()
        draw_grass(P,P.r3_hika.x,P.r3_hika.y,-875,375,600,400,[P.px,P.py])
    if sci:
        P.r3_sci.move()
        draw_grass(P,P.r3_sci.x,P.r3_sci.y,-875,375,600,400,[P.px,P.py])
    if battle:
        P.r3_battle.move()
        draw_grass(P,P.r3_battle.x,P.r3_battle.y,-5325,175,500,200,[P.px,P.py])
    r1 = (P.px+900,P.py+450,1100,50)
    r2 = (P.px+850,P.py-150,50,590)
    r3 = (P.px+900,P.py-200,150,40)
    r4 = (P.px+1050,P.py-150,200,440)
    r5 = (P.px+1450,P.py+50,200,90)
    r6 = (P.px+1250,P.py-150,600,40)
    r7 = (P.px+2000,P.py+400,350,40)
    r8 = (P.px+1800,P.py-300,50,140)
    r9 = (P.px+1850,P.py-350,310,40)
    r90,r91,r92,r93, = r1,r1,r1,r1
    if P.px == -1825 and P.py == 600:
        r90 = (P.px+2200,P.py-350,50,15)
    if P.px == -1825 and P.py == 500:
        r91 = (P.px+2200,P.py-175,50,50)
    if P.px == -4725 and P.py == 600:
        r92 = (P.px+5100,P.py-350,50,15)
    if P.px == -4725 and P.py == 500:
        r93 = (P.px+5100,P.py-175,50,50)
    r10 = (P.px+2000,P.py-150,450,190)
    r11 = (P.px+2350,P.py+50,50,90)
    r12 = (P.px+2400,P.py+150,50,90)
    r13 = (P.px+2350,P.py+250,50,140)
    r14,r15 = r1,r1
    if P.r3_worker:
        r14 = (P.px+2150,P.py-300,50,40)
        r15 = (P.px+2150,P.py-200,50,40)
    r16 = r1
    if P.r3_worker:
        r16 = P.r3_worker.get_rect()
    r17 = P.r3_bug.get_rect()
    r18 = P.r3_hika.get_rect()
    r19 = P.r3_sci.get_rect()
    r20 = r1
    if P.prog[6][13] == 0:
        r20 = (P.px+1250,P.py-100,50,40)
    r21 = (P.px+2450,P.py-100,450,40)
    r22 = (P.px+2450,P.py,450,40)
    r23 = r1
    if P.prog[6][14] == 0:
        r23 = (P.px+2450,P.py-50,50,40)
    r24 = (P.px+2800,P.py-50,50,40)
    r25 = (P.px+2250,P.py-400,950,40)
    r26 = (P.px+2290,P.py-200,2770,40)
    r27 = (P.px+3300,P.py-400,950,40)
    r28 = (P.px+3300,P.py-500,50,90)
    r29 = (P.px+3150,P.py-500,50,90)
    r30 = (P.px+3350,P.py-700,50,190)
    r31 = (P.px+3100,P.py-700,50,190)
    r32 = (P.px+3150,P.py-750,200,40)
    r33 = (P.px+3200,P.py-650,100,90)
    r34 = (P.px+4200,P.py-800,50,390)
    r35 = (P.px+4250,P.py-850,150,40)
    r36 = (P.px+4400,P.py-800,50,440)
    if P.px <= -4025:
        r36 = (P.px+4350,P.py-800,50,440)
    r37 = (P.px+4400,P.py-400,750,40)
    if P.py >= 675 or P.px <= -4775:
        r37 = (P.px+4400,P.py-350,750,40)
    r38 = (P.px+4450,P.py-450,50,40)
    r39 = (P.px+4600,P.py-500,50,40)
    r40 = (P.px+5500,P.py-400,50,40)
    r41 = (P.px+5750,P.py-450,50,40)
    r42 = (P.px+5150,P.py-150,400,40)
    r43 = (P.px+5500,P.py-100,50,240)
    r44 = (P.px+4950,P.py+100,600,40)
    r45 = (P.px+4900,P.py+150,50,290)
    r46 = (P.px+4950,P.py+450,200,40)
    r47 = (P.px+5150,P.py+500,100,40)
    r48 = (P.px+5250,P.py+450,1000,40)
    r49 = (P.px+5700,P.py-300,50,390)
    r50 = (P.px+5750,P.py+50,150,40)
    r500 = (P.px+5800,P.py,50,40)
    r501 = (P.px+5750,P.py-200,50,190)
    r502 = (P.px+5800,P.py-250,50,40)
    r503 = (P.px+5850,P.py-300,150,40)
    r504 = (P.px+6000,P.py-250,50,40)
    r505 = (P.px+6050,P.py-200,50,190)
    r506 = (P.px+6000,P.py,50,40)
    r51 = (P.px+5950,P.py+50,250,40)
    r52 = (P.px+6200,P.py+100,50,190)
    r53 = (P.px+5750,P.py-300,100,40)
    r54 = (P.px+5850,P.py-400,50,90)
    r55 = (P.px+5900,P.py-500,50,90)
    r56 = (P.px+5850,P.py-550,50,40)
    r57 = (P.px+5750,P.py-600,100,40)
    r58 = (P.px+4850,P.py-650,900,40)
    r59 = (P.px+4550,P.py-700,300,40)
    r60 = (P.px+4400,P.py-650,150,40)
    r61,r62,r63 = r1,r1,r1
    if P.r3_worker2:
        r61 = P.r3_worker2.get_rect()
        r62 = (P.px+5550,P.py-50,50,40)
        r63 = (P.px+5650,P.py-50,50,40)
    r64 = P.r3_battle.get_rect()
    r65,r66,r67,r68 = r1,r1,r1,r1
    if P.prog[6][35] == 0:
        r65 = (P.px+4950,P.py+150,50,40)
    if P.r3_cheryl:
        r66 = (P.px+5190,P.py-300,10,40)
        if P.px == -4725 and P.py == 600:
            r66 = (P.px+5150,P.py-300,50,40)
        r67 = P.r3_rival.get_rect()
        r68 = (P.px+4250,P.py-400,150,40)
    r69,r70,r72,r73,r74,r75,r76 = r1,r1,r1,r1,r1,r1,r1
    if P.r3_fish1:
        r69 = P.r3_fish1.get_rect()
        r70 = P.r3_fish2.get_rect()
        r72 = P.r3_beauty.get_rect()
        r73 = P.r3_tri.get_rect()
        r74 = P.r3_todd.get_rect()
        r75 = P.r3_lass.get_rect()
        r76 = P.r3_tri2.get_rect()
    r71 = P.r3_hex.get_rect()
    rects = [r506,r505,r504,r503,r502,r501,r500,r76,r75,r74,r73,r72,r71,r70,r69,r68,r67,r66,r65,r64,r63,r62,r61,r60,r59,r58,r57,r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r93,r92,r91,r90,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.prog[0] == 74 and P.px == -4825 and P.py == 475:
            player_move(P,rects,manual_input = 'l')
        elif P.prog[0] == 74 and P.px == -3725:
            player_move(P,rects,manual_input = 'r')
        elif P.px >= -1800:
            player_move(P,rects,[Rect(P.px+2200,P.py-350,50,200)])
        elif P.px >= -4750:
            player_move(P,rects,[Rect(P.px+2200,P.py-350,50,190)],[Rect(P.px+5100,P.py-350,50,190)])
        else:
            if P.px == -5525 and P.py == 225 and face_u(P) and P.prog[15][6] == 0:
                player_move(P,rects,manual_input = 'd')
            else:
                player_move(P,rects,[],[Rect(P.px+5100,P.py-350,50,200)])
        # player_move(P,rects)
    else:
        if P.prog[0] == 72:
            if P.py < 525 and P.r3_cheryl.x < 5600:
                player_move(P,rects,manual_input = 'u',spd = 3)
            elif P.px < -4775 and P.r3_cheryl.x < 5600:
                player_move(P,rects,manual_input = 'l',spd = 3)
            else:
                if P.r3_rival.x == 5200:
                    P.prog[0] += 1
                blit_player(P)
        else:
            if P.prog[15][6] == 1 and P.py < 425:
                player_move(P,rects,manual_input = 'u',spd = 3)
            else:
                blit_player(P)
    draw_grass(P,temppx,temppy,-875,375,600,400)
    draw_grass(P,temppx,temppy,-1625,225,350,350,ignore = [(-1625,25),(-1625,-25),(-1625,-75),(-1675,-75),(-1925,175),(-1925,125),(-1875,125),(-1875,75),(-1925,75),(-1925,25)])
    draw_grass(P,temppx,temppy,-5325,175,500,200)
    draw_grass(P,temppx,temppy,-4575,125,600,150)
    draw_grass(P,temppx,temppy,-4575,-25,450,100,ignore = [(-4975,-75)])
    if P.r3_worker:
        if not worker:
            P.r3_worker.move(temppx,temppy)
    if P.r3_worker2:
        if not worker2:
            P.r3_worker2.move(temppx,temppy)
    if P.r3_fish1:
        if not fish1:
            P.r3_fish1.move(temppx,temppy)
        if not fish2:
            P.r3_fish2.move(temppx,temppy)
        if not beauty:
            P.r3_beauty.move(temppx,temppy)
        if not tri:
            P.r3_tri.move(temppx,temppy)
        if not todd:
            P.r3_todd.move(temppx,temppy)
        if not lass:
            P.r3_lass.move(temppx,temppy)
        if not tri2:
            P.r3_tri2.move(temppx,temppy)
    if not hex:
        P.r3_hex.move(temppx,temppy)
    if not bug:
        P.r3_bug.move(temppx,temppy)
        draw_grass(P,P.r3_bug.x,P.r3_bug.y,-1625,225,350,350,[temppx,temppy],ignore = [(-1625,25),(-1625,-25),(-1625,-75),(-1675,-75),(-1925,175),(-1925,125),(-1875,125),(-1875,75),(-1925,75),(-1925,25)])
    if not hika:
        P.r3_hika.move(temppx,temppy)
        draw_grass(P,P.r3_hika.x,P.r3_hika.y,-875,375,600,400,[temppx,temppy])
    if not sci:
        P.r3_sci.move(temppx,temppy)
        draw_grass(P,P.r3_sci.x,P.r3_sci.y,-875,375,600,400,[temppx,temppy])
    if not battle:
        P.r3_battle.move(temppx,temppy)
        draw_grass(P,P.r3_battle.x,P.r3_battle.y,-5325,175,500,200,[temppx,temppy])

def route_3_f(P,temppx,temppy,rain,tim,thunder = 0):
    if P.prog[0] <= 74:
        P.surface.blit(P.traffic_cone,(temppx+2150,temppy-210))
    P.surface.blit(P.r3_f,(temppx+750,temppy-852))
    if P.py > 625:
        P.surface.blit(P.r3_fence,(temppx+4397,temppy-374))
    sky = True
    if P.prog[0] >= 70 and P.prog[0] <= 75 and P.px >= -5000:
        if pygame.mixer.Channel(0).get_busy() == False:
            set_channel_volume(P,P.sfx_vol*2,0)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/sfx/rain.wav'),loops = -1)
        if (random.random() < 0.03 and P.px >= -4300 and thunder == 0) or P.prog[0] == 75:
            sky = False
            thunder = 150
            set_channel_volume(P,P.sfx_vol,1)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('music/sfx/thunderclap.wav'))
        elif thunder >= 148:
            sky = False
        tmod = rain%100
        tmod = abs(tmod-50)/5
        if sky:
            P.surface.blit(P.r3_shad,(temppx+4250,temppy-500-tmod))
        else:
            P.surface.blit(P.r3_thun,(temppx+4250,temppy-500-tmod))
        P.surface.blit(P.r3_cloud,(temppx+3600,temppy-750))
        blit_rain(P,rain)
    if sky:
        draw_lamps(P, temppx, temppy, [6438], [550])
    # if sky:
    #     set_sky(P)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pia_light,(temppx+6340,temppy+512))
        P.surface.blit(P.r3_lights,(temppx+3207,temppy-582))
    show_location(P, P.loc_txt, tim)
    return thunder

def route_3(P,enter = False,x_pos = 5900) -> None:
    if P.song != "music/route_3.wav":
        P.song = "music/route_3.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] >= 81:
        if P.prog[5][22] == 0:
            P.r3_fish1 = npc.NPC(P,'Fisherman','Santiago',[4300,-800],[['u',60]],["Guess what? It turns out fish", "still bite even if the worms","are soggy!"],["Guess you did't find it that","interesting, huh?",""],True,[0,0,200,100],P.r3_fishteam,22,loc = "route_3")
        else:
            P.r3_fish1 = npc.NPC(P,'Fisherman','Santiago',[4300,-800],[['u',80]],["Well if you ever need some","more useless facts, you know","where to find me..."],loc = "route_3")
        if P.prog[5][23] == 0:
            P.r3_fish2 = npc.NPC(P,'Fisherman','Curt',[4250,-600],[['l',60]],["Whoo! Feels great to be back", "in the swing of things!",""],["Everything was going so great","today and then you just had to","come by..."],True,[0,0,200,100],P.r3_fishteam2,23,loc = "route_3")
        else:
            P.r3_fish2 = npc.NPC(P,'Fisherman','Curt',[4250,-600],[['l',60]],["Maybe I should just pack up","and go back home...",""],loc = "route_3")
        if P.prog[5][24] == 0:
            P.r3_tri2 = npc.NPC(P,'Triathelete','Ethan',[2500,-350],[['mr',500],['ml',500]],["Outta my way!", "",""],["Hey, I asked pretty nicely","didn't I?",""],True,[0,0,200,200],P.r3_triteam,24,loc = "route_3",spd = 1)
        else:
            P.r3_tri2 = npc.NPC(P,'Triathelete','Ethan',[2500,-350],[['mr',500],['ml',500]],["I don't have the time to talk","to you, okay?",""],loc = "route_3",spd = 1)
        P.r3_beauty = npc.NPC(P,'Beauty','Harper',[5700,-450],[['u',60]],["Don't you just love relaxing","here on the sand and taking in","the ocean breeze?",'I feel like I could lie here',"all day!",""])
        P.r3_tri = npc.NPC(P,'Triathelete','Harper',[4550,-500],[['u',60]],["I've decided to take a short","jog out here on the beach","every day!","But I've been too busy","enjoying the view to start...",""])
        P.r3_todd = npc.NPC(P,'Preschoolerb','Harper',[5200,-550],[['mr',40],['md',20],['ml',40],['mu',20]],["You know what? Sometimes","Pokemon come up to the shore","to poke their heads out!","Then you can pounce on them","and scare them away!","Mwahahahaha!"],spd = 1)
        P.r3_lass = npc.NPC(P,'Lass','Harper',[4050,-250],[['d',20]],["I have a good friend that","lives in Fiore Town.","","When I want to send him a","gift, I just box it up and","toss it down this river!","He doesn't always get it, but","that's fine! I have plenty of","money to spare!"])
    else:
        P.r3_fish1 = None
        P.r3_fish2 = None
        P.r3_beauty = None
        P.r3_tri = None
        P.r3_tri2 = None
        P.r3_todd = None
        P.r3_lass = None
    beachx = [4425,4475,4525,4575,4625,4675,4725,4775,4825,4875,4925,4975,5025,5075,5125,5175,5225,5275,5325,5375,5425,5475,5525,5575,5625,5675,5725,5775]
    beachy = [-700,-710,-720,-725,-730,-730,-730,-725,-715,-705,-695,-685,-680,-675,-675,-680,-685,-690,-695,-700,-705,-705,-705,-700,-690,-680,-660,-645]
    beachy_pos = [875,875,925,925,925,925,925,925,875,875,875,875,875,875,875,875,875,875,875,875,875,875,875,875,875,875,825,825]
    P.r3_hex = npc.NPC(P,'Hex Maniac','Harper',[3250,-550],[['u',60]],["This shrine is dedicated to","Manaphy, one of the fairies","that guards these islands.","I recommend you make an","offering as a sign of respect.",""])
    P.r3_battle.x = x_pos
    if P.prog[15][6] == 0:
        P.r3_lop = npc.NPC(P,'Lopunny','Dude',[5900,-200],[['d',20]],["","",""])
    else:
        P.r3_lop = None
    if P.prog[5][3] == 0:
        P.r3_noland = npc.NPC(P,'Gentleman','Noland',[700,450],[['r',100]],["","",""])
    else:
        P.r3_noland = None
    if P.prog[0] <= 74:
        P.r3_worker = npc.NPC(P,'Officer','Dude',[2150,-250],[['l',20]],["I'm sorry, but it's far too","dangerous to continue down","Route 3 at the moment.", "If you need to get to Pianura","City, you'll have better luck","passing through Scarab Woods."])
    else:
        P.r3_worker = None
    if P.prog[0] <= 69:
        P.r3_worker2 = npc.NPC(P,'Officer','Dude',[5600,-50],[['d',20]],["I'm sorry, but access to","Slowpoke Beach is restricted","at the moment.", "We're in a bit of a crisis","right now, thanks for being","patient with us!"])
    elif P.prog[0] <= 74:
        P.r3_worker2 = npc.NPC(P,'Officer','Dude',[5550,-100],[['r',20]],["","",""])
    else:
        P.r3_worker2 = None
    if P.prog[0] in [69,70]:
        P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5600,-250],[['d',20]],["","",""])
        P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5650,-250],[['d',20]],["","",""])
    elif P.prog[0] == 74:
        P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5150,-300],[['l',20]],["","",""])
        P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5200,-250],[['l',20]],["","",""])
    else:
        P.r3_cheryl = None
        P.r3_rival = None
    P.habitat = 'grass'
    thunder = 0
    rain = 0
    move = True
    wx = 0
    wy = 0
    tim = 0
    beach_poke = 0
    set_location(P)
    if enter == False:
        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
        route_3_p(P,P.px,P.py,False)
        route_3_f(P,P.px,P.py,rain,tim)
        fade_in(P)
    end = True
    m = 0
    while end:
        print(P.px,P.py)
        # print(beach_poke)
        if P.prog[0] >= 80 and type(beach_poke) == float and tim%10 == 0:
            if random.random() < beach_poke:
                beach_poke = [random.randint(0,len(beachx)-1),random.randint(20,150)]
        if P.prog[0] >= 70 and P.prog[0] <= 75 and P.px >= -5000:
            v = P.vol*((5000+P.px)/50)/30
            set_mixer_volume(P,P.vol-v)
        if P.prog[0] == 69 and P.r3_worker2.x == 5550 and P.r3_worker2.face() == 'r':
            move = True
            P.r3_worker2 = npc.NPC(P,'Officer','Dude',[5550,-100],[['r',20]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 70 and P.py == 375:
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5600,-250],[['md',20],['d',20]],["","",""])
            move = False
            P.prog[0] += 1
        if P.prog[0] == 71 and P.r3_cheryl.y == -200:
            txt(P,'Hello, '+P.save_data.name+"! I assume","you're finished making your", "preparations?")
            txt(P,"Follow me. The cause of our","problems is waiting right down", "this road.")
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5600,-200],[['mu',40],['ml',180],['l',200]],["","",""])
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5650,-250],[['l',100],['ml',180],['l',200]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 73:
            txt(P,"Right in the middle of that","storm is a being straight out","of the legends.")
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5150,-300],[['d',20]],["","",""])
            P.p = P.u1
            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
            route_3_p(P,P.px,P.py,False)
            route_3_f(P,P.px,P.py,rain,tim)
            txt(P,"I've done my part trying to","keep it at bay, but my Pokemon","are quite exhausted.")
            txt(P,"I'd like you to head in there","to finish the job I started.","Good luck!")
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5150,-300],[['l',20]],["","",""])
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5200,-250],[['l',20]],["","",""])
            P.prog[0] += 1
            move = True
        if P.prog[0] == 74 and P.px == -4825 and P.py == 475:
            P.p = P.u1
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5200,-250],[['d',20]],["","",""])
            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
            route_3_p(P,P.px,P.py,False)
            route_3_f(P,P.px,P.py,rain,tim)
            txt(P,"Wait! You're going the wrong","way! Don't worry, I'm sure", "you'll be fine!")
            txt(P,"Cheryl wouldn't have asked you","to help if she didn't think","you could handle it!")
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[5200,-250],[['l',20]],["","",""])
        if P.prog[0] == 74 and P.px == -3725:
            txt(P,"You feel like you passed by","something in the darkness.")
        if P.prog[0] == 77 and P.r3_cheryl.x == 4350:
            txt(P,"You managed to chase it off!","Thanks for the help! Hopefully","it's gone for good!")
            txt(P,"I believe you came here to","claim the Pianura City Gym","badge?")
            txt(P,"Well I'll be waiting for you!","You better not disappoint me","with your challenge!")
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[4350,-350],[['mr',60]],["","",""])
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[4400,-300],[['l',120],['mu',20],['ml',20],['l',100]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 78 and P.r3_rival.x == 4350:
            txt(P,"I couldn't see through all the","clouds and rain, but I bet","that was a crazy fight!")
            txt(P,"I can't wait until we get the","chance to battle again!","See you later!")
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[4350,-350],[['mr',20]],["","",""],spd = 1)
            P.r3_worker = None
            P.r3_worker2 = None
            P.prog[0] += 1
        if P.prog[0] == 79 and P.r3_rival.x == 4750:
            move = True
            P.r3_cheryl = None
            P.r3_rival = None
            P.prog[0] += 1
        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
        if move == True and P.r3_bug.trainer_check():
            move = False
        if move == True and P.r3_hika.trainer_check():
            move = False
        if move == True and P.r3_sci.trainer_check():
            move = False
        if move == True and P.r3_battle.trainer_check():
            move = False
        if move == True and P.r3_fish1 and P.r3_fish1.trainer_check():
            move = False
        if move == True and P.r3_fish2 and P.r3_fish2.trainer_check():
            move = False
        if move == True and P.r3_tri2 and P.r3_tri2.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        route_3_p(P,temppx,temppy,move)
        thunder = route_3_f(P,temppx,temppy,rain,tim,thunder)
        if P.prog[0] == 76:
            fade_in(P)
            P.prog[0] += 1
        if P.prog[0] == 75:
            P.habitat = 'dock_night'
            P.song = "music/fon_battle.wav"
            pygame.mixer.Channel(0).stop()
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            battle(P,[poke.Poke('Thundurus_T',[40,0,50,'Shock Wave',2,'Frustration',2,'Bite',-1,'Revenge',-1,None,None,0,"Poke Ball"])])
            P.legendary_battle = False
            P.clock.tick(1)
            P.prog[0] += 1
            move = False
            set_mixer_volume(P,P.vol)
            play_music(P,"music/route_3.wav")
            P.habitat = 'grass'
            P.p = P.r1
            P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[4750,-350],[['ml',160],['l',50]],["","",""])
            P.r3_rival = npc.NPC(P,'Rival',P.save_data.rival,[4800,-300],[['ml',160],['l',50]],["","",""])
        if P.px == -5525 and P.py == 225 and face_u(P) and P.prog[15][6] == 0:
            if P.prog[15][0] == 0:
                txt(P,"The Lopunny is eyeing you","funny.")
                print_mega_area(P)
            elif P.prog[15][6] == 0:
                txt(P,"The Lopunny is eyeing you","funny.")
                if in_party(P,'Lopunny',True):
                    new_txt(P)
                    write(P,"Approach the Lopunny?")
                    if choice(P):
                        move = False
                        P.prog[15][6] += 1
                else:
                    txt(P,"You should bring a Lopunny","before approaching it.")
        if P.py == 425 and P.prog[15][6] == 1:
            te = P.surface.copy()
            txt(P,"The Lopunny attacked!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Lopunny' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Lopunny',[30,1,334,'Dizzy Punch',-1,None,None,None,None,None,None,None,None,0,"Poke Ball",200,'Dodge'])],no_pc = True)
            play_music(P,"music/route_3.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][6] = 0
                txt(P,"The Lopunny didn't seem very","happy with how quickly you","lost the battle.")
                txt(P,"It drove you away from the","clearing!")
                fade_out(P)
                P.p = P.d1
                P.px = -5525
                P.py = 175
                route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                route_3_p(P,P.px,P.py,False)
                route_3_f(P,P.px,P.py,rain,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][6] += 1
                txt(P,"The Lopunny looks quite happy!","It handed you a mysterious","stone before leaving.")
                add_item(P,'Lopunnite',1)
                fade_out(P)
                P.r3_lop = None
                route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                route_3_p(P,P.px,P.py,False)
                route_3_f(P,P.px,P.py,rain,tim)
                fade_in(P)
                move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
        if trainer_check(P,P.r3_bug,"music/route_3.wav"):
            P.r3_bug = npc.NPC(P,'Bug Catcher','Charlie',[P.r3_bug.x,P.r3_bug.y],[['md',60],['d',20],['mr',40],['r',80],['mu',60],['u',60],['ml',40],['l',20]],["Hurry up and leave already!","I only said you could stay for", "a little while!","I can't have you finding all","the Pokemon here before I get","the chance to!"],tim = P.r3_bug.tim,curr = P.r3_bug.curr,extra_walk = P.r3_bug.extra_walk)
            move = True
        if trainer_check(P,P.r3_hika,"music/route_3.wav"):
            P.r3_hika = npc.NPC(P,'Hiker','Bryson',[1500,200],[['u',20]],["Despite all the expeditions","I've been on, I've never seen", "crystals like these.","The way they're glowing...It's","almost as if they're alive!",""])
            move = True
        if trainer_check(P,P.r3_sci,"music/route_3.wav"):
            P.r3_sci = npc.NPC(P,'Scientistf','Rosa',[P.r3_sci.x,P.r3_sci.y],[['l',100],['mu',40],['ml',60],['d',140],['mr',60],['md',40]],["Ugh! I'm already tired again!","How important could a little", "pink crystal possibly be?"],tim = P.r3_sci.tim,curr = P.r3_sci.curr,extra_walk = P.r3_sci.extra_walk)
            move = True
        if trainer_check(P,P.r3_battle,"music/route_3.wav"):
            P.r3_battle = npc.NPC(P,'Battle Girl','Harper',[P.r3_battle.x,P.r3_battle.y],[['mr',80],['r',100],['ml',80],['l',60]],["I can't remember if I turned","off the oven before I left...",""],tim = P.r3_battle.tim,curr = P.r3_battle.curr,extra_walk = P.r3_battle.extra_walk)
            move = True
        if trainer_check(P,P.r3_fish1,"music/route_3.wav"):
            P.r3_fish1 = npc.NPC(P,'Fisherman','Harper',[4300,-800],[['u',60]],["Well if you ever need some","more useless facts, you know","where to find me..."])
            move = True
        if trainer_check(P,P.r3_fish2,"music/route_3.wav"):
            P.r3_fish2 = npc.NPC(P,'Fisherman','Harper',[4250,-600],[['l',60]],["Maybe I should just pack up","and go back home...",""])
            move = True
        if trainer_check(P,P.r3_tri2,"music/route_3.wav"):
            P.r3_tri2 = npc.NPC(P,'Triathelete','Harper',[P.r3_tri2.x,P.r3_tri2.y],[['mr',500],['ml',500]],["I don't have the time to talk","to you, okay?",""],tim = P.r3_tri2.tim,curr = P.r3_tri2.curr,extra_walk = P.r3_tri2.extra_walk,spd = 1)
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.r3_bug.talk():
                        if P.r3_bug.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_bug.write()
                    elif P.r3_hika.talk():
                        if P.r3_hika.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_hika.write()
                    elif P.r3_sci.talk():
                        if P.r3_sci.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_sci.write()
                    elif P.r3_battle.talk():
                        if P.r3_battle.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_battle.write()
                    elif P.r3_fish1 and P.r3_fish1.talk():
                        if P.r3_fish1.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_fish1.write()
                    elif P.r3_fish2 and P.r3_fish2.talk():
                        if P.r3_fish2.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_fish2.write()
                    elif P.r3_tri2 and P.r3_tri2.talk():
                        if P.r3_tri2.trainer:
                            move = False
                        else:
                            route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                            route_3_p(P,P.px,P.py,False)
                            route_3_f(P,P.px,P.py,rain,tim)
                            P.r3_tri2.write()
                    elif P.r3_hex and P.r3_hex.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_hex.write()
                    elif P.r3_beauty and P.r3_beauty.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_beauty.write()
                    elif P.r3_tri and P.r3_tri.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_tri.write()
                    elif P.r3_todd and P.r3_todd.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_todd.write()
                    elif P.r3_lass and P.r3_lass.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_lass.write()
                    elif P.px == -3925 and P.py == 625 and face_u(P) and P.prog[0] == 74:
                        P.prog[0] += 1
                    elif P.prog[0] == 74 and next_to(P,5200,-250):
                        txt(P,"Go get 'em, "+P.save_data.name+"! I've","seen you fight enough to know","this'll be easy for you!")
                    elif P.prog[0] == 74 and next_to(P,5150,-300):
                        P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5150,-300],[['d',20]],["","",""])
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        txt(P,"I've already weakened it quite","a bit for you. I'm sure you'll","be fine!")
                        P.r3_cheryl = npc.NPC(P,'Cheryl','Cherry',[5150,-300],[['l',20]],["","",""])
                    elif P.prog[0] == 74 and P.px == -4725 and P.py == 600 and face_r(P):
                        txt(P,'You feel a strange sense of',"superiority looking down at", "Cheryl's head.")
                    elif next_to(P,1450,100) or next_to(P,1500,100) or next_to(P,1550,100) or next_to(P,1600,100) or next_to(P,1450,50) or next_to(P,1500,50) or next_to(P,1550,50) or next_to(P,1600,50):
                        txt(P,'The crystals on top of this',"rock seem to be glowing with","some kind of energy.")
                    elif P.px == -3875 and P.py >= 675 and face_l(P):
                        txt(P,"You could probably fish here","if you had a fishing rod.")
                    elif P.py == 1075 and face_u(P):
                        if P.prog[15][0] == 0:
                            txt(P,"There's a Slowbro asleep on","the rock.")
                            print_mega_area(P)
                        elif P.prog[15][7] == 0:
                            txt(P,"There's a Slowbro asleep on","the rock.")
                            if in_party(P,'Slowbro',True):
                                new_txt(P)
                                write(P,"Say something?")
                                if choice(P):
                                    move = False
                                    P.prog[15][7] += 1
                            else:
                                txt(P,"You should come back with a","Slowbro in your party.")
                    elif next_to(P,3250,-600) or next_to(P,3200,-600) or next_to(P,3250,-650) or next_to(P,3200,-650):
                        if P.px == -2825 and P.py == 825:
                            new_txt(P)
                            write(P,'Throw a coin into the offering',"box?")
                            if choice(P):
                                if P.save_data.money > 0:
                                    txt(P,"You tossed a coin in the box","and made a short prayer.")
                                    txt(P,"You feel strangely at peace.")
                                    for p in P.party:
                                        if p.status != 'Faint':
                                            p.status = None
                                    P.save_data.money -= 1
                                else:
                                    txt(P,"You don't have enough to make","an offering. How pathetic!")
                        else:
                            txt(P,"It's a small shrine.")
                    elif next_to(P,1250,-100) and P.prog[6][13] == 0:
                        txt(P,P.save_data.name + " found a", "Heart Scale!")
                        txt(P,P.save_data.name + " put the Heart Scale","in the Items pocket.")
                        add_item(P,"Heart Scale",1)
                        P.prog[6][13] = 1
                    elif next_to(P,4950,150) and P.prog[6][35] == 0:
                        txt(P,P.save_data.name + " found a", "Heart Scale!")
                        txt(P,P.save_data.name + " put the Heart Scale","in the Items pocket.")
                        add_item(P,"Heart Scale",1)
                        P.prog[6][35] = 1
                    elif P.px == -2125 and P.py == 325 and face_l(P) and P.prog[6][14] == 0:
                        txt(P,P.save_data.name + " found a", "Miracle Seed!")
                        txt(P,P.save_data.name + " put the Miracle","Seed in the Items pocket.")
                        add_item(P,"Miracle Seed",1)
                        P.prog[6][14] = 1
                    elif P.px == -3825 and P.py == 625 and face_u(P):
                        txt(P,"It's a fishing sign.")
                    elif type(beach_poke) == list and P.px+beachx[beach_poke[0]] == 350 and P.py == beachy_pos[beach_poke[0]] and face_u(P):
                        te = P.surface.copy()
                        txt(P,"The Pokemon came out of the","water!")
                        P.habitat = "beach"
                        P.song = "music/wild_battle.wav"
                        pygame.mixer.music.load(P.song)
                        set_mixer_volume(P,P.vol)
                        pygame.mixer.music.play(0)
                        rando = random.random()
                        if rando < 0.25:
                            r = random.randint(19,22)
                            if r < 21:
                                battle(P,[poke.Poke('Krabby',[r,random.randint(0,1),334,"Bubble Beam",-1,"Vice Grip",-1,"Harden",-1,"Mud Shot",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Krabby',[r,random.randint(0,1),334,"Bubble Beam",-1,"Metal Claw",-1,"Harden",-1,"Mud Shot",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .25 and rando < .35:
                            r = random.randint(20,23)
                            if r < 23:
                                battle(P,[poke.Poke('Slowpoke',[r,random.randint(0,1),334,"Confusion",-1,"Curse",-1,"Yawn",-1,"Water Gun",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Slowpoke',[r,random.randint(0,1),334,"Confusion",-1,"Headbutt",-1,"Yawn",-1,"Water Gun",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .35 and rando < .6:
                            battle(P,[poke.Poke('Shellder',[random.randint(17,20),random.randint(0,1),334,"Protect",-1,"Icicle Spear",-1,"Withdraw",-1,"Water Gun",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .6 and rando < .75:
                            r = random.randint(19,22)
                            if r < 22:
                                battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Water Pulse",-1,"Confusion",-1,"Disable",-1,"Fury Swipes",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Water Pulse",-1,"Confusion",-1,"Screech",-1,"Fury Swipes",-1,None,None,0,"Poke Ball"])])
                        elif rando >= .75:
                            r = random.randint(19,22)
                            if r < 20:
                                battle(P,[poke.Poke('Corphish',[r,random.randint(0,1),334,"Protect",-1,"Bubble Beam",-1,"Vice Grip",-1,"Leer",-1,None,None,0,"Poke Ball"])])
                            else:
                                battle(P,[poke.Poke('Corphish',[r,random.randint(0,1),334,"Protect",-1,"Bubble Beam",-1,"Double Hit",-1,"Leer",-1,None,None,0,"Poke Ball"])])
                        P.song = "music/route_3.wav"
                        P.habitat = "grass"
                        pygame.mixer.music.load(P.song)
                        set_mixer_volume(P,P.vol)
                        pygame.mixer.music.play(-1)
                        P.surface.blit(te,(0,0))
                        fade_in(P)
                        beach_poke = 0
                    elif P.r3_worker and P.r3_worker.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        P.r3_worker.write()
                    elif P.r3_worker2 and P.r3_worker2.talk():
                        route_3_b(P,wx,wy,beachx,beachy,beach_poke)
                        route_3_p(P,P.px,P.py,False)
                        route_3_f(P,P.px,P.py,rain,tim)
                        if P.prog[0] == 69:
                            txt(P,"You are "+P.save_data.name+", correct?","Right this way, Cheryl is","waiting for you.")
                            P.r3_worker2 = npc.NPC(P,'Officer','Dude',[5600,-50],[['mu',20],['ml',20],['r',20]],["","",""])
                            move = False
                        else:
                            P.r3_worker2.write()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == -1975 and P.py >= 75 and P.py <= 125 and face_r(P):
            P.px = -1125
            P.py += 650
            P.move_out_dir = 'r'
            P.loc = "scarab_l"
            end = False
        if P.px == -2375 and P.py == 325 and face_r(P):
            P.px = -1625
            P.py = 975
            P.move_out_dir = 'r'
            P.loc = "scarab_l"
            end = False
        if P.px in [-4825,-4775] and P.py == -175 and face_d(P):
            P.py = 625
            P.px += 2550
            P.move_out_dir = 'd'
            P.loc = "scarab_r"
            end = False
        if P.py in [-25,-75,-125] and P.px == -5825 and face_r(P):
            # P.py -= 50
            P.px = 275
            P.loc = "pianura"
            update_locs(P)
            pianura(P,True,P.r3_battle.x-6100)
            end = False
        if P.py == 425 and P.px >= -625 and P.px <= -525 and face_u(P):
            P.px -= 900
            P.py = -75
            P.move_out_dir = 'u'
            P.loc = "egida_under"
            end = False
        #left
        if move and (wild_grass(P,-1625,225,350,350,ignore = [(-1625,25),(-1625,-25),(-1625,-75),(-1675,-75),(-1925,175),(-1925,125),(-1875,125),(-1875,75),(-1925,75),(-1925,25)]) or wild_grass(P,-875,375,600,400)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.1:
                if P.px > -1525:
                    battle(P,[poke.Poke('Carbink',[random.randint(13,15),2,334,"Tackle",-1,"Harden",-1,"Sharpen",-1,"Smack Down",-1,None,None,0,"Poke Ball"])])
                else:
                    r = random.randint(10,14)
                    if r < 13:
                        battle(P,[poke.Poke('Metapod',[r,random.randint(0,1),334,"Tackle",-1,"String Shot",-1,"Harden",-1,None,None,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Butterfree',[r,random.randint(0,1),334,"Confusion",-1,"Poison Powder",-1,"Stun Spore",-1,"Gust",-1,None,None,0,"Poke Ball"])])
            elif rando >= .1 and rando < .35:
                r = random.randint(11,14)
                if r < 13:
                    battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Scratch",-1,"Tail Whip",-1,"Water Gun",-1,"Confusion",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Fury Swipes",-1,"Tail Whip",-1,"Water Gun",-1,"Confusion",-1,None,None,0,"Poke Ball"])])
            elif rando >= .35 and rando < .55:
                r = random.randint(12,14)
                if r < 13:
                    battle(P,[poke.Poke('Drowzee',[r,random.randint(0,1),334,"Hypnosis",-1,"Disable",-1,"Confusion",-1,"Pound",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Drowzee',[r,random.randint(0,1),334,"Hypnosis",-1,"Disable",-1,"Confusion",-1,"Headbutt",-1,None,None,0,"Poke Ball"])])
            elif rando >= .55 and rando < .80:
                battle(P,[poke.Poke('Seedot',[random.randint(10,13),random.randint(0,1),334,"Bide",-1,"Harden",-1,"Growth",-1,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .8:
                r = random.randint(11,14)
                if r < 13:
                    battle(P,[poke.Poke('Bellsprout',[r,random.randint(0,1),334,"Vine Whip",-1,"Growth",-1,"Wrap",-1,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Bellsprout',[r,random.randint(0,1),334,"Vine Whip",-1,"Growth",-1,"Wrap",-1,"Sleep Powder",-1,None,None,0,"Poke Ball"])])
            P.song = "music/route_3.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        #right
        if move and (wild_grass(P,-5325,175,500,200) or wild_grass(P,-4575,-25,450,100,ignore = [(-4975,-75)]) or wild_grass(P,-4575,125,600,150)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.15:
                r = random.randint(17,21)
                if r < 18:
                    battle(P,[poke.Poke('Lotad',[r,random.randint(0,1),334,"Absorb",-1,"Mist",-1,"Bubble",-1,"Natural Gift",-1,None,None,0,"Poke Ball"])])
                elif r < 21:
                    battle(P,[poke.Poke('Lotad',[r,random.randint(0,1),334,"Mega Drain",-1,"Mist",-1,"Bubble",-1,"Natural Gift",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Lombre',[r,random.randint(0,1),334,"Fake Out",-1,"Water Sport",-1,"Fury Swipes",-1,"Bubble",-1,None,None,0,"Poke Ball"])])
            elif rando >= .15 and rando < .3:
                battle(P,[poke.Poke('Drowzee',[random.randint(17,20),random.randint(0,1),334,"Disable",-1,"Confusion",-1,"Headbutt",-1,"Poison Gas",-1,None,None,0,"Poke Ball"])])
            elif rando >= .3 and rando < .4:
                r = random.randint(18,21)
                if r < 21:
                    battle(P,[poke.Poke('Ponyta',[r,random.randint(0,1),334,"Flame Wheel",-1,"Stomp",-1,"Growl",-1,"Tail Whip",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Ponyta',[r,random.randint(0,1),334,"Flame Wheel",-1,"Stomp",-1,"Flame Charge",-1,"Tail Whip",-1,None,None,0,"Poke Ball"])])
            elif rando >= .4 and rando < .6:
                battle(P,[poke.Poke('Buneary',[random.randint(16,19),random.randint(0,1),334,"Quick Attack",-1,"Baby-Doll Eyes",-1,"Endure",-1,"Defense Curl",-1,None,None,0,"Poke Ball"])])
            elif rando >= .6 and rando < .75:
                r = random.randint(16,19)
                if r < 18:
                    battle(P,[poke.Poke('Joltik',[r,random.randint(0,1),334,"Electroweb",-1,"Fury Cutter",-1,"Thunder Wave",-1,"Screech",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Joltik',[r,random.randint(0,1),334,"Electroweb",-1,"Bug Bite",-1,"Thunder Wave",-1,"Screech",-1,None,None,0,"Poke Ball"])])
            else:
                r = random.randint(17,21)
                gen = random.randint(0,1)
                if r < 19:
                    if gen == 0:
                        battle(P,[poke.Poke('Nidoran_M',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Focus Energy",-1,"Peck",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Nidoran_F',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Tail Whip",-1,"Scratch",-1,None,None,0,"Poke Ball"])])
                elif r < 21:
                    if gen == 0:
                        battle(P,[poke.Poke('Nidoran_M',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Focus Energy",-1,"Fury Attack",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Nidoran_F',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Tail Whip",-1,"Fury Swipes",-1,None,None,0,"Poke Ball"])])
                else:
                    if gen == 0:
                        battle(P,[poke.Poke('Nidorino',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Focus Energy",-1,"Fury Attack",-1,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Nidorina',[r,gen,334,"Double Kick",-1,"Poison Sting",-1,"Tail Whip",-1,"Fury Swipes",-1,None,None,0,"Poke Ball"])])
            P.song = "music/route_3.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if tim%20 == 0:
            if P.r3_slow == P.r3_slow1:
                P.r3_slow = P.r3_slow2
            else:
                P.r3_slow = P.r3_slow1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if type(beach_poke) == list:
                beach_poke[1] -= 1
                if beach_poke[1] == 0:
                    beach_poke = 0
            else:
                beach_poke += 0.001
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        tim += 1
        if P.prog[0] >= 70 and P.prog[0] <= 74 and P.px >= -5000:
            rain += 1
            if thunder > 0:
                thunder -= 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def power_plant_2_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pp2_back,(P.px,P.py))

def power_plant_2_p(P,temppx,temppy,move):
    #rects start
    r1 = (P.px,P.py+50,150,40)
    r2 = (P.px+150,P.py+100,50,190)
    r3 = (P.px+50,P.py+100,50,40)
    r4 = (P.px-50,P.py+100,50,190)
    r5 = (P.px,P.py+300,150,50)
    r6 = (P.px+50,P.py+150,50,40)
    if P.px <= 325:
        r6 = (P.px,P.py+150,50,40)
    rects = [r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)

def power_plant_2_f(P,temppx,temppy,tim):
    P.surface.blit(P.ss_d1,(temppx,temppy+100))
    P.surface.blit(P.pp2_wall,(temppx,temppy+50))
    show_location(P, P.loc_txt, tim)

def power_plant_2(P) -> None:
    if P.song != "music/power_plant.wav":
        P.song = "music/power_plant.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.pp2_back = load("p/egida/Power_Plant_2F.png")
    P.pp2_wall = load("p/egida/pp2_wall.png")
    move = True
    tim = 0
    set_location(P)
    power_plant_2_b(P)
    power_plant_2_p(P,P.px,P.py,False)
    power_plant_2_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    fade = None
    while end:
        power_plant_2_b(P)
        #print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        power_plant_2_p(P,temppx,temppy,move)
        power_plant_2_f(P,temppx,temppy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if next_to(P,50,100):
                        txt(P,"This rose looks like it's","wilting.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 325 and P.py == 25 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -2775
            P.py = 1075
            P.loc = "vigore"
            fade = P.song
            end = False
        if P.px == 375 and P.py == 175 and face_u(P):
            P.py += 50
            P.p = P.d1
            P.loc = "power_plant_1"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P,fade)

def power_plant_b_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.ppb_back,(P.px,P.py))

def power_plant_b_p(P,temppx,temppy,move):
    #rects start
    if P.ppb_rocket2:
        rocket2 = P.ppb_rocket2.y_dist()
        if rocket2 > 0:
            P.ppb_rocket2.move()
    if P.ppb_rocket1:
        rocket1 = P.ppb_rocket1.y_dist()
        colress = P.ppb_colress.y_dist()
        if rocket1 > 0:
            P.ppb_rocket1.move()
        if colress > 0:
            P.ppb_colress.move()
    if P.ppb_eusine:
        eusine = P.ppb_eusine.y_dist()
        if eusine > 0:
            P.ppb_eusine.move()
    r1 = (P.px,P.py+50,200,40)
    r2 = (P.px+200,P.py+50,350,90)
    r3 = (P.px,P.py+300,50,40)
    r4 = (P.px-50,P.py+50,50,390)
    r5 = (P.px,P.py+450,600,50)
    r6 = (P.px+650,P.py+50,50,340)
    r7 = (P.px+550,P.py,100,40)
    r8 = (P.px+50,P.py+250,50,140)
    r9 = (P.px+600,P.py+400,50,50)
    rects = [r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if P.prog[0] == 27:
        player_move(P,rects,manual_input = 'd',spd = 3)
    elif P.prog[0] == 28:
        player_move(P,rects,manual_input = 'l',spd = 3)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.ppb_eusine:
        if eusine <= 0:
            P.ppb_eusine.move(temppx,temppy)
    if P.ppb_rocket2:
        if rocket2 <= 0:
            P.ppb_rocket2.move()
    if P.ppb_rocket1:
        if rocket1 <= 0:
            P.ppb_rocket1.move(temppx,temppy)
        if colress <= 0:
            P.ppb_colress.move(temppx,temppy)

def power_plant_b_f(P,temppx,temppy,tim):
    #P.surface.blit(P.ss_d2,(temppx+550,temppy+100))
    P.surface.blit(P.ss_u2,(temppx+550,temppy))
    P.surface.blit(P.ppb_comp,(temppx+49,temppy+225))
    #P.surface.blit(P.pp1_wall,(temppx+550,temppy+50))
    show_location(P, P.loc_txt, tim)

def power_plant_b(P) -> None:
    if P.song != "music/power_plant.wav":
        P.song = "music/power_plant.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.habitat = 'indoor'
    P.ppb_comp = load("p/egida/pp_bff.png")
    P.ppb_back = load("p/egida/Power_Plant_BF.png")
    if P.prog[0] == 26:
        P.ppb_rocket1 = npc.NPC(P,'Team Rocketf','Grunt',[150,350],[['u',20]],["","",""])
        P.ppb_colress = npc.NPC(P,'Colress','',[150,200],[['d',20]],["","",""])
    else:
        P.ppb_rocket1 = None
        P.ppb_colress = None
    if P.prog[0] >= 39:
        P.ppb_eusine = npc.NPC(P,'Eusine','',[0,300],[['r',20]],["Thanks again for helping out","with those strangers. The","research I'm doing helps run","this facility, so it would","have been quite problematic","if they had messed it all up."])
    else:
        P.ppb_eusine = None
    P.ppb_rocket2 = None
    move = True
    tim = 0
    set_location(P)
    power_plant_b_b(P)
    power_plant_b_p(P,P.px,P.py,False)
    power_plant_b_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        if P.prog[0] == 26 and P.py == 125 and (P.px == -175 or P.px == -225):
            P.prog[0] += 1
            move = False
        if P.prog[0] == 27 and P.py == 75:
            P.prog[0] += 1
        if P.prog[0] == 28 and P.px == 75:
            P.prog[0] += 1
        if P.prog[0] == 29:
            P.ppb_colress = npc.NPC(P,'Colress','',[150,200],[['r',20]],["","",""])
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,"Ah, thank you for coming. You","showed up at the perfect", "time.")
            txt(P,"I found the one who's been","causing the problems we've", "been having!")
            P.prog[0] += 1
            P.ppb_rocket2 = npc.NPC(P,'Team Rocketm','Grunt',[600,50],[['md',60],['ml',60],['l',80]],["","",""])
        if P.prog[0] == 30 and P.ppb_rocket2.x == 450:
            P.p = P.r1
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,'Hey, I brought the research', 'papers from his lab!')
            P.ppb_rocket1 = npc.NPC(P,'Team Rocketf','Grunt',[150,350],[['mu',20],['r',60]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 31 and P.ppb_rocket1.y == 300:
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,'Why did you come back here?!!','You\'re supposed to bring those','back to headquarters!')
            txt(P,'I led them here so we wouldn\'t','have to get our hands dirty!', '')
            txt(P,'Ahh whatever...we\'ll just have', 'to beat you guys up and get', 'outta here!')
            P.ppb_rocket1 = npc.NPC(P,'Team Rocketf','Grunt',[150,300],[['u',20]],["","",""])
            P.ppb_colress = npc.NPC(P,'Colress','',[150,200],[['md',20],['d',200]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 32 and P.ppb_colress.y == 250:
            txt(P,'I\'ll take care of this young','lady. I trust you can handle','the other one?')
            P.prog[0] += 1
            P.ppb_rocket2 = npc.NPC(P,'Team Rocketm','Grunt',[450,200],[['ml',60],['l',40]],["","",""])
        if P.prog[0] == 33 and P.ppb_rocket2.x == 350:
            te = P.surface.copy()
            txt(P,'I\'m gonna make you regret', 'underestimating us!')
            play_music(P,"music/trainer_battle.wav",0)
            battle(P,["Team Rocketm Grunt",poke.Poke('Whismur',[14,random.randint(0,1),334,"Pound",-1,"Echoed Voice",-1,"Astonish",-1,"Howl",-1,None,None,0,"Poke Ball",0,"Soundproof"]),poke.Poke('Bellsprout',[14,random.randint(0,1),334,"Vine Whip",-1,"Growth",-1,"Wrap",-1,"Sleep Powder",-1,None,None,0,"Poke Ball",0,"Chlorophyll"]),poke.Poke('Spinarak',[14,random.randint(0,1),334,"Poison Sting",-1,"String Shot",-1,"Infestation",-1,"Scary Face",-1,None,None,0,"Poke Ball",0,"Swarm"])])
            play_music(P,"music/power_plant.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            txt(P,'Ugh. you guys are way too', 'strong!')
            P.ppb_colress = npc.NPC(P,'Colress','',[150,250],[['mu',20],['r',100]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 34 and P.ppb_colress.y == 200:
            P.p = P.l1
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,'Perfect, you\'re finished up','as well!')
            P.p = P.r1
            P.ppb_rocket2 = npc.NPC(P,'Team Rocketm','Grunt',[350,200],[['mr',20],['l',80]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 35 and P.ppb_rocket2.x == 400:
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,'You\'re not getting your hands','on me! I\'m outta here!')
            P.ppb_rocket2 = npc.NPC(P,'Team Rocketm','Grunt',[400,200],[['mr',30],['mu',30]],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 36 and P.ppb_rocket2.y == 50:
            P.ppb_rocket2 = None
            P.ppb_colress = npc.NPC(P,'Colress','',[150,200],[['mr',40],['r',80]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 37 and P.ppb_colress.x == 250:
            P.p = P.l1
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            update_screen(P)
            P.clock.tick(P.ani_spd)
            txt(P,'I\'ll take this troublemaker', 'back to Egida to question her','about this incident.')
            txt(P,'Do you think you could chase','after that guy and bring him','back as well?')
            txt(P,'He shouldn\'t have been able','to get that far away.')
            P.ppb_colress = None
            P.ppb_rocket1 = None
            fade_out(P)
            power_plant_b_b(P)
            power_plant_b_p(P,P.px,P.py,False)
            power_plant_b_f(P,P.px,P.py,tim)
            fade_in(P)
            P.prog[0] += 1
            move = True
        power_plant_b_b(P)
        # print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        power_plant_b_p(P,temppx,temppy,move)
        power_plant_b_f(P,temppx,temppy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.ppb_eusine and P.ppb_eusine.talk():
                        power_plant_b_b(P)
                        power_plant_b_p(P,P.px,P.py,False)
                        power_plant_b_f(P,P.px,P.py,tim)
                        P.ppb_eusine.write()
                    elif P.py == 175 and P.px in [275,325] and face_u(P):
                        txt(P,"You don't really understand","any of it.")
                    elif (P.px == 225 and P.py == 175 and face_r(P)) or (P.py == 125 and P.px in [175,125,75,25,-25,-75] and face_u(P)):
                        txt(P,"You can hear the machines","whirring.")
                    elif next_to(P,600,400):
                        txt(P,"The trashcan's empty.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.px == -175 or P.px == -225) and P.py == 225 and face_u(P):
            P.py -= 50
            P.p = P.d1
            P.loc = "power_plant_1"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)

def power_plant_1_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pp1_back,(P.px,P.py))

def power_plant_1_p(P,temppx,temppy,move):
    #rects start
    if P.pp1_eusine:
        eusine = P.pp1_eusine.y_dist()
        if eusine > 0:
            P.pp1_eusine.move()
    r1 = (P.px+100,P.py+50,550,40)
    r2 = (P.px+50,P.py+50,50,90)
    r3 = (P.px,P.py,50,40)
    r4 = (P.px-50,P.py+50,50,390)
    r5 = (P.px,P.py+450,600,50)
    r6 = (P.px+650,P.py+100,50,290)
    r7 = (P.px+550,P.py+100,50,90)
    if P.px <= -175:
        r7 = (P.px+500,P.py+100,50,90)
    r8 = r1
    if P.pp1_eusine:
        r8 = P.pp1_eusine.get_rect()
    r9 = (P.px+600,P.py+400,50,50)
    rects = [r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.pp1_eusine:
        if eusine <= 0:
            P.pp1_eusine.move(temppx,temppy)

def power_plant_1_f(P,temppx,temppy,tim):
    P.surface.blit(P.ss_d2,(temppx+550,temppy+100))
    P.surface.blit(P.ss_u1,(temppx,temppy))
    P.surface.blit(P.pp1_wall,(temppx+550,temppy+50))
    show_location(P, P.loc_txt, tim)

def power_plant_1(P) -> None:
    if P.song != "music/power_plant.wav":
        P.song = "music/power_plant.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.pp1_back = load("p/egida/Power_Plant_1F.png")
    P.pp1_wall = load("p/egida/pp1_wall.png")
    if P.prog[0] == 26:
        P.pp1_eusine = npc.NPC(P,'Eusine','',[600,300],[['r',20]],["Ahh! What am I gonna do if","they mess up all my research","papers!","Please go downstairs to back","up Colress! He might need help","dealing with those punks!"])
    elif P.prog[0] == 38:
        P.pp1_eusine = npc.NPC(P,'Eusine','',[500,400],[['u',20]],["Colress told me what happened","down there! Thank you for","dealing with those rascals!","Oh, my name is Eusine. Sorry","I forgot to introduce myself","in all the chaos."])
    else:
        P.pp1_eusine = None
    move = True
    tim = 0
    set_location(P)
    power_plant_1_b(P)
    power_plant_1_p(P,P.px,P.py,False)
    power_plant_1_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    fade = None
    while end:
        power_plant_1_b(P)
        # print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        power_plant_1_p(P,temppx,temppy,move)
        power_plant_1_f(P,temppx,temppy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.pp1_eusine and P.pp1_eusine.talk():
                        power_plant_1_b(P)
                        power_plant_1_p(P,P.px,P.py,False)
                        power_plant_1_f(P,P.px,P.py,tim)
                        P.pp1_eusine.write()
                    elif next_to(P,600,400):
                        txt(P,"The trashcan's empty.")
                    elif P.py == 175 and P.px in [125,75,25] and face_u(P):
                        txt(P,"It looks like a presentation","of a large glowing stone.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 75 and P.py == -125 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -2875
            P.py = 775
            P.loc = "vigore"
            fade = P.song
            end = False
        if (P.px == -175 or P.px == -225) and P.py == 175 and face_u(P):
            P.py += 50
            P.p = P.d1
            P.loc = "power_plant_b"
            end = False
        if P.px == 375 and P.py == 225 and face_u(P):
            P.py -= 50
            P.p = P.d1
            P.loc = "power_plant_2"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P,fade)

def vigore_dam_b(P,wx,wy,fall):
    draw_waves(P,wx,wy)
    P.surface.blit(P.vigore,(P.px+50,P.py-2000))
    if P.px == -2775 and P.py > 1025 and P.py < 1100:
        P.surface.blit(P.vigore_pp2_door,(P.px+3150,P.py-815))
    draw_falls(P,fall,2014,-1050,350)
    draw_falls(P,fall-50,2164,-1050,350)
    draw_falls(P,fall-100,2314,-1050,350)
    draw_falls(P,fall-80,2464,-1050,350)
    draw_falls(P,fall-30,2614,-1050,350)
    draw_falls(P,fall-120,2764,-1050,350)
    if P.px == -2875 and P.py > 725 and P.py < 800:
        P.surface.blit(P.vigore_door,(P.px+3250,P.py-550))
    if P.prog[6][10] == 0:
        P.surface.blit(P.item_out,(P.px+500,P.py-1400))
    if P.prog[6][11] == 0:
        P.surface.blit(P.item_out,(P.px+3050,P.py-900))

def vigore_dam_p(P,temppx,temppy,move):
    #rects start
    genos = P.vigore_troy.y_dist()
    healer = P.vigore_healer.y_dist()
    victor = P.vigore_victor.y_dist()
    troy = P.vigore_troy.y_dist()
    if P.vigore_rocket:
        rocket = P.vigore_rocket.y_dist()
        if rocket > 0:
            P.vigore_rocket.move()
    if genos > 0:
        P.vigore_genos.move(rects = [(P.vigore_troy.x,P.vigore_troy.y)])
    if healer > 0:
        P.vigore_healer.move()
    if victor > 0:
        P.vigore_victor.move()
    if troy > 0:
        P.vigore_troy.move(rects = [(P.vigore_genos.x,P.vigore_genos.y)])
    if P.vigore_mane1:
        P.vigore_mane1.move()
        P.vigore_mane2.move()
        P.vigore_mane3.move()
    r1 = (P.px+1000,P.py-850,650,50)
    r2 = (P.px+900,P.py-1050,50,100)
    r3 = (P.px+950,P.py-950,50,100)
    r4 = (P.px+950,P.py-1350,50,290)
    r5 = (P.px+500,P.py-1350,450,50)
    r6 = (P.px+500,P.py-1450,1150,40)
    r7 = (P.px+450,P.py-1400,50,50)
    if P.prog[6][10] == 0:
        r7 = (P.px+450,P.py-1400,100,50)
    r8 = r1
    if P.py == 1375:
        r8 = (P.px+1000,P.py-1150,350,40)
    r9 = (P.px+1650,P.py-1400,50,90)
    r10 = (P.px+1650,P.py-1150,50,300)
    r11 = (P.px+1700,P.py-1350,1500,40)
    #r12 = (P.px+1700,P.py-1150,1450,50)
    r12 = (P.px+1700,P.py-1150,1500,50)
    r13 = (P.px+3200,P.py-1150,50,190)
    r14 = (P.px+3200,P.py-1550,50,240)
    r15 = (P.px+3250,P.py-1600,450,40)
    r16 = (P.px+3250,P.py-1000,250,90)
    r17 = (P.px+3700,P.py-1550,50,490)
    r18 = (P.px+3650,P.py-1000,50,700)
    r19 = (P.px+3700,P.py-1000,750,50)
    r190 = (P.px+4050,P.py-1150,50,40)
    r191 = (P.px+4100,P.py-1200,50,40)
    r192 = (P.px+4150,P.py-1250,300,40)
    r193 = (P.px+4450,P.py-1200,50,190)
    r20 = (P.px+3700,P.py-1100,350,40)
    r21 = r1
    if P.vigore_mane1:
        r21 = P.vigore_mane1.get_rect()

    r22 = (P.px+3450,P.py-900,50,440)
    if P.px >= -3075 and P.py >= 875:
        r22 = (P.px+3500,P.py-900,50,40)
    r23 = (P.px+3050,P.py-500,200,40)
    r231 = (P.px+3300,P.py-500,150,40)
    r232 = (P.px+3250,P.py-550,50,40)
    r24 = (P.px+3000,P.py-450,50,140)
    r25 = (P.px+3050,P.py-300,600,50)
    r26 = P.vigore_victor.get_rect()
    r27 = P.vigore_healer.get_rect()
    r28 = P.vigore_troy.get_rect()
    r29 = P.vigore_genos.get_rect()
    r295 = r1
    if P.vigore_rocket:
        r295 = P.vigore_rocket.get_rect()
    r30 = (P.px+3050,P.py-650,350,40)
    r31 = (P.px+3000,P.py-900,50,240)
    r32 = (P.px+3100,P.py-900,150,90)
    r33 = (P.px+3050,P.py-950,50,40)
    if P.prog[6][11] == 0:
        r33 = (P.px+3050,P.py-950,50,90)
    r34 = (P.px+3100,P.py-800,50,40)
    r35 = (P.px+3200,P.py-800,50,40)
    r36 = (P.px+3400,P.py-850,100,190)
    rects = [r193,r192,r191,r190,r295,r36,r35,r34,r33,r32,r31,r30,r232,r231,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        if P.prog[15][3] == 1 and P.vigore_mane1.x >= 4000 and P.px >= -3875:
            player_move(P,rects,manual_input = 'r',spd = 3)
        else:
            blit_player(P)
    if P.vigore_rocket:
        if rocket <= 0:
            P.vigore_rocket.move(temppx,temppy)
    if genos <= 0:
        P.vigore_genos.move(temppx,temppy,[(P.vigore_troy.x,P.vigore_troy.y)])
    if victor <= 0:
        P.vigore_victor.move(temppx,temppy)
    if troy <= 0:
        P.vigore_troy.move(temppx,temppy,[(P.vigore_genos.x,P.vigore_genos.y)])
    if healer <= 0:
        P.vigore_healer.move(temppx,temppy)

def vigore_dam_f(P,temppx,temppy,tim):
    draw_grass(P,temppx,temppy,-625,1675,650,100)
    draw_grass(P,temppx,temppy,-975,1425,300,300)
    draw_grass(P,temppx,temppy,-2875,1825,450,250)
    draw_grass(P,temppx,temppy,-2875,1425,250,150)
    P.surface.blit(P.cave_out_r,(temppx+900,temppy-1100))
    P.surface.blit(P.vigore_ppf,(temppx+3049,temppy-945))
    P.surface.blit(P.vigore_fl,(temppx+400,temppy-1458))
    P.surface.blit(P.vigore_fr,(temppx+3050,temppy-594))
    P.surface.blit(P.vigore_fence,(temppx+1697,temppy-1178))
    P.surface.blit(P.vigore_foam_1,(temppx+1845,temppy-780+abs(P.ocean)/2))
    P.surface.blit(P.vigore_foam_2,(temppx+1848,temppy-780+abs(P.f2)))
    P.surface.blit(P.vigore_foam_3,(temppx+1845,temppy-778+abs(P.f3)))
    if P.px == -2875 and P.py > 725 and P.py < 800:
        P.surface.blit(P.shadow_u,(P.px+3250,P.py-510))
    if P.px == -2775 and P.py > 1025 and P.py < 1100:
        P.surface.blit(P.shadow_u,(P.px+3150,P.py-810))
    set_sky(P)
    show_location(P, P.loc_txt, tim)

def vigore_dam(P) -> None:
    if P.song != "music/vigore.wav":
        P.song = "music/vigore.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.habitat = 'grass'
    P.vigore_healer = npc.NPC(P,'Healer','Joy',[1000,-1100],[['r',100]],["You look pretty exhausted.","Let me heal your Pokemon for","you."])
    P.vigore_pp2_door = load("p/egida/pp2_door.png")
    P.vigore = load("p/egida/Vigore_Dam.png")
    P.vigore_fl = load("p/egida/vigore_f_l.png")
    P.vigore_fr = load("p/egida/vigore_f_r.png")
    P.vigore_ppf = load("p/egida/vigore_ppf.png")
    P.vigore_fence = load("p/egida/vigore_fence.png")
    P.vigore_foam_1 = load("p/egida/vigore_foam_1.png")
    P.vigore_foam_2 = load("p/egida/vigore_foam_2.png")
    P.vigore_foam_3 = load("p/egida/vigore_foam_3.png")
    P.vigore_door = load("p/egida/pp_door.png")
    if P.prog[15][3] == 0:
        P.vigore_mane1 = npc.NPC(P,'Manectric','Grunt',[3850,-1050],[['l',20]],["","",""])
        P.vigore_mane2 = npc.NPC(P,'Manectric','Grunt',[4350,-1100],[['l',20]],["","",""])
        P.vigore_mane3 = npc.NPC(P,'Manectric','Grunt',[4250,-1150],[['d',20]],["","",""])
    else:
        P.vigore_mane1 = None
        P.vigore_mane2 = None
        P.vigore_mane3 = None
    P.vigore_rocket = None
    if P.prog[0] == 38:
        P.vigore_rocket = npc.NPC(P,'Team Rocketm','Grunt',[3250,-900],[['d',20]],["Ack! How did you know I was","hiding here?!!","","Ugh. Fine, you got me. But","just so you know, our boss","ain't gonna let this slide."])
    move = True
    wx = 0
    wy = 0
    fall = 0
    tim = 0
    P.f2 = 0
    P.f3 = 0
    set_location(P)
    vigore_dam_b(P,wx,wy,fall)
    vigore_dam_p(P,P.px,P.py,False)
    vigore_dam_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        vigore_dam_b(P,wx,wy,fall)
        #print(P.px,P.py)
        if move == True and P.vigore_victor.trainer_check():
            move = False
        if move == True and P.vigore_troy.trainer_check(rects = [(P.vigore_genos.bx,P.vigore_genos.by)]):
            move = False
        if move == True and P.vigore_genos.trainer_check(rects = [(P.vigore_troy.bx,P.vigore_troy.by)]):
            move = False
        temppx = P.px
        temppy = P.py
        P.ledge = 0
        if (P.px <= -625 and P.px >= -925):
            if P.py > 1400 and P.py < 1425:
                P.ledge = -((1425-P.py)/2)
            elif P.py > 1375 and P.py <= 1400:
                P.ledge = (1375-P.py)/2
        vigore_dam_p(P,temppx,temppy,move)
        vigore_dam_f(P,temppx,temppy,tim)
        if trainer_check(P,P.vigore_victor,"music/vigore.wav"):
            P.vigore_victor = npc.NPC(P,'Ace Trainerm','Victor',[P.vigore_victor.x,P.vigore_victor.y],[[P.vigore_victor.face(),100]],["There's an Electrike down that","trail that keeps snarling when","you approach him."])
            move = True
        if trainer_check(P,P.vigore_troy,"music/vigore.wav"):
            P.vigore_troy = npc.NPC(P,'Triathelete','Troy',[P.vigore_troy.x,P.vigore_troy.y],[['md',20],['mr',250],['mu',20],['ml',250]],["*Huff* *puff*","I can't...feel...my legs...","anymore..."],tim = P.vigore_troy.tim,curr = P.vigore_troy.curr,extra_walk = P.vigore_troy.extra_walk,spd = 1)
            move = True
        if trainer_check(P,P.vigore_genos,"music/vigore.wav"):
            P.vigore_genos = npc.NPC(P,'Expertm','Chuck',[P.vigore_genos.x,P.vigore_genos.y],[['mr',250],['mu',20],['ml',250],['md',20]],["No breaks allowed!","Stopping to rest is admitting","defeat!"],tim = P.vigore_genos.tim,curr = P.vigore_genos.curr,extra_walk = P.vigore_genos.extra_walk,spd = 1)
            move = True
        if (P.prog[15][3] == 1 and P.px == -3875) or (P.prog[15][3] == 2 and P.vigore_mane2.y == -1050 and P.vigore_mane2.face() == 'l') or (P.prog[15][3] == 3 and P.vigore_mane3.y == -1100 and P.vigore_mane2.face() == 'l'):
            te = P.surface.copy()
            txt(P,"The Manectric attacked!")
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Manectric' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Manectric',[26,0,334,'Spark',-1,'Quick Attack',-1,'Bite',-1,'Howl',-1,None,None,0,"Poke Ball",0,'Lightning Rod'])],no_pc = True)
            play_music(P,"music/vigore.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint':
                P.party[0].status = None
                P.party[0].ch = P.party[0].hp
                P.prog[15][3] = 0
                txt(P,"The Manectric look quite","disappointed and chase you","away!")
                fade_out(P)
                P.p = P.l1
                P.px = -3375
                P.py = 1325
                P.vigore_mane1 = npc.NPC(P,'Manectric','Grunt',[3850,-1050],[['l',20]],["","",""])
                P.vigore_mane2 = npc.NPC(P,'Manectric','Grunt',[4350,-1100],[['l',20]],["","",""])
                P.vigore_mane3 = npc.NPC(P,'Manectric','Grunt',[4250,-1150],[['d',20]],["","",""])
                vigore_dam_b(P,wx,wy,fall)
                vigore_dam_p(P,P.px,P.py,False)
                vigore_dam_f(P,P.px,P.py,tim)
                fade_in(P)
                move = True
            else:
                P.prog[15][3] += 1
                if P.prog[15][3] == 2:
                    P.vigore_mane1 = npc.NPC(P,'Manectric','Grunt',[P.vigore_mane1.x,P.vigore_mane1.y],[['mr',40],['l',500]],["","",""])
                    P.vigore_mane2 = npc.NPC(P,'Manectric','Grunt',[4350,-1100],[['ml',20],['md',20],['l',500]],["","",""])
                elif P.prog[15][3] == 3:
                    P.vigore_mane2 = npc.NPC(P,'Manectric','Grunt',[P.vigore_mane2.x,P.vigore_mane2.y],[['mr',20],['l',500]],["","",""])
                    P.vigore_mane3 = npc.NPC(P,'Manectric','Grunt',[4250,-1150],[['md',20],['d',500]],["","",""])
                    P.p = P.u1
                else:
                    txt(P,"The Manectric look pleased.","They leave a mysterious stone","with you before leaving.")
                    add_item(P,'Manectite',1)
                    fade_out(P)
                    P.vigore_mane1 = None
                    P.vigore_mane2 = None
                    P.vigore_mane3 = None
                    vigore_dam_b(P,wx,wy,fall)
                    vigore_dam_p(P,P.px,P.py,False)
                    vigore_dam_f(P,P.px,P.py,tim)
                    fade_in(P)
                    move = True
            P.party = P.temp_party.copy()
            P.legendary_battle = False
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                if (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.vigore_rocket and P.vigore_rocket.talk():
                        vigore_dam_b(P,wx,wy,fall)
                        vigore_dam_p(P,P.px,P.py,False)
                        vigore_dam_f(P,P.px,P.py,tim)
                        P.vigore_rocket.write()
                        P.prog[0] += 1
                        P.px = -775
                        P.py = 975
                        P.p = P.u1
                        P.loc = "egida"
                        end = False
                    if P.vigore_victor.talk():
                        if P.vigore_victor.trainer:
                            move = False
                        else:
                            vigore_dam_b(P,wx,wy,fall)
                            vigore_dam_p(P,P.px,P.py,False)
                            vigore_dam_f(P,P.px,P.py,tim)
                            P.vigore_victor.write()
                    elif next_to(P,500,-1400) and P.prog[6][10] == 0:
                        txt(P,P.save_data.name + " found a Common", "Candy!")
                        txt(P,P.save_data.name + " put the Common","Candy in the Medicine pocket.")
                        add_item(P,"Common Candy",1)
                        P.prog[6][10] = 1
                    elif next_to(P,3050,-900) and P.prog[6][11] == 0:
                        txt(P,P.save_data.name + " found a TM01","Work Up!")
                        txt(P,P.save_data.name + " put the TM01 in","the TMs pocket.")
                        add_item(P,"TM01 Work Up",1)
                        P.prog[6][11] = 1
                    elif P.px == -3425 and P.py == 1325 and face_r(P) and P.prog[15][3] == 0:
                        if P.prog[15][0] == 0:
                            txt(P,"The Manectric snarls when you","try to approach it.")
                            print_mega_area(P)
                        else:
                            txt(P,"The Manectric snarls when you","try to approach it.")
                            if in_party(P,'Manectric',True):
                                new_txt(P)
                                write(P,"Challenge the Manectric?")
                                if choice(P):
                                    move = False
                                    P.vigore_mane1 = npc.NPC(P,'Manectric','Grunt',[3850,-1050],[['mr',180],['l',1000]],["","",""])
                                    P.prog[15][3] += 1
                            else:
                                txt(P,"If you brought an Manectric it","would probably let you through.")
                    elif P.vigore_troy.talk():
                        if P.vigore_troy.trainer:
                            P.vigore_troy.extra_walk = ['u',0,0]
                            move = False
                        else:
                            vigore_dam_b(P,wx,wy,fall)
                            vigore_dam_p(P,P.px,P.py,False)
                            vigore_dam_f(P,P.px,P.py,tim)
                            P.vigore_troy.write()
                    elif P.vigore_genos.talk():
                        if P.vigore_genos.trainer:
                            P.vigore_genos.extra_walk = ['u',0,0]
                            move = False
                        else:
                            vigore_dam_b(P,wx,wy,fall)
                            vigore_dam_p(P,P.px,P.py,False)
                            vigore_dam_f(P,P.px,P.py,tim)
                            P.vigore_genos.write()
                    elif face_d(P) == False and P.vigore_healer.talk():
                        vigore_dam_b(P,wx,wy,fall)
                        vigore_dam_p(P,P.px,P.py,False)
                        vigore_dam_f(P,P.px,P.py,tim)
                        t = P.surface.copy()
                        P.vigore_healer.write()
                        fade_out(P)
                        P.clock.tick(1)
                        P.surface.blit(t,(0,0))
                        fade_in(P)
                        heal_party(P)
                        txt(P,"Feel free to come back if", "you're ever feeling tired!","")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 1275 or P.py == 1325) and P.px == -575 and face_l(P):
            P.px -= 600
            P.py += 600
            P.move_out_dir = 'l'
            P.loc = "echo_cave"
            end = False
        if P.px == -2875 and P.py == 775 and face_u(P):
            P.px = 75
            P.py = -125
            P.loc = "power_plant_1"
            end = False
        if P.px == -2775 and P.py == 1075 and face_u(P):
            P.px = 325
            P.py = 25
            P.loc = "power_plant_2"
            end = False
        if move and (wild_grass(P,-625,1675,650,100) or wild_grass(P,-975,1425,300,300) or wild_grass(P,-2875,1825,450,250) or wild_grass(P,-2875,1425,250,150)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < 0.07:
                battle(P,[poke.Poke('Magnemite',[random.randint(11,12),2,334,"Supersonic",-1,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,None,None,0,"Poke Ball"])])
            elif rando >= .07 and rando < .25:
                battle(P,[poke.Poke('Machop',[random.randint(9,11),random.randint(0,1),334,"Low Kick",-1,"Focus Energy",-1,"Karate Chop",-1,"Foresight",-1,None,None,0,"Poke Ball"])])
                # else:
                #     battle(P,[poke.Poke('Machop',[r,random.randint(0,1),334,"Pound",-1,"Focus Energy",-1,"Bide",-1,"Low Kick",-1,None,None,0,"Poke Ball"])])
            elif rando >= .25 and rando < .5:
                r = random.randint(8,11)
                if r < 10:
                    battle(P,[poke.Poke('Electrike',[r,random.randint(0,1),334,"Tackle",-1,"Thunder Wave",-1,"Leer",-1,"Howl",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Electrike',[r,random.randint(0,1),334,"Quick Attack",-1,"Thunder Wave",-1,"Leer",-1,"Howl",-1,None,None,0,"Poke Ball"])])
            elif rando >= .5 and rando < .75:
                r = random.randint(7,10)
                if r < 10:
                    battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Water Sport",-1,"Scratch",-1,"Tail Whip",-1,"Water Gun",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Psyduck',[r,random.randint(0,1),334,"Confusion",-1,"Scratch",-1,"Tail Whip",-1,"Water Gun",-1,None,None,0,"Poke Ball"])])
            elif rando >= .75 and rando < .85:
                battle(P,[poke.Poke('Togedemaru',[random.randint(10,11),random.randint(0,1),334,"Charge",-1,"Thunder Shock",-1,"Defense Curl",-1,"Rollout",-1,None,None,0,"Poke Ball"])])
            elif rando >= .85:
                r = random.randint(9,11)
                if r < 11:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Peck",-1,"Growl",-1,"Leer",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Peck",-1,"Fury Attack",-1,"Leer",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
            P.song = "music/vigore.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if P.f2 == 7:
            P.f2 = -7
        if P.f3 == 5:
            P.f3 = -5
        if tim%5 == 0:
            P.f2 += 1
            P.f3 += 1
            P.ocean += 1
        fall += 5
        if fall == 150:
            fall = 0
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)
    if P.loc == 'egida':
        P.clock.tick(.5)

def echo_cave_b(P,wx,wy):
    draw_waves(P,wx,wy)
    P.surface.blit(P.echo_cave,(P.px,P.py-2000))
    if P.prog[6][0] == 0:
        P.surface.blit(P.item_cave,(P.px+400,P.py-1000))
    if P.prog[6][1] == 0:
        P.surface.blit(P.item_cave,(P.px+600,P.py-1100))
    if P.prog[6][2] == 0:
        P.surface.blit(P.item_cave,(P.px+750,P.py-1000))
    if P.prog[6][3] == 0:
        P.surface.blit(P.item_cave,(P.px+400,P.py-1500))
    if P.prog[6][4] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+400,P.py-950))
    if P.prog[6][5] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+550,P.py-900))
    if P.prog[6][6] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+650,P.py-1050))
    if P.prog[6][7] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+500,P.py-1200))
    if P.prog[6][8] == 0:
        P.surface.blit(P.dwebble_rock,(P.px+400,P.py-1450))

def echo_cave_p(P,temppx,temppy,move):
    if P.echo_colress:
        P.echo_colress.move()
    vivi = P.echo_vivi.y_dist()
    carlos = P.echo_carlos.y_dist()
    if vivi > 0:
        P.echo_vivi.move()
    if carlos > 0:
        P.echo_carlos.move()
    if P.echo_man:
        P.echo_man.move()
    #rects start
    r1 = (P.px+350,P.py-1550,50,840)
    r2 = (P.px+350,P.py-1550,450,40)
    r3 = (P.px+400,P.py-750,150,90)
    r4 = (P.px+650,P.py-750,300,140)
    r5 = (P.px+450,P.py-650,50,240)
    r6 = (P.px+600,P.py-300,350,40)
    r61 = (P.px+500,P.py-350,100,40)
    r62 = (P.px+500,P.py-400,50,40)
    r7 = (P.px+800,P.py-1000,50,240)
    r71 = (P.px+750,P.py-1350,50,340)
    #maze
    if P.prog[0] < 26:
        r72 = (P.px+700,P.py-1000,50,140)
        r73 = (P.px+450,P.py-850,250,40)
        r74 = (P.px+650,P.py-1000,50,40)
        r75 = (P.px+450,P.py-1050,50,140)
        r76 = (P.px+550,P.py-1100,50,190)
        r77 = (P.px+400,P.py-1150,250,40)
        r78 = (P.px+650,P.py-1200,50,140)
        r79 = (P.px+500,P.py-1300,250,40)
        r711 = (P.px+450,P.py-1250,100,40)
        r712 = (P.px+500,P.py-1350,50,40)
    else:
        r72 = (P.px+500,P.py-800,50,40)
        r73 = (P.px+400,P.py-900,100,140)
        r74 = (P.px+700,P.py-950,100,40)
        r75 = (P.px+750,P.py-900,50,40)
        r76 = (P.px+700,P.py-850,100,40)
        r77 = (P.px+650,P.py-800,150,40)
        r78 = (P.px+650,P.py-1100,50,40)
        r79 = (P.px+700,P.py-1250,50,240)
        r711 = (P.px+450,P.py-1250,50,190)
        r712 = (P.px+400,P.py-1400,50,390)
    r713 = (P.px+450,P.py-1500,50,40)
    #items
    r00,r01,r02,r03,r04,r05,r06,r07,r08 = r1,r1,r1,r1,r1,r1,r1,r1,r1
    if P.prog[6][0] == 0:
        r00 = (P.px+400,P.py-1000,50,40)
    if P.prog[6][1] == 0:
        r01 = (P.px+600,P.py-1100,50,40)
    if P.prog[6][2] == 0:
        r02 = (P.px+750,P.py-1000,50,40)
    if P.prog[6][3] == 0:
        r03 = (P.px+400,P.py-1500,50,40)
    if P.prog[6][4] == 0:
        r04 = (P.px+400,P.py-950,50,40)
    if P.prog[6][5] == 0:
        r05 = (P.px+550,P.py-900,50,40)
    if P.prog[6][6] == 0:
        r06 = (P.px+650,P.py-1050,50,40)
    if P.prog[6][7] == 0:
        r07 = (P.px+500,P.py-1200,50,40)
    if P.prog[6][8] == 0:
        r08 = (P.px+400,P.py-1450,50,40)

    r8 = (P.px+1050,P.py-550,50,40)
    r81 = (P.px+1500,P.py-250,50,40)
    r9 = (P.px+950,P.py-410,10,90)
    r10 = (P.px+950,P.py-600,350,40)
    r100 = (P.px+1300,P.py-650,50,40)
    r101 = (P.px+1350,P.py-600,100,40)
    r11 = (P.px+800,P.py-1550,10,50)
    r12 = r1
    if P.px == -425:
        if P.py == 1750:
            r12 = (P.px+800,P.py-1500,50,15)
        elif P.py == 1700:
            r12 = (P.px+800,P.py-1375,50,15)
    if P.px == -475:
        if P.py == 1750:
            r12 = (P.px+850,P.py-1425,50,15)
        elif P.py == 1800:
            r12 = (P.px+850,P.py-1550,50,15)
    if P.px == -525:
        if P.py == 1800:
            r12 = (P.px+900,P.py-1475,50,15)
        elif P.py == 1850:
            r12 = (P.px+900,P.py-1600,50,15)
    if P.px == -575:
        if P.py == 1850:
            r12 = (P.px+950,P.py-1525,50,15)
        elif P.py == 1900:
            r12 = (P.px+950,P.py-1650,50,15)
        elif P.py == 800:
            r12 = (P.px+950,P.py-550,50,15)
        elif P.py == 750:
            r12 = (P.px+950,P.py-425,50,15)
    if P.px == -625:
        if P.py == 1825:
            r12 = (P.px+950,P.py-1525,50,15)
        elif P.py == 750:
            r12 = (P.px+1000,P.py-500,50,15)
        elif P.py == 700:
            r12 = (P.px+1000,P.py-375,50,15)
    r13 = (P.px+950,P.py-1700,50,15)
    r14 = (P.px+1000,P.py-1750,550,40)
    r15 = (P.px+1000,P.py-1500,550,40)
    r16 = (P.px+1550,P.py-1700,50,40)
    r17 = (P.px+1550,P.py-1550,50,40)
    r18 = (P.px+1040,P.py-550,10,50)
    r19 = (P.px+1000,P.py-350,50,140)
    r20 = (P.px+1550,P.py-450,50,190)
    r201 = (P.px+1500,P.py-550,50,90)
    r202 = (P.px+1450,P.py-550,50,40)
    r21 = (P.px+1050,P.py-200,150,90)
    r22 = (P.px+1300,P.py-200,250,90)
    r23 = (P.px+1000,P.py-100,50,490)
    r24 = (P.px+1450,P.py-100,50,490)
    r25 = (P.px+1050,P.py+400,150,40)
    r26 = (P.px+1300,P.py+400,150,40)
    r27 = (P.px+1200,P.py+450,100,40)
    r28 = (P.px+1600,P.py-1650,50,90)
    r29 = P.echo_vivi.get_rect()
    r30 = P.echo_carlos.get_rect()
    rects = [r100,r101,r00,r01,r02,r03,r04,r05,r06,r07,r08,r711,r712,r713,r76,r77,r78,r79,r71,r72,r73,r74,r75,r61,r62,r81,r201,r202,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    #rects end
    if move:
        if P.py < 1000:
            if P.px <= -625:
                if P.px == -925 and P.py == 875 and face_u(P):
                    player_move(P,rects,[],[Rect(P.px+950,P.py-550,100,200)],manual_input = 'd')
                else:
                    player_move(P,rects,[],[Rect(P.px+950,P.py-550,100,200)])
            else:
                player_move(P,rects,[],[Rect(P.px+950,P.py-550,100,190)])
        else:
            if P.px >= -425:
                player_move(P,rects,[Rect(P.px+800,P.py-1650,200,300)])
            else:
                player_move(P,rects,[Rect(P.px+800,P.py-1650,200,290)])
    else:
        blit_player(P)
    if carlos <= 0:
        P.echo_carlos.move(temppx,temppy)
    if vivi <= 0:
        P.echo_vivi.move(temppx,temppy)

def echo_cave_f(P,temppx,temppy,tim):
    P.surface.blit(P.cave_in_d,(temppx+1150,temppy+300))
    P.surface.blit(P.cave_in_r,(temppx+1400,temppy-1700))
    P.surface.blit(P.echo_iron,(temppx+1275,temppy-650))
    trans = pygame.Surface((800,600))
    trans.set_alpha(50)
    trans.fill((0,0,20))
    P.surface.blit(trans,(0,0))
    P.surface.blit(P.echo_ld,(temppx+1150,temppy+300))
    P.surface.blit(P.echo_lr,(temppx+1400,temppy-1700))
    show_location(P, P.loc_txt, tim)

def echo_cave(P) -> None:
    if P.song != "music/echoing_cave.wav":
        play_music(P,"music/echoing_cave.wav")
    P.echo_cave1 = load("p/egida/Echoing_Cave.png")
    P.echo_cave2 = load("p/egida/Echoing_Cave_update.png")
    P.echo_ld = load("p/egida/light_in_d.png")
    P.echo_lr = load("p/egida/light_in_r.png")
    P.echo_water = pygame.transform.scale(load("p/egida/manaphy_wave.png"),(1200,600))
    if P.prog[0] < 26:
        P.echo_cave = P.echo_cave1
    else:
        P.echo_cave = P.echo_cave2
    aron_in = False
    P.echo_iron = load("p/egida/iron_cave.png")
    P.habitat = 'cave'
    move = True
    P.echo_man = None
    water_y = 0
    if P.prog[0] == 22:
        P.echo_colress = npc.NPC(P,'Colress','',[1200,100],[['u',100]],["","",""],["","",""])
    else:
        P.echo_colress = None
    wx = 0
    wy = 0
    trans = pygame.Surface((800,600))
    a = 0
    set_location(P)
    tim = 0
    echo_cave_b(P,wx,wy)
    echo_cave_p(P,P.px,P.py,move)
    echo_cave_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        echo_cave_b(P,wx,wy)
        if move == True and P.echo_carlos.trainer_check():
            move = False
        if move == True and P.echo_vivi.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        echo_cave_p(P,temppx,temppy,move)
        echo_cave_f(P,temppx,temppy,tim)
        if P.prog[0] == -2 or P.prog[0] == -3:
            trans.set_alpha(a)
            trans.blit(P.echo_water,(0,0+water_y))
            trans.blit(P.echo_water,(0,-600+water_y))
            P.surface.blit(trans,(0,0))
        if trainer_check(P,P.echo_carlos,"music/echoing_cave.wav",font = pygame.font.SysFont("courier", 70, italic = True)):
            P.echo_carlos = npc.NPC(P,'Preschoolerb','Carlos',[P.echo_carlos.x,P.echo_carlos.y],[['mr',60],['md',40],['ml',60],['mu',40]],["This place is awesome!!!","I can yell as much as I want","and Mom won't get mad at me!"],tim = P.echo_carlos.tim,curr = P.echo_carlos.curr,extra_walk = P.echo_carlos.extra_walk,spd = 1)
            move = True
        if trainer_check(P,P.echo_vivi,"music/echoing_cave.wav"):
            P.echo_vivi = npc.NPC(P,'Ace Trainerf','Vivian',[P.echo_vivi.x,P.echo_vivi.y],[[P.echo_vivi.face(),100]],["Hehe, looks like I was the one","who got crushed...",""])
            move = True
        if P.prog[0] == -1 and P.echo_man.y == -1500 and P.echo_man.face() == 'd':
            P.prog[0] -= 1
            P.font = pygame.font.SysFont("courier", 40, bold = False, italic = True)
            txt(P,"MANA-PHY!!!!!")
            P.font = pygame.font.SysFont("courier", 40, bold = True, italic = False)
        if P.py == 25 and P.prog[0] == 22:
            if P.echo_colress.x_dist() >= 50:
                P.echo_colress = npc.NPC(P,'Colress','',[1200,100],[['mr',abs(P.echo_colress.x_dist())*2/5],['md',100],['d',10]],[],[])
            elif P.echo_colress.x_dist() < 50:
                P.echo_colress = npc.NPC(P,'Colress','',[1200,100],[['ml',abs(P.echo_colress.x_dist())*2/5],['md',100],['d',10]],[],[])
            P.prog[0] += 1
            move = False
        if P.prog[0] == 23 and P.echo_colress.y_dist() == 50:
            txt(P,'Hmm?','You look like a new adventurer.')
            txt(P,"I don't know if you noticed,",'but the lift in Egida City had','its power cut off.')
            txt(P,"I'm heading over to the Power","Plant right now to check what", "happened.")
            txt(P,"Perhaps you'd like to come","along? You never know what","could happen.")
            txt(P,"Well, I'll be on my way.")
            P.echo_colress = npc.NPC(P,'Colress','',[P.echo_colress.x,P.echo_colress.y],[['mu',140]],[],[])
            P.prog[0] += 1
        if P.prog[0] == 24 and P.echo_colress.y == -150:
            P.echo_colress = None
            move = True
            P.prog[0] += 1
        if P.prog[0] == 25 and P.py >= 1675 and P.px == -375:
            P.p = P.l1
            echo_cave_b(P,wx,wy)
            echo_cave_p(P,P.px,P.py,False)
            echo_cave_f(P,P.px,P.py,tim)
            P.prog[0] = -1
            P.echo_man = npc.NPC(P,'Manaphy','one',[600,-1000],[['mu',200],['d',300]],["","",""],["","",""])
            move = False
        if P.px == -925 and P.py == 875 and face_u(P):
            if P.prog[15][0] == 0:
                txt(P,"The cave entrance is crowded","with Aron.")
                print_mega_area(P)
            elif P.prog[15][2] == 0:
                txt(P,"The cave entrance is crowded","with Aron.")
                if in_party(P,'Aggron',True):
                    new_txt(P)
                    write(P,"Enter the cave?")
                    if choice(P):
                        aron_in = True
                else:
                    txt(P,"If you brought an Aggron you","could probably enter the cave","safely.")
            else:
                aron_in = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if next_to(P,400,-1000) and P.prog[6][0] == 0:
                        item_fight(P,"music/echoing_cave.wav",0,8,('Explosion',None,None,None),'Voltorb')
                    elif next_to(P,600,-1100) and P.prog[6][1] == 0:
                        item_fight(P,"music/echoing_cave.wav",1,8,('Explosion',None,None,None),'Voltorb')
                    elif next_to(P,750,-1000) and P.prog[6][2] == 0:
                        item_fight(P,"music/echoing_cave.wav",2,8,('Explosion',None,None,None),'Voltorb')
                    elif next_to(P,400,-1500) and P.prog[6][3] == 0:
                        txt(P,P.save_data.name + " found a Ground Gem!")
                        txt(P,P.save_data.name + " put the Ground Gem","in the Items pocket.")
                        add_item(P,"Ground Gem",1)
                        P.prog[6][3] = 1
                    elif next_to(P,400,-950) and P.prog[6][4] == 0:
                        item_fight(P,"music/echoing_cave.wav",4,7,('Fury Cutter','Rock Blast','Withdraw',None),'Dwebble','The rock started to move!')
                    elif next_to(P,550,-900) and P.prog[6][5] == 0:
                        item_fight(P,"music/echoing_cave.wav",5,7,('Fury Cutter','Rock Blast','Withdraw',None),'Dwebble','The rock started to move!')
                    elif next_to(P,650,-1050) and P.prog[6][6] == 0:
                        item_fight(P,"music/echoing_cave.wav",6,7,('Fury Cutter','Rock Blast','Withdraw',None),'Dwebble','The rock started to move!')
                    elif next_to(P,500,-1200) and P.prog[6][7] == 0:
                        item_fight(P,"music/echoing_cave.wav",7,7,('Fury Cutter','Rock Blast','Withdraw',None),'Dwebble','The rock started to move!')
                    elif next_to(P,400,-1450) and P.prog[6][8] == 0:
                        item_fight(P,"music/echoing_cave.wav",8,10,('Fury Cutter','Rock Blast','Withdraw',None),'Dwebble','The rock started to move!')
                    elif P.px == -675 and P.py <= 375 and face_l(P):
                        txt(P,"You could probably fish here","if you had a fishing rod.")
                    elif P.px == -675 and P.py == 375 and face_u(P):
                        txt(P,"It's a fishing sign.")
                    elif P.echo_carlos.talk():
                        if P.echo_carlos.trainer:
                            move = False
                        else:
                            echo_cave_b(P,wx,wy)
                            echo_cave_p(P,P.px,P.py,False)
                            echo_cave_f(P,P.px,P.py,tim)
                            P.echo_carlos.write()
                    elif P.echo_vivi.talk():
                        if P.echo_vivi.trainer:
                            move = False
                        else:
                            echo_cave_b(P,wx,wy)
                            echo_cave_p(P,P.px,P.py,False)
                            echo_cave_f(P,P.px,P.py,tim)
                            P.echo_vivi.write()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 1925 or P.py == 1875) and P.px == -1175 and face_r(P):
            P.px += 600
            P.py -= 600
            P.move_out_dir = 'r'
            P.loc = "vigore"
            end = False
        if (P.px == -825 or P.px == -875) and P.py == -125 and face_d(P):
            P.px += 400
            P.py += 2050
            P.move_out_dir = 'd'
            P.loc = "route_2"
            end = False
        if move and wild_grass(P,0,0,0,0,0.7,all = True):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < .1:
                battle(P,[poke.Poke('Noibat',[random.randint(9,10),random.randint(0,1),334,"Screech",-1,"Supersonic",-1,"Absorb",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
            elif rando >= .1 and rando < .35:
                battle(P,[poke.Poke('Aron',[random.randint(7,9),random.randint(0,1),334,"Tackle",-1,"Harden",-1,"Mud-Slap",-1,"Headbutt",-1,None,None,0,"Poke Ball"])])
            elif rando >= .35 and rando < .63:
                r = random.randint(6,9)
                if r < 8:
                    battle(P,[poke.Poke('Whismur',[r,random.randint(0,1),334,"Pound",-1,"Echoed Voice",-1,None,None,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Whismur',[r,random.randint(0,1),334,"Pound",-1,"Echoed Voice",-1,"Astonish",-1,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .63 and rando < .93:
                r = random.randint(6,8)
                if r < 7:
                    battle(P,[poke.Poke('Zubat',[r,random.randint(0,1),334,"Absorb",-1,"Supersonic",-1,None,None,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Zubat',[r,random.randint(0,1),334,"Absorb",-1,"Supersonic",-1,"Astonish",-1,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .93:
                battle(P,[poke.Poke('Dunsparce',[random.randint(8,9),random.randint(0,1),334,"Defense Curl",-1,"Rollout",-1,"Spite",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
            play_music(P,"music/echoing_cave.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
        if P.prog[0] == -2 or P.prog[0] == -3:
            if a == -9:
                P.prog[0] = 26
                move = True
            if a == 330:
                P.prog[0] -= 1
                P.echo_cave = P.echo_cave2
                P.echo_man = None
            if P.prog[0] == -2:
                a += 2
            else:
                a -= 3
            water_y += 15
            if water_y == 600:
                water_y = 0
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%3 == 0:
            wx += 1
        if tim%7 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%7 == 0:
            P.ocean += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,P.song)

def route_2_b(P):
    P.surface.blit(P.route_2,(P.px+50,P.py-2000))

def route_2_p(P,temppx,temppy,move = False):
    #rect start
    ayla = P.r2_ayla.y_dist()
    robby = P.r2_robby.y_dist()
    if robby > 0:
        P.r2_robby.move()
    if ayla > 0:
        P.r2_ayla.move()
        draw_grass(P,P.r2_ayla.x,P.r2_ayla.y,-525,1425,200,200,[P.px,P.py])
        draw_grass(P,P.r2_ayla.x,P.r2_ayla.y,-525,1425,200,200,[P.px,P.py])
    tree1 = P.r2_tree1.y_dist() > 0
    if tree1:
        P.r2_tree1.blit()
    r1 = (P.px+900,P.py-950,800,40)
    r2 = (P.px+850,P.py-1150,50,190)
    r3 = (P.px+1200,P.py-1200,500,90)
    r4 = (P.px+650,P.py-1200,450,40)
    r5 = (P.px+600,P.py-1600,50,390)
    r6 = (P.px+1250,P.py-1600,50,390)
    r7 = (P.px+650,P.py-1650,150,40)
    r8 = (P.px+900,P.py-1650,350,40)
    r9 = (P.px+800,P.py-1700,100,40)
    r10 = P.r2_ayla.get_rect()
    r11 = P.r2_robby.get_rect()
    r12 = P.r2_tree1.get_rect()
    rects = [r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect end
    if (P.py <= 875 and P.py >= 725):
        if P.px > -1575 and P.px < -1550:
            P.ledge = -((1575+P.px)/1.5)
        elif P.px > -1550 and P.px < -1525 and P.ledge < 0:
            P.ledge = (1525+P.px)/1.5
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    draw_grass(P,temppx,temppy,-525,1425,200,200)
    draw_grass(P,temppx,temppy,-425,1625,300,150)
    draw_grass(P,temppx,temppy,-275,1875,150,150)
    draw_grass(P,temppx,temppy,-525,1875,300,150)
    if not tree1:
        P.r2_tree1.blit(temppx,temppy)
    if robby <= 0:
        P.r2_robby.move(temppx,temppy)
    if ayla <= 0:
        P.r2_ayla.move(temppx,temppy)
        draw_grass(P,P.r2_ayla.x,P.r2_ayla.y,-525,1425,200,200,[temppx,temppy])
        draw_grass(P,P.r2_ayla.x,P.r2_ayla.y,-525,1425,200,200,[temppx,temppy])

def route_2_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.r2_f,(temppx+650,temppy-1257))
    P.surface.blit(P.cave_out_u,(temppx+800,temppy-1700))
    if int(tim/3)%2 == 0:
        P.surface.blit(P.egi_gen,(temppx+1625,temppy-1353))
    draw_lamps(P,temppx,temppy,listx,listy,bf = 'b')
    draw_lamps(P,temppx,temppy,listx,listy)
    show_location(P,P.loc_txt,tim)

def route_2(P,enter = False) -> None:
    if P.song != "music/route_2.wav":
        P.song = "music/route_2.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.r2_tree1 = cut_tree(P,1200,-1600,16)
    tim = 0
    P.habitat = 'grass'
    listx = [1915]
    listy = [-1250]
    set_location(P)
    if enter == False:
        route_2_b(P)
        route_2_p(P,P.px,P.py)
        route_2_f(P,P.px,P.py,listx,listy,tim)
        fade_in(P)
    end = True
    move = True
    pause = False
    m = 0
    tim = 0
    fade = False
    while end:
        #print(P.px,P.py)
        route_2_b(P)
        if move == True and P.r2_ayla.trainer_check():
            move = False
        if move == True and P.r2_robby.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        route_2_p(P,temppx,temppy,move)
        route_2_f(P,temppx,temppy,listx,listy,tim)
        if trainer_check(P,P.r2_ayla,"music/route_2.wav"):
            P.r2_ayla = npc.NPC(P,'Battle Girl','Ayla',[P.r2_ayla.x,P.r2_ayla.y],[['d',40],['r',20],['l',20],['md',20],['u',40],['r',20],['l',20],['mu',20]],["I'm gonna beat the next","trainer I see as part of my","training!","Not you of course!","",""],tim = P.r2_ayla.tim,curr = P.r2_ayla.curr,extra_walk = P.r2_ayla.extra_walk)
            move = True
        if trainer_check(P,P.r2_robby,"music/route_2.wav"):
            P.r2_robby = npc.NPC(P,'Hiker','Robby',[P.r2_robby.x,P.r2_robby.y],[['mr',140],['ml',140]],["Heh.", "I've never actually gone into", "the caves.","I'm too scared of the creepy","sounds you hear just standing", "at the entrance..."],tim = P.r2_robby.tim,curr = P.r2_robby.curr,extra_walk = P.r2_robby.extra_walk)
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.r2_ayla.talk():
                        if P.r2_ayla.trainer:
                            move = False
                        else:
                            route_2_b(P)
                            route_2_p(P,P.px,P.py,False)
                            route_2_f(P,P.px,P.py,listx,listy,tim)
                            P.r2_ayla.write()
                    elif next_to(P,P.r2_tree1.x,P.r2_tree1.y):
                        P.r2_tree1.cut()
                    elif P.r2_robby.talk():
                        if P.r2_robby.trainer:
                            move = False
                        else:
                            route_2_b(P)
                            route_2_p(P,P.px,P.py,False)
                            route_2_f(P,P.px,P.py,listx,listy,tim)
                            P.r2_robby.write()
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.px == -425 or P.px == -475) and P.py == 1925 and face_u(P):
            P.px -= 400
            P.py -= 2050
            P.move_out_dir = 'u'
            P.loc = "echo_cave"
            #manaphy skip
            if P.prog[3] <= 4:
                P.prog[3] = 5
            fade = True
            end = False
        if (P.py == 1275 or P.py == 1375 or P.py == 1325) and P.px <= -1225 and face_r(P):
            P.px += 1200
            P.py -= 400
            P.loc = "egida"
            egida(P,True)
            end = False
        if move and (wild_grass(P,-525,1425,200,200) or wild_grass(P,-425,1625,300,150) or wild_grass(P,-275,1875,150,150) or wild_grass(P,-525,1875,300,150)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < .15:
                r = random.randint(6,8)
                if r < 8:
                    battle(P,[poke.Poke('Weedle',[r,random.randint(0,1),334,"Poison Sting",-1,"String Shot",-1,None,None,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Kakuna',[r,random.randint(0,1),334,"Poison Sting",-1,"Harden",-1,"String Shot",-1,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .15 and rando < .4:
                r = random.randint(5,7)
                if random.randint(0,1) == 0:
                    if r < 7:
                        battle(P,[poke.Poke('Nidoran_M',[r,0,334,"Leer",-1,"Peck",-1,None,None,None,None,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Nidoran_M',[r,0,334,"Leer",-1,"Peck",-1,"Focus Energy",-1,None,None,None,None,0,"Poke Ball"])])
                else:
                    if r < 7:
                        battle(P,[poke.Poke('Nidoran_F',[r,1,334,"Growl",-1,"Scratch",-1,None,None,None,None,None,None,0,"Poke Ball"])])
                    else:
                        battle(P,[poke.Poke('Nidoran_F',[r,1,334,"Growl",-1,"Scratch",-1,"Tail Whip",-1,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .4 and rando < .55:
                r = random.randint(5,7)
                if r < 7:
                    battle(P,[poke.Poke('Machop',[r,random.randint(0,1),334,"Low Kick",-1,"Leer",-1,"Focus Energy",-1,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Machop',[r,random.randint(0,1),334,"Low Kick",-1,"Leer",-1,"Focus Energy",-1,"Karate Chop",-1,None,None,0,"Poke Ball"])])
            elif rando >= .55 and rando < .75:
                battle(P,[poke.Poke('Pidgey',[random.randint(5,7),random.randint(0,1),334,"Tackle",-1,"Sand Attack",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .75 and rando < .9:
                r = random.randint(6,8)
                if r < 8:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Peck",-1,"Growl",-1,"Leer",-1,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Spearow',[r,random.randint(0,1),334,"Peck",-1,"Growl",-1,"Leer",-1,"Pursuit",-1,None,None,0,"Poke Ball"])])
            elif rando >= .9:
                r = random.randint(6,8)
                if r < 7:
                    battle(P,[poke.Poke('Skitty',[r,random.randint(0,1),334,"Fake Out",-1,"Foresight",-1,"Growl",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Skitty',[r,random.randint(0,1),334,"Fake Out",-1,"Foresight",-1,"Sing",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
            P.song = "music/route_2.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
        if pause:
            P.clock.tick(P.ani_spd/30)
            pause = False
    if fade:
        fade_out(P,P.song)

def egida_gym_b_b(P,cam_mod = 0):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_gymb_back,(P.px,P.py+cam_mod))

def egida_gym_b_p(P,temppx,temppy,move,cam_mod = 0):
    if P.egi_gymb_steven:
        steve = P.egi_gymb_steven.y_dist()
        if steve > 0:
            P.egi_gymb_steven.move()
    if P.egi_gymb_colress:
        colress = P.egi_gymb_colress.y_dist()
        if colress > 0:
            P.egi_gymb_colress.move(cam_mod = cam_mod)
    #rects start
    r1 = (P.px+50,P.py+50,150,40)
    r2 = (P.px+100,P.py+1000,250,40)
    r3 = (P.px+50,P.py+550,50,440)
    r4 = (P.px+350,P.py+550,50,440)
    r5 = (P.px+400,P.py+550,50,40)
    r6 = (P.px,P.py+550,50,40)
    r7 = (P.px-50,P.py+300,50,240)
    r8 = (P.px+450,P.py+300,50,240)
    r9 = (P.px+50,P.py+100,50,340)
    r10 = (P.px+350,P.py+100,50,340)
    r11 = (P.px,P.py+250,50,40)
    r12 = (P.px+400,P.py+250,50,40)
    r13 = (P.px+100,P.py+400,100,40)
    r14 = (P.px+250,P.py+400,100,40)
    r15 = (P.px+250,P.py+50,150,40)
    r16 = (P.px+200,P.py,50,40)
    r17 = r1
    r18 = r1
    if P.px == 225 or P.px == 125:
        r17 = (P.px+200,P.py+450,50,40)
    if P.px == 175:
        r17 = (P.px+250,P.py+450,50,40)
        r18 = (P.px+150,P.py+450,50,40)
    r19 = r1
    r20 = r1
    if P.egi_gymb_steven:
        r19 = P.egi_gymb_steven.get_rect()
    if P.egi_gymb_colress:
        r20 = P.egi_gymb_colress.get_rect()
    rects = [r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        if P.prog[0] == 41 and P.py < -575:
            player_move(P,rects,manual_input = 'u',spd = 3)
        elif P.prog[0] == 45 and P.py > -125:
            player_move(P,rects,manual_input = 'd',spd = 3)
        else:
            player_move(P,rects,mod = cam_mod)
    else:
        blit_player(P,mod = cam_mod)
    if P.egi_gymb_steven:
        if steve <= 0:
            P.egi_gymb_steven.move(temppx,temppy)
    # if P.egi_gymb_colress:
    #     if colress <= 0:
    #         P.egi_gymb_colress.move(temppx,temppy)

def egida_gym_b_f(P,temppx,temppy,tim,cam_mod = 0):
    show_location(P, P.loc_txt, tim)

def egida_gym_b(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.egi_gymb_back = load("p/egida/Egida_Gym_Back.png")
    P.egi_gymb_steven = None
    P.egi_gymb_colress = None
    if P.prog[0] == 41:
        P.egi_gymb_steven = npc.NPC(P,'Steven','',[200,700],[['d',40]],["","",""])
    if P.prog[0] <= 47:
        P.egi_gymb_colress = npc.NPC(P,'Colress','',[200,50],[['d',40]],["","",""])
    P.habitat = 'indoor'
    move = True
    cam_mod = 0
    tim = 0
    set_location(P)
    egida_gym_b_b(P)
    egida_gym_b_p(P,P.px,P.py,False)
    egida_gym_b_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        # print(P.px,P.py)
        if P.prog[0] == 41 and P.py == -575:
            P.egi_gymb_steven = npc.NPC(P,'Steven','',[200,700],[['d',20],['md',40],['d',40]],["","",""])
            move = False
            P.prog[0] += 1
        if P.prog[0] == 42 and P.egi_gymb_steven.y == 800:
            te = P.surface.copy()
            txt(P,'Are you the challenger Colress','is expecting? He had some good','things to say about you.')
            txt(P,"I'm Steven. Pleased to make",'your acquaintance. I came to', 'discuss something with Colress.')
            txt(P,'On a second thought, would you','mind humoring me with a quick', 'battle?')
            txt(P,"I'm curious as to why Colress",'sees so much potential in a','trainer like you.')
            play_music(P,"music/steven_battle.wav",0)
            battle(P,["Steven",poke.Poke('Metang',[20,2,334,"Take Down",-1,"Confusion",-1,"Metal Claw",-1,"Magnet Rise",-1,None,None,0,"Poke Ball",0,'Clear Body'])])
            play_music(P,"music/gym.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            P.prog[0] += 1
            txt(P,"Hmm...very impressive. I'm","excited to see how you develop","as a trainer.")
            txt(P,"Well I'll be on my way. Good","luck with your challenge!")
            P.egi_gymb_steven = npc.NPC(P,'Steven','',[200,800],[['mr',20],['md',40],['ml',20],['md',40]],["","",""])
        if P.prog[0] == 43 and P.egi_gymb_steven.y == 950:
            P.egi_gymb_steven = None
            move = True
            P.prog[0] += 1
        if P.prog[0] == 45 and P.py == -125:
            P.p = P.u1
            P.prog[0] += 1
            move = False
        egida_gym_b_b(P,cam_mod)
        temppx = P.px
        temppy = P.py
        egida_gym_b_p(P,temppx,temppy,move,cam_mod)
        egida_gym_b_f(P,temppx,temppy,tim,cam_mod)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 175 and P.py == 175 and face_u(P):
                        if P.prog[0] == 44:
                            txt(P,"Ah, you finally made it!","Seeing your fight earlier made","me eager to test your skills.")
                            txt(P,"Go ahead and get ready on the","other side of the arena.","")
                            P.prog[0] += 1
                        elif P.prog[0] == 47:
                            txt(P,"Apparently it's some sort of","unnatural occurence that's","causing problems for Pianura.")
                            txt(P,"I'd love to see what's going","on, but I have my own matters","to attend to here in Egida.")
                            txt(P,"Don't forget to visit the lab","every now and then. I'd love","to teach you a few things.")
                    elif P.py == -25 and P.px in [375,-25] and face_u(P):
                        txt(P,"It's a statue with a colorful","orb on the top.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 175 and P.py == -675 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = -75
            P.py = 225
            P.loc = "egi_gym"
            end = False
        if P.prog[0] == 46:
            if cam_mod == 150:
                t = P.surface.copy()
                txt(P,"A truly strong trainer can","discern any opponent's tactic","and counter it.")
                txt(P,"If you haven't adequetely","prepared I'm afraid I'll have","to hand you a defeat!")
                play_music(P,"music/colress_battle.wav",0)
                #battle(P,["Leader Colress",poke.Poke('Magnemite',[15,0,334,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,"Light Screen",-1,None,None,0,"Poke Ball",0,'Magnet Pull']),poke.Poke('Mega_Mawile',[15,0,334,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,"Light Screen",-1,None,None,0,"Poke Ball",0,'Magnet Pull'])])
                battle(P,["Leader Colress",poke.Poke('Magnemite',[15,2,334,"Thunder Shock",-1,"Thunder Wave",-1,"Gyro Ball",-1,"Light Screen",-1,None,None,0,"Poke Ball",0,'Magnet Pull']),poke.Poke('Klink',[15,2,334,"Vice Grip",-1,"Charge",-1,"Thunder Shock",-1,None,None,None,None,0,"Poke Ball",0,'Plus']),poke.Poke('Ferroseed',[15,0,334,"Harden",-1,"Rollout",-1,"Curse",-1,"Gyro Ball",-1,None,None,0,"Poke Ball",0,'Iron Barbs']),poke.Poke('Mega_Mawile',[15,0,334,"Taunt",-1,"Fairy Wind",-1,"Bite",-1,"Astonish",-1,None,None,0,"Premier Ball",0,'Huge Power'])])
                play_music(P,"music/gym.wav")
                P.surface.blit(t,(0,0))
                fade_in(P)
                txt(P,"Well it certainly appears that","my analysis of your potential","was on point!")
                txt(P,"I'm honored to award you the","Analytic Badge! Your Pokemon","can now reach level 25.")
                txt(P,"Take this TM74 Gyro Ball.","You can use it to teach your","Pokemon Gyro Ball.")
                txt(P,"It's a steel type attack that","becomes stronger the slower","you are than your opponent.")
                txt(P,"On another note, a pretty big","issue has sprung up around","Pianura City.")
                txt(P,"If you don't mind, I'd like","you to head over there to lend","a hand.")
                txt(P,"There is another gym located","there, so it would be well","worth your time.")
                txt(P,"You can get there by following","Route 3. I'll inform the city","security to grant you access.")
                txt(P,"Oh, and if you ever have time,","feel free to stop by my lab.","I could really use your help.")
                txt(P,"Anyways, I hope our battle","helped you grow as a trainer.","I'll let you be on your way.")
                add_item(P,"TM74 Gyro Ball",1)
                P.prog[0] = -4
            else:
                cam_mod += 2
        if P.prog[0] == -4:
            cam_mod -= 2
            if cam_mod == 0:
                move = True
                P.prog[0] = 47
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def egida_gym_l_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_gyml_back,(P.px,P.py))

def egida_gym_l_p(P,temppx,temppy,move):
    sci = P.egi_gyml_sci.y_dist()
    if sci > 0:
        P.egi_gyml_sci.move()
    #rects start
    r1 = (P.px,P.py+100,350,40)
    r2 = (P.px-50,P.py+150,50,340)
    r3 = (P.px+350,P.py+150,50,340)
    r4 = (P.px,P.py+500,350,40)
    r5 = (P.px,P.py+250,150,90)
    r6 = (P.px+200,P.py+250,150,90)
    r8 = P.egi_gyml_sci.get_rect()
    rects = [r8,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if sci <= 0:
        P.egi_gyml_sci.move(temppx,temppy)

def egida_gym_l_f(P,temppx,temppy,tim):
    P.surface.blit(P.egi_gyml_f,(temppx,temppy+220))
    show_location(P, P.loc_txt, tim)

def egida_gym_l(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.egi_gyml_back = load("p/egida/Egida_Gym_Left.png")
    P.egi_gyml_f = load("p/egida/egida_Gym_lf.png")
    move = True
    tim = 0
    P.habitat = 'indoor'
    set_location(P)
    egida_gym_l_b(P)
    egida_gym_l_p(P,P.px,P.py,False)
    egida_gym_l_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        egida_gym_l_b(P)
        # print(P.px,P.py)
        if move == True and P.egi_gyml_sci.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        egida_gym_l_p(P,temppx,temppy,move)
        egida_gym_l_f(P,temppx,temppy,tim)
        if trainer_check(P,P.egi_gyml_sci,"music/gym.wav"):
            P.egi_gyml_sci = npc.NPC(P,'Scientistf','Bob',[50,350],[['u',20]],["Very sorry about that. I'm","usually not so clumsy.",""])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.egi_gyml_sci.talk():
                        if P.egi_gyml_sci.trainer:
                            move = False
                        else:
                            egida_gym_l_b(P)
                            egida_gym_l_p(P,P.px,P.py,False)
                            egida_gym_l_f(P,P.px,P.py,tim)
                            P.egi_gyml_sci.write()
                    elif P.px == 225 and P.py == 125 and face_u(P):
                        if P.prog[0] == 40:
                            new_txt(P)
                            write(P,"There's a controller inside","with a single button. Push it?")
                            if choice(P,550,600) == True:
                                txt(P,"*BEEP*")
                                P.prog[0] += 1
                        else:
                            txt(P,"The controller in the trash","can doesn't seem to be of use","anymore.")
                    elif P.py in [125,-75] and P.px in [375,325,275,175,125,75] and face_u(P):
                        txt(P,"The file cabinet is locked","shut.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 225 and P.py == -175 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = 225
            P.py = -25
            P.loc = "egi_gym"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def egida_gym_r_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_gymr_back,(P.px,P.py))

def egida_gym_r_p(P,temppx,temppy,move):
    sci = P.egi_gymr_sci.y_dist()
    if sci > 0:
        P.egi_gymr_sci.move()
    #rects start
    r1 = (P.px,P.py+50,350,40)
    r2 = (P.px-50,P.py+100,50,390)
    r3 = (P.px+350,P.py+100,50,390)
    r4 = (P.px,P.py+500,350,40)
    r5 = (P.px+50,P.py+200,50,40)
    r6 = (P.px+250,P.py+200,50,40)
    r7 = (P.px+50,P.py+350,50,40)
    r8 = (P.px+250,P.py+350,50,40)
    r30 = P.egi_gymr_sci.get_rect()
    rects = [r30,r4,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if sci <= 0:
        P.egi_gymr_sci.move(temppx,temppy)

def egida_gym_r_f(P,temppx,temppy,tim):
    P.surface.blit(P.egi_gymr_f,(temppx+50,temppy+155))
    show_location(P, P.loc_txt, tim)

def egida_gym_r(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.egi_gymr_back = load("p/egida/Egida_Gym_Right.png")
    P.egi_gymr_f = load("p/egida/egida_gym_rf.png")
    move = True
    if P.prog[8][0][0] != -1:
        P.egi_gymr_sci = npc.NPC(P,'Scientistm','George',[150,300],[['d',20]],["Oh! You started working at the","Egida Lab? I have a tip that", "may help you out!","If you start out with a lens","that is both strong and weak","against many types, you can","rule out more options and","narrow it down from there!",""])
    P.habitat = 'indoor'
    tim = 0
    set_location(P)
    egida_gym_r_b(P)
    egida_gym_r_p(P,P.px,P.py,False)
    egida_gym_r_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        egida_gym_r_b(P)
        if move == True and P.egi_gymr_sci.trainer_check():
            move = False
        # print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        egida_gym_r_p(P,temppx,temppy,move)
        egida_gym_r_f(P,temppx,temppy,tim)
        if trainer_check(P,P.egi_gymr_sci,"music/gym.wav"):
            P.egi_gymr_sci = npc.NPC(P,'Scientistm','Ross',[150,300],[['d',20]],["Let me know if you ever want","to dabble in research. I would", "love to give you some tips."])
            move = True
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.egi_gymr_sci.talk():
                        if P.egi_gymr_sci.trainer:
                            move = False
                        else:
                            egida_gym_r_b(P)
                            egida_gym_r_p(P,P.px,P.py,False)
                            egida_gym_r_f(P,P.px,P.py,tim)
                            P.egi_gymr_sci.write()
                    elif next_to(P,50,350) or next_to(P,250,350) or next_to(P,50,200) or next_to(P,250,200):
                        txt(P,"There's a fossil on display.")
                    elif P.py == 175 and face_u(P):
                        txt(P,"The wall is lined with various","patents.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == 225 and P.py == -175 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = -375
            P.py = -25
            P.loc = "egi_gym"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def egida_gym_main_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_gym_mdoor,(P.px+440,P.py+31))
    doormod = 50
    if P.py > 175:
        doormod = 225-P.py
    P.surface.blit(P.egi_gym_ldoor,(P.px+390+doormod,P.py+31))
    P.surface.blit(P.egi_gym_rdoor,(P.px+525-doormod,P.py+31))
    P.surface.blit(P.egi_gym_back,(P.px,P.py))
    if P.px == 225 and P.py > -75:
        P.surface.blit(P.egi_gym_black,(P.px+151,P.py+285))
    if P.px == -375 and P.py > -75:
        P.surface.blit(P.egi_gym_black,(P.px+751,P.py+285))

def egida_gym_main_p(P,temppx,temppy,move):
    #rects start
    guide = P.egi_gym_guide.y_dist() > 0
    if guide:
        P.egi_gym_guide.move()
    r1 = (P.px+350,P.py+50,100,40)
    r2 = (P.px+300,P.py+100,50,240)
    r3 = (P.px+600,P.py+100,50,240)
    r4 = (P.px+500,P.py+50,100,40)
    r5 = (P.px,P.py+300,150,40)
    r6 = (P.px+200,P.py+300,100,40)
    r7 = (P.px+650,P.py+300,100,40)
    r8 = (P.px+800,P.py+300,150,40)
    r9 = (P.px+350,P.py+350,50,40)
    r10 = (P.px+550,P.py+350,50,40)
    r11 = (P.px-50,P.py+350,50,140)
    r12 = (P.px+950,P.py+350,50,140)
    r13 = (P.px,P.py+500,950,40)
    r14 = (P.px+150,P.py+250,50,40)
    r15 = (P.px+750,P.py+250,50,40)
    r16 = (P.px+450,P.py,50,40)
    r17 = r1
    if P.prog[0] <= 40 or P.prog[5][12] == 0:
        r17 = (P.px+450,P.py+50,50,40)
    r18 = P.egi_gym_guide.get_rect()
    rects = [r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    # if P.pp1_eusine:
    #     eusine = P.pp1_eusine.y_dist()
    #     if eusine > 0:
    #         P.pp1_eusine.move()
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if not guide:
        P.egi_gym_guide.move(temppx,temppy)
    # if P.pp1_eusine:
    #     if eusine <= 0:
    #         P.pp1_eusine.move(temppx,temppy)

def egida_gym_main_f(P,temppx,temppy,tim):
    if P.prog[5][12] == 1:
        P.surface.blit(P.egi_gym_light,(temppx+513,temppy+29))
    if P.prog[0] >= 41:
        P.surface.blit(P.egi_gym_light,(temppx+423,temppy+29))
    P.surface.blit(P.egi_gym_f,(temppx+348,temppy+288))
    show_location(P, P.loc_txt, tim)

def egida_gym_main(P) -> None:
    if P.song != "music/gym.wav":
        P.song = "music/gym.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.egi_gym_back = load("p/egida/Egida_Gym_Main.png")
    P.egi_gym_light = load("p/egida/green_light.png")
    P.egi_gym_black = load("p/egida/black_door.png")
    P.egi_gym_mdoor = load("p/egida/gym_main_door.png")
    P.egi_gym_ldoor = load("p/egida/gym_l_door.png")
    P.egi_gym_rdoor = load("p/egida/gym_r_door.png")
    P.egi_gym_f = load("p/egida/egida_gym_mf.png")
    P.egi_gym_guide = npc.NPC(P,'Officer','Ross',[400,350],[['d',20]],["Welcome to the Egida City Gym!","Our gym leader Colress uses", "Steel-type Pokemon.","Steel Pokemon are resistant to","many types of attacks, but if","you can fill your team with","plenty of Ground or Fighting","type moves, you should be good","to go!"])
    move = True
    tim = 0
    set_location(P)
    egida_gym_main_b(P)
    egida_gym_main_p(P,P.px,P.py,False)
    egida_gym_main_f(P,P.px,P.py,tim)
    fade_in(P)
    fade = None
    end = True
    m = 0
    while end:
        egida_gym_main_b(P)
        # print(P.px,P.py)
        temppx = P.px
        temppy = P.py
        egida_gym_main_p(P,temppx,temppy,move)
        egida_gym_main_f(P,temppx,temppy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.egi_gym_guide.talk():
                        egida_gym_main_b(P)
                        egida_gym_main_p(P,P.px,P.py,False)
                        egida_gym_main_f(P,P.px,P.py,tim)
                        P.egi_gym_guide.write()
                    elif next_to(P,350,350):
                        txt(P,"It's a status in the shape of","Latias' head.")
                    elif next_to(P,550,350):
                        txt(P,"It's a status in the shape of","Latios' head.")
                    elif P.px == -75 and P.py == 175 and (P.prog[0] <= 40 or P.prog[5][12] == 0):
                        txt(P,"The door seems to be locked by","some mechanism.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        keys = pygame.key.get_pressed()
        if P.px == -75 and P.py == 225 and face_u(P):
            P.px = 175
            P.py = -675
            P.loc = "egi_gym_b"
            end = False
        if P.px == -75 and P.py == -175 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            P.px = -875
            P.py = 1125
            fade = P.song
            P.loc = "egida_under"
            end = False
        if P.px == 225 and P.py == -25 and face_u(P):
            P.px = 225
            P.py = -175
            P.loc = "egi_gym_l"
            end = False
        if P.px == -375 and P.py == -25 and face_u(P):
            P.px = 225
            P.py = -175
            P.loc = "egi_gym_r"
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def egida_mine_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_mine_back, (P.px, P.py))
    P.surface.blit(P.char_shad,(P.px+350,P.py+113))
    P.surface.blit(P.egi_mine_clerk,(P.px+348,P.py+84))

def egida_mine_p(P,temppx,temppy,move):
    #rects start
    P.egi_mine_hiker.move()
    r0 = (P.px,P.py+150,450,40)
    r1 = (P.px,P.py+350,250,40)
    r3 = (P.px-50,P.py+200,50,140)
    r4 = (P.px+250,P.py+400,200,40)
    r2 = (P.px+450,P.py+200,50,190)
    rects = [r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)

def egida_mine_f(P,temppx,temppy):
    P.surface.blit(P.egi_mine_f,(temppx+5,temppy+325))

def egida_mine(P) -> None:
    set_mixer_volume(P,P.vol)
    if P.song != "music/egida_city.wav":
        P.song = "music/egida_city.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    box = load("p/3_box.png")
    P.egi_mine_clerk = pygame.transform.scale(load("p/spr/mart_clerk_d1.png"),(55,66))
    P.egi_mine_back = load("p/egida/egida_mine.png")
    P.egi_mine_f = load("p/egida/egida_mine_f.png")
    P.egi_mine_hiker = npc.NPC(P,'Hiker','Dude',[100,100],[['d',20]],["Man would just you look at all","those gems! I wish I could see","these when I'm out hiking!"])
    move = True
    tim = 0
    egida_mine_b(P)
    egida_mine_p(P,P.px,P.py,False)
    egida_mine_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        # print(P.px,P.py)
        egida_mine_b(P)
        temppx = P.px
        temppy = P.py
        egida_mine_p(P,temppx,temppy,move)
        egida_mine_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 25 and P.py == 75 and face_u(P):
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Welcome to the Egida Gem Shop!","May I help you?")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            poke_mart(P, mt)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"Please come again!")
                    elif (P.py == -25 and P.px in [175,225,275,325,375] and face_d(P)) or (P.py == -75 and P.px == 125 and face_l(P)):
                        txt(P,"A bunch of gems are being","displayed.")
                    elif P.px == 275 and P.py == 75 and face_u(P):
                        txt(P,"Oh ho ho!", "Are you here to test your luck", "in the mines of Egida?")
                        txt(P,"We'll pay you for the gems you","dig out, and you can keep","anything else you find!")
                        txt(P,"Hmm, it appears you don't have","the right qualifications for","this line of work.")
                        txt(P,"Well if you ever do, feel free","to stop by and we'll get you","set right up!")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 75 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -375
            P.py = 1125
            P.loc = 'egida_under'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def egida_lab_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.egi_lab_back, (P.px, P.py))
    #P.surface.blit(P.char_shad,(P.px+350,P.py+113))
    #P.surface.blit(P.egi_mine_clerk,(P.px+348,P.py+84))

def egida_lab_p(P,temppx,temppy,move):
    scif = P.egi_lab_scif.y_dist() > 0
    scim = P.egi_lab_scim.y_dist() > 0
    if P.egi_lab_colress:
        col = P.egi_lab_colress.y_dist() > 0
        if col:
            P.egi_lab_colress.move()
    if scif:
        P.egi_lab_scif.move()
    if scim:
        P.egi_lab_scim.move()
    #rects start
    r0 = (P.px+200,P.py+50,250,40)
    r1 = (P.px,P.py+100,200,40)
    r2 = (P.px+450,P.py+100,50,40)
    r3 = (P.px+500,P.py+150,50,40)
    r4 = (P.px+550,P.py+200,50,240)
    r5 = (P.px-50,P.py+150,50,290)
    r6 = (P.px+100,P.py+300,100,140)
    r7 = (P.px+200,P.py+350,50,40)
    r8 = (P.px+250,P.py+250,50,190)
    if P.px >= 125:
        r8 = (P.px+300,P.py+250,50,190)
    r9 = (P.px,P.py+450,550,40)
    r10 = P.egi_lab_scif.get_rect()
    r11 = P.egi_lab_scim.get_rect()
    r12 = r1
    if P.egi_lab_colress:
        r12 = P.egi_lab_colress.get_rect()
    rects = [r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if not scif:
        P.egi_lab_scif.move(temppx,temppy)
    if not scim:
        P.egi_lab_scim.move(temppx,temppy)
    if P.egi_lab_colress:
        if not col:
            P.egi_lab_colress.move(temppx,temppy)

def egida_lab_f(P,temppx,temppy):
    P.surface.blit(P.egi_lab_f,(temppx+98,temppy+242))

def egida_lab(P) -> None:
    set_mixer_volume(P,P.vol)
    if P.song != "music/egida_city.wav":
        P.song = "music/egida_city.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.egi_lab_back = load("p/egida/egida_lab.png")
    P.egi_lab_f = load("p/egida/egida_lab_f.png")
    P.egi_lab_scif = npc.NPC(P,'Scientistf','Dude',[50,350],[['r',20]],["I'm researching the various","methods of evolution. You","wanna see what I've found?","Hee hee, it's secret! Well","maybe if you get the approval","of Colress I'll show you!"])
    P.egi_lab_scim = npc.NPC(P,'Scientistm','Dude',[100,150],[['d',20]],["In this facility, we have the","latest tools for analyzing","elemental gems!","You don't seem qualified to","help out, but if that changes","don't be afraid to stop by!"])
    if P.prog[0] < 48:
        P.egi_lab_colress = None
    elif P.prog[8][0][0] == -1:
        P.egi_lab_colress = npc.NPC(P,'Colress','Colly',[200,100],[['l',20]],["Welcome "+P.save_data.name+"!","Glad you found the time to","stop by!","I have a research project I","would like your assistance","with.","Egida City is known for its","elemental gems, but the color","of the gems are artificial.","Here in the lab, we have the","tools to analyze the gems","collected from the mines.","We use lenses corresponding to" ,"each of the types, just like","the ones Pokemon have.","Viewing a gem through the lens","will change its appearance","depending on the lens used.","If the element of the lens is","effective on the gem, it will","appear to glow.","If it isn't very effective,","the gem will appear duller","than usual.","In cases where the elements","are neutral, the gem will","appear unchanged.","I'd like you to help with this","work to help us identify the","gems we have stored here.","If you use fewer lenses and","guesses, you'll earn more","money and research experience.","You can see how much you've","improved in the skills section","of your profile.","If you reach a high research","level, I can treat you to some","of the other projects here.","Anyways, when you're ready","tell my assistant, and he'll","get you set up.","Let me know if you ever need","me to remind you how to use","the lenses."])
    else:
        P.egi_lab_colress = npc.NPC(P,'Colress','Colly',[200,350],[['l',20]],["Well the gems will appear to","change depending on the type","of lens you view it through.","If the element of the lens is","effective on the gem, it will","appear to glow.","If it isn't very effective,","the gem will appear duller","than usual.","In cases where the elements","are neutral, the gem will","appear unchanged.","If you use fewer lenses and","guesses, you'll earn more","money and research experience."])
    P.h1_npc1 = None
    P.h1_npc2 = None
    move = True
    tim = 0
    egida_lab_b(P)
    egida_lab_p(P,P.px,P.py,False)
    egida_lab_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        # print(P.px,P.py)
        egida_lab_b(P)
        temppx = P.px
        temppy = P.py
        egida_lab_p(P,temppx,temppy,move)
        egida_lab_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.egi_lab_scif.talk():
                        egida_lab_b(P)
                        egida_lab_p(P,P.px,P.py,False)
                        egida_lab_f(P,P.px,P.py)
                        P.egi_lab_scif.write()
                    elif next_to(P,0,100):
                        if date_diff(P.prog[8][0][2][0]) < 21600 and P.prog[8][0][2][0] != None:
                            txt(P,'The box is empty.')
                        else:
                            txt(P,"The box is filled with gems.")
                    elif next_to(P,450,100) or next_to(P,500,150):
                        txt(P,"You can't tell what's inside,","but it's quite heavy.")
                    elif P.py == 175 and P.px in [125,75,25] and face_u(P):
                        txt(P,"The monitor is off.")
                    elif P.egi_lab_scim.talk():
                        egida_lab_b(P)
                        egida_lab_p(P,P.px,P.py,False)
                        egida_lab_f(P,P.px,P.py)
                        if P.prog[8][0][0] == -1:
                            P.egi_lab_scim.write()
                        elif date_diff(P.prog[8][0][2][0]) < 21600:
                            txt(P,"I'm glad you're so eager to","help, but we're still waiting", "on our next shipment of gems.")
                            txt(P,"You may want to do something", "else in the meantime.")
                        else:
                            temp = P.surface.copy()
                            txt(P,"We have gems ready to analyze.","I'll set things up and guide","you through the process.")
                            if P.prog[8][0][0] >= 3 and P.prog[15][0] <= 1:
                                txt(P,"On a side note, Colress wanted","me to remind you that his","reward for you is ready.")
                                # txt(P,"I can still pay you for your","work, but you won't be able to","increase your research level.")
                            # if P.prog[8][0][0] == 3:
                            #     txt(P,"Oh yeah, Colress wanted me to","remind you that his reward","for you is ready.")
                            new_txt(P)
                            write(P,'Are you ready to begin?')
                            if choice(P):
                                fade_out(P)
                                points = research_game(P,3)
                                lowest = points[1]
                                points = points[0]
                                print("points"+str(points))
                                P.surface.blit(temp,(0,0))
                                fade_in(P)
                                if points == -1:
                                    txt(P,"Thanks anyways for offering to","help. I understand you're a","busy person.")
                                    txt(P,"I'll be waiting here for", "when you return.")
                                elif points == 3000:
                                    txt(P,"Wow! I didn't even see you","touch the analysis tools!")
                                    txt(P,"You must really be getting","the hang of this! That was", "incredible!")
                                elif lowest == True:
                                    txt(P,"Hmm, I think you could use","a little more training.")
                                    txt(P,"Pokemon type interactions are","very well documented. You may","want to research a bit.")
                                elif points > 2800:
                                    txt(P,"Amazing job! You worked so","efficiently, I almost feel bad","that we're out of gems.")
                                elif points > 2550:
                                    txt(P,"Nice going! Thanks for lending","a hand, it really helps a lot!")
                                elif points > 2100:
                                    txt(P,"Pretty good! With some more","experience, I'm sure you'll","keep improving!")
                                else:
                                    txt(P,"Not bad! If you ever need a","few tips, feel free to ask","around.")
                                lvled = False
                                if points == -1:
                                    pass
                                elif points == 3000:
                                    txt(P,"Here, take $2000 for that","stellar performance!")
                                    P.save_data.money += 2000
                                    lvled = gain_skill(P,0,20)
                                else:
                                    exp = 100+round((points**2)/50000)*5
                                    print(exp)
                                    lvled = gain_skill(P,0,int(exp/100))
                                    money = int(exp*(0.6+(0.1*P.prog[8][0][0])))
                                    txt(P,"Here, have $"+str(money)+" for your","help. Be sure to stop by when","our next shipment is in!")
                                    if points == 105:
                                        txt(P,"Actually, have another $100.","Think of it as funding to","help you study up a bit.")
                                        money += 100
                                    P.save_data.money += money
                                if lvled:
                                    txt(P,"Congratulations, your research","skill leveled up!")
                                    txt(P,"You may find it easier to","identify some of these gems.")
                                    if P.prog[8][0][0] == 3:
                                        txt(P,"You should talk to Colress to","receive the reward he has","prepared for you.")
                                if points != -1:
                                    P.prog[8][0][2][0] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                            else:
                                txt(P,"Alright, well let me know when","you have the time!")
                    elif P.egi_lab_colress and P.egi_lab_colress.talk():
                        egida_lab_b(P)
                        egida_lab_p(P,P.px,P.py,False)
                        egida_lab_f(P,P.px,P.py)
                        if P.prog[8][0][0] >= 3 and P.prog[15][0] == 0:
                            if P.prog[0] < 87:
                                txt(P,"Thanks for all the hard work","you've been putting in. It's","been a great help!")
                                txt(P,"My reward for you is prepared,","but I'm not sure you're ready","for it just yet.")
                                txt(P,"I'd like you to get the gym","badge from Pianura City before","I show it to you.")
                            else:
                                txt(P,"Thanks for all the hard work","you've been putting in. It's","been a great help!")
                                txt(P,"I don't know if you've noticed","but there are some areas where","some species like to dwell.")
                                txt(P,"In these places, they are","guarding artifacts tied to a","special type of evolution.")
                                txt(P,"If you can get one of those","stones and bring it here, I'll","give you something special!")
                                P.prog[15][0] += 1
                        else:
                            keep_talk = True
                            if P.prog[15][0] == 1:
                                t = P.surface.copy()
                                new_txt(P)
                                write(P,"Did you bring one of those","stones?")
                                if choice(P):
                                    txt(P,"Which Pokemon do you have a","stone for?")
                                    fade_out(P)
                                    ans = trade_poke(P,None,True,mega_poke = True)
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if ans != None:
                                        keep_talk = False
                                        txt(P,"Great! I can evolve "+ans.name,"with the "+has_mega_stone(P,ans.code_nos(),True)+"!")
                                        txt(P,"In the future when you have","more gym badges and a higher","research level, I'll be able")
                                        txt(P,"to evolve more Pokemon this","way, but for now I can only do","this process once.")
                                        new_txt(P)
                                        write(P,"Are you sure you want to","evolve "+ans.name+"?")
                                        if choice(P):
                                            txt(P,"Alright, here we go!")
                                            fade_out(P,P.song)
                                            for p in range(len(P.party)):
                                                if P.party[p].equals(ans):
                                                    pos = p
                                            P.party[pos] = poke.Poke(ans.evo[1],[ans.lvl,ans.gen,ans.ch,ans.m1,ans.p1,ans.m2,ans.p2,ans.m3,ans.p3,ans.m4,ans.p4,ans.item,ans.status,ans.exp,ans.ball,ans.friend,ans.ability,True])
                                            evolve(P,ans,P.party[pos])
                                            P.surface.blit(t,(0,0))
                                            play_music(P,"music/egida_city.wav")
                                            fade_in(P)
                                            P.prog[15][0] += 1
                                            add_item(P,has_mega_stone(P,ans.code_nos(),True),-1)
                                            txt(P,ans.name+" has successfully","Mega Evolved!")
                                            txt(P,"I'm sure you'll find them more","useful in your battles!")
                                            txt(P,"Good luck with the rest of","your journey!")
                                        else:
                                            txt(P,"Well come back when you've","given it more thought!")
                                    else:
                                        txt(P,"Well come back when you have","a stone for me!")
                                else:
                                    txt(P,"Well come back when you have","a stone for me!")
                            if keep_talk:
                                new_txt(P)
                                write(P,"Do you need me to give you","another explanation of the","lenses?")
                                if choice(P):
                                    P.egi_lab_colress.write()
                                if P.prog[15][0] == 0:
                                    txt(P,"I have a special gift waiting", "for you, so work hard to level","up your research skill!")
                                elif P.prog[15][0] == 1:
                                    txt(P,"Remember to bring me one of","those stones! You can get them","from Pokemon in special areas.")
                                elif P.prog[15][0] == 2:
                                    txt(P,"I hope your Mega Pokemon has","been doing well!")
                                    txt(P,"Once you have another gym","badge and reach research level","5, I'll be able to Mega Evolve")
                                    txt(P,"a few more Pokemon for you!","So keep working hard!")
                                if P.prog[8][0][0] == -1:
                                    P.egi_lab_colress = npc.NPC(P,'Colress','Colly',[200,100],[['l',20]],["Well the gems will appear to","change depending on the type","of lens you view it through.","If the element of the lens is","effective on the gem, it will","appear to glow.","If it isn't very effective,","the gem will appear duller","than usual.","In cases where the elements","are neutral, the gem will","appear unchanged.","If you use fewer lenses and","guesses, you'll earn more","money and research experience."])
                                    P.prog[8][0][0] = 1
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == -25 and P.py == -125 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.px = -375
            P.py = 125
            P.loc = 'egida_under'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def egida_under_b(P,wx,wy,lifty,listx,listy,gy):
    draw_waves(P,wx,wy)
    P.surface.blit(P.black_back,(P.px+1230,P.py-870))
    doormod = 50
    if P.py > 1075:
        doormod = 1125-P.py
    P.surface.blit(P.egidau_gymdl,(P.px+1195+doormod,P.py-860))
    P.surface.blit(P.egidau_gymdr,(P.px+1325-doormod,P.py-860))
    P.surface.blit(P.egidau_back,(P.px,P.py-1300))
    P.surface.blit(P.egi_lift,(P.px+902,P.py-642-lifty))
    if lifty > 0:
        P.surface.blit(P.char_shad,(376,288-lifty))
        P.surface.blit(P.p,(375,265-lifty))
    P.surface.blit(P.egidau_cover,(P.px+875,P.py-600))
    if P.px == -975 and P.py > 575 and P.py <= 625:
        blit_small_door(P,625)
    if P.px == -275 and P.py > 575 and P.py <= 625:
        blit_small_door(P,625)
    if P.px == -1125 and P.py > 75 and P.py <= 125:
        blit_small_door(P,125)
    if P.px == -375 and P.py > 1075:
        P.surface.blit(P.egidau_mine_door,(P.px+750,P.py-860))
    if P.prog[0] < 48:
        P.surface.blit(P.traffic_cone,(P.px+1700,P.py-310))
    P.surface.blit(P.gondola, (P.px + 1726, P.py - 50 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 1737, P.py + 10 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 1738, P.py - 10 + abs(P.foam)+gy))
    #lab door
    if P.px == -375 and P.py > 75 and P.py <= 125:
        P.surface.fill((173,192,206), Rect(P.px+750,P.py+140,125-P.py,60))
    else:
        if P.px <= -750 and P.px >= -800:
            P.surface.fill((173,192,206), Rect(P.px+800-(800+P.px),P.py+140,800+P.px,60))
        else:
            P.surface.fill((173,192,206), Rect(P.px+750,P.py+140,50,60))
    draw_lamps(P, P.px, P.py, listx, listy,bf = "b")

def egida_under_p(P,temppx,temppy,move,lifty,gond,gy):
    scif = P.egidau_scif.y_dist() > 0
    scim = P.egidau_scim.y_dist() > 0
    hiker = P.egidau_hiker.y_dist() > 0
    if P.egidau_worker:
        worker = P.egidau_worker.y_dist() > 0
        if worker:
            P.egidau_worker.move()
    if scif:
        P.egidau_scif.move()
    if scim:
        P.egidau_scim.move()
    if hiker:
        P.egidau_hiker.move()
    #rects start
    r1 = (P.px+400,P.py-850,350,40)
    r1_0 = (P.px+750,P.py-900,50,40)
    r1_01 = (P.px+800,P.py-850,450,40)
    r1_1 = (P.px+1250,P.py-900,50,40)
    r1_2 = (P.px+1300,P.py-850,350,40)
    r2 = (P.px+350,P.py-800,50,640)
    r3 = (P.px+1650,P.py-800,50,490)
    r4 = (P.px+550,P.py-650,950,40)
    r5 = (P.px+550,P.py-600,50,290)
    r6 = (P.px+1450,P.py-600,50,290)
    r7 = (P.px+600,P.py-350,50,40)
    r70 = (P.px+700,P.py-350,250,40)
    r71 = (P.px+650,P.py-400,50,40)
    r8 = (P.px+1100,P.py-350,250,40)
    r80 = (P.px+1400,P.py-350,50,40)
    r81 = (P.px+1350,P.py-400,50,40)
    r9 = (P.px+850,P.py-600,50,40)
    r10 = (P.px+1150,P.py-600,50,40)
    r11 = (P.px+900,P.py-550,50,40)
    r12 = (P.px+1100,P.py-550,50,40)
    r13 = (P.px+950,P.py-500,50,40)
    r14 = (P.px+1050,P.py-500,50,40)
    r15 = (P.px+900,P.py-450,50,100)
    r16 = (P.px+1100,P.py-450,50,100)
    r17 = (P.px+400,P.py-150,550,40)
    r18 = (P.px+1100,P.py-150,700,40)
    r19 = (P.px+1100,P.py-100,50,290)
    r20 = (P.px+900,P.py-100,50,290)
    r21 = (P.px+400,P.py+150,350,40)
    r210 = (P.px+750,P.py+100,50,40)
    r211 = (P.px+800,P.py+150,100,40)
    r22 = (P.px+1150,P.py+150,350,40)
    r220 = (P.px+1550,P.py+150,100,40)
    r221 = (P.px+1500,P.py+100,50,40)
    r23 = (P.px+400,P.py+350,1250,40)
    r24 = (P.px+350,P.py+200,50,140)
    r25 = (P.px+1650,P.py+200,50,140)
    r26 = (P.px+1700,P.py-350,350,40)
    r27 = (P.px+1750,P.py-100,50,490)
    r28 = (P.px+1950,P.py-300,50,690)
    r29 = P.egidau_scif.get_rect()
    r30 = P.egidau_scim.get_rect()
    r31 = P.egidau_hiker.get_rect()
    r32 = r1
    if P.egidau_worker:
        r32 = P.egidau_worker.get_rect()
    r33 = r1
    if P.prog[0] < 48:
        r33 = (P.px+1700,P.py-300,50,140)
    r34 = (P.px+1800,P.py+400,150,40)
    rects = [r210,r211,r1_0,r1_01,r34,r33,r32,r221,r220,r81,r80,r71,r70,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1_2,r1_1,r1]
    #rects end
    #rect_draw(P,rects)
    if lifty == 0:
        if gond != 0:
            P.surface.blit(P.char_shad,(P.px+1737,P.py+63+abs(P.foam)+gy))
            P.surface.blit(P.p,(P.px+1736,P.py+40+abs(P.foam)+gy))
        else:
            if move:
                player_move(P,rects)
            else:
                blit_player(P)
    if P.egidau_worker:
        if not worker:
            P.egidau_worker.move(temppx,temppy)
    if not scif:
        P.egidau_scif.move(temppx,temppy)
    if not scim:
        P.egidau_scim.move(temppx,temppy)
    if not hiker:
        P.egidau_hiker.move(temppx,temppy)

def egida_under_f(P,temppx,temppy,listx,listy,tim,lifty):
    if P.prog[0] < 48:
        P.surface.blit(P.traffic_cone,(temppx+1700,temppy-210))
    P.surface.blit(P.egidau_front, (temppx + 504, temppy - 707))
    P.surface.blit(P.egidau_cave,(temppx+1600,temppy+200))
    draw_lamps(P, temppx, temppy, listx, listy)
    P.surface.blit(P.egidau_cavelight,(temppx+1600,temppy+200))
    if P.graphic == 1:
        light = P.egidau_light
        if get_time() > 16 or get_time() < 9:
            light = P.egidau_night
        P.surface.blit(light,(temppx+280,temppy-440))
        P.surface.blit(light,(temppx+950,temppy-440))
        P.surface.blit(light,(temppx+280,temppy-940))
        P.surface.blit(light,(temppx+950,temppy-940))
        P.surface.blit(light,(temppx+280,temppy+60))
        P.surface.blit(light,(temppx+950,temppy+60))
    show_location(P, P.loc_txt, tim)
    if lifty > 50:
        trans = pygame.Surface((800,600))
        trans.set_alpha((lifty-50)*10)
        trans.fill((0,0,0))
        P.surface.blit(trans,(0,0))

def egida_under(P) -> None:
    if P.song != "music/egida_city.wav":
        P.song = "music/egida_city.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    if P.prog[0] in [80,47]:
        P.prog[0] += 1
    set_location(P)
    P.egidau_mine_door = load("p/egida/mine_door.png")
    P.egidau_cave = load("p/egida/egida_cave.png")
    P.egidau_cavelight = load("p/egida/egida_cavelight.png")
    P.egidau_light = load("p/egida/egida_under_light.png")
    P.egidau_night = load("p/egida/egida_under_lightn.png")
    P.egidau_back = load("p/egida/Egida_City_Underground.png")
    P.egidau_front = load("p/egida/Egida_Under_f.png")
    P.egidau_cover = load("p/egida/lift_cover.png")
    P.egidau_gymdr = load("p/egida/Egida_gym_doorr.png")
    P.egidau_gymdl = load("p/egida/Egida_gym_doorl.png")
    P.egidau_scim = npc.NPC(P,'Scientistm','Nerd',[500,250],[['mr',60],['r',100],['ml',60],['l',140]],["Yeah, I can do that for you.","Mmhm...Mmhm...Of course...","Don't worry about it!","Hey I'm in the middle of an","important call, would you mind","giving me some space?"])
    P.egidau_scif = npc.NPC(P,'Scientistf','Nerd',[1550,-600],[['md',60],['d',60],['mu',60],['u',80]],["Do you ever get the feeling","that someone's watching your","every movement?","I've been feeling that a lot","lately for some reason.",""])
    P.egidau_hiker = npc.NPC(P,'Hiker','Dude',[650,-800],[['u',20]],["Man would just you look at all","those gems! I wish I could see","these when I'm out hiking!"])
    if P.prog[0] < 48:
        P.egidau_worker = npc.NPC(P,'Officer','Dude',[1700,-250],[['l',20]],["The route to Pianura City is","having issues at the moment.","","I apologize, but I'll have","to ask you to come back","later."])
    else:
        P.egidau_worker = None
    move = True
    gond = 0
    gy = 0
    wx = 0
    wy = 0
    tim = 0
    listx = [542,938,1092,1489,1938,391,938,1639,391,1639,391,1639,391,938,1092,1365,1639,1938,1938]
    listy = [-450,-450,-450,-450,-450,-950,-950,-950,-700,-700,-450,-450,50,50,50,50,50,-200,50]
    lifty = 0
    fade = None
    use_l = False
    egida_under_b(P,wx,wy,lifty,listx,listy,gy)
    egida_under_p(P,P.px,P.py,False,lifty,gond,gy)
    egida_under_f(P,P.px,P.py,listx,listy,tim,lifty)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        egida_under_b(P,wx,wy,lifty,listx,listy,gy)
        temppx = P.px
        temppy = P.py
        egida_under_p(P,temppx,temppy,move,lifty,gond,gy)
        egida_under_f(P,temppx,temppy,listx,listy,tim,lifty)
        if gond == 1:
            gond = 2
            fade_in(P)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -625 and P.py == 875 and face_u(P):
                        new_txt(P)
                        write(P,"Use the lift?")
                        if choice(P,550,600):
                            move = False
                            use_l = True
                    elif P.px == -825 and P.py == 75 and face_u(P):
                        txt(P,"It's locked.")
                    elif P.px == -1425 and P.py == 275 and face_l(P):
                        nxtl = gondolier(P)
                        if nxtl != "Egida City":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.egidau_scif.talk():
                        egida_under_b(P,wx,wy,lifty,listx,listy,gy)
                        egida_under_p(P,P.px,P.py,False,lifty,gond,gy)
                        egida_under_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egidau_scif.write()
                    elif P.egidau_scim.talk():
                        egida_under_b(P,wx,wy,lifty,listx,listy,gy)
                        egida_under_p(P,P.px,P.py,False,lifty,gond,gy)
                        egida_under_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egidau_scim.write()
                    elif P.egidau_hiker.talk():
                        egida_under_b(P,wx,wy,lifty,listx,listy,gy)
                        egida_under_p(P,P.px,P.py,False,lifty,gond,gy)
                        egida_under_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egidau_hiker.write()
                    elif P.egidau_worker and P.egidau_worker.talk():
                        egida_under_b(P,wx,wy,lifty,listx,listy,gy)
                        egida_under_p(P,P.px,P.py,False,lifty,gond,gy)
                        egida_under_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egidau_worker.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            fade = P.song
            end = False
        if use_l:
            lifty += 1
            if lifty == 75:
                P.loc = "egida"
                P.px -= 150
                P.py += 300
                end = False
        if P.py == -75 and P.px >= -1525 and P.px <= -1425 and face_d(P):
            P.loc = 'route_3'
            fade = P.song
            P.move_out_dir = 'd'
            P.px += 900
            P.py = 425
            end = False
        if P.px == -375 and P.py == 1125 and face_u(P):
            P.loc = "egida_mine"
            P.px = 75
            P.py = -75
            end = False
        if P.px == -375 and P.py == 125 and face_u(P):
            P.loc = "egida_lab"
            P.px = -25
            P.py = -125
            end = False
        if P.px == -975 and P.py == 625 and face_u(P):
            P.loc = "house_1_6"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -275 and P.py == 625 and face_u(P):
            P.loc = "house_1_7"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -1125 and P.py == 125 and face_u(P):
            P.loc = "house_1_8"
            P.px = 175
            P.py = -75
            end = False
        if P.px == -875 and P.py == 1125 and face_u(P):
            P.loc = "egi_gym"
            P.px = -75
            P.py = -175
            fade = P.song
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def egida_b(P,pcx,pcy,lifty,listx,listy,tim):
    P.surface.blit(P.egi_back,(P.px+1040,P.py-1204))
    P.surface.blit(P.egi_lift,(P.px+1052,P.py-942+lifty))
    if lifty > 0:
        P.surface.blit(P.char_shad,(376,288+lifty))
        P.surface.blit(P.p,(375,265+lifty))
    P.surface.blit(P.egi_clip,(P.px+1601,P.py-549))
    P.egi_sciu.move()
    P.surface.blit(P.pc_black,(P.px+880,P.py-270))
    P.surface.blit(P.pcdr,(P.px+925+pcx,P.py-270-pcy))
    P.surface.blit(P.pcdl,(P.px+888-pcx,P.py-270-pcy))
    P.surface.blit(P.egida,(P.px-100,P.py-1300))
    if P.prog[6][9] == 0:
        P.surface.blit(P.item_out,(P.px+400,P.py+100))
    if int(tim/3)%2 == 0:
        P.surface.blit(P.egi_gen,(P.px+425,P.py-953))
    draw_lamps(P,P.px,P.py,listx,listy,"b")

    #P.surface.blit(P.egi_pc,(P.px+815,P.py-294))
    if P.px == -975 and P.py > 475 and P.py <= 525:
        blit_small_door(P,525)
    if P.px == -1375 and P.py > 475 and P.py <= 525:
        blit_small_door(P,525)
    if P.px == -1075 and P.py > 975 and P.py <= 1025:
        blit_small_door(P,1025)
    if P.px == -175 and P.py > 975 and P.py <= 1025:
        blit_small_door(P,1025)

def egida_p(P,temppx,temppy,move,temp_y,lifty):
    pre = P.egi_pre.y_dist() > 0
    sci = P.egi_sci.y_dist() > 0
    if pre:
        P.egi_pre.move()
    if sci:
        P.egi_sci.move()
    P.egi_robb.move()
    if P.egi_rocket:
        rocket = P.egi_rocket.y_dist()
        if rocket > 0:
            P.egi_rocket.move()
    if P.egi_colress:
        colress = P.egi_colress.y_dist()
        if colress > 0:
            P.egi_colress.move()
    #rects start
    r1 = (P.px+400,P.py-750,150,40)
    r100 = (P.px+600,P.py-750,500,40)
    r101 = (P.px+550,P.py-800,50,40)
    r2 = (P.px+400,P.py-550,700,40)
    r3 = (P.px+1250,P.py-750,200,40)
    r31 = (P.px+1500,P.py-750,100,40)
    r32 = (P.px+1450,P.py-800,50,40)
    r4 = (P.px+1250,P.py-550,400,40)
    r5 = (P.px+1600,P.py-750,50,200)
    r6 = (P.px+1300,P.py-900,50,40)
    r7 = (P.px+1000,P.py-900,50,40)
    r62 = (P.px+1250,P.py-850,50,40)
    r72 = (P.px+1050,P.py-850,50,40)
    r63 = (P.px+1200,P.py-800,50,40)
    r73 = (P.px+1100,P.py-800,50,40)
    r8 = (P.px+1050,P.py-950,250,40)
    r9 = (P.px+750,P.py-250,150,40)
    r95 = (P.px+900,P.py-300,50,40)
    r10 = (P.px+750,P.py-50,350,140)
    r11 = (P.px+1250,P.py-250,100,40)
    r110 = (P.px+1400,P.py-250,350,40)
    r111 = (P.px+1800,P.py-250,150,40)
    r112 = (P.px+1350,P.py-300,50,40)
    r113 = (P.px+1750,P.py-300,50,40)
    r12 = (P.px+1250,P.py-50,700,140)
    r13 = (P.px+1250,P.py-500,50,250)
    r14 = (P.px+1050,P.py-500,50,250)
    r15 = (P.px+700,P.py-200,50,150)
    r16 = (P.px+1950,P.py-200,50,150)
    r17 = (P.px+950,P.py-250,150,40)
    r18 = r1
    r19 = r1
    if P.egi_rocket:
        r18 = P.egi_rocket.get_rect()
    if P.egi_colress:
        r19 = P.egi_colress.get_rect()
    r20 = P.egi_pre.get_rect()
    r21 = P.egi_sci.get_rect()
    rects = [r101,r100,r32,r31,r113,r112,r110,r111,r21,r20,r95,r19,r18,r62,r72,r63,r73,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    #rects end
    if P.prog[0] == 20:
        if temp_y < P.py:
            player_move(P,rects,manual_input = 'd')
        elif temp_y > P.py:
            player_move(P,rects,manual_input = 'u')
        if P.py == temp_y:
            if face_u(P):
                P.p = P.d1
                blit_player(P)
            else:
                P.p = P.u1
                blit_player(P)
    if lifty == 0:
        if move:
            player_move(P,rects)
        else:
            blit_player(P)
    if not pre:
        P.egi_pre.move(temppx,temppy)
    if not sci:
        P.egi_sci.move(temppx,temppy)
    if P.egi_rocket:
        if rocket <= 0:
            P.egi_rocket.move()
    if P.egi_colress:
        if colress <= 0:
            P.egi_colress.move(temppx,temppy)

def egida_f(P,temppx,temppy,listx,listy,tim,lifty):
    P.surface.blit(P.egi_f, (temppx + 395, temppy - 684))
    P.surface.blit(P.grass,(temppx+500,temppy+140))
    draw_lamps(P, temppx, temppy, listx, listy)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+865,temppy-449))
    show_location(P, P.loc_txt, tim)
    if lifty > 50:
        trans = pygame.Surface((800,600))
        trans.set_alpha((lifty-50)*10)
        trans.fill((0,0,0))
        P.surface.blit(trans,(0,0))

def egida(P, enter = False,sci_tim = None,sci_curr = None,x_pos = 1500) -> None:
    if P.song != "music/egida_city.wav":
        P.song = "music/egida_city.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    set_location(P)
    P.egi_rocket = None
    move = True
    P.egi_pre = npc.NPC(P,'Preschoolerg','Creep',[1400,-600],[['d',60]],["Sometimes I like to just stare","at the people walking around","down there.","They're so small it makes me","feel like a grown up!",""])
    P.egi_sci = npc.NPC(P,'Scientistm','Nerd',[x_pos,-150],[['mr',60],['r',60],['ml',60],['l',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""],tim = sci_tim,curr = sci_curr)
    P.egi_sciu = npc.NPC(P,'Scientistf','Nerd',[1700,-680],[['md',60],['d',60],['mu',60],['u',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""],tim = sci_tim,curr = sci_curr)
    if P.prog[5][2] == 0:
        P.egi_robb = npc.NPC(P,'Bug Catcher','Robb',[500,150],[['d',60],['r',80],['l',90],['u',40]],["","",""])
    else:
        P.egi_robb = npc.NPC(P,'Bug Catcher','Robb',[500,150],[['u',100]],["","",""])
    if P.prog[0] == 38:
        P.egi_colress = npc.NPC(P,'Colress','',[1150,-800],[['u',40]],["Were you able to track down","the one that ran away?","","I would imagine he is still","pretty close to the Power", "Plant."])
    elif P.prog[0] == 39:
        move = False
        P.egi_colress = npc.NPC(P,'Colress','',[1150,-800],[['d',40]],["","",""])
    else:
        P.egi_colress = None
    lifty = 0
    use_l = False
    pcx = 0
    pcy = 0
    tim = 0
    listx = [742,1088,1242,1565,1915,715,1088,1242,1589]
    listy = [-350,-350,-350,-350,-350,-850,-850,-850,-850]
    temp_y = 0
    if enter == False:
        if P.px == -525 and P.py > 475 and P.py <= 525:
            pcx = 50-(1425 - P.py)
            pcy = 10-((1425 - P.py)/5)
        else:
            pcx = 0
            pcy = 0
        egida_b(P,pcx,pcy,lifty,listx,listy,tim)
        egida_p(P,P.px,P.py,False,temp_y,lifty)
        egida_f(P,P.px,P.py,listx,listy,tim,lifty)
        fade_in(P)
    end = True
    m = 0
    fade = True
    while end:
        #print(P.px,P.py)
        # fps = str(int(P.clock.get_fps()))
        # print(fps)
        if P.prog[0] == 39:
            txt(P,"Thanks for your help dealing","with those scoundrels.")
            txt(P,"I've gotten someone to check","on the lift and it should be","working properly now.")
            txt(P,"I forgot to mention last time","we met, but I run the gym in","this city.")
            txt(P,"If you have the time, I would","love to accept a challenge","from you.")
            fade_out(P)
            P.egi_colress = None
            egida_b(P,pcx,pcy,lifty,listx,listy,tim)
            egida_p(P,P.px,P.py,False,temp_y,lifty)
            egida_f(P,P.px,P.py,listx,listy,tim,lifty)
            fade_in(P)
            P.prog[0] += 1
            move = True
        egida_b(P,pcx,pcy,lifty,listx,listy,tim)
        temppx = P.px
        temppy = P.py
        egida_p(P,temppx,temppy,move,temp_y,lifty)
        egida_f(P,temppx,temppy,listx,listy,tim,lifty)
        if P.px == -275 and P.prog[0] == 19 and move:
            P.egi_rocket = npc.NPC(P,'Team Rocketm','Toby',[200,-1*(P.py-275)],[['mr',160],['r',50]],["Toby's gay","",""],["","",""],spd = 1)
            move = False
        if P.prog[0] == 19 and P.egi_rocket and P.egi_rocket.x_dist() == 50:
            new_txt(P)
            write(P,"Hey outta my way!")
            cont(P)
            temp_y = P.py
            if P.py == 975:
                temp_y -= 50
            else:
                temp_y += 50
            P.prog[0] += 1
        if P.prog[0] == 20 and P.py == temp_y:
            P.egi_rocket = npc.NPC(P,'Team Rocketm','Toby',[P.egi_rocket.x,P.egi_rocket.y],[['mr',100]],["Toby's gay","",""],["","",""],spd = 1)
            P.prog[0] += 1
        if P.prog[0] == 21 and P.egi_rocket.x > 1100:
            move = True
            P.egi_rocket = None
            P.prog[0] += 1
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.egi_colress and P.egi_colress.talk():
                        egida_b(P,pcx,pcy,lifty,listx,listy,tim)
                        egida_p(P,P.px,P.py,False,temp_y,lifty)
                        egida_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egi_colress.write()
                    elif P.px == -475 and P.py == 975:
                        txt(P,"It's locked.")
                    elif P.px == -775 and P.py == 1175:
                        if P.prog[0] < 40:
                            txt(P,"The lift doesn't seem to be","working...")
                        else:
                            new_txt(P)
                            write(P,"Use the lift?")
                            if choice(P,550,600):
                                move = False
                                use_l = True
                    elif P.egi_pre.talk():
                        egida_b(P,pcx,pcy,lifty,listx,listy,tim)
                        egida_p(P,P.px,P.py,False,temp_y,lifty)
                        egida_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egi_pre.write()
                    elif P.egi_sci.talk():
                        egida_b(P,pcx,pcy,lifty,listx,listy,tim)
                        egida_p(P,P.px,P.py,False,temp_y,lifty)
                        egida_f(P,P.px,P.py,listx,listy,tim,lifty)
                        P.egi_sci.write()
                    else:
                        P.buffer_talk = temp_buff
        if use_l:
            lifty += 1
            if lifty == 75:
                P.loc = "egida_under"
                P.px += 150
                P.py -= 300
                end = False
        if P.px == -525 and P.py > 475 and P.py <= 525:
            pcx = 50-(525 - P.py)
            pcy = 10-((525 - P.py)/5)
        else:
            pcx = 0
            pcy = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if P.px == -975 and P.py == 525 and face_u(P):
            P.px = 175
            P.py = -75
            P.loc = "house_1_2"
            end = False
        if P.px == -1375 and P.py == 525 and face_u(P):
            P.px = 175
            P.py = -75
            P.loc = "house_1_3"
            end = False
        if P.px == -1075 and P.py == 1025 and face_u(P):
            P.px = 175
            P.py = -75
            P.loc = "house_1_4"
            end = False
        if P.px == -175 and P.py == 1025 and face_u(P):
            P.px = 175
            P.py = -75
            P.loc = "house_1_5"
            end = False
        if P.px == -525 and P.py == 525 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_egida"
            end = False
        if (P.py == 975 or P.py == 925 or P.py == 875) and P.px >= 25 and face_l(P):
            P.px -= 1200
            P.py += 400
            P.loc = "route_2"
            update_locs(P)
            route_2(P,True)
            fade = False
            end = False
        if (P.px == -775 or P.px == -725 or P.px == -825) and P.py <= 225 and face_d(P):
            P.px -= 1000
            P.py += 1350
            P.loc = "route_1"
            route_1(P,True,P.egi_sci.tim,P.egi_sci.curr,P.egi_sci.x+1000)
            fade = False
            end = False
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if fade:
        fade_out(P)


def bee_zone_b(P):
    P.surface.blit(P.beez_back, (P.px, P.py))
    if P.prog[15][1] < 3:
        P.surface.blit(P.char_shad,(P.px+450,P.py+413))
        P.surface.blit(P.beez_meta,(P.px+450,P.py+388))

def bee_zone_p(P,temppx,temppy,move):
    #rects start
    # if P.beez_drill:
    #     drill = P.beez_drill.y_dist() > 0
    #     if drill:
    #         P.beez_drill.move()
    r0 = (P.px+450,P.py+300,250,40)
    r1 = (P.px+650,P.py+450,100,40)
    r3 = (P.px+400,P.py+350,50,140)
    r4 = (P.px+450,P.py+500,250,40)
    r2 = (P.px+750,P.py+400,50,40)
    r5 = (P.px+700,P.py+350,50,40)
    r6 = (P.px+500,P.py+350,50,40)
    rects = [r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        if P.prog[15][1] == 2 and P.px <= -125:
            player_move(P,rects,manual_input = 'l',spd = 3)
        else:
            player_move(P,rects)
    else:
        blit_player(P)
    if P.beez_drill:
        # if not drill:
        P.beez_drill.move(temppx,temppy)

def bee_zone_f(P,temppx,temppy,tim):
    P.surface.blit(P.beez_f,(temppx+458,temppy+350))
    set_sky(P)
    show_location(P,P.loc_txt,tim)
    

def bee_zone(P) -> None:
    if P.song != "music/route_1.wav":
        P.song = "music/route_1.wav"
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    set_location(P)
    P.habitat = 'forest'
    P.beez_back = load("p/am/Beedrill_Zone.png")
    P.beez_f = load("p/am/Beedrill_f.png")
    P.beez_meta = pygame.transform.scale(load("p/am/Metapod.png"),(50,60))
    if P.prog[15][1] == 0:
        P.beez_drill = npc.NPC(P,'Beedrill','Lightyear',[500,400],[['l',20]],["","",""])
    else:
        P.beez_drill = None
    move = True
    tim = 0
    bee_zone_b(P)
    bee_zone_p(P,P.px,P.py,False)
    bee_zone_f(P,P.px,P.py,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        bee_zone_b(P)
        temppx = P.px
        temppy = P.py
        bee_zone_p(P,temppx,temppy,move)
        bee_zone_f(P,temppx,temppy,tim)
        if P.px == -275 and P.py == -125 and P.prog[15][1] == 0:
            move = False
            P.beez_drill = npc.NPC(P,'Beedrill','Lightyear',[500,400],[['r',20]],["","",""])
            bee_zone_b(P)
            bee_zone_p(P,P.px,P.py,False)
            bee_zone_f(P,P.px,P.py,tim)
            P.beez_drill.trainer_walk = ['d',100,20]
            P.prog[15][1] += 1
        if P.prog[15][1] == 1 and P.beez_drill.y == 450:
            P.beez_drill = npc.NPC(P,'Beedrill','Lightyear',[500,450],[['u',20]],["","",""])
            bee_zone_b(P)
            bee_zone_p(P,P.px,P.py,False)
            bee_zone_f(P,P.px,P.py,tim)
            txt(P,"The Beedrill is pointing","aggresively at the Metapod.")
            P.prog[15][1] += 1
            move = True
        if P.prog[15][1] == 2 and P.px == -125:
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            P.legendary_battle = True
            P.temp_party = P.party.copy()
            pos = 0
            while len(P.party) > 1:
                if P.party[pos].code_nos() != 'Beedrill' or P.party[pos].status == 'Faint' or pos == 1:
                    P.party.remove(P.party[pos])
                else:
                    pos += 1
            battle(P,[poke.Poke('Metapod',[20,1,334,'Rejuvenate',-1,None,None,None,None,None,None,None,None,0,"Nursery Ball",300,'Shed Skin'])],no_pc = True)
            play_music(P,"music/route_1.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            if P.party[0].status == 'Faint' or P.turn_count == 4:
                if P.party[0].status == 'Faint':
                    P.party[0].status = None
                    P.party[0].ch = P.party[0].hp
                P.prog[15][1] = 0
                txt(P,"The Beedrill looked at you","disapprovingly before chasing","you out of the forest!")
                P.p = P.r1
                P.px = -975
                P.py = 1375
                P.loc = 'route_1'
                end = False
            else:
                P.prog[15][1] += 1
                P.p = P.d1
                bee_zone_b(P)
                bee_zone_p(P,P.px,P.py,False)
                bee_zone_f(P,P.px,P.py,tim)
                txt(P,"The Beedrill looked pleased.","It left a mysterious stone in","your hand before leaving.")
                add_item(P,'Beedrillite',1)
                fade_out(P)
                P.beez_drill = None
                bee_zone_b(P)
                bee_zone_p(P,P.px,P.py,False)
                bee_zone_f(P,P.px,P.py,tim)
                fade_in(P)
            P.party = P.temp_party.copy()
            P.legendary_battle = False
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                # elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                #     if event.key == pygame.key.key_code(P.controls[4]):
                #         P.buffer_talk = 10
                #     temp_buff = P.buffer_talk
                #     P.buffer_talk = None
                #     P.buffer_talk = temp_buff
        if P.px == -325 and P.py == -125 and face_r(P):
            P.px = -975
            P.py = 1375
            P.loc = 'route_1'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'r'
    fade_out(P)
    set_mixer_volume(P,P.vol)


def route_1_b(P,wx,wy):
    draw_waves(P,wx,wy)
    P.surface.blit(P.route_1,(P.px+50,P.py-2000))
    P.surface.blit(P.r1_foam,(P.px+338,P.py-760+abs(P.foam)))
    P.surface.blit(P.r1_path,(P.px+763,P.py-424))
    P.surface.blit(P.r1_grass,(P.px+2855,P.py-685))
    if P.prog[6][9] == 0:
        P.surface.blit(P.item_out,(P.px+1400,P.py-1250))

def route_1_p(P,temppx,temppy,move = False):
    timmy = P.r1_timmy.y_dist()
    amy = P.r1_amy.y_dist()
    robb = P.r1_robb.y_dist()
    noland = P.r1_noland.y_dist()
    if timmy > 0:
        P.r1_timmy.move()
    if amy > 0:
        P.r1_amy.move()
    if noland > 0:
        P.r1_noland.move()
    P.r1_sci.move()
    if robb > 0:
        P.r1_robb.move()
        draw_grass(P,P.r1_robb.x,P.r1_robb.y,-1025,1525,600,200,[P.px,P.py])
        draw_grass(P,P.r1_robb.x,P.r1_robb.y,-1025,1325,200,250,[P.px,P.py])
    if P.r1_rival != None:
        P.r1_rival.move()
    #rects start
    r1 = (P.px+450,P.py-250,1500,50)
    r2 = (P.px+450,P.py-450,750,40)
    r3 = (P.px+400,P.py-400,50,150)
    r4 = (P.px+1150,P.py-800,50,350)
    r5 = (P.px+1200,P.py-850,200,40)
    r6 = (P.px+1300,P.py-600,200,90)
    r7 = (P.px+1350,P.py-1250,50,140)
    r70 = (P.px+1300,P.py-1100,50,40)
    r71 = (P.px+1350,P.py-1050,50,190)
    r8 = (P.px+1400,P.py-1300,700,40)
    r9 = (P.px+2250,P.py-1300,200,40)
    r10 = (P.px+2450,P.py-1250,50,740)
    r11 = (P.px+1950,P.py-800,300,190)
    r12 = (P.px+1950,P.py-400,50,140)
    r13 = (P.px+1950,P.py-400,950,50)
    r14 = (P.px+2450,P.py-550,450,40)
    r15 = r1
    if P.px == -1525 and (P.py <= 875 and P.py >= 725):
        r15 = (P.px+1950,P.py-600,50,200)
    elif P.prog[6][9] == 0:
        r15 = (P.px+1400,P.py-1250,50,40)
    r21 = r1
    if P.r1_rival != None:
        r21 = P.r1_rival.get_rect()
    r16 = P.r1_timmy.get_rect()
    r18 = P.r1_amy.get_rect()
    r19 = P.r1_robb.get_rect()
    r20 = P.r1_noland.get_rect()
    r17 = (P.px+2900,P.py-500,50,90)
    rects = [r71,r70,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    P.ledge = 0
    if (P.py <= 875 and P.py >= 725):
        if P.px > -1575 and P.px < -1550:
            P.ledge = -((1575+P.px)/1.5)
        elif P.px >= -1550 and P.px < -1525:
            P.ledge = (1525+P.px)/1.5
    if move:
        if P.px == -975 and P.py == 1375:
            player_move(P,rects,manual_input = 'r')
        else:
            player_move(P,rects)
    else:
        blit_player(P)
    draw_grass(P,temppx,temppy,-1025,1525,600,200,ignore = [(-1025,1525)])
    draw_grass(P,temppx,temppy,-1025,1325,200,250)
    draw_grass(P,temppx,temppy,-1875,1525,200,300)
    draw_grass(P,temppx,temppy,-1875,1075,200,200)
    if timmy <= 0:
        P.r1_timmy.move(temppx,temppy)
    if amy <= 0:
        P.r1_amy.move(temppx,temppy)
    if noland <= 0:
        P.r1_noland.move(temppx,temppy)
    if robb <= 0:
        P.r1_robb.move(temppx,temppy)
        draw_grass(P,P.r1_robb.x,P.r1_robb.y,-1025,1525,600,200,[temppx,temppy])
        draw_grass(P,P.r1_robb.x,P.r1_robb.y,-1025,1325,200,250,[temppx,temppy])

def route_1_f(P,temppx,temppy,listx,listy,tim):
    if int(tim/3)%2 == 0:
        P.surface.blit(P.egi_gen,(temppx+1425,temppy-2303))
    P.surface.blit(P.egi_f,(temppx+1395,temppy-2036))
    P.surface.blit(P.r1_trees,(temppx+1940,temppy-858))
    P.surface.blit(P.r1_statue,(temppx+1284,temppy-1133))
    P.surface.blit(P.r1_bridge_l,(temppx+450,temppy-450))
    P.surface.blit(P.r1_fence,(temppx+541,temppy-275))
    draw_lamps(P,temppx,temppy,listx,listy)
    show_location(P,P.loc_txt,tim)

def route_1(P,enter = False,sci_tim = None,sci_curr = None,x_pos = 2500) -> None:
    if P.song != "music/route_1.wav":
        P.song = "music/route_1.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.r1_sci = npc.NPC(P,'Scientistm','Nerd',[x_pos,-1500],[['mr',60],['r',60],['ml',60],['l',80]],["The energy we get from the","Vigore Dam is enough to power","the entire city!","With all the research we've","been doing here, it may not be","that long until we can power","the entire island using only","renewable energy!",""],tim = sci_tim,curr = sci_curr)
    if P.prog[0] == 16:
        P.r1_rival = npc.NPC(P,'Rival',P.save_data.rival,[2150,-1300],[['u',100]],["","",""])
    else:
        P.r1_rival = None
    P.habitat = 'grass'
    set_location(P)
    listx = [0]
    listy = [0]
    wx = 0
    wy = 0
    tim = 0
    noland_talk = 50
    if enter == False:
        route_1_b(P,wx,wy)
        route_1_p(P,P.px,P.py)
        route_1_f(P,P.px,P.py,listx,listy,tim)
        fade_in(P)
    bee_in = False
    end = True
    move = True
    pause = False
    m = 0
    fade = True
    while end:
        #print(P.px,P.py)
        route_1_b(P,wx,wy)
        if move == True and P.r1_timmy.trainer_check():
            move = False
        if move == True and P.r1_amy.trainer_check():
            move = False
        if move == True and P.r1_robb.trainer_check():
            move = False
        if move == True and noland_talk > 50 and P.r1_noland.trainer_check():
            move = False
        temppx = P.px
        temppy = P.py
        if P.py == 1525 and move and P.prog[0] == 16:
            if P.px == -1725:
                move = False
                P.prog[0] += 1
                P.p = P.u1
                P.r1_rival = npc.NPC(P,'Rival',P.save_data.rival,[2150,-1300],[['ml',20],['d',10]],["","",""])
            elif P.px == -1775:
                move = False
                P.prog[0] += 1
                P.p = P.u1
                P.r1_rival = npc.NPC(P,'Rival',P.save_data.rival,[2150,-1300],[['d',10]],["","",""])
            elif P.px == -1825:
                move = False
                P.prog[0] += 1
                P.p = P.u1
                P.r1_rival = npc.NPC(P,'Rival',P.save_data.rival,[2150,-1300],[['mr',20],['d',10]],["","",""])
        route_1_p(P,temppx,temppy,move)
        route_1_f(P,temppx,temppy,listx,listy,tim)
        if P.px == -975 and P.py == 1375 and face_l(P):
            if P.prog[15][0] == 0:
                txt(P,"There are swarms of Beedrill","buzzing around.")
                print_mega_area(P)
            elif P.prog[15][1] == 0:
                txt(P,"There are swarms of Beedrill","buzzing around.")
                if in_party(P,'Beedrill',True):
                    new_txt(P)
                    write(P,"Enter the forest?")
                    if choice(P):
                        bee_in = True
                else:
                    txt(P,"If you brought a Beedrill you","could probably enter the","forest unharmed.")
            else:
                bee_in = True
        if P.prog[0] == 17 and P.r1_rival.face() == 'd':
            te = P.surface.copy()
            txt(P,"Hey there "+P.save_data.name+"!","Looks like your team has grown","a lot since we last met.")
            txt(P,"Let's have a friendly match","to see who's stronger!")
            play_music(P,"music/trainer_battle.wav",0)
            P.habitat = 'road'
            battle(P,["Rival "+P.save_data.rival,poke.Poke('Pidgey',[5,0,334,"Tackle",-1,"Sand Attack",-1,None,None,None,None,None,None,0,"Poke Ball",0,'Keen Eye']),get_rival_poke(P,0),get_rival_poke(P,1)])
            P.habitat = 'grass'
            play_music(P,"music/route_1.wav")
            P.surface.blit(te,(0,0))
            fade_in(P)
            txt(P,"Wow you're a fast learner!","I can tell you've trained your","Pokemon well.")
            txt(P,"Anyways, I sure hope the gym","leader in Egida City isn't out","as well.")
            txt(P,"Catch you later!")
            P.r1_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.r1_rival.x,P.r1_rival.y],[['mu',120]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 18 and P.r1_rival.y == -1600:
            P.r1_rival = None
            P.prog[0] += 1
            move = True
        if trainer_check(P,P.r1_timmy,"music/route_1.wav"):
            P.r1_timmy = npc.NPC(P,'Youngster','Timmy',[P.r1_timmy.x,P.r1_timmy.y],[[P.r1_timmy.face(),100]],["Why won't anyone listen","to me?",""])
            move = True
        if trainer_check(P,P.r1_amy,"music/route_1.wav"):
            P.r1_amy = npc.NPC(P,'Lass','Amy',[P.r1_amy.x,P.r1_amy.y],[[P.r1_amy.face(),100]],["My teacher could learn a thing","or two from you.",""])
            move = True
        if trainer_check(P,P.r1_robb,"music/route_1.wav"):
            P.r1_robb = npc.NPC(P,'Bug Catcher','Robb',[P.r1_robb.x,P.r1_robb.y],[[P.r1_robb.face(),100]],["I bet there's an even cooler","Pokemon hiding in this grass!",""])
            move = True
        if noland_talk > 50 and trainer_check(P,P.r1_noland,"music/route_1.wav"):
            if P.prog[5][3] == 0:
                P.r1_noland = npc.NPC(P,'Gentleman','Noland',[2850,-500],[['r',100]],["It's not often I see a new","adventurer around here.","","Perhaps you would be willing", "to entertain this old man with","a battle?"],["Hmmph!","That certainly brought back","old memories!","It's been ages since I got","this heated over a Pokemon","battle!","Who knows, maybe you have what", "it takes to beat the champion!","Ha!"],True,[50,150,50,200],[poke.Poke('Nidorino',[16,0,334,"Focus Energy",-1,"Leer",-1,"Double Kick",-1,"Poison Sting",-1,None,None,0,"Poke Ball",0,"Rivalry"]),poke.Poke('Nidorina',[16,1,334,"Growl",-1,"Scratch",-1,"Poison Sting",-1,"Double Kick",-1,None,None,0,"Poke Ball",0,"Rivalry"])],3,loc = "route_1")
                noland_talk = 0
                move = True
            else:
                if face_r(P):
                    P.r1_noland = npc.NPC(P,'Gentleman','Noland',[P.r1_noland.x,P.r1_noland.y],[['md',20],['ml',200]],["","",""])
                else:
                    P.r1_noland = npc.NPC(P,'Gentleman','Noland',[P.r1_noland.x,P.r1_noland.y],[['ml',200]],["","",""])
        if move == False and P.r1_noland.x == 2350:
            move = True
            P.r1_noland = npc.NPC(P,'Gentleman','Noland',[1500,-550],[['l',100]],["I still remember when this was","a statue of Cynthia back when","she oversaw the city.","I heard you can still find","that statue standing in the", "Alto Mare gym."])
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.r1_timmy.talk():
                        if P.r1_timmy.trainer:
                            move = False
                        else:
                            route_1_b(P,wx,wy)
                            route_1_p(P,P.px,P.py,False)
                            route_1_f(P,P.px,P.py,listx,listy,tim)
                            P.r1_timmy.write()
                    elif next_to(P,1400,-1250) and P.prog[6][9] == 0:
                        txt(P,P.save_data.name + " found an Everstone!")
                        txt(P,P.save_data.name + " put the Everstone","in the Items pocket.")
                        add_item(P,"Everstone",1)
                        P.prog[6][9] = 1
                    elif P.r1_amy.talk():
                        if P.r1_amy.trainer:
                            move = False
                        else:
                            route_1_b(P,wx,wy)
                            route_1_p(P,P.px,P.py,False)
                            route_1_f(P,P.px,P.py,listx,listy,tim)
                            P.r1_amy.write()
                    elif P.r1_robb.talk():
                        if P.r1_robb.trainer:
                            move = False
                        else:
                            route_1_b(P,wx,wy)
                            route_1_p(P,P.px,P.py,False)
                            route_1_f(P,P.px,P.py,listx,listy,tim)
                            P.r1_robb.write()
                    elif noland_talk > 50 and P.r1_noland.talk():
                        if P.r1_noland.trainer:
                            move = False
                        else:
                            route_1_b(P,wx,wy)
                            route_1_p(P,P.px,P.py,False)
                            route_1_f(P,P.px,P.py,listx,listy,tim)
                            P.r1_noland.write()
                    elif next_to(P,1300,-550) or next_to(P,1350,-550) or next_to(P,1400,-550) or next_to(P,1450,-550) or next_to(P,1300,-600) or next_to(P,1350,-600) or next_to(P,1400,-600) or next_to(P,1450,-600):
                        if face_u(P):
                            txt(P,"Zinnia: Guardian of Alto Mare")
                        else:
                            txt(P,"It's a large statue of someone","with a Salamence and Whismur.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 675 or P.py == 625 or P.py == 575) and P.px == -75 and face_l(P):
            P.px -= 1650
            P.py += 1150
            P.move_out_dir = 'l'
            P.loc = "north_am"
            end = False
        if bee_in and P.px == -975 and P.py == 1375 and face_l(P):
            P.px = -325
            P.py = -125
            P.loc = 'beedrill'
            P.move_out_dir = 'l'
            fade = False
            end = False
        if (P.px == -1775 or P.px == -1725 or P.px == -1825) and P.py >= 1575 and face_u(P):
            P.px += 1000
            P.py -= 1350
            P.loc = "egida"
            update_locs(P)
            egida(P,True,P.r1_sci.tim,P.r1_sci.curr,P.r1_sci.x-1000)
            fade = False
            end = False
        if move and (wild_grass(P,-1025,1525,600,200,ignore = [(-1025,1525)]) or wild_grass(P,-1025,1325,200,250) or wild_grass(P,-1875,1525,200,300) or wild_grass(P,-1875,1075,200,200)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < .07:
                #r = random.randint(6,7)
                # if r < 9:
                #     battle(P,[poke.Poke('Scyther',[r,random.randint(0,1),334,"Vacuum Wave",-1,"Quick Attack",-1,"Leer",-1,"Focus Energy",-1,None,None,0,"Poke Ball"])])
                # else:
                battle(P,[poke.Poke('Scyther',[random.randint(6,7),random.randint(0,1),334,"Vacuum Wave",-1,"Quick Attack",-1,"Leer",-1,"Focus Energy",-1,None,None,0,"Poke Ball"])])
            elif rando >= .07 and rando < .35:
                battle(P,[poke.Poke('Weedle',[random.randint(3,5),random.randint(0,1),334,"Poison Sting",-1,"String Shot",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .35 and rando < .6:
                r = random.randint(4,6)
                if r < 5:
                    battle(P,[poke.Poke('Pidgey',[r,random.randint(0,1),334,"Tackle",-1,None,None,None,None,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Pidgey',[r,random.randint(0,1),334,"Tackle",-1,"Sand Attack",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .6 and rando < .75:
                battle(P,[poke.Poke('Bellsprout',[random.randint(4,6),random.randint(0,1),334,"Vine Whip",-1,None,None,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .75 and rando < .9:
                battle(P,[poke.Poke('Poochyena',[random.randint(4,6),random.randint(0,1),334,"Tackle",-1,"Howl",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .9:
                battle(P,[poke.Poke('Oddish',[random.randint(5,6),random.randint(0,1),334,"Absorb",-1,"Growth",-1,"Sweet Scent",-1,None,None,None,None,0,"Poke Ball"])])
            P.song = "music/route_1.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        noland_talk += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
        if pause:
            P.clock.tick(P.ani_spd/30)
            pause = False
    if fade:
        fade_out(P,P.song)
    elif P.loc == 'beedrill':
        fade_out(P)

def poke_center_b(P,heal,poke_list,pokemon_list):
    P.surface.fill((0,0,0))
    P.surface.blit(P.pc_back,(P.px,P.py+100))
    if heal < 220:
        P.surface.blit(poke_list[0],(P.px+210,P.py+233))
        P.surface.blit(pokemon_list[0],(P.px+185,P.py+145))
        if len(P.party) < 2 and heal < 75:
                heal = 75
    if heal > 15 and heal < 215 and len(P.party) > 1:
        P.surface.blit(poke_list[1],(P.px+227,P.py+249))
        P.surface.blit(pokemon_list[1],(P.px+195,P.py+190))
        if len(P.party) < 3 and heal < 75:
            heal = 75
    if heal > 30 and heal < 210 and len(P.party) > 2:
        P.surface.blit(poke_list[2],(P.px+250,P.py+258))
        P.surface.blit(pokemon_list[2],(P.px+255,P.py+155))
        if len(P.party) < 4 and heal < 75:
            heal = 75
    if heal > 45 and heal < 205 and len(P.party) > 3:
        P.surface.blit(poke_list[3],(P.px+278,P.py+258))
        P.surface.blit(pokemon_list[3],(P.px+260,P.py+200))
        if len(P.party) < 5 and heal < 75:
            heal = 75
    if heal > 60 and heal < 200 and len(P.party) > 4:
        P.surface.blit(poke_list[4],(P.px+302,P.py+249))
        P.surface.blit(pokemon_list[4],(P.px+315,P.py+145))
        if len(P.party) < 6 and heal < 75:
            heal = 75
    if heal > 75 and heal < 195 and len(P.party) > 5:
        P.surface.blit(poke_list[5],(P.px+318,P.py+233))
        P.surface.blit(pokemon_list[5],(P.px+325,P.py+190))
    if heal == 300 and P.prog[13] != None and P.prog[13][2] != 0:
        P.surface.blit(P.pc_cake,(P.px+225,P.py+145))
    P.surface.blit(P.pc_machine,(P.px+175,P.py+120))
    P.surface.blit(P.pc_nurse,(P.px+250,P.py+300))
    P.surface.blit(P.char_shad,(P.px+452,P.py+563))
    P.surface.blit(P.pc_clerk,(P.px+450,P.py+534))
    P.surface.blit(P.pc_wall,(P.px+250,P.py+350))

def poke_center_p(P,temppx,temppy,heal):
    if P.pc_npc1:
        one = P.pc_npc1.y_dist() > 0
        if one:
            P.pc_npc1.move()
    if P.pc_npc2:
        two = P.pc_npc2.y_dist() > 0
        if two:
            P.pc_npc2.move()
    if P.pc_npc3:
        three = P.pc_npc3.y_dist() > 0
        if three:
            P.pc_npc3.move()
    if P.pc_candy:
        candy = P.pc_candy.y_dist() > 0
        if candy:
            P.pc_candy.move()
    r1 = (P.px+150,P.py+250,250,140)
    r2 = (P.px,P.py+250,550,40)
    r3 = (P.px+50,P.py+500,100,90)
    r4 = (P.px+400,P.py+350,50,40)
    r5 = (P.px+400,P.py+450,150,190)
    r6 = (P.px-50,P.py+300,50,350)
    r7 = (P.px+550,P.py+300,50,350)
    r8 = (P.px,P.py+650,550,50)
    r9 = (P.px,P.py+300,150,40)
    r10,r11,r12,r13 = r1,r1,r1,r1
    if P.pc_npc1:
        r10 = P.pc_npc1.get_rect()
    if P.pc_npc2:
        r11 = P.pc_npc2.get_rect()
    if P.pc_npc3:
        r12 = P.pc_npc3.get_rect()
    if P.pc_candy:
        r13 = P.pc_candy.get_rect()
    rects = [r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    if heal < 300:
        blit_player(P)
    else:
        if P.prog[13] != None and P.prog[13][2] == 2 and P.py < -125:
            player_move(P,rects,manual_input = 'u')
        elif P.prog[13] != None and P.prog[13][2] not in [0,4]:
            blit_player(P)
        else:
            player_move(P,rects)
    if P.pc_npc1:
        if not one:
            P.pc_npc1.move(temppx,temppy)
    if P.pc_npc2:
        if not two:
            P.pc_npc2.move(temppx,temppy)
    if P.pc_npc3:
        if not three:
            P.pc_npc3.move(temppx,temppy)
    if P.pc_candy:
        if not candy:
            P.pc_candy.move(temppx,temppy)
    #rects end

def poke_center_f(P,temppx,temppy):
    P.surface.blit(P.pc_cpu,(temppx+400,temppy+322))
    P.surface.blit(P.pc_couch,(temppx,temppy+487))
    if P.prog[13] != None and P.prog[13][2] in [1,2]:
        P.surface.blit(P.pc_dark,(0,0))

def poke_center(P,loc) -> None:
    P.pc_npc1 = None
    P.pc_npc2 = None
    P.pc_npc3 = None
    birthday = False
    if P.prog[13] != None and datetime.datetime.now().month == P.prog[13][0] and datetime.datetime.now().day == P.prog[13][1] and party_fainted(P) == False and P.prog[13][2] == 0:
        birthday = True
        P.prog[13][2] += 1
    if P.prog[13] != None and (datetime.datetime.now().month != P.prog[13][0] or datetime.datetime.now().day != P.prog[13][1]) and P.prog[13][2] != 0:
        P.prog[13][2] = 0    
    P.pc_candy = None
    if loc == 'am':
        P.pc_npc1 = npc.NPC(P,'Lass','Reader',[100,350],[['u',40]],["Did you know that Oddish will", "wander up to 1000 feet during", "the night to scatter its seeds", "and find a nutrient-rich patch", "of soil to plant itself in?", "","Turns out books can be quite","interesting sometimes. Who","could've guessed?"])
        P.pc_npc2 = npc.NPC(P,'Triathelete','Runner',[0,550],[['r',40]],["","",""])
        if P.prog[9] == 1 and get_time() in [6,14,22]:
            if P.px == -125 and P.py == -25:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[450,300],[['d',40]],[""])
            else:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[500,300],[['d',40]],[""])
    elif loc == 'egida':
        P.pc_npc1 = npc.NPC(P,'Preschoolerg','Kate',[0,550],[['r',40]],["Hi! I'm Tate!","",""])
        P.pc_npc2 = npc.NPC(P,'Preschoolerg','Sally',[0,500],[['r',40]],["Hi! I'm Liza!","",""])
        P.pc_npc3 = npc.NPC(P,'Youngster','Jojo',[500,400],[['l',40]],["Those two won't stop staring","at me. It's starting to give","me the creeps.","How long does it take to heal","a few Pokemon anyways?",""])
        if P.prog[9] == 1 and get_time() in [4,12,20]:
            if P.px == -125 and P.py == -25:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[450,300],[['d',40]],[""])
            else:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[500,300],[['d',40]],[""])
    elif loc == 'fiore':
        P.pc_npc1 = npc.NPC(P,'Poke Fan','Sleepy',[50,600],[['u',40]],["Zzz...Zzz...","Hey, stop! That tickles!",""])
    elif loc == 'pianura':
        P.pc_npc1 = npc.NPC(P,'Gentleman','Friend',[0,550],[['r',40]],["Always make sure to take good","care of your Pokemon.","","The potential of a Pokemon","lies in the relationship it","has with its trainer."])
        P.pc_npc2 = npc.NPC(P,'Beauty','Trainer',[200,400],[['u',40]],["I really hope my precious","Skitty is okay...","","I'll never forgive that ugly","Poochyena for brutally biting","my little baby!"])
        if get_time() >= 7 and get_time() < 11 and P.prog[0] >= 87:
            x = 0
            if P.px == 325 and P.py == -75:
                x = 50
            P.pc_npc3 = npc.NPC(P,'Cheryl','Jojo',[50+x,350],[['u',40]],["Hey there "+P.save_data.name+"!","Make sure to keep your Pokemon","well rested!","That's the easiest step to","building a good relationship","with them!"])
        if P.prog[9] == 1 and get_time() in [8,16,0]:
            if P.px == -125 and P.py == -25:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[450,300],[['d',40]],[""])
            else:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[500,300],[['d',40]],[""])
    elif loc == 'isola':
        P.pc_npc1 = npc.NPC(P,'Fisherman','Sleepy',[100,400],[['ml',20],['l',80],['mr',20],['r',140]],["Just the other day I was on a","walk outside when a Wailord","leaped out of the water!","It was so huge it scared the","bejeebers outta me!",""])
    elif loc == 'verde':
        if P.prog[9] == 1 and get_time() in [10,18,2]:
            if P.px == -125 and P.py == -25:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[450,300],[['d',40]],[""])
            else:
                P.pc_candy = npc.NPC(P,'Candyman','Bro',[500,300],[['d',40]],[""])
    if P.pc_candy:
        song = "music/pc_candy.wav"
    else:
        song = "music/pc.wav"
    if P.prog[13] != None and P.prog[13][2] == 4:
        song = "music/birthday_pc.wav"
    if P.song != song and birthday == False:
        P.song = song
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.pc_back = load("p/am/poke_center_inside.png")
    P.pc_nursef = load("p/spr/nj_d1.png")
    P.pc_nurseb = load("p/spr/nj_u1.png")
    P.pc_dark = load("p/pianura/cave_darkness.png")
    P.pc_cake = load("p/pianura/pc_cake.png")
    P.pc_nurse = P.pc_nursef
    P.pc_clerk = pygame.transform.scale(load("p/spr/mart_clerk_l1.png"),(55,66))
    P.pc_cpu = load("p/am/cpu_top.png")
    P.pc_wall = load("p/am/poke_center_wall.png")
    machine1 = load("p/am/pc_machine.png")
    machine2 = load("p/am/pc_machine_2.png")
    P.pc_machine = machine1
    P.pc_couch = load("p/am/pc_couch.png")
    box = load("p/3_box.png")
    heal = 300
    m = 0
    tim = 0
    plugged = 1
    poke_list = []
    pokemon_list = []
    poke_center_b(P,heal,[],[])
    poke_center_p(P,P.px,P.py,300)
    poke_center_f(P,P.px,P.py)
    end = True
    fade_in(P)
    while end:
        #print(P.px,P.py)
        if P.prog[13] != None and P.prog[13][2] == 3:
            P.clock.tick(1)
            txt(P,"Happy Birthday " + P.save_data.name+"!")
            P.song = "music/birthday_pc.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            txt(P,"Take this gift to commemorate","this special day!")
            txt(P,"You received a Balm Mushroom!")
            add_item(P,"Balm Mushroom",1)
            txt(P,"I hope this will be a","wonderful year for you!")
            P.prog[13][2] += 1
        if P.prog[13] != None and P.prog[13][2] == 1:
            P.clock.tick(1)
            P.prog[13][2] += 1
        if P.px == 125 and P.py == -125 and P.prog[13] != None and P.prog[13][2] == 2:
            P.clock.tick(1)
            P.prog[13][2] += 1
            set_channel_volume(P,P.sfx_vol,1)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('music/sfx/birthday_pop.wav'))
        if P.px == 125 and P.py == -125 and party_fainted(P) and tim == 0:
            P.pc_nurse = P.pc_nurseb
            heal = 0
            poke_list = []
            pokemon_list = []
            for x in P.party:
                pokemon_list.append(pygame.transform.scale(load("p/poke/"+x.code+"_full.png"),(40,40)))
            for x in P.party:
                poke_list.append(pygame.transform.scale(load("p/spr/enemy_"+x.ball+"_1.png"),(25,43)))
        poke_center_b(P,heal,poke_list,pokemon_list)
        temppx = P.px
        temppy = P.py
        poke_center_p(P,temppx,temppy,heal)
        poke_center_f(P,temppx,temppy)
        #rect_draw(P,rects)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20 and heal == 300:
                if event.key == pygame.key.key_code(P.controls[6]):
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 25 and P.py == -275 and face_r(P):
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Welcome to the Poke Mart!","May I help you?")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            poke_mart(P, mt)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P, "Is there anything else I", "may do for you?")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50                                        
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"Please come again!")
                        #P.surface.blit(mt,(0,0))
                        #update_screen(P)
                    elif P.px == -25 and P.py == -25 and face_u(P):
                        if plugged == 1:
                            txt(P,"You plugged out the computer.")
                            plugged = 0
                        else:
                            txt(P,"You plugged the computer back", "in.")
                            plugged = 1
                    elif P.px == -25 and P.py == -125 and face_u(P):
                        t = P.surface.copy()
                        if plugged == 1:
                            txt(P,P.save_data.name+" booted up the", "computer.")
                            fade_out(P)
                            open_cpu(P)
                            P.surface.blit(t,(0,0))
                            fade_in(P)
                        else:
                            txt(P,"The computer won't boot up.")
                    elif P.px == 125 and P.py == -125 and face_u(P):
                        new_txt(P)
                        write(P,"Welcome to the Pokemon Center.","Would you like to rest your", "Pokemon?")
                        if choice(P,550,600):
                            txt(P,"Okay, I'll take your Pokemon", "for a few seconds then.")
                            P.pc_nurse = P.pc_nurseb
                            heal = 0
                            poke_list = []
                            pokemon_list = []
                            for x in P.party:
                                pokemon_list.append(pygame.transform.scale(load("p/poke/"+x.code+"_full.png"),(40,40)))
                            for x in P.party:
                                poke_list.append(pygame.transform.scale(load("p/spr/enemy_"+x.ball+"_1.png"),(25,43)))
                        else:
                            txt(P,"Good luck on your adventure!")
                    elif P.pc_candy and P.pc_candy.talk():
                        poke_center_b(P,heal,poke_list,pokemon_list)
                        poke_center_p(P,P.px,P.py,heal)
                        poke_center_f(P,P.px,P.py)
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Hey there Munchkin!","Wanna buy some sweets?")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            poke_mart(P, mt, candy = True)
                                            new_txt(P)
                                            write(P, "Need anything else cupcake?", "I got you covered.")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P, True)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P, "Need anything else cupcake?", "I got you covered.")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"Hee hee, pleasure doing","business with ya!")
                    elif P.pc_npc1 and P.pc_npc1.talk():
                        poke_center_b(P,heal,poke_list,pokemon_list)
                        poke_center_p(P,P.px,P.py,heal)
                        poke_center_f(P,P.px,P.py)
                        P.pc_npc1.write()
                    elif P.pc_npc2 and P.pc_npc2.talk():
                        poke_center_b(P,heal,poke_list,pokemon_list)
                        poke_center_p(P,P.px,P.py,heal)
                        poke_center_f(P,P.px,P.py)
                        if P.loc == 'pc_am':
                            txt(P,"Press ["+P.controls[5]+"] to run!","Feel the wind blowing through", "your hair!")
                            txt(P,"Indoors, outdoors, everything","is better when you're running!","")
                            txt(P,"Too bad I'm stuck here waiting","for my Pokemon to finish","resting.")
                        else:
                            P.pc_npc2.write()
                    elif P.pc_npc3 and P.pc_npc3.talk():
                        poke_center_b(P,heal,poke_list,pokemon_list)
                        poke_center_p(P,P.px,P.py,heal)
                        poke_center_f(P,P.px,P.py)
                        P.pc_npc3.write()
                    elif next_to(P,0,300):
                        txt(P,"These are some pretty roses!")
                    elif next_to(P,50,300) or next_to(P,100,300):
                        if loc == 'fiore':
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.09:","Karrablast and Shelmet","Read?")
                            if choice(P):
                                txt(P,"Karrablast and Shelmet have a","peculiar relationship with","each other.")
                                txt(P,"When they are both present at","a mature level of 30, they","undergo evolution.")
                                txt(P,"During this process, the","Karrablast takes the shell of","the Shelmet to armor itself.")
                        elif loc == 'am':
                            new_txt(P)
                            write(P,"Oddish: The Weed Pokemon","Read?")
                            if choice(P):
                                txt(P,"Oddish will wander up to 1000","feet during the night to","scatter its seeds and find a")
                                txt(P,"nutrient-rich patch of soil to","plant itself in.")
                        elif loc == 'egida':
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.01:","Evolution Stones","Read?")
                            if choice(P):
                                txt(P,"While most Pokemon evolve upon","reaching a certain level, some","need other conditions.")
                                txt(P,"When exposed to special stones","known as Evolution stones,","some Pokemon will evolve.")
                        elif loc == 'pianura':
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.04:","Friendship Evolution","Read?")
                            if choice(P):
                                txt(P,"Some Pokemon will only evolve","when the bond with its trainer","is strong enough.")
                                txt(P,"This bond is commonly referred","to as the Pokemon's friendship","level.")
                        elif loc == 'isola':
                            new_txt(P)
                            write(P,"Guide to Pokemon Candies","Read?")
                            if choice(P):
                                txt(P,"Pokemon will gain experience","points when consuming Pokemon","Candies.")
                                txt(P,"The quality of the Candy will","affect how much experience the","Pokemon gains.")
                                txt(P,"However, Pokemon won't gain","friendship when leveling from","eating Candies.")
                        else:
                            txt(P,"There's nothing interesting to","read here.")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 125 and P.py == -325 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            if loc == "am":
                P.px = -525
                P.py = 1425
                P.loc = "north_am"
                end = False
            if loc == "egida":
                P.px = -525
                P.py = 525
                P.loc = "egida"
                end = False
            if loc == "fiore":
                P.py = 325
                P.px = -425
                P.loc = "fiore"
                end = False
            if loc == "pianura":
                P.py = -975
                P.px = -975
                P.loc = "pianura"
                end = False
            if loc == 'isola':
                P.py = 125
                P.px = -375
                P.loc = 'isola'
                end = False
            if loc == 'verde':
                P.py = 125
                P.px = -725
                P.loc = 'verde'
                end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if heal == 166:
            heal += (6-len(P.party))*5
        if heal == 225:
            P.pc_nurse = P.pc_nursef
        if heal == 95 or heal == 115 or heal == 135 or heal == 155:
            poke_list = []
            for x in P.party:
                poke_list.append(pygame.transform.scale(load("p/spr/enemy_"+x.ball+"_3.png"),(25,43)))
        if heal == 105 or heal == 125 or heal == 145 or heal == 165:
            poke_list = []
            for x in P.party:
                poke_list.append(pygame.transform.scale(load("p/spr/enemy_"+x.ball+"_1.png"),(25,43)))
        if tim % 10 == 0:
            if P.pc_machine == machine1:
                P.pc_machine = machine2
            else:
                P.pc_machine = machine1
        if heal == 230:
            txt(P,"Thank you for waiting.")
            txt(P,"We've restored your Pokemon","to full health.")
            txt(P,"We hope to see you again!")
            heal_party(P)
            heal = 300
        if heal < 300:
            heal += 1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P,P.song)
    if P.prog[9] == 0:
        P.prog[9] = 1
        
def house_3_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.h3_back, (P.px, P.py))

def house_3_p(P,temppx,temppy,move):
    if P.h3_npc1:
        one = P.h3_npc1.y_dist() > 0
        if one:
            P.h3_npc1.move()
    if P.h3_npc2:
        two = P.h3_npc2.y_dist() > 0
        if two:
            P.h3_npc2.move()
    #rects start
    r0 = (P.px,P.py+100,200,40)
    r1 = (P.px+450,P.py+100,100,40)
    r2 = (P.px+200,P.py+50,250,40)
    r3 = (P.px-50,P.py+150,50,240)
    r4 = (P.px,P.py+400,550,40)
    r5 = (P.px+550,P.py+100,50,290)
    r6 = (P.px+150,P.py+250,100,90)
    r7,r8 = r1,r1
    if P.h3_npc1:
        r7 = P.h3_npc1.get_rect()
    if P.h3_npc2:
        r8 = P.h3_npc2.get_rect()
    rects = [r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.h3_npc1:
        if not one:
            P.h3_npc1.move(temppx,temppy)
    if P.h3_npc2:
        if not two:
            P.h3_npc2.move(temppx,temppy)

def house_3_f(P,temppx,temppy):
    pass

def house_3(P,num) -> None:
    music = None
    if num == 1:
        music = "music/fiore.wav"
    elif num <= 4:
        music = "music/isola.wav"
    set_mixer_volume(P,P.vol)
    if P.song != music:
        P.song = music
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.h3_back = load("p/fiore/house_3.png")
    P.h3_npc1 = None
    P.h3_npc2 = None
    if num == 1:
        if not (datetime.datetime.today().weekday() == 5 and get_time() >= 6 and P.prog[1] == 3):
            P.h3_npc1 = npc.NPC(P,'Gentleman','Pineapple',[250,250],[['l',40]],["Thanks again for the help!","Don't forget to stop by my","stand in Alto Mare!"])
    elif num == 2:
        P.h3_npc1 = npc.NPC(P,'Preschoolerb','Clamperl',[100,300],[['r',40]],["This Loudred is so much more","interesting than that lame","Clamperl!","I just hope my mom doesn't get","too mad at me for giving it","away!"])
    elif num == 4:
        P.h3_npc1 = npc.NPC(P,'Hiker','Nature',[50,150],[['u',40]],["I feel like living in Isola","Town is the perfect balance","between city and nature!","I can go out and take in the","fresh air, but always come","back to relax in my home!"])
    # elif num == 10:
    #     P.h1_npc1 = npc.NPC(P,'Preschoolerb','Kid',[300,300],[['u',40]],["Oh...Looks like mom forgot to","lock the door again. That's","the third time this week...","What if someone just came in","here and kidnapped me? That'd","be pretty scary!","Well I'm pretty sure that only","happens in movies and stuff.","Right?"])
    move = True
    tim = 0
    house_3_b(P)
    house_3_p(P,P.px,P.py,False)
    house_3_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        house_3_b(P)
        temppx = P.px
        temppy = P.py
        house_3_p(P,temppx,temppy,move)
        house_3_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.h3_npc1 and P.h3_npc1.talk():
                        house_3_b(P)
                        house_3_p(P,P.px,P.py,False)
                        house_3_f(P,P.px,P.py)
                        if P.h3_npc1.name == 'Pineapple':
                            if P.prog[1] == 0:
                                txt(P,"My Pinab Berries haven't been","doing that well lately.")
                                txt(P,"I feel like there's a pest","running rampant in there, but","I can't seem to find it.")
                                txt(P,"Do you think you could take a","look for me? I'm starting to","run out of options.")
                                txt(P,"If something is running loose,","you could try baiting it out","with a berry.")
                                P.prog[1] = 1
                            elif P.prog[1] == 1:
                                txt(P,"Have you been able to see if","there's anything off about the", "garden?")
                                txt(P,"The residents of Alto Mare","love my Pinaps, but I can't","sell ones like these.")
                                txt(P,"If you had a berry, whatever","is causing the trouble might","come out.")
                            elif P.prog[1] == 2:
                                txt(P,"I don't know what you managed","to do, but it's been working","wonders!")
                                txt(P,"I spend my Saturdays selling","my berries in Alto Mare with","the other lady in town.")
                                txt(P,"If you find the time to stop","by, I'll be sure to reward you","for helping me out!")
                                P.prog[1] = 3
                            else:
                                P.h3_npc1.write()
                        elif P.h3_npc1.name == 'Clamperl':
                            if P.prog[12][2] == 0:
                                txt(P,"You there! I've got this nice","and pretty Clamperl sitting","here with me!")
                                txt(P,"But it's a little bit on the","boring side, if you know what", "I mean?")
                                txt(P,"If you had a livelier Pokemon", "like Loudred, I'll trade with", "you for this Clamperl!")
                                txt(P,"Well get to it! I don't have","all day!")
                                P.prog[12][2] += 1
                            elif P.prog[12][2] == 1:
                                t = P.surface.copy()
                                new_txt(P)
                                write(P,"So did you bring the Loudred?")
                                if choice(P):
                                    fade_out(P)
                                    ans = trade_poke(P,"Loudred")
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if ans != None:
                                        txt(P,"Oh boy! You actually brought","one! I can't believe it!")
                                        txt(P,"Well here's the Clamperl I","promised to give you!")
                                        txt(P,"I'm gonna have so much fun","messing around with this bad","boy!")
                                        P.party.remove(ans)
                                        get_poke(P,poke.Poke('Clamperl',[20,random.randint(0,1),334,"Clamp",-1,"Water Gun",-1,"Whirlpool",-1,"Iron Defense",-1,'Pearl',None,0,"Luxury Ball",0,'Shell Armor']),False)
                                        P.prog[12][2] += 1
                                    else:
                                        txt(P,"Come on, surely it's not too","much to ask from a trainer of","your caliber!")
                                else:
                                    txt(P,"Come on, surely it's not too","much to ask from a trainer of","your caliber!")
                            else:
                                P.h3_npc1.write()
                        else:
                            P.h3_npc1.write()
                    elif P.h3_npc2 and P.h3_npc2.talk():
                        house_3_b(P)
                        house_3_p(P,P.px,P.py,False)
                        house_3_f(P,P.px,P.py)
                        P.h3_npc2.write()
                    elif P.py == 125 and P.px in [-75,-125] and face_u(P):
                        if num == 1:
                            new_txt(P)
                            write(P,"The Ultimate Guide to Berries","Read?")
                            if choice(P):
                                txt(P,"Many berries have medicinal","properties that are beneficial","for Pokemon.")
                                txt(P,"Pokemon can use them to heal,","or even cure statuses like","Burn or Sleep.")
                                txt(P,"Pokemon will eat them during","battle if held, or you can","feed it to them directly.")
                        elif num == 3:
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.02:","Special Evolution Items","Read?")
                            if choice(P):
                                txt(P,"Multiple Pokemon evolve with","evolution stones, but a few","need more unique items.")
                                txt(P,"For example, both Onix and","Scyther will evolve when given","a Metal Coat.")
                        elif num == 4:
                            new_txt(P)
                            write(P,"Legends of Alto Mare Vol.04:","Diancie: The Jewel Pokemon","Read?")
                            if choice(P):
                                txt(P,"Diancie is a Mythical Pokemon","said to have been born from a","mutated Carbink.")
                                txt(P,"It supposedly has the power to","create diamonds by compressing","carbon in the air.")
                        else:
                            txt(P,"There's nothing interesting to","read here.")
                    elif next_to(P,150,100):
                        if num == 3 and P.prog[6][49] == 0:
                            txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                            txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                            add_item(P,"Tiny Mushroom",1)
                            P.prog[6][49] = 1
                        elif num == 4 and P.prog[6][50] == 0:
                            txt(P,P.save_data.name + " found an Expired", "Candy!")
                            txt(P,P.save_data.name + " put the Expired","Candy in the Medicine pocket.")
                            add_item(P,"Expired Candy",1)
                            P.prog[6][50] = 1
                        else:
                            txt(P,"The trashcan's empty.")
                    elif P.px == 275 and P.py == 125 and face_u(P):
                        txt(P,"The fridge is filled with all","kinds of food.")
                    elif P.px == 325 and P.py == 125 and face_u(P):
                        txt(P,"You wash your hands.")
                    elif P.px == 375 and P.py == 125 and face_u(P):
                        if num in [1,4]:
                            txt(P,"Something smells delicious!")
                        else:
                            txt(P,"Nothing's cooking.")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == -25 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            if num == 1:
                P.px = -525
                P.py = 725
                P.loc = "fiore"
            elif num == 2:
                P.px = -825
                P.py = 125
                P.loc = "isola"
            elif num == 3:
                P.px = -975
                P.py = 525
                P.loc = "isola"
            elif num == 4:
                P.px = -525
                P.py = 725
                P.loc = "isola"
            end = False    
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)
    set_mixer_volume(P,P.vol)

def house_2_2_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.h22_back, (P.px, P.py))

def house_2_2_p(P,temppx,temppy,move):
    if P.h22_npc1:
        one = P.h22_npc1.y_dist() > 0
        if one:
            P.h22_npc1.move()
    if P.h22_npc2:
        two = P.h22_npc2.y_dist() > 0
        if two:
            P.h22_npc2.move()
    #rects start
    r1 = (P.px+50,P.py+100,100,90)
    r2 = (P.px,P.py+50,600,40)
    r3 = (P.px-50,P.py+100,50,340)
    r4 = (P.px,P.py+450,600,40)
    r5 = (P.px+600,P.py+100,50,340)
    r6 = (P.px+150,P.py+100,50,40)
    r7 = (P.px+250,P.py+100,50,40)
    r8 = (P.px+500,P.py+250,100,140)
    r9 = (P.px+250,P.py+250,200,90)
    r10 = (P.px+200,P.py+350,50,90)
    if P.px > 125:
        r10 = (P.px+250,P.py+350,50,90)
    r11 = (P.px+200,P.py+100,50,90)
    if P.px > 125:
        r11 = (P.px+250,P.py+150,50,40)
    r12 = r1
    if P.py > 75:
        if P.px == -175:
            r12 = (P.px+500,P.py+100,50,90)
        else:
            r12 = (P.px+550,P.py+100,50,90)
    r13,r14 = r1,r1
    if P.h22_npc1:
        r13 = P.h22_npc1.get_rect()
    if P.h22_npc2:
        r14 = P.h22_npc2.get_rect()
    rects = [r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.h22_npc1:
        if not one:
            P.h22_npc1.move(temppx,temppy)
    if P.h22_npc2:
        if not two:
            P.h22_npc2.move(temppx,temppy)

def house_2_2_f(P,temppx,temppy):
    P.surface.blit(P.ss_d1,(temppx+550,temppy+100))
    P.surface.blit(P.h22_wall,(temppx+550,temppy+70))
    P.surface.blit(P.h22_roof,(temppx+246,temppy+242))

def house_2_2(P,num) -> None:
    if num <= 3:
        if (P.song != "music/am_night.wav" and P.song != "music/am_day.wav"):
            if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
                music = "music/am_night.wav"
            else:
                music = "music/am_day.wav"
        else:
            music = P.song
    elif num <= 5:
        music = "music/pianura.wav"
    else:
        music = "music/egida_city.wav"
    set_mixer_volume(P,P.vol)
    if P.song != music:
        P.song = music
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.h22_back = load("p/am/house_2_2.png")
    P.h22_wall = load("p/am/house_2_2_wall.png")
    P.h22_roof = load("p/am/house_2_2_roof.png")
    P.h22_npc1 = None
    P.h22_npc2 = None
    if num == 1:
        P.h22_npc1 = npc.NPC(P,'Lass','Sis',[100,300],[['u',40]],["No matter how many times I","tell him, my stupid brother","just doesn't get it!","He thinks he can win with just","a Pidgey, but he needs a gym","badge to get past level 15.","And he's not about to beat any","gym leaders with a useless","Pidgey!"])
    elif num == 2:
        P.h22_npc1 = npc.NPC(P,'Expertf','Granny',[550,400],[['u',40]],["I'm so blessed by my grandson.","He's always working hard on","his homework and studying.","If only my son had been such","a good kid, I wouldn't have","this many gray hairs!"])
    elif num == 3:
        P.h22_npc1 = npc.NPC(P,'Youngster','Punk1',[150,200],[['u',40]],["Our parents are out, so we're","grinding together in this new","game I just got.","The kid that lives just down","the street is playing in our","party too!"])
        P.h22_npc2 = npc.NPC(P,'Preschoolerb','Punk2',[150,150],[['d',40]],["Hey hey! I just hit level 17!","Check out this new move I got!","It just goes BAAAAM!","Doesn't it look so cool?! And","look at how much damage it","does!"])
    elif num == 4:
        P.h22_npc1 = npc.NPC(P,'Lass','Sis',[150,150],[['l',40]],["Just the other day, we were","assigned a statistics project","for homework.","And of all things, my sister", "wanted to get the distribution","of birthdays in the city!","What a nutcase, am I right?","",""])
    else:
        P.h22_npc1 = None
    move = True
    tim = 0
    house_2_2_b(P)
    house_2_2_p(P,P.px,P.py,False)
    house_2_2_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        house_2_2_b(P)
        temppx = P.px
        temppy = P.py
        house_2_2_p(P,temppx,temppy,move)
        house_2_2_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.h22_npc1 and P.h22_npc1.talk():
                        house_2_2_b(P)
                        house_2_2_p(P,P.px,P.py,False)
                        house_2_2_f(P,P.px,P.py)
                        P.h22_npc1.write()
                    elif P.h22_npc2 and P.h22_npc2.talk():
                        house_2_2_b(P)
                        house_2_2_p(P,P.px,P.py,False)
                        house_2_2_f(P,P.px,P.py)
                        P.h22_npc2.write()
                    elif P.px == 75 and P.py == -75 and face_u(P):
                        time = datetime.datetime.now()
                        hour = time.hour
                        minutes = time.minute
                        if minutes < 10:
                            min = "0"
                        else:
                            min = ""
                        min += str(minutes)
                        ap = " AM."
                        if hour > 12:
                            ap = " PM."
                            hour -= 12
                        txt(P,"It's "+str(hour)+":"+min+ap)
                    elif next_to(P,250,100):
                        txt(P,"It's a healthy plant.")
                    elif next_to(P,150,100):
                        txt(P,"It's a nightstand.")
                    elif next_to(P,100,100) or next_to(P,100,150) or next_to(P,50,150) or next_to(P,50,100):
                        txt(P,"You probably shouldn't take a","nap here.")
                    elif P.py == -125 and P.px in [-125,-175] and face_u(P):
                        if num == 1:
                            new_txt(P)
                            write(P,"How to Train Your Pokemon","Read?")
                            if choice(P):
                                txt(P,"When your Pokemon win battles,","they will gain experience and","level up.")
                                txt(P,"However, trainers must earn","gym badges to fully unlock the","potential of their Pokemon.")
                        elif num == 2:
                            new_txt(P)
                            write(P,"History of Alto Mare","Read?")
                            if choice(P):
                                txt(P,"Alto Mare is a city renown for","it's attractions, and makes","for a popular tourist spot.")
                                txt(P,"Many tournaments and races are","held there, most notably the","Tour de Alto Mare.")
                                txt(P,"Locals from all the islands","gather in its square every","weekend to share their wares.")
                        elif num == 3:
                            new_txt(P)
                            write(P,"Wonders of Evolution Vol.03:","Evolution By Trade","Read?")
                            if choice(P):
                                txt(P,"In many regions of the world,","some Pokemon evolve when they","are traded.")
                                txt(P,"In the islands of Alto Mare,","these Pokemon are capable of","evolving naturally.")
                        elif num == 4:
                            new_txt(P)
                            write(P,"Legends of Alto Mare Vol.03","Forces of Nature","Read?")
                            if choice(P):
                                txt(P,"The Forces of Nature are a","legendary trio with power over","the land and skies.")
                                txt(P,"There are legends of their","disputes causing destruction","across the islands.")
                                txt(P,"Some say they are reasonable","beings, while others say they","are like raging beasts.")
                        elif num == 5:
                            new_txt(P)
                            write(P,"Pokemon and Friendship","Read?")
                            if choice(P):
                                txt(P,"The friendlier a Pokemon is","with its trainer, the stronger","they will be in battle.")
                                txt(P,"Trainers can grow closer to","their Pokemon by traveling and","battling together.")
                                txt(P,"Giving Pokemon tasty treats is","another great way to earn","their favor.")
                        else:
                            txt(P,"There's nothing interesting to","read here.")
                    else:
                        P.buffer_talk = temp_buff
        if P.px == -175 and P.py == 175 and face_u(P):
            P.p = P.d1
            P.py = 225
            P.loc = "house_21_"+str(num)
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    fade_out(P)

def house_2_1_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.h21_back, (P.px, P.py))

def house_2_1_p(P,temppx,temppy,move):
    if P.h21_npc1:
        one = P.h21_npc1.y_dist() > 0
        if one:
            P.h21_npc1.move()
    if P.h21_npc2:
        two = P.h21_npc2.y_dist() > 0
        if two:
            P.h21_npc2.move()
    #rects start
    r1 = (P.px,P.py+100,150,40)
    r2 = (P.px+150,P.py+50,400,40)
    r3 = (P.px-50,P.py+150,50,290)
    r4 = (P.px,P.py+450,600,40)
    r5 = (P.px+600,P.py+50,50,390)
    r6 = (P.px+300,P.py+200,100,90)
    r7 = (P.px,P.py+200,150,40)
    r8 = (P.px+550,P.py,50,40)
    r9 = (P.px+500,P.py+100,50,40)
    r10 = (P.px,P.py+400,50,40)
    r11,r12 = r1,r1
    if P.h21_npc1:
        r11 = P.h21_npc1.get_rect()
    if P.h21_npc2:
        r12 = P.h21_npc2.get_rect()
    rects = [r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.h21_npc1:
        if not one:
            P.h21_npc1.move(temppx,temppy)
    if P.h21_npc2:
        if not two:
            P.h21_npc2.move(temppx,temppy)

def house_2_1_f(P,temppx,temppy):
    P.surface.blit(P.ss_u1,(temppx+550,temppy))
    P.surface.blit(P.h21_jar,(temppx+12,temppy+188))

def house_2_1(P,num) -> None:
    music = None
    if num < 4:
        if (P.song != "music/am_night.wav" and P.song != "music/am_day.wav"):
            if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
                music = "music/am_night.wav"
            else:
                music = "music/am_day.wav"
        else:
            music = P.song
    elif num < 6:
        music = "music/pianura.wav"
    else:
        music = "music/egida_city.wav"
    set_mixer_volume(P,P.vol)
    if P.song != music:
        P.song = music
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.h21_jar = load("p/am/top_jar.png")
    P.h21_back = load("p/am/house_2_1.png")
    P.h21_npc1 = None
    P.h21_npc2 = None
    if num == 1:
        P.h21_npc1 = npc.NPC(P,'Healer','Mom',[0,150],[['u',180],['mr',40],['d',140],['ml',20],['u',300],['ml',20]],["Why can't my boy be a little","more patient about getting his","first Pokemon?","I'm glad he's so excited, but","he's still too young for me to","trust him with one."])
    elif num == 2:
        P.h21_npc1 = npc.NPC(P,'Youngster','Bad Boy',[400,200],[['l',40]],["Hey I'm busy working on my","homework! Quit being so nosy,","will ya?"])
    elif num == 3:
        P.h21_npc1 = None
    elif num == 4:
        P.h21_npc1 = npc.NPC(P,'Lass','Birthday',[250,250],[['r',40]],["My project's been going great!","Thanks for the help!",""])
    elif num == 5:
        P.h21_npc1 = npc.NPC(P,'Ace Trainerm','fail',[400,200],[['l',40]],["Ugh. I lost a battle a few","days ago and all my Pokemon","fainted.","Ever since, training has been","pretty rough, and they've been","looking unmotivated."])
        P.h21_npc2 = npc.NPC(P,'Ace Trainerf','good',[250,200],[['r',40]],["I've been treating my Pokemon","to sweets from the bakery","every week!","When your Pokemon are nice and","happy, they'll work really","hard to win battles for you!"])
    else:
        P.h21_npc1 = None
    move = True
    tim = 0
    house_2_1_b(P)
    house_2_1_p(P,P.px,P.py,False)
    house_2_1_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        # print(P.px,P.py)
        house_2_1_b(P)
        temppx = P.px
        temppy = P.py
        house_2_1_p(P,temppx,temppy,move)
        house_2_1_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.h21_npc1 and P.h21_npc1.talk():
                        house_2_1_b(P)
                        house_2_1_p(P,P.px,P.py,False)
                        house_2_1_f(P,P.px,P.py)
                        if P.h21_npc1.name == 'Birthday' and P.prog[13] == None:
                            txt(P,"Heya! I'm collecting birthdays","for this super important","school project!")
                            txt(P,"Gimme your birthday! But no","lying! My project has to be","flawless!")
                            new_txt(P)
                            write(P,"Which month were you born in?")
                            month = choose_num(P,12,day = True)
                            new_txt(P)
                            write(P,"Alright, now what day were you", "born on?")
                            if month in [1,3,5,7,8,10,12]:
                                days = 31
                            elif month == 2:
                                days = 29
                            else:
                                days = 30
                            day = choose_num(P,days,day = True)
                            if month == 10 and day == 14:
                                txt(P,"Hey! You have the exact same","birthday as this really cool","friend of mine!")
                                txt(P,"That's pretty awesome! You","must be really cool too!")
                            elif month == datetime.datetime.now().month and day == datetime.datetime.now().day:
                                txt(P,"Hey! That means today is your","birthday, right?")
                                txt(P,"Happy Birthday!")
                            else:
                                txt(P,"Sweet! Thanks a lot!")
                            P.prog[13] = [month,day,0]
                        else:
                            P.h21_npc1.write()
                    elif next_to(P,0,400):
                        if num == 1 and P.prog[6][18] == 0:
                            txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                            txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                            add_item(P,"Tiny Mushroom",1)
                            P.prog[6][18] = 1
                        elif num == 3 and P.prog[6][24] == 0:
                            txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                            txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                            add_item(P,"Tiny Mushroom",1)
                            P.prog[6][24] = 1
                        elif num == 5 and P.prog[6][33] == 0:
                            txt(P,P.save_data.name + " found a Poffin!")
                            txt(P,P.save_data.name + " put the Poffin","in the Items pocket.")
                            add_item(P,"Poffin",1)
                            P.prog[6][33] = 1
                        else:
                            txt(P,"The trashcan's empty.")
                    elif P.h21_npc2 and P.h21_npc2.talk():
                        house_2_1_b(P)
                        house_2_1_p(P,P.px,P.py,False)
                        house_2_1_f(P,P.px,P.py)
                        P.h21_npc2.write()
                    elif P.px == 275 and P.py == 125 and face_u(P):
                        txt(P,"The fridge is filled with all","kinds of food.")
                    elif P.px == 325 and P.py == 125 and face_u(P):
                        txt(P,"You wash your hands.")
                    elif P.px == 375 and P.py == 125 and face_u(P):
                        txt(P,"Nothing's cooking.")
                    elif next_to(P,0,200):
                        txt(P,"It's an empty jar.")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if (P.px == 125 or P.px == 75) and P.py == -125 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            P.move_out_dir = 'd'
            if num == 1:
                P.px -= 1800
                P.py = 675
                P.loc = "dock_1"
            elif num == 2:
                P.px -= 350
                P.py = 1925
                P.loc = "north_am"
            elif num == 3:
                P.px -= 1350
                P.py = 1925
                P.loc = "north_am"
            elif num == 4:
                P.px -= 500
                P.py = 25
                P.loc = "pianura"
            elif num == 5:
                P.px -= 1150
                P.py = 25
                P.loc = "pianura"
            end = False
        if P.px == -175 and P.py == 225 and face_u(P):
            P.p = P.d1
            P.py = 175
            P.move_out_dir = 'd'
            P.loc = "house_22_"+str(num)
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if P.loc[:8] != 'house_22' and (((((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night') and music == "music/am_day.wav") or ((((get_time() <= 19 and get_time() >= 6) and P.lighting == 'Dynamic') or P.lighting == 'Day') and music == "music/am_night.wav")):
        fade_out(P,music)
    else:
        fade_out(P)
    if P.loc[:8] != "house_22":
        set_mixer_volume(P,P.vol)

def house_1_b(P):
    P.surface.fill((0,0,0))
    P.surface.blit(P.h1_back, (P.px, P.py))

def house_1_p(P,temppx,temppy,move):
    if P.h1_npc1:
        one = P.h1_npc1.y_dist() > 0
        if one:
            P.h1_npc1.move()
    if P.h1_npc2:
        two = P.h1_npc2.y_dist() > 0
        if two:
            P.h1_npc2.move()
    #rects start
    r0 = (P.px,P.py+100,150,40)
    r1 = (P.px,P.py+350,50,40)
    r2 = (P.px+150,P.py+50,300,40)
    r3 = (P.px-50,P.py+150,50,240)
    r4 = (P.px,P.py+400,450,40)
    r5 = (P.px+450,P.py+100,50,290)
    r6 = (P.px+300,P.py+200,100,90)
    r7,r8 = r1,r1
    if P.h1_npc1:
        r7 = P.h1_npc1.get_rect()
    if P.h1_npc2:
        r8 = P.h1_npc2.get_rect()
    rects = [r8,r7,r6,r5,r4,r3,r2,r1,r0]
    #rects end
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.h1_npc1:
        if not one:
            P.h1_npc1.move(temppx,temppy)
    if P.h1_npc2:
        if not two:
            P.h1_npc2.move(temppx,temppy)

def house_1_f(P,temppx,temppy):
    pass

def house_1(P,num) -> None:
    music = None
    if num == 1:
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            music = "music/am_night.wav"
        else:
            music = "music/am_day.wav"
    elif num < 9:
        music = "music/egida_city.wav"
    elif num < 12:
        music = "music/fiore.wav"
    else:
        music = "music/pianura.wav"
    set_mixer_volume(P,P.vol)
    if P.song != music:
        P.song = music
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    P.h1_back = load("p/am/house_1.png")
    P.h1_npc1 = None
    P.h1_npc2 = None
    if num == 1:
        P.h1_npc1 = npc.NPC(P,'Rich Boy','Dude',[200,150],[['u',40]],["Oi! Can't you see I'm busy","prepping for a date? What's up","with people just barging into","some random stranger's homes","without asking for permission?",""])
    elif num == 2:
        P.h1_npc1 = npc.NPC(P,'Healer','Mom',[0,150],[['u',40]],["Where did my little Carlos run","off to this time? I never know","what he's up to.","He's always late for dinner,","even though I tell him it's","ready at 6 pm every day!","I should just have him make","his own dinner! That'll teach","him a lesson!"])
    elif num == 3:
        P.h1_npc1 = npc.NPC(P,'Scientistf','Ever',[250,200],[['r',40]],["Some Pokemon evolve in certain","conditions, changing all sorts","of things about them!","Once those conditions are met,","it will start evolving, and", "there's no stopping it!","If you don't want a Pokemon to","change, give them an Everstone","and they won't evolve!"])
    elif num == 4:
        P.h1_npc1 = npc.NPC(P,'Hiker','Boyscout',[100,150],[['u',40]],["Energy Bars, Check! Gatorade,","Check! Cookies, Check!","Lollipops, Check!","Alright! I'm good to go! The","world awaits me!",""])
    elif num == 5:
        P.h1_npc1 = npc.NPC(P,'Lass','Girl',[350,300],[['u',40]],["I'm supposed to be helping him","with the project, but I'd","rather just slack off.","He seems too busy working to","notice anyways.",""])
        P.h1_npc2 = npc.NPC(P,'Youngster','Guy',[350,150],[['d',40]],["Buzz off! Can't you see we're","busy working on a project?",""])
    elif num == 6:
        P.h1_npc1 = npc.NPC(P,'Ace Trainerf','Challenger',[0,300],[['d',40]],["I thought I was finally strong","enough to challenge the gym,","but I just got smacked!","I spent so much time training","too! Maybe I'm just not cut","out for this..."])
    elif num == 7:
        P.h1_npc1 = npc.NPC(P,'Scientistm','TM',[300,300],[['u',40]],["TM is short for Technical","Machine. You can find them in","all sorts of places!","Each one holds a specific move","you can teach to your Pokemon","by using it.","Not all Pokemon are capable of","using every TM, but you can","use TMs as much as you want!"])
    elif num == 8:
        P.h1_npc1 = npc.NPC(P,'Expertm','Move Tut',[200,200],[['d',40]],["I'm the Move Tutor! Bring me a","heart scale, and I can help","your Pokemon remember a move!","At least that's what I used to","do. Now everyone can just do","it themselves...","It does get kinda lonely here","sometimes but boy does it feel","good to have free time!"])
    elif num == 9:
        P.h1_npc1 = npc.NPC(P,'Youngster','Heracross',[200,200],[['u',40]],["","",""])
    elif num == 10:
        P.h1_npc1 = npc.NPC(P,'Expertm','Lumber',[300,150],[['d',40]],["I used to love training my","strength by chopping down the","huge trees in the woods.","As of late, my back has been","aching a lot, so I've been","taking a break.","I think I left my axe out","there but I probably won't be","using it again."])
    elif num == 11:
        P.h1_npc1 = npc.NPC(P,'Youngster','Pinsir',[200,200],[['u',40]],["","",""])
    elif num == 12:
        P.h1_npc1 = npc.NPC(P,'Expertm','Name Rater',[300,150],[['d',40]],["","",""])
        P.h1_npc2 = npc.NPC(P,'Expertf','Name Hater',[300,300],[['u',40]],["","",""])
    elif num == 13:
        pass
    elif num == 14:
        P.h1_npc1 = npc.NPC(P,'Preschoolerb','Lost',[350,300],[['u',40]],["My mom always tells me I'm not","supposed to talk to strangers.","","You're a stranger.","Shoo!",""])
    # elif num == 10:
    #     P.h1_npc1 = npc.NPC(P,'Preschoolerb','Kid',[300,300],[['u',40]],["Oh...Looks like mom forgot to","lock the door again. That's","the third time this week...","What if someone just came in","here and kidnapped me? That'd","be pretty scary!","Well I'm pretty sure that only","happens in movies and stuff.","Right?"])
    else:
        P.h1_npc1 = None
    move = True
    tim = 0
    house_1_b(P)
    house_1_p(P,P.px,P.py,False)
    house_1_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    while end:
        # print(P.px,P.py)
        house_1_b(P)
        temppx = P.px
        temppy = P.py
        house_1_p(P,temppx,temppy,move)
        house_1_f(P,temppx,temppy)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.h1_npc1 and P.h1_npc1.talk():
                        house_1_b(P)
                        house_1_p(P,P.px,P.py,False)
                        house_1_f(P,P.px,P.py)
                        if P.h1_npc1.name == 'Name Rater':
                            t = P.surface.copy()
                            txt(P,"Hello there traveler!","I'm the official Name Rater!")
                            new_txt(P)
                            write(P,"Want me to rate the nicknames","of your Pokemon?")
                            if choice(P):
                                txt(P,"Alright! Which Pokemon shall","I rate for you?")
                                fade_out(P)
                                ans = trade_poke(P,None,True)
                                P.surface.blit(t,(0,0))
                                fade_in(P)
                                if ans != None:
                                    if ans.name == ans.actual_name:
                                        txt(P,ans.name+"? It's not bad,","but a little too mainstream","don't you think?")
                                    else:
                                        txt(P,ans.name+"? A good start,","but it's not quite there, you","know what I mean?")
                                    new_txt(P)
                                    write(P,"I think it could really use an","upgrade! What do you say?")
                                    if choice(P):
                                        new = None
                                        ret = pygame.transform.scale(load("p/return.png"),(25,25))
                                        enter = P.font.render("[ENTER]",True,(0,0,0))
                                        esc = P.font.render("[ESC]",True,(0,0,0))
                                        new_txt(P)
                                        write(P,ans.name+"'s new name?")
                                        name = ""
                                        temp = P.surface.copy()
                                        end2 = True
                                        b = 0
                                        while end2:
                                            for event in pygame.event.get(eventtype = KEYDOWN):
                                                if event.type == pygame.KEYDOWN:
                                                    if len(name) < 9:
                                                        if (pygame.K_a <= event.key <= pygame.key.key_code(P.controls[4])) or (pygame.K_0 <= event.key <= pygame.K_9):
                                                            name += event.unicode
                                                        if event.key == K_SPACE:
                                                            name += " "
                                                    if event.key == K_ESCAPE:
                                                        new_txt(P)
                                                        write(P,"Don't give "+ans.name + " a","new name?")
                                                        if choice(P):
                                                            end2 = False
                                                        else:
                                                            new_txt(P)
                                                            write(P,ans.name+"'s new name?")
                                                            name = ""
                                                            temp = P.surface.copy()
                                                    if event.key == K_BACKSPACE:
                                                        name = name[:-1]
                                                    if event.key == K_RETURN:
                                                        onlyspc = True
                                                        for let in name:
                                                            if let != ' ':
                                                                onlyspc = False
                                                        if onlyspc:
                                                            new_txt(P)
                                                            write(P,"That name doesn't seem very","good...")
                                                            cont(P)
                                                            new_txt(P)
                                                            write(P,ans.name+"'s new name?")
                                                            temp = P.surface.copy()
                                                        else:
                                                            for p in range(len(P.party)):
                                                                if P.party[p].same(ans):
                                                                    new = P.party[p].name
                                                                    P.party[p].name = name
                                                            end2 = False
                                            P.surface.blit(temp,(0,0))
                                            if len(name) == 9 or int(b/20)%2 == 1:
                                                txt0 = P.font.render(name,True,(0,0,0))
                                            else:
                                                txt0 = P.font.render(name+"_",True,(0,0,0))
                                            b += 1
                                            if len(name) == 9:
                                                P.surface.blit(ret,(250,513))
                                            P.surface.blit(esc,(650,460))
                                            P.surface.blit(enter,(625,500))
                                            P.surface.blit(txt0,(20,500))
                                            P.clock.tick(P.ani_spd)
                                            update_screen(P)
                                        if new != None:
                                            txt(P,new+" will now be known","as "+name+"! It sounds so","much better already!")
                                        else:
                                            txt(P,"Okay, well let me know if you","change your mind!")
                                    else:
                                        txt(P,"Okay, well let me know if you","change your mind!")
                                else:
                                    txt(P,"Okay, well let me know if you","change your mind!")
                            else:
                                txt(P,"Okay, well let me know if you","change your mind!")
                        elif P.h1_npc1.name == 'Heracross':
                            if P.prog[12][0] == 0:
                                new_txt(P)
                                write(P,"Hey! Don't you agree that","Karrablast is like the coolest","Pokemon ever?")
                                if choice(P):
                                    txt(P,"I know right? That stupid kid","down the street doesn't agree","with me!")
                                    txt(P,"He thinks Shelmet is the","stuff! Like you've got to be","kidding me!")
                                    P.prog[12][0] += 1
                                else:
                                    txt(P,"Really? Well I sure hope you","realize you're wrong!")
                            elif P.prog[12][0] == 1:
                                if P.prog[12][1] == 0:
                                    txt(P,"You should teach that kid a","lesson or two! That'll put him","in his place!")
                                else:
                                    txt(P,"Hey! I heard you told the","other kid that Shelmet is the","better Pokemon!")
                                    txt(P,"But you told me that you knew","Karrablast was way cooler!","")
                                    txt(P,"Maybe that kid lied to me, but","you've got to prove that you","love Karrablast!")
                                    txt(P,"If you can bring me one, then","I'll know for sure that you","weren't lying!")
                                    txt(P,"Yeah! That's definitely what","you have to do!")
                                    P.prog[12][0] += 1
                            elif P.prog[12][0] == 2:
                                if P.prog[12][1] != 3:
                                    t = P.surface.copy()
                                    new_txt(P)
                                    write(P,"You brought the Karrablast", "right?")
                                    if choice(P):
                                        fade_out(P)
                                        ans = trade_poke(P,"Karrablast")
                                        P.surface.blit(t,(0,0))
                                        fade_in(P)
                                        if ans != None:
                                            txt(P,'Wow! You actually brought a',"Karrablast! I've never seen","one in real life!")
                                            new_txt(P)
                                            write(P,"Can I have it? Then I'll know","that you really do think","Karrablast is the best!")
                                            if choice(P):
                                                txt(P,"You're the best!","I can't believe I actually get","to own a Karrablast!")
                                                txt(P,"Here, you can have this! It's","not as cool as Karrablast, but","it's pretty close!")
                                                txt(P,"You received Heracross!")
                                                P.party.remove(ans)
                                                get_poke(P,poke.Poke('Heracross',[15,random.randint(0,1),334,"Feint",-1,"Horn Attack",-1,"Arm Thrust",-1,"Aerial Ace",-1,None,None,0,"Net Ball",0,'Guts']),False)
                                                P.prog[12][0] += 1
                                                P.prog[12][1] = 2
                                            else:
                                                txt(P,"What? Do you really just think","Shelmet is better? There's no","way, right?")
                                        else:
                                            txt(P,"Well, you'd better hurry it","up! I can't just wait here","forever!")
                                    else:
                                        txt(P,"Well, you'd better hurry it","up! I can't just wait here","forever!")
                                else:
                                    txt(P,'I heard you gave that kid a',"Shelmet! I thought we had","something going!")
                                    txt(P,"I would've given you something","super cool for a Karrablast,","but not anymore!")
                                    txt(P,"Well...maybe if you brought me","an Escavalier, I might change","my mind.")
                                    txt(P,"You know, if you happen to","just have one.")
                                    P.prog[12][0] = 4
                            elif P.prog[12][0] == 4:
                                t = P.surface.copy()
                                new_txt(P)
                                write(P,"You didn't actually get me an","Escavalier did you?")
                                if choice(P):
                                    fade_out(P)
                                    ans = trade_poke(P,"Escavalier")
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if ans != None:
                                        new_txt(P)
                                        write(P,"Wow! No way! Are you going to","give it to me?","")
                                        if choice(P):
                                            txt(P,"Thanks so much!","I'm sorry I ever doubted you!","")
                                            txt(P,"You're the best trainer ever!","Here, you can take this!","")
                                            txt(P,"You received Heracross!")
                                            P.party.remove(ans)
                                            get_poke(P,poke.Poke('Heracross',[20,1,334,"Counter",-1,"Chip Away",-1,"Arm Thrust",-1,"Aerial Ace",-1,None,None,0,"Net Ball",0,'Guts']),False)
                                            P.save_data.pokedex['Heracross'] = [1,[]]
                                            P.prog[12][0] += 1
                                        else:
                                            txt(P,"Come on! Pretty please?","I've got to have it now that","I've seen one!")
                                    else:
                                        txt(P,"Well, I suppose it would be","pretty ambitious of me to","expect one.")
                                else:
                                    txt(P,"Well, I suppose it would be","pretty ambitious of me to","expect one.")
                            elif P.prog[12][0] == 3:
                                txt(P,"The Karrablast is so cool!","I'm gonna treasure it for the","rest of my life!")
                            else:
                                txt(P,"The Escavalier is so cool!","I'm gonna treasure it for the","rest of my life!")
                        elif P.h1_npc1.name == 'Pinsir':
                            if P.prog[12][1] == 0:
                                new_txt(P)
                                write(P,"Hey there! Do you think that","Shelmet is a pretty cool","Pokemon?")
                                if choice(P):
                                    txt(P,"I know right? That kid down","the street keeps making fun of","me for thinking that!")
                                    txt(P,"He thinks Karrablast is the","best, and every other Pokemon","sucks!")
                                    P.prog[12][1] += 1
                                else:
                                    txt(P,"Oh, well I guess that's fair.","Maybe you just need to learn","more about them.")
                            elif P.prog[12][1] == 1:
                                if P.prog[12][0] == 0:
                                    txt(P,"You should tell that kid so he","doesn't keep bullying me about","liking Shelmet!")
                                else:
                                    txt(P,"Um, that other kid told me you","said that Karrablast was way","cooler than Shelmet.")
                                    txt(P,"I know you said Shelmet was","cool, but I didn't know you","thought Karrablast was better.")
                                    txt(P,"I mean not that it matters","that much, but I don't want to","keep getting picked on.")
                                    txt(P,"If you get me a Shelmet, then","at least I could say you like","them as well right?")
                                    txt(P,"If you would do that for me,","I'll make sure to give you","something in return!")
                                    P.prog[12][1] += 1
                            elif P.prog[12][1] == 2:
                                if P.prog[12][0] != 3:
                                    t = P.surface.copy()
                                    new_txt(P)
                                    write(P,"Did you bring me a Shelmet?")
                                    if choice(P):
                                        fade_out(P)
                                        ans = trade_poke(P,"Shelmet")
                                        P.surface.blit(t,(0,0))
                                        fade_in(P)
                                        if ans != None:
                                            txt(P,'Wow! You actually brought me a',"Shelmet! It looks so cool and","shiny!")
                                            new_txt(P)
                                            write(P,"Are you really okay giving it","to me? I do have something I","can exchange with it!")
                                            if choice(P):
                                                txt(P,"Thanks so much!","I'm going to take super duper","care of this Shelmet!")
                                                txt(P,"Here, you can have this! It's","not that cute, but it's still","pretty cool!")
                                                txt(P,"You received Pinsir!")
                                                P.party.remove(ans)
                                                get_poke(P,poke.Poke('Pinsir',[15,random.random(0,1),334,"Focus Energy",-1,"Bind",-1,"Seismic Toss",-1,"Revenge",-1,None,None,0,"Net Ball",0,'Hyper Cutter']),False)
                                                P.prog[12][1] += 1
                                                P.prog[12][0] = 2
                                            else:
                                                txt(P,"Are you sure? I guess if you","really don't want to that's","fine too...")
                                        else:
                                            txt(P,"Oh, I hope you're working on","getting it. It really means a","lot to me.")
                                    else:
                                        txt(P,"Oh, I hope you're working on","getting it. It really means a","lot to me.")
                                else:
                                    txt(P,'I heard you gave the other kid',"a Karrablast. That's pretty","cool I guess...")
                                    txt(P,"I would have liked to trade","with you for a Shelmet, but","now I'm not so sure.")
                                    txt(P,"Well maybe if you brought me","an Accelgor, that would be","pretty cool!")
                                    txt(P,"That's asking for a bit much","though, isn't it?")
                                    P.prog[12][1] = 4
                            elif P.prog[12][1] == 4:
                                t = P.surface.copy()
                                new_txt(P)
                                write(P,"You didn't actually get me an","Accelgor did you?")
                                if choice(P):
                                    fade_out(P)
                                    ans = trade_poke(P,"Accelgor")
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if ans != None:
                                        new_txt(P)
                                        write(P,"Wow! No way! Are you really","going to give that to me?","")
                                        if choice(P):
                                            txt(P,"Thanks so much!","I'm sorry about how I acted","before.")
                                            txt(P,"You're the best trainer ever!","Here, you can have this!","")
                                            txt(P,"You received Pinsir!")
                                            P.party.remove(ans)
                                            get_poke(P,poke.Poke('Pinsir',[20,1,334,"Focus Energy",-1,"Bind",-1,"Vital Throw",-1,"Revenge",-1,None,None,0,"Net Ball",0,'Hyper Cutter']),False)
                                            P.save_data.pokedex['Pinsir'] = [1,[]]
                                            P.prog[12][1] += 1
                                        else:
                                            txt(P,"Really? It's so cool though!","","")
                                    else:
                                        txt(P,"Well, I suppose it would be","pretty ambitious of me to","expect one.")
                                else:
                                    txt(P,"Well, I suppose it would be","pretty ambitious of me to","expect one.")
                            elif P.prog[12][1] == 3:
                                txt(P,"The Shelmet you gave me is","doing great! We've been having","so much fun together!")
                            else:
                                txt(P,"The Accelgor you gave me is","doing great! We've been having","so much fun together!")
                        else:
                            P.h1_npc1.write()
                    elif P.h1_npc2 and P.h1_npc2.talk():
                        house_1_b(P)
                        house_1_p(P,P.px,P.py,False)
                        house_1_f(P,P.px,P.py)
                        if P.h1_npc2.name == 'Name Hater':
                            t = P.surface.copy()
                            txt(P,"Hey there kid!","I'm the official Name Hater!")
                            txt(P,"If you hate your Pokemon's","nickname as much as I do, I","can help you eradicate it!")
                            new_txt(P)
                            write(P,"Do you have any Pokemon like","that?")
                            if choice(P):
                                txt(P,"Alright! Which Pokemon's name","can I remove for you?")
                                fade_out(P)
                                ans = trade_poke(P,None,True,True)
                                P.surface.blit(t,(0,0))
                                fade_in(P)
                                if ans != None:
                                    for p in range(len(P.party)):
                                        if P.party[p].equals(ans):
                                            name = [ans.name,ans.actual_name]
                                            P.party[p].name = P.party[p].actual_name
                                    txt(P,name[0]+" is back to being","called "+name[1]+", just as it","should be!")
                                else:
                                    txt(P,"Well come back if you're ever","in need of my services!")
                            else:
                                txt(P,"Well come back if you're ever","in need of my services!")
                        else:
                            P.h1_npc2.write()
                    elif next_to(P,0,350):
                        if num == 2 and P.prog[6][15] == 0:
                            txt(P,P.save_data.name + " found a Tiny", "Mushroom!")
                            txt(P,P.save_data.name + " put the Tiny","Mushroom in the Items pocket.")
                            add_item(P,"Tiny Mushroom",1)
                            P.prog[6][15] = 1
                        elif num == 4 and P.prog[6][16] == 0:
                            txt(P,P.save_data.name + " found an Old Candy!")
                            txt(P,P.save_data.name + " put the Old Candy","in the Medicine pocket.")
                            add_item(P,"Old Candy",1)
                            P.prog[6][16] = 1
                        elif num == 6 and P.prog[6][17] == 0:
                            txt(P,P.save_data.name + " found a Poke Ball!")
                            txt(P,P.save_data.name + " put the Poke Ball","in the Balls pocket.")
                            add_item(P,"Poke Ball",1)
                            P.prog[6][17] = 1
                        elif num == 10 and P.prog[6][27] == 0:
                            txt(P,P.save_data.name + " found an Expired", "Candy!")
                            txt(P,P.save_data.name + " put the Expired","Candy in the Medicine pocket.")
                            add_item(P,"Expired Candy",1)
                            P.prog[6][27] = 1
                        elif num == 13 and P.prog[6][34] == 0:
                            txt(P,P.save_data.name + " found a Lum Berry!")
                            txt(P,P.save_data.name + " put the Lum Berry","in the Medicine pocket.")
                            add_item(P,"Lum Berry",1)
                            P.prog[6][34] = 1
                        elif num == 14 and P.prog[6][32] == 0:
                            txt(P,P.save_data.name + " found an Old Candy!")
                            txt(P,P.save_data.name + " put the Old Candy","in the Medicine pocket.")
                            add_item(P,"Old Candy",1)
                            P.prog[6][32] = 1
                        else:
                            txt(P,"The trashcan's empty.")
                    elif P.px == 275 and P.py == 125 and face_u(P):
                        txt(P,"The fridge is filled with all","kinds of food.")
                    elif P.px == 325 and P.py == 125 and face_u(P):
                        txt(P,"You wash your hands.")
                    elif P.px == 375 and P.py == 125 and face_u(P):
                        if num == 4:
                            txt(P,"It smells like something died","in the oven.")
                        elif num == 13:
                            txt(P,"It smells like something's","burning.")
                        else:
                            txt(P,"Nothing's cooking.")
                    else:
                        P.buffer_talk = temp_buff
        keys = pygame.key.get_pressed()
        if P.px == 175 and P.py == -75 and keys[pygame.key.key_code(P.controls[1])] and P.p == P.d1:
            if num == 1:
                P.px = -175
                P.py = 1425
                P.loc = "north_am"
            elif num == 2:
                P.px = -975
                P.py = 525
                P.loc = "egida"
            elif num == 3:
                P.px = -1375
                P.py = 525
                P.loc = 'egida'
            elif num == 4:
                P.px = -1075
                P.py = 1025
                P.loc = 'egida'
            elif num == 5:
                P.px = -175
                P.py = 1025
                P.loc = 'egida'
            elif num == 6:
                P.px = -975
                P.py = 625
                P.loc = 'egida_under'
            elif num == 7:
                P.px = -275
                P.py = 625
                P.loc = 'egida_under'
            elif num == 8:
                P.px = -1125
                P.py = 125
                P.loc = 'egida_under'
            elif num == 9:
                P.px = 75
                P.py = 325
                P.loc = 'fiore'
            elif num == 10:
                P.px = -1075
                P.py = 325
                P.loc = 'fiore'
            elif num == 11:
                P.px = -1525
                P.py = 325
                P.loc = 'fiore'
            elif num == 12:
                P.px = -1325
                P.py = -975
                P.loc = 'pianura'
            elif num == 13:
                P.px = -1425
                P.py = 25
                P.loc = 'pianura'
            elif num == 14:
                P.px = -1725
                P.py = 25
                P.loc = 'pianura'
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'd'
    if ((((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night') and music == "music/am_day.wav") or ((((get_time() <= 19 and get_time() >= 6) and P.lighting == 'Dynamic') or P.lighting == 'Day') and music == "music/am_night.wav"):
        fade_out(P,music)
    else:
        fade_out(P)
    set_mixer_volume(P,P.vol)

def north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy):
    draw_waves(P, wx, wy)
    P.surface.blit(P.pc_black,(P.px+880,P.py-1170))
    P.surface.blit(P.pcdr, (P.px + 925 + pcx, P.py - 1170 - pcy))
    P.surface.blit(P.pcdl, (P.px + 888 - pcx, P.py - 1170 - pcy))
    P.surface.blit(P.nam_square, (P.px - 450, P.py - 2300))
    P.surface.blit(P.nam_fenceu,(P.px+449,P.py-1075))
    P.surface.blit(P.nam_corner, (P.px+449, P.py - 925))
    P.surface.blit(P.gondola, (P.px + 276, P.py - 1000 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 287, P.py - 940 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 288, P.py - 960 + abs(P.foam)+gy))
    if P.px == -175 and P.py > 1375 and P.py <= 1425:
        blit_small_door(P,1425)
    if P.py > 1875:
        if P.px == -225:
            P.surface.blit(P.d1_door,(P.px+602,P.py-1671))
        elif P.px == -275:
            P.surface.blit(P.d1_door,(P.px+650,P.py-1671))
        elif P.px == -1225:
            P.surface.blit(P.d1_door,(P.px+1602,P.py-1671))
        elif P.px == -1275:
            P.surface.blit(P.d1_door,(P.px+1650,P.py-1671))
    draw_lamps(P,P.px,P.py,listx,listy,"b")

def north_am_p(P,temppx,temppy,move,gond,gy):
    P.nam_temp.move()
    pre = P.nam_pre.y_dist() > 0
    ace = P.nam_ace.y_dist() > 0
    expert = P.nam_expert.y_dist() > 0
    if P.nam_rival:
        rival = P.nam_rival.y_dist() > 0
        if rival:
            P.nam_rival.move()
    if P.nam_vic:
        vic = P.nam_vic.y_dist() > 0
        if vic:
            P.nam_vic.move()
    if pre:
        P.nam_pre.move()
    if ace:
        P.nam_ace.move()
    if expert:
        P.nam_expert.move()
    #rects start
    r1 = (P.px+350,P.py-850,1500,50)
    r2 = (P.px+300,P.py-1000,50,150)
    r3 = (P.px+350,P.py-1050,60,40)
    r4 = (P.px+450,P.py-1350,450,190)
    r41 = (P.px+450,P.py-1150,100,40)
    r42 = (P.px+600,P.py-1150,300,40)
    r5,r6,r7,r8,r9 = r1,r1,r1,r1,r1
    if P.px == -75 and P.py == 1375:
        r5 = (P.px+400,P.py-1100,50,50)
        r6 = (P.px+450,P.py-1050,50,50)
    if P.px == -75 and P.py == 1175:
        r6 = (P.px+400,P.py-900,50,50)
        r7 = (P.px+450,P.py-950,50,40)
    if P.px == -75 and P.py == 1300:
        r8 = (P.px+450,P.py-1050,50,15)
    if P.px == -75 and P.py == 1200:
        r9 = (P.px+450,P.py-875,50,50)
    r10 = (P.px+750,P.py-1400,350,240)
    r22 = (P.px+950,P.py-1150,150,40)
    r11 = (P.px+1300,P.py-1350,550,240)
    r12 = (P.px+1850,P.py-1100,50,250)
    r13 = (P.px+450,P.py-1650,150,40)
    if P.px == -275:
        r13 = (P.px+450,P.py-1650,200,40)
    r130 = (P.px+700,P.py-1650,900,40)
    if P.px == -225:
        r130 = (P.px+650,P.py-1650,900,40)
    if P.px == -1275:
        r130 = (P.px+700,P.py-1650,950,40)
    r131 = (P.px+1700,P.py-1650,150,40)
    if P.px == -1225:
        r131 = (P.px+1650,P.py-1650,150,40)
    r132 = (P.px+600,P.py-1700,100,40)
    r133 = (P.px+1600,P.py-1700,100,40)
    r14 = (P.px+1850,P.py-1400,250,50)
    r15 = (P.px+1850,P.py-1600,250,40)
    r16 = (P.px+150,P.py-1600,300,40)
    r17 = (P.px+150,P.py-1400,300,50)
    r18 = (P.px-50,P.py-1350,200,50)
    r19 = (P.px-100,P.py-1750,50,400)
    r20 = (P.px-50,P.py-1800,200,40)
    r21 = (P.px+150,P.py-1750,50,150)
    r23 = P.nam_pre.get_rect()
    r24 = P.nam_ace.get_rect()
    r25 = P.nam_expert.get_rect()
    r27 = P.nam_temp.get_rect()
    r26 = (P.px+1100,P.py-1600,100,40)
    rects = [r27,r26,r133,r132,r131,r130,r41,r42,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rects end
    #rect_draw(P,rects)
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+287,P.py-887+abs(P.foam)+gy))
        P.surface.blit(P.p,(P.px+286,P.py-910+abs(P.foam)+gy))
    else:
        if move:
            if P.px >= -50:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,200)])
            else:
                player_move(P,rects,[Rect(P.px+450,P.py-1050,50,190)])
        else:
            blit_player(P)
    if not pre:
        P.nam_pre.move(temppx,temppy)
    if not ace:
        P.nam_ace.move(temppx,temppy)
    if not expert:
        P.nam_expert.move(temppx,temppy)
    if P.nam_vic:
        if not vic:
            P.nam_vic.move(temppx,temppy)
    if P.nam_rival:
        if not rival:
            P.nam_rival.move(temppx,temppy)

def north_am_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.nam_fence,(temppx-150, temppy - 1425))
    if P.py == 1375:
        P.surface.blit(P.nam_fenceu, (temppx + 449, temppy - 1075))
    if P.py > 1175 or P.px > -75:
        P.surface.blit(P.nam_corner, (temppx + 449, temppy - 925))
    P.surface.blit(P.nam_roof, (temppx + 449, temppy - 1400))
    P.surface.blit(P.nam_roof, (temppx + 1299, temppy - 1400))
    P.surface.blit(P.nam_roof, (temppx + 1599, temppy - 1400))
    P.surface.blit(P.nam_roof, (temppx + 449, temppy - 900))
    P.surface.blit(P.nam_roof, (temppx + 736, temppy - 900))
    P.surface.blit(P.nam_roof, (temppx + 1023, temppy - 900))
    P.surface.blit(P.nam_roof, (temppx + 1311, temppy - 900))
    P.surface.blit(P.nam_roof, (temppx + 1599, temppy - 900))
    P.surface.blit(P.nam_proof, (temppx + 825, temppy - 1452))
    P.surface.blit(P.nam_bridge_r, (temppx + 2031, temppy - 1600))
    P.surface.blit(P.nam_mus, (temppx * (8 / 7) + 444, temppy - 1425))
    P.surface.blit(P.nam_garden, (temppx + 123, temppy - 1700))
    P.surface.blit(P.nam_foam, (temppx - 450, temppy - 1320 + abs(P.foam)))
    draw_lamps(P, temppx, temppy, listx, listy)
    if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
        P.surface.blit(P.pc_light,(temppx+865,temppy-1349))
    show_location(P, P.loc_txt, tim)

def north_am(P) -> None:
    if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
        song = "music/am_night.wav"
    else:
        song = "music/am_day.wav"
    if P.song != song:
        P.song = song
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.nam_mus = load("p/am/museum_top.png")
    P.nam_fence = load("p/am/nam_fence.png")
    P.nam_fenceu = load("p/am/nam_fenceu.png")
    P.nam_corner = load("p/am/nam_corner.png")
    P.nam_roof = load("p/am/building_3_roof.png")
    P.nam_proof = load("p/am/poke_center_roof.png")
    P.nam_foam = load("p/am/square_3_foam.png")
    P.nam_square = load("p/am/square_3.png")
    P.nam_bridge_r = load("p/am/bridge_l.png")
    P.nam_garden = load("p/am/garden_hang.png")
    P.nam_pre = npc.NPC(P,'Preschoolerb','Birb',[-50,-1450],[['l',100]],["I wanna catch one of those","birdies, but I'm not tall","enough to reach them."])
    P.nam_ace = npc.NPC(P,'Ace Trainerm','Challenger',[1250,-1500],[['ml',40],['mr',40]],["All that's left now is to walk","in. I'm gonna do it! I'm","really gonna do it!","I'm too scared to do it! But","then all my training will have","been for nothing!"])
    P.nam_temp = npc.NPC(P,'Officer','Challenger',[1100,-1550],[['d',40]],["Our gym leader isn't in right","now. Come back later if you're","looking to challenge the gym."])
    P.nam_expert = npc.NPC(P,'Expertm','Tourney Dude',[1650,-1100],[['r',40]],["Every match is so exciting to","watch! Back in my day, we had","competitions out in the open.","Now we've got these stunning","stadiums! It's crazy how much","can change in a few years."])
    P.nam_rival = None
    temp_vic = 0
    fade = None
    if P.prog[4] == 0:
        P.nam_vic = npc.NPC(P,'Victini','Number One',[50,-1750],[['u',40]],["Every match is so exciting to","watch! Back in my day, we had","competitions out in the open.","Now we've got these stunning","stadiums! It's crazy how much","can change in a few years."])
    else:
        P.nam_vic = None
    if P.prog[0] < 14:
        P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[900,-1100],[['u',100]],["","",""])
        if P.py == 1425:
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[900,-1050],[['u',100]],["","",""])
    set_location(P)
    gond = 0
    gy = 0
    if P.px == -525 and P.py > 1375 and P.py <= 1425:
        pcx = 50-(1425 - P.py)
        pcy = 10-((1425 - P.py)/5)
    else:
        pcx = 0
        pcy = 0
    move = True
    wx = 0
    wy = 0
    tim = 0
    trans = pygame.Surface((800,600))
    vic_trans = 0
    listx = [442,715,1088,1289,1565,1838,709,995,1283,1571,715,1565,1838,1838,1434,846,-60]
    listy = [-1250,-1250,-1250,-1250,-1250,-1250,-1000,-1000,-1000,-1000,-1500,-1500,-1550,-1700,-1745,-1745,-1600]
    north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
    north_am_p(P,P.px,P.py,False,gond,gy)
    north_am_f(P,P.px,P.py,listx,listy,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            song = "music/am_night.wav"
        else:
            song = "music/am_day.wav"
        if P.song != song:
            P.song = song
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
        #print(P.px,P.py)
        if P.prog[4] == 0 and P.px >= 275 and P.py >= 1775:
            move = False
            P.prog[4] += 1
            P.nam_vic = npc.NPC(P,'Victini','Number One',[50,-1750],[['u',60],['d',200]],["Every match is so exciting to","watch! Back in my day, we had","competitions out in the open.","Now we've got these stunning","stadiums! It's crazy how much","can change in a few years."])
            temp_vic = tim
        if P.prog[4] == 1 and tim-temp_vic == 120:
            P.prog[4] += 1
        north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
        temppx = P.px
        temppy = P.py
        north_am_p(P,temppx,temppy,move,gond,gy)
        north_am_f(P, temppx, temppy, listx, listy, tim)
        if P.px == -325 and P.prog[0] == 13:
            move = False
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[900,-1100],[['md',int(abs(npc_y_dist(P,P.nam_rival))*2/5)],['ml',60],['l',10]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 14 and npc_x_dist(P,P.nam_rival) == 50:
            north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
            north_am_p(P,P.px,P.py,False,gond,gy)
            north_am_f(P,P.px,P.py,listx,listy,tim)
            new_txt(P)
            write(P,"Hey "+P.save_data.name +"!","Hope you and your Pokemon have","been doing well.")
            cont(P)
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.nam_rival.x,P.nam_rival.y],[['u',10]],["","",""])
            north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
            north_am_p(P,P.px,P.py,False,gond,gy)
            north_am_f(P,P.px,P.py,listx,listy,tim)
            new_txt(P)
            write(P,"This big building is a Pokemon","Center. You can stock up on","items and rest your Pokemon.")
            cont(P)
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.nam_rival.x,P.nam_rival.y],[['l',10]],["","",""])
            north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
            north_am_p(P,P.px,P.py,False,gond,gy)
            north_am_f(P,P.px,P.py,listx,listy,tim)
            new_txt(P)
            write(P,"I'm gonna see if the gym","leader is taking challenges.","See you later!")
            cont(P)
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.nam_rival.x,P.nam_rival.y],[['mr',200]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 15 and (npc_x_dist(P,P.nam_rival) == 450 or P.nam_rival.y == -1450):
            move = True
            P.nam_rival = None
            P.prog[0] += 1
        if P.px == -525 and P.py == 1375 and P.prog[0] == 13:
            move = False
            pcx = 0
            pcy = 0
            north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
            north_am_p(P,P.px,P.py,False,gond,gy)
            north_am_f(P,P.px,P.py,listx,listy,tim)
            txt(P,"Hey there "+P.save_data.name+"!","I see you've already paid a",'visit to the Pokemon Center.')
            txt(P,"As you might have already","noticed, it's a good place to",'rest and restock on items.')
            txt(P,"I'm gonna see if the gym","leader is taking challenges.","See you later!")
            P.nam_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.nam_rival.x,P.nam_rival.y],[['mr',100],['mu',200]],["","",""])
            P.prog[0] += 2
        if P.prog[4] == 2 or P.prog[4] == 3:
            trans.set_alpha(vic_trans)
            trans.fill((255,230,230))
            P.surface.blit(trans,(0,0))
        if gond == 1:
            gond = 2
            fade_in(P)
        # show_location(P,loc_txt,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and gond == 0 and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == 25 and P.py == 1225 and face_l(P):
                        nxtl = gondolier(P)
                        if nxtl != "North Alto Mare":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.py == 2025 and face_u(P):
                        txt(P,"What a strange place to have","a deadend...","")
                    elif P.py == 1375 and (P.px == -1025 or P.px == -1325) and face_u(P):
                        txt(P,"You feel like this house needs","a renovation...")
                    elif P.nam_pre.talk():
                        north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        north_am_p(P,P.px,P.py,False,gond,gy)
                        north_am_f(P,P.px,P.py,listx,listy,tim)
                        P.nam_pre.write()
                    elif P.nam_temp.talk():
                        north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        north_am_p(P,P.px,P.py,False,gond,gy)
                        north_am_f(P,P.px,P.py,listx,listy,tim)
                        P.nam_temp.write()
                    elif P.nam_ace.talk():
                        north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        north_am_p(P,P.px,P.py,False,gond,gy)
                        north_am_f(P,P.px,P.py,listx,listy,tim)
                        P.nam_ace.write()
                    elif P.nam_expert.talk():
                        north_am_b(P,wx,wy,listx,listy,pcx,pcy,gy)
                        north_am_p(P,P.px,P.py,False,gond,gy)
                        north_am_f(P,P.px,P.py,listx,listy,tim)
                        P.nam_expert.write()
                    elif P.px == 425 and P.py == 1675:
                        txt(P,"There are some birds resting","in the bath.")
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy += 3
        if gy >= 300:
            fade_out(P)
            get_gondo(P,nxtl)
            if P.loc != 'square_1':
                fade = P.song
            end = False
        if P.px == -525 and P.py > 1375 and P.py <= 1425:
            pcx = 50-(1425 - P.py)
            pcy = 10-((1425 - P.py)/5)
        else:
            pcx = 0
            pcy = 0
        if P.px == -525 and P.py == 1425 and face_u(P):
            P.px = 125
            P.py = -325
            P.loc = "pc_am"
            fade = P.song
            end = False
        if P.py == 1925 and face_u(P):
            if P.px == -1275 or P.px == -1225:
                P.px += 1350
                P.py = -125
                P.loc = "house_21_3"
                end = False
            elif P.px == -275 or P.px == -225:
                P.px += 350
                P.py = -125
                P.loc = "house_21_2"
                end = False
        if P.px == -175 and P.py == 1425 and face_u(P):
            P.px = 175 
            P.py = -75
            P.loc = "house_1_1"
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 1825 or P.py == 1775 or P.py == 1725) and P.px == -1725 and face_r(P):
            P.px += 1650
            P.py -= 1150
            P.move_out_dir = 'r'
            P.loc = "route_1"
            fade = P.song
            end = False
        if P.prog[4] == 2:
            vic_trans += 20
        if P.prog[4] == 3:
            vic_trans -= 15
        if vic_trans > 255 and P.prog[4] == 2:
            P.nam_vic = None
            P.prog[4] += 1
        if vic_trans < 0 and P.prog[4] == 3:
            P.prog[4] += 1
            move = True
        #ocean start
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def square_1_b(P,wx,wy,listx,listy,gy,celebi = False):
    draw_waves(P, wx, wy)
    P.surface.blit(P.s1_square, (P.px, P.py - 2000))
    P.surface.blit(P.s1_fence2, (P.px + 1139, P.py - 1025))
    P.surface.blit(P.s1_corner, (P.px + 1139, P.py - 874))
    P.surface.blit(P.gondola, (P.px + 1300, P.py - 950 + abs(P.foam)+gy))
    P.surface.blit(P.char_shad, (P.px + 1311, P.py - 890 + abs(P.foam)+gy))
    P.surface.blit(P.gondolier, (P.px + 1312, P.py - 910 + abs(P.foam)+gy))
    draw_lamps(P,P.px,P.py,listx,listy,"b")
    if celebi:
        P.surface.blit(P.s1_tree, (P.px + 288, P.py - 725))

def square_1_p(P,temppx,temppy,move,gond,gy):
    beauty = P.s1_beauty.y_dist() > 0
    bug = P.s1_bug.y_dist() > 0
    lass = P.s1_lass.y_dist() > 0
    if beauty:
        P.s1_beauty.move()
    if P.s1_rival:
        P.s1_rival.move()
    if bug:
        P.s1_bug.move()
    if lass:
        P.s1_lass.move()
        P.surface.blit(P.s1_fence3, (temppx + 399, temppy - 824))
    #rects start
    r1 = (P.px+400,P.py-300,800,50)
    r2 = (P.px+350,P.py-1350,50,1050)
    r3 = (P.px+400,P.py-1400,800,40)
    r4 = (P.px+1200,P.py-1350,400,40)
    r5 = (P.px+1600,P.py-1300,50,150)
    r6 = (P.px+1200,P.py-1150,400,50)
    r7 = (P.px+1200,P.py-1100,50,100)
    r8 = (P.px+1200,P.py-800,100,500)
    r9 = (P.px+1300,P.py-950,50,150)
    r17,r16,r10,r11,r12,r13,r14,r15 = r1,r1,r1,r1,r1,r1,r1,r1
    if P.px == -775 and P.py == 1325:
        r10 = (P.px+1150,P.py-1000,50,50)
    if P.px == -775 and P.py == 1125:
        r11 = (P.px+1150,P.py-900,50,40)
        r12 = (P.px+1200,P.py-850,50,50)
    if P.px == -775 and P.py == 1250:
        r13 = (P.px+1150,P.py-1000,50,15)
    if P.px == -775 and P.py == 1150:
        r14 = (P.px+1150,P.py-825,50,50)
    if P.px <= -825:
        r15 = (P.px+1200,P.py-1000,100,40)
    if P.py == 1125 and (P.px != -525 and P.px != -475):
        r16 = (P.px+400,P.py-800,800,50)
    if P.py == 1075 and (P.px != -525 and P.px != -475):
        r17 = (P.px+400,P.py-850,800,40)
    r18 = (P.px+450,P.py-500,50,40)
    r19 = P.s1_beauty.get_rect()
    r20 = P.s1_bug.get_rect()
    r21 = P.s1_lass.get_rect()
    rects = [r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    #rects end
    if gond != 0:
        P.surface.blit(P.char_shad,(P.px+1311,P.py-837+abs(P.foam)+gy))
        P.surface.blit(P.p,(P.px+1310,P.py-860+abs(P.foam)+gy))
    else:
        if move:
            if P.px <= -800:
                player_move(P,rects,[],[Rect(1150+P.px,P.py-1000,50,200)])
            else:
                player_move(P,rects,[],[Rect(P.px+1150,P.py-1000,50,190)])
        else:
            blit_player(P)
    if not beauty:
        P.s1_beauty.move(temppx,temppy)
    if not bug:
        P.s1_bug.move(temppx,temppy)
    if not lass:
        P.s1_lass.move(temppx,temppy)
        P.surface.blit(P.s1_fence3, (temppx + 399, temppy - 824))

def square_1_f(P,temppx,temppy,listx,listy,gond,tim,celebi = False):
    draw_grass(P, temppx, temppy, -575, 1075, 250, 300)
    draw_grass(P, temppx, temppy, -175, 1075, 300, 300)
    if gond != 0:
        P.surface.blit(P.s1_bridge, (temppx + 1275, temppy - 1325))
    P.surface.blit(P.s1_bridge_r, (temppx + 1481, temppy - 1350))
    P.surface.blit(P.s1_fence, (temppx + 399, temppy - 1175))
    if not celebi:
        P.surface.blit(P.s1_tree, (temppx + 288, temppy - 725))
    else:
        P.surface.blit(P.s1_tree2, (temppx + 288, temppy - 725))
    if (P.py > 1275):
        P.surface.blit(P.s1_fence2, (temppx + 1139, temppy - 1025))
    if P.py > 1125 or P.px <= -800:
        P.surface.blit(P.s1_corner, (temppx + 1139, temppy - 874))
    P.surface.blit(P.s1_foam, (temppx + 390, temppy - 1070 + abs(P.foam)))
    draw_lamps(P,temppx,temppy,listx,listy)
    show_location(P, P.loc_txt, tim)

def s1_celebi(P,wx,wy,listx,listy):
    cl1 = pygame.transform.scale(load("p/spr/Celebi_l1.png"),(50,60))
    cl2 = pygame.transform.scale(load("p/spr/Celebi_l2.png"),(50,60))
    cl3 = pygame.transform.scale(load("p/spr/Celebi_l3.png"),(50,60))
    cr1 = pygame.transform.scale(load("p/spr/Celebi_r1.png"),(50,60))
    cr2 = pygame.transform.scale(load("p/spr/Celebi_r2.png"),(50,60))
    cr3 = pygame.transform.scale(load("p/spr/Celebi_r3.png"),(50,60))
    cel = cl1
    P.s1_tree2 = load("p/am/cel_tree.png")
    P.habitat = 'grass'
    counter = 300
    tim = 100
    P.py += 250
    P.p = P.l1
    cely = 0
    square_1_b(P,wx,wy,listx,listy,0,True)
    square_1_p(P,P.px,P.py,False,0,tim)
    if P.prog[2] == 0:
        P.surface.blit(cel,(P.px + 340, P.py - 720 + cely))
    square_1_f(P,P.px,P.py,listx,listy,0,0,True)
    fade_in(P)
    end = True
    while end:
        pygame.event.pump()
        square_1_b(P,wx,wy,listx,listy,0,True)
        square_1_p(P,P.px,P.py,False,0,tim)
        if P.prog[2] == 0:
            P.surface.blit(cel,(P.px + 340, P.py - 720 + cely))
        square_1_f(P,P.px,P.py,listx,listy,0,0,True)
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                    P.foam = -5
            if counter > 200:
                if cel == cl1:
                    cel = cl2
                elif cel == cl2:
                    cel = cl3
                else:
                    cel = cl1
            else:
                if cel == cr1:
                    cel = cr2
                elif cel == cr2:
                    cel = cr3
                else:
                    cel = cr1
        if counter <= 120 and counter > 50:
            cely += 1
        tim += 1
        counter -= 1
        if counter == 0:
            end = False
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if P.prog[2] == 0:
        P.prog[2] = 1
        P.s1_bug = npc.NPC(P,'Bug Catcher','Buggy',[500,-450],[['u',20]],["I wonder what Pokemon it was?","Maybe it was a Kakuna? Or even","better, a Beedrill!"])
    P.p = P.u1
    P.py -= 250
    fade_out(P)

def square_1(P) -> None:
    if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
        song = "music/am_night.wav"
    else:
        song = "music/am_day.wav"
    if P.song != song:
        P.song = song
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.s1_bridge = load("p/am/square_2_bridge.png")
    P.s1_square = load("p/am/square_2.png")
    P.s1_bridge_r = load("p/am/bridge_l.png")
    P.s1_tree = load("p/am/tree_1_top.png")
    P.s1_foam = load("p/am/square_2_foam.png")
    set_location(P)
    P.s1_rival = None
    P.s1_fence = load("p/am/square_fence_2.png")
    P.s1_fence2 = load("p/am/square_fence_2_2.png")
    P.s1_fence3 = load("p/am/square_fence_2_extra.png")
    P.s1_corner = load("p/am/square_2_wall.png")
    P.s1_beauty = npc.NPC(P,'Beauty','Beauty',[950,-1350],[['mr',40],['ml',40]],["I'm dying to go in for the","show but my friend is taking","his sweet time getting here."])
    if P.prog[2] == 0:
        P.s1_bug = npc.NPC(P,'Bug Catcher','Buggy',[500,-450],[['u',20]],["There's something rustling in","that tree, but I can't quite","make out what it is."])
    else:
        P.s1_bug = npc.NPC(P,'Bug Catcher','Buggy',[500,-450],[['u',20]],["I wonder what Pokemon it was?","Maybe it was a Kakuna? Or even","better, an Ariados!"])
    P.s1_lass = npc.NPC(P,'Lass','Lassy',[750,-850],[['d',20]],["Ugh! Why do I need to watch","my brother when he's just","messing around?","This is just a waste of my","time! It's so unfair!",""])
    gond = 0
    gy = 0
    wx = 0
    wy = 0
    tim = 0
    move = True
    fade = None
    listx = [1188,1188,788,392,392,392,1188,940,840,1188,392,1188,789]
    listy = [-1500,-1300,-1500,-1500,-1225,-950,-950,-950,-950,-450,-450,-700,-450]
    square_1_b(P,wx,wy,listx,listy,gy)
    square_1_p(P,P.px,P.py,False,gond,gy)
    square_1_f(P,P.px,P.py,listx,listy,gond,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            song = "music/am_night.wav"
        else:
            song = "music/am_day.wav"
        if P.song != song:
            P.song = song
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
        #print(P.px,P.py)
        square_1_b(P,wx,wy,listx,listy,gy)
        temppx = P.px
        temppy = P.py
        square_1_p(P,temppx,temppy,move,gond,gy)
        square_1_f(P,temppx,temppy,listx,listy,gond,tim)
        if P.prog[0] == 9 and P.px == -825:
            P.s1_rival = npc.NPC(P,'Rival',P.save_data.rival,[1500,-1*(P.py-275)],[['ml',100],['l',10]],["","",""])
            move = False
            P.prog[0] += 1
        if P.prog[0] == 11 and P.s1_rival.x == 1250:
            new_txt(P)
            write(P,f'Hey there {P.save_data.name}!', "I\'m "+P.save_data.rival+", one of Professor", "Burnet\'s assistants.")
            cont(P)
            new_txt(P)
            write(P,"Have some Pokeballs, there\'s a","park right there where a lot","of Pokemon go to visit.")
            cont(P)
            new_txt(P)
            write(P,"Just toss a Pokeball from your","bag when they\'re low and you","might catch some.")
            cont(P)
            new_txt(P)
            write(P,"There\'s also a gondolier that", "can take you to the northern", "part of town.")
            cont(P)
            new_txt(P)
            write(P,"Good luck on your adventure!")
            cont(P)
            add_item(P,'Poke Ball',5)
            P.s1_rival = npc.NPC(P,'Rival',P.save_data.rival,[P.s1_rival.x,P.s1_rival.y],[['mr',100]],["","",""])
            P.prog[0] += 1
        if P.prog[0] == 10 and P.s1_rival.x == 1250:
            P.p = P.r1
            P.prog[0] += 1
        if P.prog[0] == 12 and P.s1_rival.x == 1500:
            move = True
            P.s1_rival = None
            P.prog[0] += 1
        if gond == 1:
            gond = 2
            fade_in(P)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.px == -875 and P.py == 1175 and face_r(P):
                        if P.prog[7] == 0:
                            P.prog[7] += 1
                        nxtl = gondolier(P)
                        if nxtl != "South Alto Mare":
                            gond = 1
                            new_txt(P)
                            write(P,"Alright, come aboard.")
                            cont(P)
                            new_txt(P)
                            write(P,"Next stop, " + nxtl + "!")
                            cont(P)
                            fade_out(P)
                            P.p = P.d1
                    elif P.py == 1625 and (P.px == -575 or P.px == -625):
                        txt(P,"You feel like this house needs","a renovation...")
                    elif next_to(P,450,-500):
                        if face_u(P):
                            temp = P.surface.copy()
                            new_txt(P)
                            write(P,'Climb the tree?')
                            if choice(P,550,600):
                                fade_out(P)
                                P.clock.tick(1)
                                s1_celebi(P,wx,wy,listx,listy)
                                P.clock.tick(1)
                                P.surface.blit(temp,(0,0))
                                fade_in(P)
                        else:
                            txt(P,"You could probably climb the","tree with the ladder.")
                    elif P.s1_beauty.talk():
                        square_1_b(P,wx,wy,listx,listy,gy)
                        square_1_p(P,P.px,P.py,False,gond,gy)
                        square_1_f(P,P.px,P.py,listx,listy,gond,tim)
                        P.s1_beauty.write()
                    elif P.s1_bug.talk():
                        square_1_b(P,wx,wy,listx,listy,gy)
                        square_1_p(P,P.px,P.py,False,gond,gy)
                        square_1_f(P,P.px,P.py,listx,listy,gond,tim)
                        P.s1_bug.write()
                    elif P.s1_lass.talk():
                        square_1_b(P,wx,wy,listx,listy,gy)
                        square_1_p(P,P.px,P.py,False,gond,gy)
                        square_1_f(P,P.px,P.py,listx,listy,gond,tim)
                        P.s1_lass.write()
                    else:
                        P.buffer_talk = temp_buff
        if gond == 2:
            gy -= 3
        if gy <= -300:
            fade_out(P)
            get_gondo(P,nxtl)
            if P.loc != 'north_am':
                fade = P.song
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if move and (wild_grass(P,-175,1075,300,300) or wild_grass(P,-575,1075,250,300)):
            te = P.surface.copy()
            P.song = "music/wild_battle.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(0)
            rando = random.random()
            if rando < .2:
                r = random.randint(3,4)
                if r < 4:
                    battle(P,[poke.Poke('Skitty',[r,random.randint(0,1),334,"Fake Out",-1,"Growl",-1,"Tail Whip",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Skitty',[r,random.randint(0,1),334,"Fake Out",-1,"Growl",-1,"Foresight",-1,"Tackle",-1,None,None,0,"Poke Ball"])])
            elif rando >= .2 and rando < .45:
                r = random.randint(3,4)
                if r < 4:
                    battle(P,[poke.Poke('Poochyena',[r,random.randint(0,1),334,"Tackle",-1,None,None,None,None,None,None,None,None,0,"Poke Ball"])])
                else:
                    battle(P,[poke.Poke('Poochyena',[r,random.randint(0,1),334,"Tackle",-1,"Howl",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .45 and rando < .75:
                battle(P,[poke.Poke('Caterpie',[random.randint(2,3),random.randint(0,1),334,"Tackle",-1,"String Shot",-1,None,None,None,None,None,None,0,"Poke Ball"])])
            elif rando >= .75:
                battle(P,[poke.Poke('Joltik',[random.randint(2,3),random.randint(0,1),334,"String Shot",-1,"Absorb",-1,"Spider Web",-1,None,None,None,None,0,"Poke Ball"])])
            if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
                P.song = "music/am_night.wav"
            else:
                P.song = "music/am_day.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
            P.surface.blit(te,(0,0))
            fade_in(P)
        if (P.py == 1575 or P.py == 1525 or P.py == 1475) and P.px == -1175 and face_r(P):
            P.px += 1150
            P.py -= 1250
            P.move_out_dir = 'r'
            if datetime.datetime.today().weekday() in [5,6] and (get_time() >= 6 and get_time() <= 19):
                fade = P.song
            P.loc = "am_square"
            end = False
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
            if P.gondola == P.gondola_1:
                P.gondola = P.gondola_2
            else:
                P.gondola = P.gondola_1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def am_square_b(P,wx,wy,listx,listy):
    draw_waves(P, wx, wy)
    P.surface.blit(P.ams_square, (P.px, P.py - 2000))
    draw_lamps(P,P.px,P.py,listx,listy,"b")
    # P.surface.blit(P.ams_young, (P.px + 1500, P.py - 110))

def am_square_p(P,temppx,temppy,move):
    beauty = P.ams_beauty.y_dist() > 0
    joey = P.ams_joey.y_dist() > 0
    scientist = P.ams_scientist.y_dist() > 0
    sci = P.ams_sci.y_dist() > 0
    pre = P.ams_pre.y_dist() > 0
    gentle = P.ams_gentle.y_dist() > 0
    lass = P.ams_lass.y_dist() > 0
    boi = P.ams_boi.y_dist() > 0
    if P.ams_npc1:
        one = P.ams_npc1.y_dist() > 0
        if one:
            P.ams_npc1.move()
    if P.ams_npc2:
        two = P.ams_npc2.y_dist() > 0
        if two:
            P.ams_npc2.move()
    if P.ams_npc3:
        three = P.ams_npc3.y_dist() > 0
        if three:
            P.ams_npc3.move()
            P.surface.blit(P.ams_bs,(P.px + 2025, P.py - 280))
    if P.ams_npc4:
        four = P.ams_npc4.y_dist() > 0
        if four:
            P.ams_npc4.move()
            P.surface.blit(P.ams_box,(P.px + 1200, P.py - 465))
    if P.ams_npc5:
        five = P.ams_npc5.y_dist() > 0
        if five:
            P.ams_npc5.move()
    if P.ams_npc6:
        six = P.ams_npc6.y_dist() > 0
        if six:
            P.ams_npc6.move()
    if P.ams_npc7:
        seven = P.ams_npc7.y_dist() > 0
        if seven:
            P.ams_npc7.move()
    if P.ams_npc8:
        eight = P.ams_npc8.y_dist() > 0
        if eight:
            P.ams_npc8.move()
    if P.ams_npc9:
        nine = P.ams_npc9.y_dist() > 0
        if nine:
            P.ams_npc9.move()
        ten = P.ams_npc10.y_dist() > 0
        if ten:
            P.ams_npc10.move()
    if beauty:
        P.ams_beauty.move()
    if joey:
        P.ams_joey.move()
    if scientist:
        P.ams_scientist.move()
    if sci:
        P.ams_sci.move()
    if pre:
        P.ame_pre.move()
    if gentle:
        P.ams_gentle.move()
    if lass:
        P.ams_lass.move()
    if boi:
        P.ams_boi.move()
    #rect start
    r1 = (P.px+400,P.py-100,500,40)
    r2 = (P.px+400,P.py+100,700,50)
    r3 = (P.px+1050,P.py+100,50,800)
    r4 = (P.px+1300,P.py+100,50,800)
    r5 = (P.px+1050,P.py+850,300,50)
    r6 = (P.px+1150,P.py+750,100,40)
    r7 = (P.px+1300,P.py+100,400,50)
    r8 = (P.px+1650,P.py+100,50,800)
    r9 = (P.px+1650,P.py+850,300,50)
    r10 = (P.px+1750,P.py+750,100,40)
    r11 = (P.px+1900,P.py+100,50,800)
    r12 = (P.px+1900,P.py+100,700,50)
    r13 = (P.px+2100,P.py-100,500,40)
    r14 = (P.px+2600,P.py-50,50,150)
    r15 = (P.px+2100,P.py-600,50,540)
    r16 = (P.px+2000,P.py-650,100,40)
    r17 = (P.px+1700,P.py-600,300,40)
    r18,r19,r20,r21,r22,r23,r26,r27,r28,r29,r30,r31 = r1,r1,r1,r1,r1,r1,r1,r1,r1,r1,r1,r1
    if P.py == 825:
        if P.px == -1625:
            r18 = (P.px+1950,P.py-550,50,40)
        if P.px == -1575:
            r19 = (P.px+2000,P.py-550,50,40)
        if P.px == -1525:
            r20 = (P.px+1850,P.py-550,50,40)
        if P.px == -1475:
            r21 = (P.px+1900,P.py-550,50,40)
        if P.px == -1425:
            r22 = (P.px+1750,P.py-550,50,40)
        if P.px == -1375:
            r23 = (P.px+1800,P.py-550,50,40)
        if P.px == -825:
            r26 = (P.px+1150,P.py-550,50,40)
        if P.px == -775:
            r27 = (P.px+1200,P.py-550,50,40)
        if P.px == -725:
            r28 = (P.px+1050,P.py-550,50,40)
        if P.px == -675:
            r29 = (P.px+1100,P.py-550,50,40)
        if P.px == -625:
            r30 = (P.px+950,P.py-550,50,40)
        if P.px == -575:
            r31 = (P.px+1000,P.py-550,50,40)
    r24 = (P.px+1650,P.py-650,50,140)
    r25 = (P.px+1300,P.py-650,50,140)
    r32 = (P.px+1000,P.py-600,300,40)
    r33 = (P.px+900,P.py-650,100,40)
    r34 = (P.px+850,P.py-650,50,540)
    r35 = (P.px+350,P.py-50,50,150)
    r36 = (P.px+1350,P.py-300,300,190)
    r37 = (P.px+1250,P.py-250,500,90)
    r38 = (P.px+1350,P.py-650,300,40)
    # ry = (P.px+1500,P.py-100,50,40)
    r39 = P.ams_joey.get_rect()
    r40 = P.ams_beauty.get_rect()
    r41 = P.ams_scientist.get_rect()
    r42 = P.ams_pre.get_rect()
    r43 = P.ams_sci.get_rect()
    r44 = P.ams_gentle.get_rect()
    r45 = P.ams_lass.get_rect()
    r46 = P.ams_boi.get_rect()
    r47,r48,r49,r50,r51,r52,r53,r54,r55,r56 = r1,r1,r1,r1,r1,r1,r1,r1,r1,r1
    if P.ams_npc1:
        r47 = P.ams_npc1.get_rect()
    if P.ams_npc2:
        r48 = P.ams_npc2.get_rect()
    if P.ams_npc3:
        r49 = (P.px+2050,P.py-300,50,140)
    if P.ams_npc4:
        r50 = (P.px+1200,P.py-450,100,40)
    if P.ams_npc5:
        r51 = P.ams_npc5.get_rect()
    if P.ams_npc6:
        r52 = P.ams_npc6.get_rect()
    if P.ams_npc7:
        r53 = P.ams_npc7.get_rect()
    if P.ams_npc8:
        r54 = P.ams_npc8.get_rect()
    if P.ams_npc9:
        r55 = P.ams_npc9.get_rect()
        r56 = P.ams_npc10.get_rect()
    rects = [r56,r55,r54,r53,r52,r51,r50,r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,r37,r36,r35,r34,r33,r32,r31,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects)
    else:
        blit_player(P)
    if P.ams_npc1:
        if not one:
            P.ams_npc1.move(temppx,temppy)
    if P.ams_npc2:
        if not two:
            P.ams_npc2.move(temppx,temppy)
    if P.ams_npc3:
        if not three:
            P.ams_npc3.move(temppx,temppy)
            P.surface.blit(P.ams_bs,(temppx + 2025, temppy - 280))
    if P.ams_npc4:
        if not four:
            P.ams_npc4.move(temppx,temppy)
            P.surface.blit(P.ams_box,(temppx + 1200, temppy - 465))
    if P.ams_npc5:
        if not five:
            P.ams_npc5.move(temppx,temppy)
    if P.ams_npc6:
        if not six:
            P.ams_npc6.move(temppx,temppy)
    if P.ams_npc7:
        if not seven:
            P.ams_npc7.move(temppx,temppy)
    if P.ams_npc8:
        if not eight:
            P.ams_npc8.move(temppx,temppy)
    if P.ams_npc9:
        if not nine:
            P.ams_npc9.move(temppx,temppy)
        if not ten:
            P.ams_npc10.move(temppx,temppy)
    if not scientist:
        P.ams_scientist.move(temppx,temppy)
    if not sci:
        P.ams_sci.move(temppx,temppy)
    if not joey:
        P.ams_joey.move(temppx,temppy)
    if not beauty:
        P.ams_beauty.move(temppx,temppy)
    if not pre:
        P.ams_pre.move(temppx,temppy)
    if not gentle:
        P.ams_gentle.move(temppx,temppy)
    if not lass:
        P.ams_lass.move(temppx,temppy)
    if not boi:
        P.ams_boi.move(temppx,temppy)

def am_square_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.ams_foam, (temppx + 440, temppy + 182 + abs(P.foam)))
    P.surface.blit(P.ams_statue_l, (temppx + 1080, temppy + 150))
    P.surface.blit(P.ams_statue_r, (temppx + 1672, temppy + 123))
    P.surface.blit(P.ams_balc_r, (temppx + 2060, temppy - 550))
    P.surface.blit(P.ams_balc_l, (temppx + 902, temppy - 550))
    P.surface.blit(P.ams_fount, (temppx + 1250, temppy - 365))
    P.surface.blit(P.ams_bridge_l, (temppx + 400, temppy - 100))
    P.surface.blit(P.ams_bridge_r, (temppx + 2481, temppy - 100))
    P.surface.blit(P.ams_fence, (temppx + 491, temppy + 75))
    draw_lamps(P,temppx,temppy,listx,listy)
    if (datetime.datetime.today().weekday() in [5,6] and get_time() >= 6):
        if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
            P.surface.blit(P.ams_festive_overn,(temppx+900,temppy-625))
        else:
            P.surface.blit(P.ams_festive_over,(temppx+900,temppy-625))
    show_location(P, P.loc_txt, tim)

def am_square(P) -> None:
    saturday = False
    mus_vol = P.vol
    P.ams_npc1 = None
    P.ams_npc2 = None
    P.ams_npc3 = None
    P.ams_npc4 = None
    P.ams_npc5 = None
    P.ams_npc6 = None
    P.ams_npc7 = None
    P.ams_npc8 = None
    P.ams_npc9 = None
    P.ams_npc10 = None
    #datetime.datetime.today().weekday() == 5 and get_time() >= 6
    if datetime.datetime.today().weekday() == 5 and get_time() >= 6:
    #if True:
        P.ams_beauty = npc.NPC(P,'Beauty','Beauty',[1400,50],[['u',20]],["I love the music that guy is","playing! It reminds me of my","mom's favorite song!","I want to give him some money","but for some odd reason my","boyfriend won't let me."])
        P.ams_boi = npc.NPC(P,'Rich Boy','Boi',[1350,50],[['u',20]],["Do you think that guy's gonna","move to another spot anytime","soon?","I really want to get a good","picture in front of the","fountain but he's in the way."])
        P.ams_scientist = npc.NPC(P,'Scientistm','Scientist',[1250,400],[['md',40],['d',80],['md',20],['d',40],['u',60],['mu',20],['u',90],['mu',40],['u',60],['d',50]],["Latias is one of the guardians","of Alto Mare, distinguished by","its gorgeous red coat.","I would do anything to see it","in person some day...",""])
        P.ams_pre = npc.NPC(P,'Preschoolerg','girl',[1800,800],[['u',20]],["I wanna meet the guy that","built this statue! He must be","crazy tall!"])
        P.ams_joey = npc.NPC(P,'Youngster','Joey',[1700,-350],[['mr',40],['r',60],['ml',40],['l',120]],["There's so many people here","today! I betcha there's","something fun to do!","I feel like I could just","forget about all my problems","and have fun!"])
        P.ams_sci = npc.NPC(P,'Officer','Scientist',[1500,-550],[['d',20]],["The museum is closed for","renovations. Please come back","another time."])
        P.ams_gentle = npc.NPC(P,'Gentleman','Criminal',[2150,0],[['l',20],['u',40],['d',30],['r',50]],["More attractions means more","tourists! And that means more","business!"])
        P.ams_lass = npc.NPC(P,'Expertf','Juliet',[950,-450],[['l',100],['mr',40],['r',80],['md',20],['d',120],['mu',20],['u',40],['ml',40]],["Every time this square gets","this populated, it's always so","full of life!","I'm so thankful I chose to","retire in a city like this!",""])
        P.ams_npc1 = npc.NPC(P,'Maractus','Heya',[1500,-100],[['d',120]],["MARACA-ACA!", "", ""])
        P.ams_npc2 = npc.NPC(P,'Guitarist','Heya',[1450,-100],[['d',120]],["Maraca-aca!", "", ""])
        P.ams_npc3 = npc.NPC(P,'Aroma Lady','Berry',[2050,-300],[['l',40]],["Maraca-aca!", "", ""])
        if P.prog[1] == 3:
            P.ams_npc7 = npc.NPC(P,'Gentleman','Pinap',[2050,-350],[['l',40]],["If I give you too many for", "free, the other customers will", "get jealous!","But if you come back next","week, I'm sure I can sneak you","another one!"])
        if P.prog[0] >= 87:
            P.ams_npc8 = npc.NPC(P,'Healer','Massage',[1200,-300],[['l',40]],["My hands are feeling a little", "tired, but be sure to come", "back next week!", "I'll be ready to give your", "Pokemon more great massages!",""])
        P.ams_bs = load("p/am/berry_stand.png")
        if P.prog[11][1][0] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][1][0][0],P.prog[11][1][0][1],P.prog[11][1][0][2])).days > 6:
            berry_list = ['Oran','Sitrus','Pecha','Cheri','Lum','Persim','Chesto','Rawst','Aspear']
            berry_num = random.randint(2,4)
            store_list = []
            stocks = {}
            for x in range(berry_num):
                b = berry_list.pop(random.randint(0,len(berry_list)-1))+" Berry"
                store_list.append(b)
                stocks[b] = random.randint(2,6)
            store_list.append('Quit')
            day = datetime.datetime.today().date()
            P.prog[11][1][0] = [day.year,day.month,day.day]
            P.prog[11][1][1] = store_list
            P.prog[11][1][2] = stocks
            f = open("save_files/"+P.save_data.name+".txt","r")
            data = f.readlines()
            data_temp = save.Save(data)
            data_temp.prog[11][1] = P.save_data.prog[11][1]
            data[6] = str(data_temp.prog)+"\n"
            f.close()
            f2 = open("save_files/"+P.save_data.name+".txt","w")
            f2.writelines(data)
            f2.close()
        song = "music/am_festive.wav"
        saturday = True
        fes_vol = 0
        dist = math.sqrt(P.ams_npc2.y_dist()**2+P.ams_npc2.x_dist()**2)
        if dist < 500:
            fes_vol = P.vol-(P.vol*dist/500)
        mus_vol = P.vol-(fes_vol)
        if fes_vol >= 1:
            fes_vol = fes_vol**2
        pygame.mixer.Channel(0).set_volume(fes_vol*2)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/festive.wav'),loops = -1)
        #move outta way
        if P.py == 225 and (P.px == -1025 or P.px == -975):
            #boy girl
            P.py += 50
        elif P.py == 375 and (P.px == -1075 or P.px == -1125):
            #musician
            P.py -= 50
        elif P.px == -1675 and (P.py >= 475 and P.py <= 6255):
            #berry girl + pinap man
            P.px += 50
        elif P.py == 575 and P.px == -825 and P.prog[0] >= 87:
            #massage girl
            P.py += 50
    #datetime.datetime.today().weekday() == 6 and get_time() >= 6
    elif datetime.datetime.today().weekday() == 6 and get_time() >= 6:
    # elif True:
        P.ams_beauty = npc.NPC(P,'Beauty','Beauty',[1400,50],[['u',20]],["Wow! would you look at that","guy go! Do you think he ever","get tired?"])
        P.ams_boi = npc.NPC(P,'Rich Boy','Boi',[1350,50],[['u',20]],["Ugh, there's so many people","just coming and going as they","please.","It's like they have no respect","for people trying to get some","nice photos."])
        P.ams_scientist = npc.NPC(P,'Scientistm','Scientist',[1250,400],[['md',40],['d',80],['md',20],['d',40],['u',60],['mu',20],['u',90],['mu',40],['u',60],['d',50]],["Latias is one of the guardians","of Alto Mare, distinguished by","its gorgeous red coat.","I would do anything to see it","in person some day...",""])
        P.ams_pre = npc.NPC(P,'Preschoolerg','girl',[1800,800],[['u',20]],["I wanna meet the guy that","built this statue! He must be","crazy tall!"])
        P.ams_joey = npc.NPC(P,'Youngster','Joey',[1700,-350],[['mr',40],['r',60],['ml',40],['l',120]],["There's so many people here","today! I betcha there's","something fun to do!","I feel like I could just","forget about all my problems","and have fun!"])
        P.ams_sci = npc.NPC(P,'Officer','Scientist',[1500,-550],[['d',20]],["The museum is closed for","renovations. Please come back","another time."])
        P.ams_gentle = npc.NPC(P,'Gentleman','Criminal',[2150,0],[['l',20],['u',40],['d',30],['r',50]],["More attractions means more","tourists! And that means more","business!"])
        P.ams_lass = npc.NPC(P,'Expertf','Juliet',[950,-450],[['l',100],['mr',40],['r',80],['md',20],['d',120],['mu',20],['u',40],['ml',40]],["Every time this square gets","this populated, it's always so","full of life!","I'm so thankful I chose to","retire in a city like this!",""])
        if P.prog[0] >= 48:
            P.ams_npc4 = npc.NPC(P,'Scientistf','Ball',[1250,-450],[['d',40]],["Sorry, but we only have enough", "Poke Balls to give everyone", "one sample.","Come back next week and we","will have a new batch ready","for you!"])
        P.ams_npc5 = npc.NPC(P,'Poke Fan','Shrooms',[1700,-150],[['d',120]],["Hey if you happen to have any", "mushrooms you don't need, I", "can take them off your hands.","I have some nice items I can","give you if you help me finish","this collection!"])
        P.ams_npc6 = npc.NPC(P,'Triathelete','Wata',[1000,-50],[['mr',190],['ml',190]],["You know what they say!","A bottle of water a day keeps","the old age away!","I think it goes something","along those lines...",""],spd = 1)
        if P.prog[16] == 2:
            P.ams_npc9 = npc.NPC(P,'Fisherman','Rare',[900,-200],[['r',40]],["Maraca-aca!", "", ""])
            P.ams_npc10 = npc.NPC(P,'Seedot','Seed',[900,-150],[['r',40]],["SEEDOT!!!", "", ""])
            if P.prog[11][7][0] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][7][0][0],P.prog[11][7][0][1],P.prog[11][7][0][2])).days > 6:
                l1 = ['Water Gem','Damp Rock','Mystic Water','Splash Plate','Oval Stone']
                l2 = ['Ice Gem','Icy Rock','Never-Melt Ice','Icicle Plate','Light Clay']
                l3 = ['Rock Gem','Smooth Rock','Hard Stone','Stone Plate','Everstone']
                l = [l1,l2,l3]
                store_list = []
                stocks = {}
                for x in range(3):
                    num = random.random()
                    if num < 0.3:
                        store_list.append(l[x][0])
                        stocks[l[x][0]] = random.randint(2,5)
                    elif num < 0.5:
                        store_list.append(l[x][1])
                        stocks[l[x][1]] = 1
                    elif num < .7:
                        store_list.append(l[x][2])
                        stocks[l[x][2]] = 1
                    elif num < .9:
                        store_list.append(l[x][3])
                        stocks[l[x][3]] = 1
                    else:
                        store_list.append(l[x][4])
                        stocks[l[x][4]] = 1
                if random.random() < 0.4:
                    evo_list = ['Deep Sea Scale','Deep Sea Tooth','Prism Scale','Dragon Scale']
                    num = random.randint(0,3)
                    store_list.append(evo_list[num])
                    stocks[evo_list[num]] = 1
                if random.random() < 0.4:
                    other_list = ['Heart Scale','Heart Scale','Water Stone','Shell Bell']
                    num = random.randint(0,3)
                    store_list.append(other_list[num])
                    stocks[other_list[num]] = 1
                store_list.append('Quit')
                day = datetime.datetime.today().date()
                P.prog[11][7][0] = [day.year,day.month,day.day]
                P.prog[11][7][1] = store_list
                P.prog[11][7][2] = stocks
                f = open("save_files/"+P.save_data.name+".txt","r")
                data = f.readlines()
                data_temp = save.Save(data)
                data_temp.prog[11][7] = P.save_data.prog[11][7]
                data[6] = str(data_temp.prog)+"\n"
                f.close()
                f2 = open("save_files/"+P.save_data.name+".txt","w")
                f2.writelines(data)
                f2.close()
        P.ams_box = load("p/am/ball_box.png")
        song = "music/am_festive.wav"
        if P.py == 225 and (P.px == -1025 or P.px == -975):
            #boy girl
            P.py += 50
        elif P.py == 725 and (P.px == -875 or P.px == -825) and P.prog[0] >= 48:
            #ball boi
            P.py -= 50
        elif P.py == 425 and P.px == -1325:
            #shrooms boi
            P.py -= 50
        elif P.px == -525 and (P.py == 475 or P.py == 425):
            #fisherman
            P.px -= 50
    else:
        P.ams_beauty = npc.NPC(P,'Beauty','Beauty',[1450,50],[['u',20]],["I wonder if that kid is ever","going to move out of the way.","","I want to ask him to move but","he looks awfully stressed","about something."])
        P.ams_boi = npc.NPC(P,'Rich Boy','Boi',[1450,-100],[['d',20]],["Can't you see I'm posing for","a picture? Give a man some","space."])
        P.ams_scientist = npc.NPC(P,'Scientistm','Scientist',[1250,400],[['md',40],['d',80],['md',20],['d',40],['u',60],['mu',20],['u',90],['mu',40],['u',60],['d',50]],["Latias is one of the guardians","of Alto Mare, distinguished by","its gorgeous red coat.","I would do anything to see it","in person some day...",""])
        P.ams_pre = npc.NPC(P,'Preschoolerg','girl',[1800,800],[['u',20]],["I wanna meet the guy that","built this statue! He must be","crazy tall!"])
        P.ams_joey = npc.NPC(P,'Youngster','Joey',[1700,-300],[['l',20]],["I accidentally dropped my","phone in the fountain...","","If my dad finds out he's gonna","kill me! He just bought it","yesterday...","I'm too young to die!","",""])
        P.ams_sci = npc.NPC(P,'Officer','Scientist',[1500,-550],[['d',20]],["The museum is closed for","renovations. Please come back","another time."])
        P.ams_gentle = npc.NPC(P,'Gentleman','Criminal',[2150,0],[['l',20],['u',40],['d',30],['r',50]],["The Tour de Alto Mare is one", "of the most popular tourist", "attractions.", "Trainers race in the canals","atop a wooden raft attached to","a Pokemon.","That piece of information is","going to cost you $1000.","","No?","Well it was worth a try...",""])
        P.ams_lass = npc.NPC(P,'Expertf','Juliet',[950,-450],[['l',100],['mr',40],['r',80],['md',20],['d',120],['mu',20],['u',40],['ml',40]],["On the weekends, the square", "gets filled with people from", "all over the islands!", "It's a great time for young", "people like you to come and","enjoy the festivities!"])
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            song = "music/am_night.wav"
        else:
            song = "music/am_day.wav"
        #move outta way
        if P.px == -1325 and P.py == 575:
            #youngs
            P.px -= 50
        elif P.px == -1075 and (P.py == 375 or P.py == 225):
            #boy girl
            P.px -= 50
    if P.song != song:
        P.song = song
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,mus_vol)
        pygame.mixer.music.play(-1)
    P.ams_square = load("p/am/Alto_Mare_Square.png")
    P.ams_statue_l = load("p/am/as_statue.png")
    P.ams_statue_r = load("p/am/os_statue.png")
    P.ams_balc_r = load("p/am/am_balcony_r.png")
    P.ams_balc_l = load("p/am/am_balcony_l.png")
    P.ams_bridge_l = load("p/am/bridge_r.png")
    P.ams_bridge_r = load("p/am/bridge_l.png")
    P.ams_foam = load("p/am/am_square_foam.png")
    fount_1 = load("p/am/am_fountain_1.png")
    fount_2 = load("p/am/am_fountain_2.png")
    fount_3 = load("p/am/am_fountain_3.png")
    P.ams_fount = fount_1
    P.ams_festive_over = load("p/am/festival_overhead.png")
    P.ams_festive_overn = load("p/am/festival_overhead_night.png")
    if get_time() > 19 or get_time() < 6:
        P.ams_fount = fount_3
    P.ams_fence = load("p/am/alto_mare_fence.png")
    set_location(P)
    wx = 0
    wy = 0
    move = True
    fade = None
    tim = 0
    listx = [1889,1691,1889,1691,1289,1091,1289,1091,1889,1691,1289,1091,2090,890,1666,1316,990,1090,1190,1990,1890,1790]
    listy = [-50,-50,700,700,-50,-50,700,700,325,325,325,325,-200,-200,-650,-650,-650,-650,-650,-650,-650,-650]
    am_square_b(P,wx,wy,listx,listy)
    am_square_p(P,P.px,P.py,False)
    am_square_f(P,P.px,P.py,listx,listy,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        if saturday:
            fes_vol = 0
            dist = math.sqrt(P.ams_npc2.y_dist()**2+P.ams_npc2.x_dist()**2)
            if dist < 500:
                fes_vol = P.vol-(P.vol*dist/500)
            mus_vol = P.vol-(fes_vol)
            if fes_vol >= 1:
                fes_vol = fes_vol**2
            pygame.mixer.Channel(0).set_volume(fes_vol*2)
            set_mixer_volume(P,mus_vol)
        print(P.px,P.py)
        if not (datetime.datetime.today().weekday() in [5,6] and get_time() >= 6):
            if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
                song = "music/am_night.wav"
            else:
                song = "music/am_day.wav"
            if P.song != song:
                P.song = song
                pygame.mixer.music.load(P.song)
                set_mixer_volume(P,mus_vol)
                pygame.mixer.music.play(-1)
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            if P.ams_fount != fount_3:
                    P.ams_fount = fount_3
        else:
            if P.ams_fount == fount_3:
                 P.ams_fount = fount_1
        am_square_b(P,wx,wy,listx,listy)
        #rects start
        #rects end
        temppx = P.px
        temppy = P.py
        am_square_p(P,temppx,temppy,move)
        am_square_f(P,temppx,temppy,listx,listy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.ams_joey.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_joey.write()
                    elif next_to(P,1600,-150) or next_to(P,1550,-150) or next_to(P,1500,-150) or next_to(P,1450,-150) or next_to(P,1400,-150) or next_to(P,1350,-150) or next_to(P,1250,-200) or next_to(P,1300,-200) or next_to(P,1650,-200) or next_to(P,1700,-200) or next_to(P,1250,-250) or next_to(P,1300,-250) or next_to(P,1650,-250) or next_to(P,1700,-250) or next_to(P,1600,-300) or next_to(P,1550,-300) or next_to(P,1500,-300) or next_to(P,1450,-300) or next_to(P,1400,-300) or next_to(P,1350,-300):
                        txt(P,"You can see piles of coins at","the bottom of the fountain.")
                    elif P.ams_npc1 and P.ams_npc1.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.font = pygame.font.SysFont("courier", 40, bold = False, italic = True)
                        P.ams_npc1.write()
                        P.font = pygame.font.SysFont("courier", 40, bold = True, italic = False)
                    elif P.ams_npc2 and P.ams_npc2.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        txt(P,"Hey there!","If you're enjoying the music,","feel free to give a donation!")
                        if P.save_data.money >= 10:
                            new_txt(P)
                            write(P,"Donate how much?")
                            mon = choose_num(P,P.save_data.money,True)
                            agot = False
                            if P.prog[11][0] >= 10000:
                                agot = True
                            if mon != 0:
                                if mon < 10:
                                    txt(P,"Thanks a lot buddy!", "Even the small donations are", "greatly appreciated!")
                                elif mon >= 100:
                                    txt(P,"Wow! Thanks so much! I'll be","sure to make your contribution","worth it!")
                                else:
                                    txt(P,"Much appreciated! Hope you","have a great day!")
                                P.save_data.money -= mon*10
                                P.prog[11][0] += mon*10
                                if agot == False and P.prog[11][0] >= 10000:
                                    txt(P,"Hey, I noticed you seem to","really appreciate my music and","have been pretty generous.")
                                    txt(P,"I recently got something quite","special, and I feel like you","deserve to have it.")
                                    txt(P,"Well anyways, here you go!")
                                    txt(P,"You received Maractus!")
                                    get_poke(P,poke.Poke('Maractus_S',[10,random.randint(0,1),334,"Spiky Shield",-1,"Peck",-1,"Pin Missile",-1,"Return",-1,None,None,0,"Luxury Ball",0,'Storm Drain']),False)
                                    txt(P,"Thanks again for all the","support!")
                            else:
                                txt(P,"No worries!","As long as you're having a","good time, I'm happy!")
                    elif P.ams_npc3 and P.ams_npc3.talk():
                        box = load("p/3_box.png")
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Fresh berries!","Interested in buying any?")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            P.prog[11][1][2] = poke_mart(P, mt, custom_shop = P.prog[11][1][1],stock = P.prog[11][1][2],price_mod = 0.5)
                                            new_txt(P)
                                            write(P,"Is there anything else you", "would like?")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P,"Is there anything else you", "would like?")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"Have a great day!")
                    elif P.ams_npc4 and P.ams_npc4.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        if P.prog[11][2] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][2][0],P.prog[11][2][1],P.prog[11][2][2])).days > 5:
                            txt(P,"Hey there!","I'm here as a representative","of the Poke Ball factory!")
                            txt(P,"Go ahead and press this button","to win one of our Poke Ball","samples!")
                            ball_list = ['Poke','Great','Ultra','Premier','Fast','Level','Luxury','Friend','Timer','Quick','Net','Nest']
                            choose = random.randint(0,len(ball_list)-1)
                            txt(P,"And...you get a "+ball_list[choose]+" Ball!","Here you go!")
                            txt(P,"Thanks for coming by!")
                            add_item(P,ball_list[choose]+" Ball",1)
                            day = datetime.datetime.today().date()
                            P.prog[11][2] = [day.year,day.month,day.day]
                        else:
                            P.ams_npc4.write()
                    elif P.ams_npc5 and P.ams_npc5.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        if P.prog[11][4][0] == 15 and P.prog[11][4][1] == 5:
                            txt(P,'My collection is perfect!')
                        elif item_in_bag(P,"Tiny Mushroom") != 0 and P.prog[11][4][0] < 15:
                            new_txt(P)
                            write(P,"Oh! Is that a Tiny Mushroom?","Would you be kind enough to","let me have it?")
                            if choice(P):
                                txt(P,"Wow! Thank you so much!","It fits into my collection so","perfectly!")
                                add_item(P,'Tiny Mushroom',-1)
                                P.prog[11][4][0] += 1
                                if P.prog[11][4][0] % 3 == 0:
                                    aan = 'a '
                                    if P.prog[11][4][0] == 3:
                                        item = 'Rock Incense'
                                    elif P.prog[11][4][0] == 6:
                                        item = 'Rose Incense'
                                    elif P.prog[11][4][0] == 9:
                                        item = 'Sea Incense'
                                    elif P.prog[11][4][0] == 12:
                                        item = 'Smoke Incense'
                                    else:
                                        aan = 'an '
                                        item = 'Odd Incense'
                                    txt(P,"Here, I have this incense I","want to give you for helping", "me out!")
                                    txt(P,"You received "+aan+item+"!")
                                    add_item(P,item,1)
                            else:
                                txt(P,"Oh, I've never met another","avid mushroom collector like","myself!")
                                txt(P,"It pains me to let it go but","if you really need it you can","keep it.")
                        elif item_in_bag(P,"Big Mushroom") != 0 and P.prog[11][4][1] < 5:
                            new_txt(P)
                            write(P,"Oh! Is that a Big Mushroom?","Would you be kind enough to","let me have it?")
                            if choice(P):
                                txt(P,"Wow! Thank you so much!","It fits into my collection so","perfectly!")
                                add_item(P,'Big Mushroom',-1)
                                P.prog[11][4][1] += 1
                                if P.prog[11][4][1] == 1:
                                    item = 'Full Incense'
                                elif P.prog[11][4][1] == 2:
                                    item = 'Pure Incense'
                                elif P.prog[11][4][1] == 3:
                                    item = 'Lax Incense'
                                elif P.prog[11][4][1] == 4:
                                    item = 'Luck Incense'
                                else:
                                    item = 'Balm Mushroom'
                                txt(P,"Here, you can have this","incense. Thanks for the help!")
                                txt(P,"You received a "+item+"!")
                                add_item(P,item,1)
                            else:
                                txt(P,"Oh, I've never met another","avid mushroom collector like","myself!")
                                txt(P,"It pains me to let it go but","if you really need it you can","keep it.")
                        elif item_in_bag(P,"Tiny Mushroom") != 0 and P.prog[11][4][1] < 5:
                            txt(P,"I have enough Tiny Mushrooms","in my collection, but I could","use some more Big ones.")
                        elif item_in_bag(P,"Big Mushroom") != 0 and P.prog[11][4][0] < 15:
                            txt(P,"I have enough Big Mushrooms","in my collection, but I could","use some more Tiny ones.")
                        else:
                            P.ams_npc5.write()
                    elif P.ams_npc6 and P.ams_npc6.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        if P.prog[11][3] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][3][0],P.prog[11][3][1],P.prog[11][3][2])).days > 5:
                            txt(P,"Have some water! You don't","want to get dehydrated on a","nice day like this!")
                            txt(P,"You received a Fresh Water!")
                            add_item(P,"Fresh Water",1)
                            day = datetime.datetime.today().date()
                            P.prog[11][3] = [day.year,day.month,day.day]
                        else:
                            P.ams_npc6.write()
                    elif P.ams_npc7 and P.ams_npc7.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        if P.prog[11][5] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][5][0],P.prog[11][5][1],P.prog[11][5][2])).days > 5:
                            txt(P,"So you found the time to stop","by! Thanks again for helping","me out!")
                            txt(P,"I'll let you take one of my","signature Pinap Berries for","free!")
                            txt(P,"Here ya go!")
                            txt(P,"You received a Pinap Berry!")
                            txt(P,"Their super tasty, even your","Pokemon will love being fed","one!")
                            add_item(P,"Pinap Berry",1)
                            day = datetime.datetime.today().date()
                            P.prog[11][5] = [day.year,day.month,day.day]
                        else:
                            P.ams_npc7.write()
                    elif P.ams_npc8 and P.ams_npc8.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        if P.prog[11][6] == None or (datetime.datetime.today().date()-datetime.date(P.prog[11][6][0],P.prog[11][6][1],P.prog[11][6][2])).days > 5:
                            t = P.surface.copy()
                            txt(P,"Hello! I give great massages","that will make your Pokemon","more friendly!")
                            new_txt(P)
                            write(P,"Would any of your Pokemon be","interested in getting one of","my massages?")
                            if choice(P):
                                txt(P,"Alrighty! Who's the lucky","Pokemon?")
                                fade_out(P)
                                ans = trade_poke(P,None,True)
                                P.surface.blit(t,(0,0))
                                fade_in(P)
                                if ans != None:
                                    txt(P,"Okay! I'll give "+ans.name,"the best massage they've ever","gotten!")
                                    fade_out(P)
                                    P.surface.blit(t,(0,0))
                                    P.clock.tick(1)
                                    fade_in(P)
                                    txt(P,ans.name+" is feeling nice and","relaxed! Come back next week!")
                                    ans.gain_friend(75)
                                    day = datetime.datetime.today().date()
                                    P.prog[11][6] = [day.year,day.month,day.day]
                                else:
                                    txt(P,"Well come back if you","want a free massage!")
                            else:
                                txt(P,"Well come back if you","want a free massage!")
                        else:
                            P.ams_npc8.write()
                    elif P.ams_npc9 and P.ams_npc9.talk():
                        box = load("p/3_box.png")
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        mt = P.surface.copy()
                        new_txt(P)
                        write(P,"Hey there!","Take a look at what I found","this week!")
                        mart_t = P.surface.copy()
                        buy = P.font.render("Buy",True,(0,0,0))
                        sell = P.font.render("Sell",True,(0,0,0))
                        leave = P.font.render("Leave",True,(0,0,0))
                        endl = True
                        ay = 290
                        tim = 0
                        while endl:
                            P.surface.blit(mart_t,(0,0))
                            P.surface.blit(box,(550,280))
                            P.surface.blit(buy,(600,290))
                            P.surface.blit(sell,(600,340))
                            P.surface.blit(leave,(600,390))
                            P.surface.blit(P.arrow,(550,ay))
                            for event in map_keys():
                                if event.type == KEYDOWN:
                                    if event.key == pygame.key.key_code(P.controls[4]) and tim > 20:
                                        if ay == 290:
                                            P.prog[11][7][2] = poke_mart(P, mt, custom_shop = P.prog[11][7][1],stock = P.prog[11][7][2],diff_price = [0.5,'Water Gem','Ice Gem','Rock Gem'])
                                            new_txt(P)
                                            write(P,"Is there anything else you", "need?")
                                            mart_t = P.surface.copy()
                                        elif ay == 340:
                                            fade_out(P)
                                            mart_sell(P)
                                            P.surface.blit(mt,(0,0))
                                            fade_in(P)
                                            new_txt(P)
                                            write(P, "Is there anything else you", "need?")
                                            mart_t = P.surface.copy()
                                            ay = 290
                                        else:
                                            endl = False
                                    elif event.key == pygame.key.key_code(P.controls[5]) and tim > 20:
                                        endl = False
                                    elif event.key == pygame.key.key_code(P.controls[0]) and ay > 290:
                                        ay -= 50
                                    elif event.key == pygame.key.key_code(P.controls[1]) and ay < 440:
                                        ay += 50
                            tim += 1
                            P.clock.tick(P.ani_spd)
                            update_screen(P)
                        tim = 0
                        P.surface.blit(mt,(0,0))
                        txt(P,"See ya later!")
                    elif P.ams_npc10 and P.ams_npc10.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.font = pygame.font.SysFont("courier", 40, bold = False, italic = True)
                        P.ams_npc10.write()
                        P.font = pygame.font.SysFont("courier", 40, bold = True, italic = False)
                    elif P.ams_beauty.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_beauty.write()
                    elif P.ams_scientist.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_scientist.write()
                    elif P.ams_sci.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_sci.write()
                    elif P.ams_pre.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_pre.write()
                    elif P.ams_gentle.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_gentle.write()
                    elif P.ams_boi.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_boi.write()
                    elif P.ams_lass.talk():
                        am_square_b(P,wx,wy,listx,listy)
                        am_square_p(P,P.px,P.py,False)
                        am_square_f(P,P.px,P.py,listx,listy,tim)
                        P.ams_lass.write()
                    elif next_to(P,1800,750) or next_to(P,1750,750):
                        txt(P,"It's a giant statue of Latios.")
                    elif next_to(P,1150,750) or next_to(P,1200,750):
                        txt(P,"It's a giant statue of Latias.")
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P,saturday)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 325 or P.py == 275 or P.py == 225) and P.px == -2175 and face_r(P):
            P.px = -725
            P.py += 250
            P.move_out_dir = 'r'
            P.loc = "dock_1"
            end = False
        if (P.py == 325 or P.py == 275 or P.py == 225) and P.px == -25 and face_l(P):
            P.px -= 1150
            P.py += 1250
            P.move_out_dir = 'l'
            P.loc = "square_1"
            end = False
        #ocean
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
            if P.ams_fount == fount_1:
                P.ams_fount = fount_2
            elif P.ams_fount == fount_2:
                P.ams_fount = fount_1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if P.song == "music/am_festive.wav":
        fade = P.song
    fade_out(P,fade)

def dock_1_b(P,wx,wy,listx,listy):
    draw_waves(P, wx, wy)
    if P.prog[0] < 10:
        P.surface.blit(P.d1_boat, (P.px, P.py))
        P.surface.blit(P.d1_foam, (92 + P.px, 565 + P.py + abs(P.foam)))
    P.surface.blit(P.d1_dock, (P.px - 200, P.py - 200))
    P.surface.blit(P.d1_square, (P.px + 200, P.py - 1000))
    if P.py > 625:
        if P.px == -1675:
            P.surface.blit(P.d1_door,(P.px+2052,P.py-421))
        elif P.px == -1725:
            P.surface.blit(P.d1_door,(P.px+2098,P.py-421))
    draw_lamps(P,P.px,P.py,listx,listy,"b")
    if ((P.px <= -275 and P.py > -375) and (P.px <= -1125 and P.px >= -1225)):
        P.surface.blit(P.d1_rail2, (P.px + 1191, P.py + -175))
    if P.prog[3] >= 2 and P.prog[3] <= 4:
        P.surface.blit(P.d1_manaphy,(P.px+2560,P.py+520))

def dock_1_p(P,temppx,temppy,move):
    fisher = P.d1_fisher.y_dist()
    fisher2 = P.d1_fisher2.y_dist()
    lass = P.d1_lass.y_dist()
    todd = P.d1_todd.y_dist()
    ath = P.d1_ath.y_dist()
    if P.d1_latias:
        latias = P.d1_latias.y_dist()
        if latias > 0:
            P.d1_latias.move()
    if fisher > 0:
        P.d1_fisher.move()
    if fisher2 > 0:
        P.d1_fisher2.move()
    if lass > 0:
        P.d1_lass.move()
    if todd > 0:
        P.d1_todd.move()
    if ath > 0:
        P.d1_ath.move()
    #rect start
    r1 = (P.px,P.py+100,860,40)
    r100 = r1
    if P.prog[6][12] == 0:
        r100 = (P.px+400,P.py+150,50,40)
    r2 = (200+P.px,260+P.py,400,100)
    r3 = (P.px,450+P.py,400,50)
    r3p2 = (P.px+500,450+P.py,700,50)
    r4 = (200+P.px,200+P.py,450,30)
    r5 = (200+P.px,350+P.py,450,40)
    r6 = (P.px,P.py,50,600)
    r7 = r1
    if P.px >= -525:
        r7 = (850+P.px,75+P.py,51,40)
    r8 = r1
    if P.px <= -525:
        r8 = (939+P.px,425+P.py,51,30)
    r9 = r1
    if P.px <= -575:
        r9 = (950+P.px,400+P.py,50,50)
    r10 = (1000+P.px,350+P.py,100,50)
    r11 = (1100+P.px,300+P.py,50,50)
    r12 = (1150+P.px,250+P.py,50,50)
    r13 = (1150+P.px,150+P.py,50,40)
    r13p2 = (1200+P.px,200+P.py,50,50)
    r14 = (1050+P.px,100+P.py,100,40)
    r15 = (950+P.px,50+P.py,100,40)
    r16 = (P.px+500,500+P.py,50,50)
    r17 = (P.px+350,500+P.py,50,50)
    r18 = (P.px+100,P.py+550,300,40)
    if P.prog[0] >= 10:
        r18 = (P.px+100,P.py+550,600,40)
    r19 = (P.px+50,P.py+600,50,150)
    r20 = (P.px+500,P.py+550,800,40)
    r21 = (P.px+100,P.py+750,1400,50)
    r22 = (P.px+1250,P.py+300,50,290)
    r23 = (P.px+1300,P.py+250,200,40)
    r24 = r1
    r25 = r1
    if P.px >= -1075:
        r24 = (P.px+1500,P.py+300,50,140)
    else:
        r24 = (P.px+1450,P.py+300,50,90)
    if P.px >= -1075:
        r25 = (P.px+1500,P.py+600,50,150)
    elif P.px == -1125 and P.py == -275:
        r25 = (P.px+1450,P.py+550,50,150)
    else:
        r25 = (P.px+1450,P.py+600,50,150)
    b1 = r1
    if P.px == -1125 and P.py == -275:
        b1 = (P.px+1500,P.py+500,50,40)
    elif P.px == -1125 and P.py == -75:
        b1 = (P.px+1500,P.py+400,50,50)
    r26 = r1
    if P.px >= -1125 and P.py == -150:
        r26 = (1500+P.px,375+P.py,51,40)
    r27 = r1
    if P.px <= -1125 and P.px >= -1150 and P.py == -250:
        r27 = (1539+P.px,575+P.py,51,30)
    r28 = (P.px+1500,P.py+700,800,30)
    r29 = (P.px+1450,P.py-100,50,350)
    r30 = (P.px+2300,P.py-100,50,800)
    r31 = (P.px+1500,P.py+200,300,40)
    r32 = (P.px+2000,P.py+200,300,40)
    r33 = (P.px+1750,P.py-100,50,300)
    r34 = (P.px+2000,P.py-100,30,300)
    r35 = (P.px+1500,P.py-100,300,30)
    r36 = (P.px+2000,P.py-100,300,30)
    r37 = (P.px+2300,P.py-350,30,250)
    r38 = (P.px+1900,P.py-400,150,40)
    r382 = (P.px+1500,P.py-450,400,40)
    r383 = (P.px+1450,P.py-400,50,40)
    if P.px == -1725:
        r38 = (P.px+1900,P.py-400,200,40)
    r380 = (P.px+2150,P.py-400,150,40)
    if P.px == -1675:
        r380 = (P.px+2100,P.py-400,200,40)
    r381 = (P.px+2050,P.py-450,100,40)
    r39 = (P.px+1100,P.py-350,400,40)
    r40 = (P.px+1100,P.py-150,400,40)
    r41 = (P.px+1050,P.py-300,50,150)
    r42 = P.d1_fisher.get_rect()
    r43 = P.d1_lass.get_rect()
    r44 = P.d1_fisher2.get_rect()
    r45 = r1
    if P.d1_latias:
        r45 = P.d1_latias.get_rect()
    r46 = P.d1_todd.get_rect()
    r47 = P.d1_ath.get_rect()
    rects = [r383,r382,r100,r381,r380,r47,r46,r45,r44,r43,r42,r41,r40,r39,r37,r38,r35,r36,b1,r1,r2,r3,r3p2,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r13p2,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34]
    #rect_draw(P,rects)
    if P.prog[3] == 2:
        if P.py < -325:
            player_move(P,rects,manual_input = 'u')
        else:
            if P.px > -1875:
                player_move(P,rects,manual_input = 'r')
            else:
                P.prog[3] += 1
                P.d1_latias = npc.NPC(P,'Latias','Human',[2250,650],[['r',80],['ml',200]],["","",""])
    if move:
        if P.px >= -1110:
            player_move(P,rects,[Rect(900+P.px,100+P.py,50,350),Rect(P.px+1500,P.py+400,50,200)])
        else:
            player_move(P,rects,[Rect(900+P.px,100+P.py,50,350),Rect(P.px+1500,P.py+400,50,190)])
    else:
        blit_player(P)
    if P.d1_latias:
        if latias <= 0:
            P.d1_latias.move(temppx,temppy)
    if fisher <= 0:
        P.d1_fisher.move(temppx,temppy)
    if fisher2 <= 0:
        P.d1_fisher2.move(temppx,temppy)
    if lass <= 0:
        P.d1_lass.move(temppx,temppy)
    if todd <= 0:
        P.d1_todd.move(temppx,temppy)
    if ath <= 0:
        P.d1_ath.move(temppx,temppy)

def dock_1_f(P,temppx,temppy,listx,listy,tim):
    P.surface.blit(P.d1_bridge, (temppx + 1100, temppy - 350))
    P.surface.blit(P.d1_roof, (temppx + 1497, temppy - 159))
    P.surface.blit(P.d1_roof, (temppx + 1997, temppy - 159))
    if not ((temppy <= -275 and temppy > -375) and (temppx <= -1125 and temppx >= -1225)):
        P.surface.blit(P.d1_corner, (temppx + 1500, temppy + 550))
        P.surface.blit(P.d1_rail2, (temppx + 1191, temppy + -175))
    if P.prog[0] < 10:
        P.surface.blit(P.d1_rail, (17 + temppx, 225 + temppy))
        P.surface.blit(P.d1_wall, (198 + temppx, 116 + temppy))
    P.surface.blit(P.d1_dfoam, (103 + temppx, 779 + temppy + abs(P.foam)))
    P.surface.blit(P.d1_sfoam,(1140+temppx,-70+temppy + abs(P.foam)))
    draw_lamps(P,temppx,temppy,listx,listy)
    show_location(P, P.loc_txt, tim)

def dock_1(P) -> None:
    if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
        song = "music/am_night.wav"
    else:
        song = "music/am_day.wav"
    if P.song != song:
        P.song = song
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    fade = None
    P.d1_boat = load("p/am/boat_2.png")
    P.d1_rail = load("p/am/railing_open.png")
    P.d1_wall = load("p/am/boat_wall.png")
    P.d1_foam = load("p/am/boat_foam.png")
    P.d1_dock = load("p/am/dock_1_1.png")
    P.d1_dfoam = load("p/am/dock_foam.png")
    P.d1_sfoam = load("p/am/square_foam_1.png")
    if P.prog[0] >= 10:
        P.d1_dock = load("p/am/dock_1_2.png")
    P.d1_square = load("p/am/square_1.png")
    P.d1_corner = load("p/am/dock_1_wall.png")
    P.d1_roof = load("p/am/building_1_roof.png")
    P.d1_rail2 = load("p/am/square_fence_1.png")
    P.d1_bridge = load("p/am/bridge_r.png")
    manaphy1 = pygame.transform.scale(load("p/spr/Manaphy_sleep1.png"),(60,40))
    manaphy2 = pygame.transform.scale(load("p/spr/Manaphy_sleep2.png"),(60,40))
    P.d1_manaphy = manaphy1
    set_location(P)
    wx = 0
    wy = 0
    move = True
    listx = [1492,1492,2288,2288,1992,1891,1788,1492,1492,2288,1891]
    listy = [550,100,550,100,100,550,100,-500,-300,-500,-500]
    P.d1_fisher = npc.NPC(P,'Fisherman','Fisherman',[1350,300],[['u',20]],["One of these days I'm gonna","fish up a Pokemon.", "","Then I'll stop a random","passerby and say \"Hey! Let's","battle!\"","One of these days...","",""])
    P.d1_fisher2 = npc.NPC(P,'Fisherman','Fishyman',[100,650],[['l',20]],["Hey! Let's have a Pokemon","battle!", "","Just kidding, you don't look","that strong. Come back once","you've toughened up a bit."])
    P.d1_lass = npc.NPC(P,'Lass','Lass',[1800,400],[['mr',40],['r',100],['ml',40],['l',100],['md',20],['d',50],['mu',20],['u',50]],["","",""])
    P.d1_todd = npc.NPC(P,'Preschoolerb','Todd',[2050,-300],[['l',40],['md',20],['d',40],['mr',20],['r',40],['mu',20],['u',40],['ml',20]],["I'm gonna get my own Pokemon,","and I'll just train it until", "it can sweep the gym leader!","Why does everyone say it's so","hard to be a trainer? I'll","show them how easy it is!"])
    P.d1_ath = npc.NPC(P,'Triathelete','Toby',[1500,-350],[['mr',150],['md',40],['ml',150],['mu',40]],["I'm practicing for the big","race coming up! The Pokemon", "are the ones actually racing,","but I like to think that the","faster I can run, the faster","my Pokemon can swim!"],spd=1)
    if P.prog[3] == 0:
        P.d1_latias = npc.NPC(P,'Latias','Human',[2050,650],[['d',20]],["*blink* *blink*","","","*stare*",".....................","",])
    else:
        P.d1_latias = None
    dock_1_b(P,wx,wy,listx,listy)
    dock_1_p(P,P.px,P.py,False)
    tim = 0
    dock_1_f(P,P.px,P.py,listx,listy,tim)
    fade_in(P)
    end = True
    m = 0
    while end:
        #print(P.px,P.py)
        if ((get_time() > 19 or get_time() < 6) and P.lighting == 'Dynamic') or P.lighting == 'Night':
            song = "music/am_night.wav"
        else:
            song = "music/am_day.wav"
        if P.song != song:
            P.song = song
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
        if P.prog[3] == 1 and P.d1_latias.x == 2250:
            P.prog[3] += 1
            P.d1_latias = npc.NPC(P,'Latias','Human',[2250,650],[['r',20]],["","",""])
        if P.prog[3] == 3 and P.d1_latias.x == 1800:
            move = True
            P.d1_latias = None
            P.prog[3] += 1
        if P.prog[3] == 4 and P.px == -1725:
            P.prog[3] += 1
        dock_1_b(P,wx,wy,listx,listy)
        #rects start
        #rects end
        temppx = P.px
        temppy = P.py
        dock_1_p(P,temppx,temppy,move)
        dock_1_f(P,temppx,temppy,listx,listy,tim)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.py == 625 and (P.px == -1325 or P.px == -1275) and face_u(P):
                        new_txt(P)
                        write(P,"It\'s locked.")
                        cont(P)
                    elif next_to(P,400,150) and P.prog[6][12] == 0:
                        txt(P,P.save_data.name + " found a Pearl!")
                        txt(P,P.save_data.name + " put the Pearl","in the Items pocket.")
                        add_item(P,"Pearl",1)
                        P.prog[6][12] = 1
                    elif P.d1_fisher.talk():
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        P.d1_fisher.write()
                    elif P.d1_lass.talk():
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        txt(P,"I read somewhere that you can","register up to four key items.")
                        txt(P,"Then if you press ["+P.controls[7]+"],","you can use those items really","quickly!")
                    elif P.d1_fisher2.talk():
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        P.d1_fisher2.write()
                    elif P.d1_ath.talk():
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        P.d1_ath.write()
                    elif P.d1_todd.talk():
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        P.d1_todd.write()
                    elif P.d1_latias and P.d1_latias.talk():
                        move = False
                        dock_1_b(P,wx,wy,listx,listy)
                        dock_1_p(P,P.px,P.py,False)
                        dock_1_f(P,P.px,P.py,listx,listy,tim)
                        P.d1_latias.write()
                        if face_l(P):
                            P.d1_latias = npc.NPC(P,'Latias','Human',[2050,650],[['mu',20],['mr',40],['md',20],['mr',60],['r',20]],["", "",""])
                        else:
                            P.d1_latias = npc.NPC(P,'Latias','Human',[2050,650],[['mr',80],['r',20]],["", "",""])
                        P.prog[3] += 1
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.px == -1675 or P.px == -1725) and P.py == 675 and face_u(P):
            P.px += 1800
            P.py = -125
            P.loc = "house_21_1"
            end = False
        if (P.py == 25 or P.py == -25) and P.px == -225 and face_l(P):
            P.px = -375
            P.py -= 100
            fade = P.song
            P.loc = "cruise_1"
            end = False
        if (P.py == 475 or P.py == 525 or P.py == 575) and P.px == -725 and face_l(P):
            P.px = -2175
            P.py -= 250
            P.move_out_dir = 'l'
            if datetime.datetime.today().weekday() in [5,6] and (get_time() >= 6 and get_time() <= 19):
                fade = P.song
            P.loc = "am_square"
            end = False
        #ocean
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        if tim%30 == 0:
            if P.prog[3] >= 2 and P.prog[3] <= 4:
                if P.d1_manaphy == manaphy1:
                    P.d1_manaphy = manaphy2
                else:
                    P.d1_manaphy = manaphy1
        tim += 1
        tick_buffer(P)
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P,fade)

def cruise_2_b(P,wx,wy):
    draw_waves(P, wx, wy)
    P.surface.blit(P.c2_boat, (P.px, P.py))

def cruise_2_p(P,temppx,temppy,move):
    if P.c2_prof:
        prof = P.c2_prof.y_dist()
        if prof > 0:
            P.c2_prof.move()
    r1 = (P.px,P.py+100,860,40)
    r17 = r1
    if P.prog[6][12] == 0:
        r17 = (P.px+400,P.py+150,50,40)
    r2 = (200+P.px,260+P.py,400,100)
    r3 = (P.px,450+P.py,1200,150)
    r4 = (200+P.px,200+P.py,450,30)
    r5 = (200+P.px,350+P.py,450,40)
    r6 = (P.px,P.py,50,600)
    r7 = r6
    if P.px >= -525:
        r7 = (850+P.px,75+P.py,51,40)
    r8 = r7
    if P.px <= -525:
        r8 = (939+P.px,425+P.py,51,30)
    r9 = r8
    if P.px <= -575:
        r9 = (950+P.px,400+P.py,50,50)
    r10 = (1000+P.px,350+P.py,100,50)
    r11 = (1100+P.px,300+P.py,50,50)
    r12 = (1150+P.px,250+P.py,50,50)
    r13 = (1150+P.px,150+P.py,50,40)
    r13p2 = (1200+P.px,200+P.py,50,50)
    r14 = (1050+P.px,100+P.py,100,40)
    r15 = (950+P.px,50+P.py,100,40)
    r16 = r1
    if P.c2_prof:
        r16 = P.c2_prof.get_rect()
    rects = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r13p2,r14,r15,r16,r17]
    #rect_draw(P,rects)
    if move:
        player_move(P,rects,[Rect(900+P.px,100+P.py,50,350)])
    else:
        blit_player(P)
    if P.c2_prof:
        if prof <= 0:
            P.c2_prof.move(temppx,temppy)

def cruise_2_f(P,temppx,temppy):
    P.surface.blit(P.c2_rail,(17+temppx,225+temppy))
    P.surface.blit(P.c2_wall,(198+temppx,116+temppy))
    P.surface.blit(P.c2_foam,(92+temppx,565+temppy+abs(P.foam)))
    set_sky(P)

def cruise_2(P) -> None:
    if P.song != "music/cruise.wav":
        P.song = "music/cruise.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    P.c2_boat = load("p/am/boat_2.png")
    P.c2_foam = load("p/am/boat_foam.png")
    P.c2_rail = load("p/am/railing.png")
    P.c2_wall = load("p/am/boat_wall.png")
    if P.prog[0] == 0:
        P.c2_prof = npc.NPC(P,'Professor','Burnet',[800,250],[['r',100]],["Hi "+P.save_data.name+",", "We'll arrive shortly.","","Let's go inside. I want to", "show you something.",""])
    else:
        P.c2_prof = None
    wx = 0
    wy = 0
    move = True
    cruise_2_b(P,wx,wy)
    cruise_2_p(P,P.px,P.py,False)
    cruise_2_f(P,P.px,P.py)
    fade_in(P)
    end = True
    m = 0
    tim = 0
    while end:
        #print(P.px,P.py)
        if P.prog[0] == 1 and P.c2_prof.x == 600:
            P.prog[0] = 5
            move = True
            P.c2_prof = None
        cruise_2_b(P,wx,wy)
        temppx = P.px
        temppy = P.py
        cruise_2_p(P,temppx,temppy,move)
        cruise_2_f(P,temppx,temppy)
        #rect_draw(P,rects)
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif (event.key == pygame.key.key_code(P.controls[4]) or P.buffer_talk) and move:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        P.buffer_talk = 10
                    temp_buff = P.buffer_talk
                    P.buffer_talk = None
                    if P.c2_prof and P.c2_prof.talk():
                        move = False
                        cruise_2_b(P,wx,wy)
                        cruise_2_p(P,P.px,P.py,False)
                        cruise_2_f(P,P.px,P.py)
                        P.c2_prof.write()
                        P.prog[0] += 1
                        if face_r(P):
                            P.c2_prof  = npc.NPC(P,'Professor','Burnet',[800,250],[['md',20],['ml',160]],["","",""])
                        else:
                            P.c2_prof  = npc.NPC(P,'Professor','Burnet',[800,250],[['ml',40]],["","",""])
                    elif next_to(P,400,150) and P.prog[6][12] == 0:
                        txt(P,P.save_data.name + " found a Pearl!")
                        txt(P,P.save_data.name + " put the Pearl","in the Items pocket.")
                        add_item(P,"Pearl",1)
                        P.prog[6][12] = 1
                    else:
                        P.buffer_talk = temp_buff
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        if (P.py == 25 or P.py == -25) and P.px == -225 and face_l(P):
            P.px = -375
            P.py -= 100
            P.loc = "cruise_1"
            end = False
        if wx == 400:
            wx = 0
        if wy == 400:
            wy = 0
        if tim%2 == 0:
            wx += 1
        if tim%5 == 0:
            wy += 1
        if P.ocean == 15:
            P.ocean = -15
        if tim%5 == 0:
            P.ocean += 1
        if tim%10 == 0:
            P.foam += 1
            if P.foam == 5:
                P.foam = -5
        tim += 1
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def cruise_1_b(P):
    P.surface.fill((0, 0, 0), Rect(0, 0, 800, 600))
    P.surface.blit(P.c1_back, (P.px, P.py+50))
    if P.prog[0] >= 5:
        P.surface.blit(P.c1_mat, (P.px, 350 + P.py))
        if in_party(P, 'Bounsweet') == False:
            P.surface.blit(P.item_out, (P.px, 350 + P.py))
        if in_party(P, 'Poliwag') == False:
            P.surface.blit(P.item_out, (P.px, 400 + P.py))
        if in_party(P, 'Fletchling') == False:
            P.surface.blit(P.item_out, (P.px, 450 + P.py))

def cruise_1_p(P,temppx,temppy,move):
    if P.c1_prof:
        prof = P.c1_prof.y_dist()
        if prof > 0:
            P.c1_prof.move()
    r1 = (P.px, P.py, 800, 190)
    r2 = (P.px - 50, P.py - 50, 50, 700)
    r3 = (P.px, P.py + 600, 800, 50)
    r4 = (P.px + 800, P.py, 50, 600)
    r5 = r1
    if P.c1_prof:
        r5 = (P.px, P.py+300, 50, 190)
    rects = [r1,r2,r3,r4,r5]
    player_move(P, rects)
    if P.c1_prof:
        if prof <= 0:
            P.c1_prof.move(temppx,temppy)

def cruise_1(P) -> None:
    if P.song != "music/cruise.wav":
        P.song = "music/cruise.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol)
        pygame.mixer.music.play(-1)
    fade = None
    P.habitat = 'indoor'
    P.c1_mat = load("p/am/starter_mat.png")
    c1 = load("p/am/cruise_1_1.png")
    c2 = load("p/am/cruise_1_2.png")
    c3 = load("p/am/cruise_1_3.png")
    c4 = load("p/am/cruise_1_4.png")
    c5 = load("p/am/cruise_1_5.png")
    c6 = load("p/am/cruise_1_6.png")
    Bounsweet_start = load("p/am/bounsweet_start.png")
    litwick_start = load("p/am/litwick_start.png")
    Poliwag_start = load("p/am/poliwag_start.png")
    Fletchling_start = load("p/am/fletchling_start.png")
    if P.prog[0] == 5:
        P.c1_prof  = npc.NPC(P,'Professor','Burnet',[0,300],[['r',20]],["I have three Pokemon here for", "you to choose as a starter. Go", "ahead and pick one."])
    elif P.prog[0] == 6:
        P.c1_prof = npc.NPC(P,'Professor','Burnet',[0,300],[['r',20]],["Go on, pick one.", "", ""])
    elif P.prog[0] >= 7:
        P.c1_prof = npc.NPC(P,'Professor','Burnet',[0,300],[['r',20]],["Go on, explore.", "", ""])
    else:
        P.c1_prof = None
    if in_party(P,'Litwick'):
        P.c1_back = c5
    else:
        P.c1_back = c1
    cruise_1_b(P)
    cruise_1_p(P,P.px,P.py,False)
    fade_in(P)
    move = True
    end = True
    a = 0
    m = 0
    l = 0
    tim = 0
    while end:
        #boundaries
        cruise_1_b(P)
        temppx = P.px
        temppy = P.py
        cruise_1_p(P,temppx,temppy,move)
        for event in map_keys():
            if event.type == KEYDOWN and  tim > 20:
                if event.key == pygame.key.key_code(P.controls[6]) and move:
                    m = 1
                elif event.key == pygame.key.key_code(P.controls[7]) and move:
                    P.register_click = 1
                elif event.key == pygame.key.key_code(P.controls[4]):
                    if ((P.px == -275 or P.px == 25 or P.px == 325) and P.py == 75) and face_u(P):
                        if P.prog[0] == 6 and P.px == 25:
                            if l == 0:
                                txt(P,"It's just a candle?")
                                l = 1
                            elif l == 1:
                                txt(P,"............")
                                l = 2
                            elif l == 2:
                                txt(P,"............")
                                P.c1_back = c3
                                l = 3
                            elif l == 3:
                                new_txt(P)
                                P.font = pygame.font.SysFont("courier", 40, bold = False, italic = True)
                                write(P,"............","............","LITWICK!!!!!")
                                P.font = pygame.font.SysFont("courier", 40, bold = True, italic = False)
                                cont(P)
                                txt(P,"Wow, that Litwick must have", "escaped my lab and snuck ","aboard.")
                                new_txt(P)
                                P.surface.blit(litwick_start,(250,100))
                                write(P,"I have an idea.","How about you take Litwick as","your partner?")
                                if choice(P,550,600):
                                    P.prog[0] = 7
                                    P.save_data.starter = 'Litwick'
                                    P.party.append(poke.Poke("Litwick",[5,random.randint(0,1),20,"Ember",25,"Astonish",15,"Minimize",10,"Smog",20,None,None,0,"Poke Ball",0,'Flame Body',True]))
                                    P.save_data.pokedex['Litwick'] = [1,[]]
                                    P.c1_back = c5
                                else:
                                    pass
                                l = 4
                            elif l == 4:
                                new_txt(P)
                                P.surface.blit(litwick_start,(250,100))
                                write(P,"Litwick:", "The Candle Pokemon.")
                                cont(P)
                                new_txt(P)
                                write(P,"Do you want Litwick?")
                                if choice(P,550,600):
                                    P.prog[0] = 7
                                    P.save_data.starter = 'Litwick'
                                    P.party.append(poke.Poke("Litwick",[5,random.randint(0,1),20,"Ember",25,"Astonish",15,"Minimize",10,"Smog",20,None,None,0,"Poke Ball",0,'Flame Body',True]))
                                    P.save_data.pokedex['Litwick'] = [1,[]]
                                    P.c1_back = c5
                                else:
                                    pass
                        elif (in_party(P,'Litwick')) and P.px == 25:
                            txt(P,"It's an empty lamp.")
                        else:
                            txt(P,"It's just a candle.")
                    if (P.prog[0] > 4) and ((P.px == 325 and (P.py == -75 or P.py == -125 or P.py == -175)) and face_l(P)) or (P.px == 375 and P.py == -225 and face_u(P)):
                        if P.prog[0] == 5 or P.prog[0] >= 7:
                            if P.py == -75 and (in_party(P,'Bounsweet')):
                                pass
                            elif P.py == -125 and (in_party(P,'Poliwag')):
                                pass
                            elif P.py == -175 and (in_party(P,'Fletchling')):
                                pass
                            else:
                                new_txt(P)
                                write(P,"It's a Pokeball.")
                                cont(P)
                        if P.prog[0] == 6:
                            if P.py == -75:
                                new_txt(P)
                                P.surface.blit(Bounsweet_start,(250,100))
                                write(P,"Bounsweet:", "The Fruit Pokemon.")
                                cont(P)
                                new_txt(P)
                                write(P,"Do you want Bounsweet?")
                                if choice(P,550,600):
                                    P.prog[0] = 7
                                    P.save_data.starter = 'Bounsweet'
                                    P.party.append(poke.Poke("Bounsweet",[5,1,334,"Splash",-1,"Pound",-1,'Play Nice',-1,None,None,None,None,0,"Poke Ball",0,'Leaf Guard',True]))
                                    P.save_data.pokedex['Bounsweet'] = [1,[]]
                                else:
                                    pass
                            if P.py == -125:
                                new_txt(P)
                                P.surface.blit(Poliwag_start,(250,100))
                                write(P,"Poliwag:", "The Tadpole Pokemon.")
                                cont(P)
                                new_txt(P)
                                write(P,"Do you want Poliwag?")
                                if choice(P,550,600):
                                    P.prog[0] = 7
                                    P.save_data.starter = 'Poliwag'
                                    P.party.append(poke.Poke("Poliwag",[5,random.randint(0,1),334,"Water Sport",-1,"Bubble",-1,None,None,None,None,None,None,0,"Poke Ball",0,'Water Absorb',True]))
                                    P.save_data.pokedex['Poliwag'] = [1,[]]
                                else:
                                    pass
                            if P.py == -175 or face_u(P):
                                new_txt(P)
                                P.surface.blit(Fletchling_start,(250,100))
                                write(P,"Fletchling:", "The Tiny Robin Pokemon.")
                                cont(P)
                                new_txt(P)
                                write(P,"Do you want Fletchling?")
                                if choice(P,550,600):
                                    P.prog[0] = 7
                                    P.save_data.starter = 'Fletchling'
                                    P.party.append(poke.Poke("Fletchling",[5,random.randint(0,1),334,"Tackle",-1,"Growl",-1,None,None,None,None,None,None,0,"Poke Ball",0,'Big Pecks',True]))
                                    P.save_data.pokedex['Fletchling'] = [1,[]]
                                else:
                                    pass
                    if P.c1_prof and P.c1_prof.talk():
                        cruise_1_b(P)
                        cruise_1_p(P,P.px,P.py,False)
                        if P.prog[0] == 7:
                            te = P.surface.copy()
                            txt(P,"Good Choice!","How about let's test it out in","a Pokemon battle?")
                            play_music(P,"music/trainer_battle.wav",0)
                            #battle(P,["Professor Burnet",poke.Poke('Cottonee',[1,0,334,"Growl",10,None,None,None,None,None,None,None,None,0,"Fast Ball",0,'Prankster']),poke.Poke('Togedemaru',[10,0,30,"Explosion",35,None,None,None,None,None,None,None,None,0,"Poke Ball",0,'Iron Barbs'])])
                            battle(P,["Professor Burnet",poke.Poke('Munchlax',[3,1,334,"Tackle",35,"Odor Sleuth",30,None,None,None,None,None,None,0,"Poke Ball",0,'Thick Fat'])],no_pc = True)
                            play_music(P,"music/cruise.wav")
                            P.surface.blit(te,(0,0))
                            fade_in(P)
                            new_txt(P)
                            if P.party[0].ch == 0:
                                write(P,'That was a good try. You\'ll','have many opportunities to', 'improve on your journey!')
                            else:
                                write(P,'That was quite impressive.','I\'m sure you\'ll make a great','Pokemon trainer one day.')
                            cont(P)
                            t = P.surface.copy()
                            txt(P,'Let me heal your Pokemon for', 'you.')
                            fade_out(P)
                            P.clock.tick(1)
                            P.surface.blit(te,(0,0))
                            fade_in(P)
                            heal_party(P)
                            txt(P,"Here, take this map. It will","be useful for keeping track of","your location.")
                            txt(P,"Open the menu by pressing","["+P.controls[6]+"] to use it from","your bag.")
                            txt(P,'Looks like we\'ve arrived.','Go ahead and take a look', 'outside while I clean up here.')
                            add_item(P,"Map",1)
                            txt(P,"If you're lucky, you might", "even catch the weekly festival","in Alto Mare Square.")
                            P.prog[0] = 9
                            P.c1_prof = P.c1_prof = npc.NPC(P,'Professor','Burnet',[0,300],[['r',20]],["Go on, explore.", "", ""])
                        else:
                            P.c1_prof.write()
                            if P.prog[0] == 5:
                                P.prog[0] += 1
                                P.c1_prof = P.c1_prof = npc.NPC(P,'Professor','Burnet',[0,300],[['r',20]],["Go on, pick one.", "", ""])
        keys = pygame.key.get_pressed()
        if (P.py == -75 or P.py == -125) and P.px == -375 and keys[pygame.key.key_code(P.controls[3])] and P.p == P.r1:
            P.px = -225
            P.py += 100
            P.loc = "cruise_2"
            if P.prog[0] > 8:
                fade = P.song
                P.loc = "dock_1"
            end = False
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and m == 1:
            menu(P)
            m = 0
        if P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0 and P.register_click == 1:
            register(P)
            P.register_click = -10
        a += 1
        tim += 1
        if a == 7:
            if P.c1_back == c1:
                P.c1_back = c2
            elif P.c1_back == c2:
                P.c1_back = c1
            elif P.c1_back == c3:
                P.c1_back = c4
            elif P.c1_back == c4:
                P.c1_back = c3
            elif P.c1_back == c5:
                P.c1_back = c6
            else:
                P.c1_back = c5
            a = 0
        update_screen(P)
        P.clock.tick(P.ani_spd)
    P.move_out_dir = 'r'
    fade_out(P,fade)