with open("text.txt","r") as f: 
    a=f.readline()
    b=f.readline()
    c=f.readline()
    print(int(a)+int(b)+int(c))
    print(int(a)*int(b)*int(c))
    import math
    print(math.sqrt(int(a)**2+int(b)**2+int(c)**2))
