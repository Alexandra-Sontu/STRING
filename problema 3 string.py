    
"""de la tastatura se citesc patru cuvinte, fiecare cuvant fiind citit intr-o singura variabila, un cuvant va fi format din minim 3 caractere.
Elaborati un program care va forma un cuvant nou, in felul urmator :din primul cuvant va adauga primele 2 caractere,din al doilea cuvant va
adauga primul caracter ,primele trei caractere din cuvantul al treilea si n/2 caractere din cuvantul patru(n-lungimea cuvantului). La ecran
se vor afisa cuvintele citite cat si cuvantul format."""
x=input("introdu primul cuvant:")
y=input("intrdou al doilea cuvant:")
z=input("introdu al treilea cuvant:")
d=input("introdu al patrulea cuvant:")
if ((len(x)<3) or (len(y)<3) or (len(z)<3) or (len(d)<3)):
    print("error")
l1=x[:2]
l2=y[0]
l3=z[:3]
l4=v[:(len(v)//2]
print("cuvintele:",x,y,z,d,sep=" ")
print("cuvintul format",l1+l2+l3+l4)