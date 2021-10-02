def main():
    y = 0
    for o in range (1,10):
        for l in range (1,10):
            if l != o:
                for u in range (1,10):
                    if (u != o) and (u!= l):
                        for w in range (1,10):
                            if (w != u) and (w != o) and (w!= l):
                                olow = o*1000+l*100+u*10+w
                                for z in range (1,10):
                                    if (z!=w) and (z != u) and (z != o) and (z!= l):
                                        for t in range (1,10):
                                            if (t!=z) and (t!=w) and (t != u) and (t != o) and (t!= l):
                                                zloto = z*10000+l*1000+o*100+t*10+o
                                                for pb in range (1,10):
                                                    if (pb!=t) and (pb!=z) and (pb!=w) and (pb != u) and (pb != o) and (pb!= l):
                                                        for au in range (1,10):
                                                            if (au!=pb) and (au!=t) and (au!=z) and (au!=w) and (au != u) and (au != o) and (au!= l):                                                            
                                                                for x in range (1,10):
                                                                    wx= w*10 + x
                                                                    iloczyn = olow * wx
                                                                    if (olow * w == zloto) and  (int(str(iloczyn)[1]) == pb) and (int(str(iloczyn)[3]) == au):
                                                                        print (olow,"*",wx,"=",x*olow,"+",zloto,"=",iloczyn)
                                                                    
main()


    
    
        
