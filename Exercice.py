#Variable

"""def main () :

    cash = 148 
    purchase = 50
    wallet = (cash - purchase)

    print("L'argent restant dans votre porte monnaie est de " + str(wallet) + " euros après votre acaht de " + str(purchase) + " euros")

if __name__ == '__main__':
    main()"""

"""def main () :

    cash = int(input("Entrer votre argent disponible ")) 
    purchase = int(input("Entrer le montant de votre achat "))
    
    wallet = (cash - purchase)
    
    print("Suite à votre achat de " +str(purchase) + " euros, votre argent restant est de " + str(wallet) + " euros. Avant vous disposiez de " + str(wallet + purchase) + " euros.")

if __name__ == '__main__':
    main()"""

def main () :

    wallet = int(input("Entrer le nombre d'€ que vous avez "))
    print("Vous avez actuellement " + str(wallet) + " euros.")

    produit = 50
    print("Le produit vaut " + str(produit) + " euros.")

    wallet -= produit 

    print("Produit acheté !")
    print("Il ne vous reste plus que " + str(wallet) + " euros.")
    print("CHEHHHHH")

if __name__ == '__main__' :
    main() 