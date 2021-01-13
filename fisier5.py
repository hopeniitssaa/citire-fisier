#Afişaţi tabla înmulţirii cu numărul n
#Exemplu: pentru n=5, se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr, în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.
with open('numar.txt','r') as f:
    a=f.readline()
with open('inmultire.txt','w') as f:
    f.write('1'+'*'+(a)+'='+(str(int(a)*1)))
    f.write('\n')
    f.write('2'+'*'+(a)+'='+(str(int(a)*2)))
    f.write('\n')
    f.write('3'+'*'+(a)+'='+(str(int(a)*3)))
    f.write('\n')
    f.write('4'+'*'+(a)+'='+(str(int(a)*4)))
    f.write('\n')
    f.write('5'+'*'+(a)+'='+(str(int(a)*5)))
    f.write('\n')
    f.write('6'+'*'+(a)+'='+(str(int(a)*6)))
    f.write('\n')
    f.write('7'+'*'+(a)+'='+(str(int(a)*7)))
    f.write('\n')
    f.write('8'+'*'+(a)+'='+(str(int(a)*8)))
    f.write('\n')
    f.write('9'+'*'+(a)+'='+(str(int(a)*9)))
    f.write('\n')
    f.write('10'+'*'+(a)+'='+(str(int(a)*10)))
    