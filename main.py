import math
import time
import os

def clear_console():
    os.system('cls')

def draw_line():
    print('----------------------------------------------------------')

def gomb_felszin():
    print('Gömb felszínszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Térfogat')
    print('2. Sugár hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()
    if opcio == 1:
        terfogat : float = 0
        while terfogat <= 0:
            terfogat : float = float(input('Adja meg a gömb térfogatát! (cm3)'))
            if terfogat <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius : float = ((terfogat * 3) / (4 * math.pi)) ** (1 / 3)
        felszin : float = 4 * radius ** 2 * math.pi
        print(f'A gömb felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        radius : float = 0
        while radius <= 0:
            radius : float = float(input('Adja meg a gömb sugarának hosszát! (cm)'))
            if radius <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        felszin : float = 4 * radius ** 2 * math.pi
        print(f'A gömb felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def gomb_terfogat():
    print('Gömb térfogatszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Felszín')
    print('2. Sugár hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()

    if opcio == 1:
        felszin : float = 0
        while felszin <= 0:
            felszin : float = float(input('Adja meg a gömb felszínét! (cm2)'))
            if felszin <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius = math.sqrt(felszin / (4 * math.pi))
        terfogat : float = (4 * radius ** 3 * math.pi) / 3
        print(f'A gömb térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        radius : float = 0
        while radius <= 0:
            radius : float = float(input('Adja meg a gömb felszínét! (cm2)'))
            if radius <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        terfogat : float = (4 * radius ** 3 * math.pi) / 3
        print(f'A gömb térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def main():
    print("Program a gömb felszínének és térfogatának kiszámolására.")
    draw_line()
    while True:
        print('Mit szeretne tenni?')
        print('1. Felszín kiszámolása')
        print('2. Térfogat kiszámolása')
        print('3. Kilépés a programból')
        opcio : int = int(input('Adja meg az opció számát: '))
        draw_line()
        if opcio == 1:
            gomb_felszin()
        elif opcio == 2:
            gomb_terfogat()
        elif opcio == 3:
            print('Kilépés a programból...')
            quit()

if __name__ == "__main__":
    main()