"""Place de cinéma 
Recolter quel est votre age 
Si la personne est mineur 7€
Si majeur 12€
Souhaitez vous du pop corn ? 
Si oui +5€ u
afficher prix total"""

print("Bienvenue au cinéma magique !")

age = int(input("Quel âge avez vous ? "))

if age >= 18:
    price = 12
    print("Prix de la place adulte est de : {}€".format(price))

else :
    price = 7
    print("Prix de la place -18 ans est de : {}€".format(price)) 

pop_corn = int(input("Le pop corn est à 5 €, combien en voulez-vous ? "))

price_pop = pop_corn*5

total = (price_pop+price)

if price_pop <=0 :

    print("Dommage, il est si bon !\n""Cependant votre total est de : {}€".format(price)) 

else :
    print("Ohla malheureux ! Doucement avec le pop corn ! Il est si bon !\n""Prix de la place : {}€".format(price))
    print("Prix du pop corn : {}€".format(price_pop)) 
    print("Prix total : {}€".format(total))
