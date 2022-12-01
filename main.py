import curses
import time
import pygame


def menu(stdscr):
    menu = ['Play', 'Exit']
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    current_row = 1
    stdscr.nodelay(1)
    while 1:
        key = stdscr.getch()

        if (current_row == 1):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(1, 1, "Play")
            stdscr.attroff(curses.color_pair(1))
            stdscr.addstr(2, 1, "exit")
        if (current_row == 2):
            stdscr.addstr(1, 1, "Play")
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(2, 1, "exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if(current_row==1):
                break

            if(current_row==2):
                return False


def main(arg):
    jeu=True
    if(menu(arg)==False):
        jeu=False

    arg.clear(

    )
    clock = pygame.time.Clock()

    curses.curs_set(0)
    arg.nodelay(1)
    arg.timeout(10)
    temps=time.time()

    pos_j1=10
    statut_j1="rest"
    pos_j2=35
    statut_j2="rest"
    pos_bloc=23
    largeur, longueur = arg.getmaxyx()
    score_j1 = 0
    score_j2 = 0
    fps=40
    mouvment_speed=20
    while(jeu):
        for i in range(3,longueur-3):
            arg.addstr(8,i,"#")
        arg.refresh()






        arg.addstr(2,5,"score player1:"+str(score_j1))
        arg.addstr(2,30,"score player2:"+str(score_j2))


        arg.refresh()
        clock.tick(1000000)
        key = arg.getch()
 # créer le blocs

        arg.addstr(7,pos_bloc,"x")
 # créer le premiers joueur

        statut_j1="rest"
        arg.addstr(4,pos_j1,"0")
        arg.addstr(5,pos_j1,"|")
        arg.addstr(5,pos_j1+1,"_")
        arg.addstr(5,pos_j1+2,"/")
        arg.addstr(6,pos_j1,"|")
        arg.addstr(7,pos_j1,"|")
        arg.addstr(7,pos_j1-1,"/")

        if(key==ord('d') and pos_j1 != pos_bloc-1) :
            pos_j1+=1
            arg.clear()
            arg.refresh()
        if(key==ord('q') and pos_j1>4 and pos_j1 != pos_bloc+2) :
            pos_j1 -= 1
            arg.clear()
            arg.refresh()

    # le joueur 1 attacks

        if(key==ord('z')):
            statut_j1="attack"
            arg.addstr(4,pos_j1,"0")
            arg.addstr(5,pos_j1,"|")
            arg.addstr(5,pos_j1+1,"_")
            arg.addstr(5,pos_j1+2,"_")
            arg.addstr(6,pos_j1,"|")
            arg.addstr(7,pos_j1,"|")
            arg.addstr(7,pos_j1-1,"/")
            arg.refresh()
            time.sleep(0.5)

    # le joueur 1 blocs

        if (key == ord('s')):
            statut_j1 = "block"
            arg.addstr(4, pos_j1, "0")
            arg.addstr(5, pos_j1, "|")
            arg.addstr(5, pos_j1 + 1, "_")
            arg.addstr(5, pos_j1 + 2, "|")
            arg.addstr(6, pos_j1, "|")
            arg.addstr(7, pos_j1, "|")
            arg.addstr(7, pos_j1 - 1, "/")
            arg.refresh()
            time.sleep(0.5)

     # le joueur 1 saute a gauche

        if (key == ord('a') and pos_j1>4):
            arg.addstr(4, pos_j1, " ")
            arg.addstr(5, pos_j1, " ")
            arg.addstr(5, pos_j1 + 1, " ")
            arg.addstr(5, pos_j1 + 2, " ")
            arg.addstr(6, pos_j1, " ")
            arg.addstr(7, pos_j1, " ")
            arg.addstr(7, pos_j1 - 1, " ")

            arg.addstr(4-1, pos_j1, "0")
            arg.addstr(5-1, pos_j1, "|")
            arg.addstr(5-1, pos_j1 + 1, "_")
            arg.addstr(5-1, pos_j1 + 2, "|")
            arg.addstr(6-1, pos_j1, "|")
            arg.addstr(7-1, pos_j1, "|")
            arg.addstr(7-1, pos_j1 - 1, "/")
            arg.refresh()
            time.sleep(0.2)


            arg.addstr(4-1, pos_j1, " ")
            arg.addstr(5-1, pos_j1, " ")
            arg.addstr(5-1, pos_j1 + 1, " ")
            arg.addstr(5-1, pos_j1 + 2, " ")
            arg.addstr(6-1, pos_j1, " ")
            arg.addstr(7-1, pos_j1, " ")
            arg.addstr(7-1, pos_j1 - 1, " ")

            pos_j1-=3

            arg.addstr(4-1, pos_j1, "0")
            arg.addstr(5-1, pos_j1, "|")
            arg.addstr(5-1, pos_j1 + 1, "_")
            arg.addstr(5-1, pos_j1 + 2, "|")
            arg.addstr(6-1, pos_j1, "|")
            arg.addstr(7-1, pos_j1, "|")
            arg.addstr(7-1, pos_j1 - 1, "/")
            arg.refresh()
            time.sleep(0.2)
            arg.addstr(4-1, pos_j1, " ")
            arg.addstr(5-1, pos_j1, " ")
            arg.addstr(5-1, pos_j1 + 1, " ")
            arg.addstr(5-1, pos_j1 + 2, " ")
            arg.addstr(6-1, pos_j1, " ")
            arg.addstr(7-1, pos_j1, " ")
            arg.addstr(7-1, pos_j1 - 1, " ")

    # le joueur 1 saute a droite :

        if (key == ord('e')):
            arg.addstr(4, pos_j1, " ")
            arg.addstr(5, pos_j1, " ")
            arg.addstr(5, pos_j1 + 1, " ")
            arg.addstr(5, pos_j1 + 2, " ")
            arg.addstr(6, pos_j1, " ")
            arg.addstr(7, pos_j1, " ")
            arg.addstr(7, pos_j1 - 1, " ")

            arg.addstr(4 - 1, pos_j1, "0")
            arg.addstr(5 - 1, pos_j1, "|")
            arg.addstr(5 - 1, pos_j1 + 1, "_")
            arg.addstr(5 - 1, pos_j1 + 2, "|")
            arg.addstr(6 - 1, pos_j1, "|")
            arg.addstr(7 - 1, pos_j1, "|")
            arg.addstr(7 - 1, pos_j1 - 1, "/")
            arg.refresh()
            time.sleep(0.2)

            arg.addstr(4 - 1, pos_j1, " ")
            arg.addstr(5 - 1, pos_j1, " ")
            arg.addstr(5 - 1, pos_j1 + 1, " ")
            arg.addstr(5 - 1, pos_j1 + 2, " ")
            arg.addstr(6 - 1, pos_j1, " ")
            arg.addstr(7 - 1, pos_j1, " ")
            arg.addstr(7 - 1, pos_j1 - 1, " ")

            pos_j1 += 3

            arg.addstr(4 - 1, pos_j1, "0")
            arg.addstr(5 - 1, pos_j1, "|")
            arg.addstr(5 - 1, pos_j1 + 1, "_")
            arg.addstr(5 - 1, pos_j1 + 2, "|")
            arg.addstr(6 - 1, pos_j1, "|")
            arg.addstr(7 - 1, pos_j1, "|")
            arg.addstr(7 - 1, pos_j1 - 1, "/")
            arg.refresh()
            time.sleep(0.2)
            arg.addstr(4 - 1, pos_j1, " ")
            arg.addstr(5 - 1, pos_j1, " ")
            arg.addstr(5 - 1, pos_j1 + 1, " ")
            arg.addstr(5 - 1, pos_j1 + 2, " ")
            arg.addstr(6 - 1, pos_j1, " ")
            arg.addstr(7 - 1, pos_j1, " ")
            arg.addstr(7 - 1, pos_j1 - 1, " ")



# créer le deuxieme joueur

        statut_j2 = "rest"
        arg.addstr(4, pos_j2, "0")
        arg.addstr(5, pos_j2, "|")
        arg.addstr(5, pos_j2-1, "_")
        arg.addstr(5, pos_j2-2, "\\")
        arg.addstr(6, pos_j2, "|")
        arg.addstr(7, pos_j2, "|")
        arg.addstr(7, pos_j2+1, "\\")
        if (key == curses.KEY_RIGHT and pos_j2 != pos_bloc-1):
            pos_j2 += 1
            arg.clear()
            arg.refresh()
        if (key == (curses.KEY_LEFT) and pos_j2 > 4 and pos_j2 != pos_bloc+1):
            pos_j2 -= 1
            arg.clear()
            arg.refresh()



    # le joueur 2 attack

        if (key == ord('o')):
            statut_j2 = "attack"
            arg.addstr(4, pos_j2, "O")
            arg.addstr(5, pos_j2, "|")
            arg.addstr(5, pos_j2 - 1, "_")
            arg.addstr(5, pos_j2 - 2, "_")
            arg.addstr(6, pos_j2, "|")
            arg.addstr(7, pos_j2, "|")
            arg.addstr(7, pos_j2 - 1, "")
            arg.refresh()
            time.sleep(0.5)





    # le joueur 2 blocs

        if (key == curses.KEY_DOWN):
            statut_j2 = "block"
            arg.addstr(4, pos_j2, "0")
            arg.addstr(5, pos_j2, "|")
            arg.addstr(5, pos_j2 - 1, "_")
            arg.addstr(5, pos_j2 - 2, "|")
            arg.addstr(6, pos_j2, "|")
            arg.addstr(7, pos_j2, "|")
            arg.addstr(7, pos_j2 - 1, "")
            arg.refresh()
            time.sleep(0.5)

    # le joueur 2 saute a gauche

        if (key == curses.KEY_UP):
            arg.addstr(4, pos_j2, " ")
            arg.addstr(5, pos_j2, " ")
            arg.addstr(5, pos_j2 - 1, " ")
            arg.addstr(5, pos_j2 - 2, " ")
            arg.addstr(6, pos_j2, " ")
            arg.addstr(7, pos_j2, " ")
            arg.addstr(7, pos_j2 + 1, " ")

            arg.addstr(4-1, pos_j2, "0")
            arg.addstr(5-1, pos_j2, "|")
            arg.addstr(5-1, pos_j2 - 1, "_")
            arg.addstr(5-1, pos_j2 - 2, "\\")
            arg.addstr(6-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2 + 1, "\\")
            arg.refresh()
            time.sleep(0.2)

            arg.addstr(4-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2 - 1, " ")
            arg.addstr(5-1, pos_j2 - 2, " ")
            arg.addstr(6-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2 + 1, " ")

            pos_j2-=3

            arg.addstr(4-1, pos_j2, "0")
            arg.addstr(5-1, pos_j2, "|")
            arg.addstr(5-1, pos_j2 - 1, "_")
            arg.addstr(5-1, pos_j2 - 2, "\\")
            arg.addstr(6-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2 + 1, "\\")
            arg.refresh()
            time.sleep(0.2)
            arg.addstr(4-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2 - 1, " ")
            arg.addstr(5-1, pos_j2 - 2, " ")
            arg.addstr(6-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2 + 1, " ")

    # le joueur 2 saute a droite

        if (key == ord('m')):
            arg.addstr(4, pos_j2, " ")
            arg.addstr(5, pos_j2, " ")
            arg.addstr(5, pos_j2 - 1, " ")
            arg.addstr(5, pos_j2 - 2, " ")
            arg.addstr(6, pos_j2, " ")
            arg.addstr(7, pos_j2, " ")
            arg.addstr(7, pos_j2 + 1, " ")

            arg.addstr(4-1, pos_j2, "0")
            arg.addstr(5-1, pos_j2, "|")
            arg.addstr(5-1, pos_j2 - 1, "_")
            arg.addstr(5-1, pos_j2 - 2, "\\")
            arg.addstr(6-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2 + 1, "\\")
            arg.refresh()
            time.sleep(0.2)

            arg.addstr(4-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2 - 1, " ")
            arg.addstr(5-1, pos_j2 - 2, " ")
            arg.addstr(6-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2 + 1, " ")

            pos_j2+=3

            arg.addstr(4-1, pos_j2, "0")
            arg.addstr(5-1, pos_j2, "|")
            arg.addstr(5-1, pos_j2 - 1, "_")
            arg.addstr(5-1, pos_j2 - 2, "\\")
            arg.addstr(6-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2, "|")
            arg.addstr(7-1, pos_j2 + 1, "\\")
            arg.refresh()
            time.sleep(0.2)
            arg.addstr(4-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2, " ")
            arg.addstr(5-1, pos_j2 - 1, " ")
            arg.addstr(5-1, pos_j2 - 2, " ")
            arg.addstr(6-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2, " ")
            arg.addstr(7-1, pos_j2 + 1, " ")



            arg.addstr(4, pos_j1, " ")
            arg.addstr(5, pos_j1, " ")
            arg.addstr(5, pos_j1 + 1, " ")
            arg.addstr(5, pos_j1 + 2, " ")
            arg.addstr(6, pos_j1, " ")
            arg.addstr(7, pos_j1, " ")
            arg.addstr(7, pos_j1 - 1, " ")




            arg.addstr(4, pos_j2, " ")
            arg.addstr(5, pos_j2, " ")
            arg.addstr(5, pos_j2 - 1, " ")
            arg.addstr(5, pos_j2 - 2, " ")
            arg.addstr(6, pos_j2, " ")
            arg.addstr(7, pos_j2, " ")
            arg.addstr(7, pos_j2 + 1, " ")
            arg.refresh()

        if (pos_j2 - pos_j1 <= 3):

            if (statut_j2 == "attack" and statut_j1!="block"):

                arg.addstr(4, pos_j2, " ")
                arg.addstr(5, pos_j2, " ")
                arg.addstr(5, pos_j2 - 1, " ")
                arg.addstr(5, pos_j2 - 2, " ")
                arg.addstr(6, pos_j2, " ")
                arg.addstr(7, pos_j2, " ")
                arg.addstr(7, pos_j2 + 1, " ")

                arg.addstr(4, pos_j1, " ")
                arg.addstr(5, pos_j1, " ")
                arg.addstr(5, pos_j1 + 1, " ")
                arg.addstr(5, pos_j1 + 2, " ")
                arg.addstr(6, pos_j1, " ")
                arg.addstr(7, pos_j1, " ")
                arg.addstr(7, pos_j1 - 1, " ")

                arg.refresh()

                pos_j2=35

                pos_j1=10
                score_j2+=1

            if (statut_j1 == "attack" and statut_j2 != "block"):
                arg.addstr(4, pos_j2, " ")
                arg.addstr(5, pos_j2, " ")
                arg.addstr(5, pos_j2 - 1, " ")
                arg.addstr(5, pos_j2 - 2, " ")
                arg.addstr(6, pos_j2, " ")
                arg.addstr(7, pos_j2, " ")
                arg.addstr(7, pos_j2 + 1, " ")

                arg.addstr(4, pos_j1, " ")
                arg.addstr(5, pos_j1, " ")
                arg.addstr(5, pos_j1 + 1, " ")
                arg.addstr(5, pos_j1 + 2, " ")
                arg.addstr(6, pos_j1, " ")
                arg.addstr(7, pos_j1, " ")
                arg.addstr(7, pos_j1 - 1, " ")

                arg.refresh()

                pos_j2 = 35

                pos_j1 = 10
                score_j1 += 1

        # créer le sol



curses.wrapper(main)
