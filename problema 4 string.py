"""Se citeste un sir de caractere care reprezinta CNP-ul unei persoane. Sa se verifice corectitudinea lui:numarul de caractere sa fie 13 si toate
caracterele sa fie cifre."""
cnp=input("introdu CNP:")
nr=0
if (len(cnp<13)or(len(cnp)>13):
    print("nu este corect")
else:
    for n in cnp:
        if ord(n) in range(48,58):
            nr+=1
        if(nr==13):
            print("este corect")
        else:
            print("nu este corect")