#Condition

"""wallet = 5000
computer_price = 50000

# le prix de l'ordi < 1000
if computer_price <= wallet or computer_price > 1000 :
    print("Ok tu peux mais après tu auras que {}€".format(wallet - computer_price))
    wallet -= computer_price

else:
    print("Nope, t'es pauvre t'as que {}€".format(wallet) + " euros et l'ordi est de {}€".format(computer_price))

text = ("L'achat est possible","l'achat est impossible") [computer_price <= 100]
print(text)
0
print (wallet)"""

# exemple : système de vérification de mot de passe 

password = int(input ("Entrer votre mot de passe"))


#vérifier si mp < 8
if password <= 8:
    print("Mot de passe trop court")
elif password > 8 and password_length <= 12:
    print("Mot de passe moyen")
else:
    print("Mot de passe parfait")

password_length = len(password)
    print(password_length)