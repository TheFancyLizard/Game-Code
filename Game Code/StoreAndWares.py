import TextFunctions
import random


def shop(playerG, playerAtributes, playerInventory):
    # In-Game Shop
    TextFunctions.merchant_speech("Welcome to The Shop!")
    while True:
        TextFunctions.write_n_wait("1 - Purchase\n2 - Sell\n3 - Leave")
        navigation = input(": ")

        if navigation == "1" and playerG > 0:
            print("1 - Weapons\n2 - Armour\n3 - Arcane Scrolls\n4 - Prayer Tomes\n5 - Consumables"
                  "\n6 - Acessories\n7 - Nevermind")
            rand =random.randint(1, 100)
            if rand >5:
                TextFunctions.write_n_wait("Catalogue: ")
            else:
                TextFunctions.merchant_speech("What're ye buying, stranger?: ")
            navigation = input(": ")

            if navigation == "1":
                TextFunctions.merchant_speech("Here are the Weapons: ")

            elif navigation == "2":
                TextFunctions.merchant_speech("Here are the Armours: ")

            elif navigation == "3" and playerAtributes["INT"] > 0:
                TextFunctions.merchant_speech("Here are the scrolls: ")

            elif navigation == "3" and not (playerAtributes["INT"] > 0):
                TextFunctions.merchant_speech("I believe you do not have what it takes to learn sorcery.")

            elif navigation == "4" and playerAtributes["FTH"] > 0:
                TextFunctions.merchant_speech("Here are the tomes: ")

            elif navigation == "4" and not (playerAtributes["FTH"] > 0):
                TextFunctions.merchant_speech("You don't seem to have enough faith for this.")

            elif navigation == "5":
                while True:
                    TextFunctions.merchant_speech("Here are the consumables, crawler:")
                    print("0 - Return\n1 - Healing Potion(5HP, 3G)\n2 - Mana Potion(2MP, 1G)")
                    purchase = str.upper(input(": "))

                    if purchase == "0":
                        break

                    elif purchase == "1" and playerG >= 3:
                        if playerInventory["POTIONS"]["HEALING"] != 3:
                            playerInventory["POTIONS"]["HEALING"] += 1
                            playerG -= 3
                        else:
                            TextFunctions.merchant_speech("You already carry too many of these, Crawler.")

                    elif purchase == "2" and playerG >= 1:
                        if playerInventory["POTIONS"]["MANA"] != 3:
                            playerInventory["POTIONS"]["MANA"] += 1
                            playerG -= 1
                        else:
                            TextFunctions.merchant_speech("You already carry too many of these, Crawler.")

                    else:
                        TextFunctions.merchant_speech("I can only sell what's in stock, Crawler.")

            elif navigation == "6":
                TextFunctions.merchant_speech("Here's what if have in this category:")

            elif navigation == "7":
                TextFunctions.merchant_speech("Very well.")

        elif navigation == "1" and playerG <= 0:
            TextFunctions.merchant_speech("Not to judge or be rude, but you seem to be unable to afford anything...")

        elif navigation == "2":
            if not (len(playerInventory) > 0):
                TextFunctions.merchant_speech("You have nothing to sell me.")

        elif navigation == "3":
            break

        else:
            TextFunctions.merchant_speech("Crawler, please chose something from the list.")
