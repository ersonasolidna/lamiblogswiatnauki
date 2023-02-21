import time

macierz = [
    [4,3,8,7],
    [7,6,8,7],
    [6,7,2,6],
    [2,5,1,2]
]

macDoc = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

macMoz = [
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
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
                   

def macDocIter(macMoz):

    # "ręczna" metoda zoptymalizowana pod macierz 4x4
    #print (macMoz[0][0])
    for macDoc[0][0] in macMoz[0][0]:
        for macDoc[0][1] in macMoz[0][1]:            
            for macDoc[0][2] in macMoz[0][2]:
                for macDoc[0][3] in macMoz[0][3]:
                    if (macDoc[0][0] + macDoc[0][1] + macDoc[0][2] +macDoc[0][3] == 100):
                        for macDoc[1][0] in macMoz[1][0]:    
                            for macDoc[1][1] in macMoz[1][1]: 
                                for macDoc[1][2] in macMoz[1][2]:
                                    for macDoc[1][3] in macMoz[1][3]: 
                                        if (macDoc[1][0] + macDoc[1][1] + macDoc[1][2] + macDoc[1][3] == 100):                                            
                                            for macDoc[2][0] in macMoz[2][0]:
                                                for macDoc[2][1] in macMoz[2][1]:
                                                    for macDoc[2][2] in macMoz[2][2]:
                                                        for macDoc[2][3] in macMoz[2][3]:
                                                            if (macDoc[2][0] + macDoc[2][1] + macDoc[2][2] + macDoc[2][3] == 100):
                                                                for macDoc[3][0] in macMoz[3][0]:
                                                                    if (macDoc[0][0] + macDoc[1][0] + macDoc[2][0] + macDoc[3][0] == 100):
                                                                        for macDoc[3][1] in macMoz[3][1]:
                                                                            if (macDoc[0][1] + macDoc[1][1] + macDoc[2][1] + macDoc[3][1] == 100):
                                                                                for macDoc[3][2] in macMoz[3][2]:
                                                                                    if (macDoc[0][2] + macDoc[1][2] + macDoc[2][2] + macDoc[3][2] == 100):
                                                                                        for macDoc[3][3] in macMoz[3][3]:
                                                                                            if (macDoc[3][0] + macDoc[3][1] + macDoc[3][2] + macDoc[3][3] == 100):
                                                                                                print("Rozwiązanie: ",macDoc)
                                                                                                return 1
                                                                                                #break
    return 0
                                                                        
def main():
    start_time = time.time()
    print("Szukam rozwiązania dla: ",macierz)
    stworzMacierzMozliwosci(macierz)
    macDocIter(macMoz)
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main() 
