##NEEDS IMPROVMENT V0.1. NOT COMPLETE VERSION

from os import *
from bitcoin import *

bankcard = False
giftcard = False
crypto = False


##Calling the wallet in other scripts - start

def make_payment():
    ##WORK ON THIS
    print("idk")

##Calling the wallet in other scripts - end

##Accessing Python wallet file - start

print("Welcome to your yas2 wallet.")
print("What would you like?")
print("To say 'bank card' say bc")
print("To say 'cryptocurrency' say c")
print("To say 'gift card' say gc")
action1 = input()

if action1 == "bc":
    if bankcard == False:
        print("You do not have a bank card listed. Would you like one?")
        makeBankCardTrue = input("'y' for yes and 'n' for no ")
        if makeBankCardTrue == "y":
            print("Credit or debit card?")
            if input("'c' for credit and 'd' for debit ") == "d":
                debitCardNumber = input("Debit card number: ")
                debitCardCVC = input("CVV2/CVC2: ")
                debitCardExpiryDateMonth = input("Month card expires (MM/YY): ")
                debitCardExpiryDateYear = input("Year card expires (MM/YY): ")
                debitCardZip = input("Zip code: ")
                print("Debit card added!")
            
            if input("'c' for credit and 'd' for debit ") == "c":
                creditCardNumber = input("Credit card number: ")
                creditCardCVC = input("CVV2/CVC2: ")
                creditCardExpiryDateMonth = input("Month card expires (MM/YY): ")
                creditCardExpiryDateYear = input("Year card expires (MM/YY): ")
                creditCardZip = input("Zip code: ")
                print("Credit card added!")

    else:
        print("Ok. Have a good day!")
    if bankcard == True:
        ##Update this
        print("This will update soon.")

if action1 == "gc":
    if giftcard == False:
        print("Would you like to add a gift card?")
        if input("type 'y' if yes and type 'n' if no") == "y":
            giftCardOrigin = input("What store is this gift card from? ")
            giftcardPIN = input("What is the PIN of the gift card? ")
        else: 
            print("Have a good day!")
    if giftcard == True:
        ##WORK ON THIS
        print("nice")

if action1 == "c":

    if crypto == False:
        print("What crypto would you like to use?")
        print("Available cryptocurrencies:")
        print(" ")
        print("Bitcoin (type 'btc' to use)")
        print("")
        if input() == "btc":
            print("Do you want a new wallet or do you already have a wallet?")
            wantACryptoWallet = input("type 'y' for new wallet and type 'n' if you already have one ")
            if wantACryptoWallet== "y":
                privateKey = random_key()
                publicKey = privkey_to_pubkey(privateKey)
                address = pubkey_to_address(publicKey)
                print("Private key:" + privateKey)
                print("")
                print("Public key: " + publicKey)
                print("")
                print("Address: " + address)
                print("")
                print("Do not share your private key with anyone. If exposed, someone may be able to get in to your wallet.")

            elif wantACryptoWallet == "n":
                if crypto == False:
                    print("Have a good day!")

                elif crypto == True:
                    ##WORK ON THIS
                    print("idk")    
        else:
            print("That cryptocurrency is not available")

##Accessing Python wallet file - end


