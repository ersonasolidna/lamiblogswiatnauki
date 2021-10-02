def main():
    y = 0
    for i in range (1000,10001):
        if (int(str(i)[3]) % 2) == 1 and (int(str(i)[2]) % 2) == 0 and (int(str(i)[1]) % 2) == 0 and (int(str(i)[0]) % 2) == 1: # nieparzysta koncowka
            for j in range(10,100):
                if (int(str(j)[1]) % 2) == 1 and (int(str(j)[0]) % 2) == 0:
                    k = i*j
                    if k > 10000 and k < 100000:
                        if (int(str(k)[4]) % 2) == 1 and (int(str(k)[3]) % 2) == 0 and (int(str(k)[2]) % 2) == 0 and (int(str(k)[1]) % 2) == 0 and (int(str(k)[0]) % 2) == 1: # nieparzysta koncowka                    
                            if (str(i)[1] == str(k)[2]):
                                if (str(i)[0] != str(i)[3] and str(i)[0] != str(j)[1] and str(i)[0] != str(k)[4] and str(k)[1] != str(k)[2] and str(k)[1] != str(k)[3] and str(i)[3] != str(j)[1]):
##                                    y = y+1
                                    podsuma1 = i*int(str(j)[1])
                                    if (podsuma1) < 10000 and (int(str(podsuma1)[1]) % 2 == 1):
                                        print(i,"*",j,"=",podsuma1,"+",i*int(str(j)[0]),"=",k)
##    print(y)
    
main()


    
    
        
