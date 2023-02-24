# Łamiblog 2023-02-11 Sześć setek
# https://penszko.blog.polityka.pl/2023/02/11/szesc-setek/

import time

macierz_lewa = [
    [2,4,9],
    [2,7,3],
    [3,8,3]
]

macierz_prawa = [
    [2,4,9],
    [2,7,3],
    [3,4,3]
]

# macierz docelowa - rozwiązanie
macDoc = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# macierz pomocnicza
macMoz = [
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
]



zestaw = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def stworzMacierzMozliwosci(macierz):
    
    r = 0
    for row in macierz:
        c = 0
        for num in row:            
            #w każdym zestawie jest przede wszystkim sama cyfra wyjściowa
            zestaw[0] = num
            k = 1
            # doklej cyfrę z przodu
            for i in range (1,10):
                zestaw[k] = int(str(i)+str(num))
                k = k +1
            # doklej cyfrę z tyłu (ale nie powtarzaj liczby złożonej z takich samych 2 cyfr)
            for i in range (0,10):
                if i != num:
                    zestaw[k] = int(str(num)+str(i))
                    k = k + 1
            #print ("Dla num = ",num,zestaw)
            for j in range (0,19):                
                macMoz[r][c][j] = zestaw[j] # co tu się odjaniepawla            
            c = c + 1            
        r = r + 1
    
    return macMoz

def passval(mac): # to jest chore

    newmac = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for i in range(0,3):
        for j in range (0,3):
            newmac[i][j] = mac[i][j]
    
    return newmac

def macDocIter(macMoz, macierz):
    
    i = 0
    global debug
    
    for macDoc[0][0] in macMoz[0][0]:
        for macDoc[0][1] in macMoz[0][1]:
            if macDoc[0][0] + macDoc[0][1] <100: # lekki przyspieszacz
                for macDoc[0][2] in macMoz[0][2]:
                    if (macDoc[0][0] + macDoc[0][1] + macDoc[0][2] == 100):
                        for macDoc[1][0] in macMoz[1][0]:    
                            for macDoc[1][1] in macMoz[1][1]: 
                                for macDoc[1][2] in macMoz[1][2]: 
                                    if (macDoc[1][0] + macDoc[1][1] + macDoc[1][2] == 100):                                            
                                        for macDoc[2][0] in macMoz[2][0]: 
                                            if (macDoc[0][0] + macDoc[1][0] + macDoc[2][0] == 100):
                                                for macDoc[2][1] in macMoz[2][1]: 
                                                    if (macDoc[0][1] + macDoc[1][1] + macDoc[2][1] == 100):
                                                        for macDoc[2][2] in macMoz[2][2]: 
                                                            if ((macDoc[0][2] + macDoc[1][2] + macDoc[2][2] == 100) and (macDoc[2][0] + macDoc[2][1] + macDoc[2][2] == 100)): 
                                                                i = i + 1                                                                
                                                                if debug:
                                                                    print("Rozwiązanie ",i,macDoc)  
                                                                

def main():
    start_time = time.time()

    global debug
    debug = True

        
    for licz in range(0,2):
        licz = licz + 1
        if licz == 1:
            macierz = macierz_lewa
        else:
            macierz = macierz_prawa

        if debug:
            print("Sprawdzam dla ",macierz)                                    
        
        macMoz = stworzMacierzMozliwosci(macierz)        
        macDocIter(macMoz, macierz)
        
        if debug:
            print(" ")
 
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 
