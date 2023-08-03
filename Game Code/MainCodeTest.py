import time
import random
import MechanicFunctions
import TextFunctions
import StoreAndWares

closegame = False


def check_save():
    try:
        with open("SavePlayerInfo.txt", "r") as arquivoInfo:
            playerInfo = {}
            expendableList = []
            for i in arquivoInfo:
                expendableList.append(i)
            playerName = expendableList[0][:-1]
            for i in range(1, len(expendableList), 2):
                playerInfo[expendableList[i][:-1]] = expendableList[i+1][:-1]

            playerInfo["Player Hp"] = int(playerInfo["Player Hp"])
            playerInfo["Player Mana"] = int(playerInfo["Player Mana"])
            playerInfo["Player AC"] = int(playerInfo["Player AC"])
            playerInfo["WeaponDmg"] = int(playerInfo["WeaponDmg"])

        with open("SavePlayerInventory.txt", "r") as arquivoInfo:
            playerInventory = {}
            expendableList = []
            for i in arquivoInfo:
                expendableList.append(i)
            for i in range(0, len(expendableList), 2):
                playerInventory[expendableList[i][:-1]] = expendableList[i + 1][:-1]

            playerInventory["ArmourValue"] = int(playerInventory["ArmourValue"])

        with open("SavePlayerAtributes.txt", "r") as arquivoInfo:
            playerAtributes = {}
            expendableList = []
            for i in arquivoInfo:
                expendableList.append(i)
            for i in range(0, len(expendableList), 2):
                playerAtributes[expendableList[i][:-1]] = expendableList[i + 1][:-1]

            for i in playerAtributes:
                playerAtributes[i] = int(playerAtributes[i])

        with open("SavePlayerSkills.txt", "r") as arquivoInfo:
            playerSkills = []
            for i in arquivoInfo:
                playerSkills.append(i[:-1])


    except FileNotFoundError:
        playerInfo, playerInventory, playerAtributes, playerSkills = MechanicFunctions.create_char()
        print("Before you go... ", end="")
        time.sleep(2)
        TextFunctions.write_n_wait("What is thy name?: ")
        while True:
            playerName = input()
            playerName = str.strip(playerName)
            if len(playerName) == 0:
                print("You must have some name or title to go by, adventurer.")

            else:
                break
    return playerName, playerInfo, playerInventory, playerAtributes, playerSkills


def dungeon_inside(playerG, playerCurrentHP, playerInfo, playerCurrentMP):
    print("Entering Dungeon", end="")
    TextFunctions.wait_time()
    while True:
        MechanicFunctions.display_hud(playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG)
        print("1 - Delve Deeper\n2 - Manage Inventory\n3 - Return to the Surface.")
        navigation = input(": ")

        if navigation == "1":
            luck = random.randint(1,2)

            if luck == 1:
                enemy = MechanicFunctions.generate_enemy()
                print("")
                print(f"\033[1;30;101mA ", enemy["EnemyName"], " appears!\033[1;0;0m\n")

                playerG, playerCurrentHP, playerCurrentMP = MechanicFunctions.combat(enemy, playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG, playerAtributes, playerSkills, currentAC)

            elif luck == 2:
                MechanicFunctions.treasure_room(playerG)

        elif navigation == "2":
            MechanicFunctions.display_inventory(playerInventory)

        elif navigation == "3":
            TextFunctions.write_slow("Exiting Dungeon")
            TextFunctions.wait_time()
            break
    return playerG, playerCurrentHP, playerCurrentMP


def surface(playerG, playerCurrentHP, playerCurrentMP):
    closegame = False
    TextFunctions.write_n_wait("Welcome to the surface!\n")
    while True:
        MechanicFunctions.display_hud(playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG)
        TextFunctions.write_n_wait("1 - Shop\n2 - Rest at Inn (5G)\n3 - Manage Inventory"
                                   "\n4 - Descend into the Dungeon\n5 - Save and Quit")
        navigation = input(": ")

        if navigation == "1":
            StoreAndWares.shop(playerG, playerAtributes, playerInventory)

        elif navigation == "2":
            if playerG >= 5:
                if playerCurrentHP >= playerInfo["Player Hp"] and playerCurrentMP >= playerInfo["Player Mana"]:
                    TextFunctions.player_speech("I need not rest.")

                else:
                    if playerCurrentHP < playerInfo["Player Hp"]:
                        playerCurrentHP += int(playerInfo["Player Hp"]/2)
                        if playerCurrentHP > playerInfo["Player Hp"]:
                            playerCurrentHP = playerInfo["Player Hp"]

                    if playerCurrentMP < playerInfo["Player Mana"]:
                        playerCurrentMP += int(playerInfo["Player Mana"]/2)
                        if playerCurrentMP > playerInfo["Player Mana"]:
                            playerCurrentMP = playerInfo["Player Mana"]

                    playerG -= 5

            else:
                TextFunctions.merchant_speech("Not Enough Gold, Crawler.")

        elif navigation == "3":
            MechanicFunctions.display_inventory(playerInventory, playerCurrentHP, playerCurrentMP)

        elif navigation == "4":
            break

        elif navigation == "5":
            closegame = True
            MechanicFunctions.save_game(playerName, playerInfo, playerInventory, playerAtributes, playerSkills)
            break

    return closegame, playerG, playerCurrentHP, playerCurrentMP


playerName, playerInfo, playerInventory, playerAtributes, playerSkills = check_save()


playerCurrentHP = int(playerInfo["Player Hp"])
playerCurrentMP = int(playerInfo["Player Mana"])
currentAC = int(playerInfo["Player AC"])
playerG = 0

TextFunctions.write_slow(f"Good luck, {playerName}...\n")

while not closegame:
    playerG, playerCurrentHP, playerCurrentMP = dungeon_inside(playerG, playerCurrentHP, playerInfo, playerCurrentMP)
    closegame, playerG, playerCurrentHP, playerCurrentMP = surface(playerG, playerCurrentHP, playerCurrentMP)
