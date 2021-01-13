#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre
#Numărul globuleţelor albe se citeşte din fişierul « globulet.txt »
#Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe
#globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii
#Numărul total de globuleţe este înscris în fişierul « bradut.txt »
#Exemplu: Date de intrare: 12 	Date de ieşire: 52. 
with open('globulet.txt ','r') as f:
    a=f.readline()
r=int(a)+2
ar=int(a)+int(r)
b=int(ar)-2
t=int(a)+b+r
with open('bradul.txt','w') as f:
    f.write(str(t))