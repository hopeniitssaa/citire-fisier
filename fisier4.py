#Ion şi Vasile joacă următorul joc:
# Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. 
# Ajutaţi-l pe Vasile să găsească răspunsul mai repede
# Din fişierul « input.txt » se citeşte un număr, în fişierul « output.txt » - se înscrie consecutivitatea numerelor.
with open("input.txt", "r") as f:
    x=f.readline()
with open('output.txt','w') as f:
    f.write(str(int(x)-2))
    f.write('\n')
    f.write(str(int(x)-1))
    f.write('\n')
    f.write(str(x))
    f.write('\n')
    f.write(str(int(x)+1))
    f.write('\n')
    f.write(str(int(x)+2))