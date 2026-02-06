print ("hello me")

messaggio_carino= "\nI hope you get cancer"

favourite_food= "sandwich"
print ("my favourite food is "+favourite_food)

nome= input("\nHey whats your name? ")

if(nome== "Marisa"):
    print ("\nUmm what a cute name >_<")
else:
    print("\nwhat a cool name")
    
location=input("\nWhere you live? ")

if(location=="Gensokyo"):
    print("by the name seems like a cool place")
else:
    print("what a shity place")

if(nome=="Marisa"):
    print(" I hope you're safe there")
else:
    print(messaggio_carino)

lunghezza_nome=len(nome)
lunghezza_nome_stringa=str(lunghezza_nome)
print("your name has "+lunghezza_nome_stringa+ " letter")

anno_di_nascita=input("\nIn which year you were born? ")
anno_di_nascita_intero=int(anno_di_nascita)
anno_corrente=input("\nIn which year you're?" )
anno_corrente_intero=int(anno_corrente)
eta=anno_corrente_intero - anno_di_nascita_intero
eta_stringa=str(eta)
print("\nYou're  "+eta_stringa+" years old")

answer=" "
while(answer  != "idk"):
    print("\n I'll BURN MY DREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAD")
    answer=input()
    if(answer !="and I will face the sun with the pride of the living"):
        print("put the sentence that will stop the cycle")
    else:
         print("congrats you have burned the dread")
           


