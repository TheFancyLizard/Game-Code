import random
import time
import TextFunctions
import SkillsSpells


def create_char():
    # Character creation
    while True:
        #Picking class
        print("1 - Warrior\n"
              "2 - Cleric\n"
              "3 - WarMage\n"
              "4 - Rogue\n"
              "5 - Class Info")
        classChoice = input("What are you, crawler?: ")

        if classChoice == "1":
            print("Ah yes... ", end="")
            time.sleep(1)
            print("a brave warrior...")
            time.sleep(1)
            break

        elif classChoice == "2":
            print("Of couse... ", end="")
            time.sleep(1)
            print("a pristine member of the clergy...")
            time.sleep(1)
            break

        elif classChoice == "3":
            print("How could i not notice... ", end="")
            time.sleep(1)
            print("an illustrious WarMage...")
            time.sleep(1)
            break

        elif classChoice == "4":
            print("A discreet rogue? ", end="")
            time.sleep(1)
            print("Perhaps being in the shadows is for the best...")
            time.sleep(1)
            break

        elif classChoice == "5":
            #Showing Info about Classes
            print("1 - Warrior\n2 - Cleirc\n3 - WarMage\n4 - Rogue")
            info = input("Which class would you like more info on?: ")

            if info == "1":
                print("Warrior info:\nHP: 20\nMana: 4\nWeapon: Greatsword (1d8 Slashing)\nDefence: 14"
                      "\nSkill (1 mana cost): Fury (+1d Damage, Heal 5 HP/Combat)\n"
                      "Atributes: STR(4)/DEX(0)/CON(2)/FTH(1)/INT(-2)/CAR(1)")
                print()

            elif info == "2":
                print("Cleric info:\nHP: 16\nMana: 8\nWeapon: Mace (1d6 Blunt)\nDefence: 15"
                      "\nPrayers (1 mana cost): Heal (1d6), Smite (1d8)\n"
                      "Atributes: STR(2)/DEX(1)/CON(1)/FTH(4)/INT(0)/CAR(-2)")

            elif info == "3":
                print("WarMage info:\nHP: 10\nMana:10\nWeapon: Fists (1d3 Blunt)\nDefence:10"
                      "\nSpells (1 mana cost): Cast Armour (+2 Defence), Runic Slash ((1d6+1d4) magic)\n"
                      "Atributes: STR(-2)/DEX(0)/CON(0)/FTH(0)/INT(5)/CAR(3)")

            elif info == "4":
                print("Rogue info:\nHP: 12\nMana: 6\nWeapon: Dagger (1d4 Slashing/18 Crit-Rate)\nDefence: 14"
                      "\nSkills (1 mana cost): Shadow Cloak (+2 Defence), Feign Attack (+2 Hit-Rate)\n"
                      "Atributes: STR(0)/DEX(4)/CON(2)/FTH(-2)/INT(1)/CAR(1)")

            else:
                print("That was not in the options.")

            print("\n")

        else:
            print("I don't recognize that title, crawler...")
            time.sleep(3)

    if classChoice == "1":
        PlayerInfo = {"Class": "Warrior", "Player Hp": 20, "Player Mana": 4, "Player AC": 14, "WeaponDmg": 8}
        PlayerAtributes = {"STR": 4, "DEX": 0, "CON": 2, "FTH": 1, "INT": -2, "CAR": 1}
        PlayerInventory = {"EQUIPMENT": {"ArmourType": "Light Mail", "ArmourValue": 4, "Weapon": "Greatsword"},
                           "POTIONS": {"HEALING": 0}}
        PlayerSkills = ["FURY"]

    elif classChoice == "2":
        PlayerInfo = {"Class": "Cleric", "Player Hp": 16, "Player Mana": 8, "Player AC": 15, "WeaponDmg": 6}
        PlayerAtributes = {"STR": 2, "DEX": 1, "CON": 1, "FTH": 4, "INT": 0, "CAR": -2}
        PlayerInventory = {"EQUIPMENT": {"ArmourType": "Leather Armour", "ArmourValue": 4, "Shield": "Targe", "ShieldValue": 1,"Weapon": "Mace"},
                           "POTIONS": {"HEALING": 0}}
        PlayerSkills = ["HEAL", "SMITE"]

    elif classChoice == "3":
        PlayerInfo = {"Class": "WarMage", "Player Hp": 10, "Player Mana": 10, "Player AC": 10, "WeaponDmg": 3}
        PlayerAtributes = {"STR": -2, "DEX": 0, "CON": 0, "FTH": 1, "INT": 5, "CAR": 2}
        PlayerInventory = {"EQUIPMENT": {"ArmourType": "Robe", "ArmourValue": 0, "Weapon": "Fists"},
                           "POTIONS": {"HEALING": 0}}
        PlayerSkills = ["CAST ARMOUR", "RUNIC SLASH"]

    elif classChoice == "4":
        PlayerInfo = {"Class": "Rogue", "Player Hp": 12, "Player Mana": 6, "Player AC": 16, "WeaponDmg": 4}
        PlayerAtributes = {"STR": 0, "DEX": 4, "CON": 2, "FTH": -2, "INT": 1, "CAR": 1}
        PlayerInventory = {"EQUIPMENT": {"ArmourType": "Leather Armour", "ArmourValue": 2, "Weapon": "Dagger"},
                           "POTIONS": {"HEALING": 0, "MANA": 0}}
        PlayerSkills = ["SHADOW CLOAK", "FEING ATTACK"]

    return PlayerInfo, PlayerInventory, PlayerAtributes, PlayerSkills


def save_game(playerName, playerInfo, playerInventory, playerAtributes, playerSkills):
    # Saving Player Character
    with open("SavePlayerInfo.txt", "w+") as arquivoInfo:
        arquivoInfo.write(f"{playerName}\n")
        for i in playerInfo:
            arquivoInfo.write(f"{i}\n")
            arquivoInfo.write(f"{playerInfo[i]}\n")

    with open("SavePlayerInventory.txt", "w+") as arquivoInv:
        for i in playerInventory:
            arquivoInv.write(f"{i}\n")
            arquivoInv.write(f"{playerInventory[i]}\n")

    with open("SavePlayerAtributes.txt", "w+") as arquivoAtr:
        for i in playerAtributes:
            arquivoAtr.write(f"{i}\n")
            arquivoAtr.write(f"{playerAtributes[i]}\n")

    with open("SavePlayerSkills.txt", "w+") as arquivoSkl:
        for i in playerSkills:
            arquivoSkl.write(f"{i}\n")


def generate_enemy():
    # Choosing Enemy for Combat
    enemy_type = random.randint(1, 4)
    enemy = {"EnemyName" : "Test", "EnemyAC" : 0, "EnemyDmg" : 1, "EnemyHp" : 5, "EnemyGoldDropMax" : 5}
    if enemy_type == 1:
        enemy = {"EnemyName" : "Slime", "EnemyAC" : 8, "EnemyDmg" : 4, "EnemyHp" : 6, "EnemyGoldDropMax" : 8}

    elif enemy_type == 2:
        enemy = {"EnemyName" : "Rat", "EnemyAC" : 8, "EnemyDmg" : 6, "EnemyHp" : 6, "EnemyGoldDropMax" : 10}

    elif enemy_type == 3:
        enemy = {"EnemyName" : "Goblin", "EnemyAC" : 10, "EnemyDmg" : 6, "EnemyHp" : 8, "EnemyGoldDropMax" : 12}

    elif enemy_type == 4:
        enemy = {"EnemyName" : "Skeleton", "EnemyAC" : 12, "EnemyDmg" : 6, "EnemyHp" : 10, "EnemyGoldDropMax" : 14}

    return enemy


def display_hud(playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG):
    #Function to show Hud info
    print(f"\033[1;96m{playerName} : ", end="")
    print(playerInfo["Class"])
    print(f"\033[1;91mHP:{playerCurrentHP}/", playerInfo["Player Hp"])
    print(f"\033[1;94mMP:{playerCurrentMP}/", playerInfo["Player Mana"])
    print("\033[1;95mDefence:", playerInfo["Player AC"])
    print(f"\033[1;93mGold: {playerG}\033[1;0;0m")


def combat(enemy, playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG, playerAtributes, playerSkills, currentAC):
    #Combat Encounter
    fury_active = False
    hitrate_bonus = False
    while enemy["EnemyHp"] > 0 and playerCurrentHP > 0:
        attack_dealt, spell_cast = False, False
        display_hud(playerCurrentHP, playerCurrentMP, playerInfo, playerName, playerG)
        print("\033[1;33m1 - Attack\n2 - Skills/Spells\n3 - Flee\033[1;0;0m")
        command = input(": ")

        if command == "1":
            attack_dealt = True
            hitRate = random.randint(1, 20)

            if hitrate_bonus:
                hitRate += 2

            print(f"You roll a {hitRate} to attack the ", enemy["EnemyName"], ".")
            time.sleep(2)
            if hitRate != 1 and hitRate != 20:
                if playerInfo["Class"] != "Rogue":
                    print(f"Adding your STRENGTH bonus, you rolled a ", hitRate + playerAtributes["STR"])

                else:
                    print(f"Adding your DEXTERITY bonus, you rolled a ", hitRate + playerAtributes["DEX"])

            time.sleep(2)

            if (playerInfo["Class"] != "Rogue" and (hitRate + playerAtributes["STR"]) >= enemy["EnemyAC"]) or (playerInfo["Class"] == "Rogue" and (hitRate + playerAtributes["DEX"] >= enemy["EnemyAC"])):
                if fury_active:
                    print("Yes")
                    dealtDMG = random.randint(2, playerInfo["WeaponDmg"] * 2)
                else:
                    dealtDMG = random.randint(1, playerInfo["WeaponDmg"])

                if hitRate == 20:
                    TextFunctions.green_message("It's a critical hit!")
                    dealtDMG *= 2

                if playerInfo["Class"] == "Rogue":
                    if hitRate == 19:
                        dealtDMG += playerAtributes["DEX"]
                        dealtDMG *= 2
                    else:
                        dealtDMG += playerAtributes["DEX"]

                else:
                    dealtDMG += playerAtributes["STR"]
                    if dealtDMG < 1:
                        dealtDMG = 1

                TextFunctions.write_n_wait(f"You caused {dealtDMG} to the enemy's health")
                enemy["EnemyHp"] -= dealtDMG

            else:
                if hitRate == 1:
                    TextFunctions.red_message("Critical miss!")
                    dealtDMG = int((random.randint(1, playerInfo["WeaponDmg"])) / 2)
                    if dealtDMG < 1:
                        dealtDMG = 1
                    print(f"You hurt youself, taking {dealtDMG} damage!")
                    playerCurrentHP -= dealtDMG

                else:
                    TextFunctions.write_n_wait("Attack missed.")


        elif command == "2":
            while not spell_cast:
                print("0 - Return")
                for i in playerSkills:
                    print(f"{i}")

                command = input(": ")

                if command == "0":
                    break

                elif command.upper() in playerSkills:
                    command = command.upper()
                    spell_cast, playerCurrentMP, playerCurrentHp, enemy, currentAC, fury_active, hitrate_bonus = SkillsSpells.check_skill(command, playerCurrentHP, playerInfo, playerCurrentMP, enemy, currentAC, fury_active, hitrate_bonus)

                else:
                    print("Command not recognized.")

        elif command == "3":
            print("You ran away from the enemy", end="")
            TextFunctions.wait_time()
            break

        if spell_cast or attack_dealt:
            if enemy["EnemyHp"] > 0:
                print(enemy["EnemyName"], "'s turn.")
                time.sleep(2)

                hitRate = random.randint(1, 20)
                if hitRate >= playerInfo["Player AC"]:
                    TextFunctions.write_n_wait("Enemy landed an attack!")
                    dealtDMG = random.randint(1, enemy["EnemyDmg"])
                    if hitRate == 20:
                        TextFunctions.write_n_wait("Crical hit from the Enemy!")
                        dealtDMG *= 2
                    TextFunctions.red_message(f"You suffered {dealtDMG} points of damage!")
                    playerCurrentHP -= dealtDMG

                else:
                    if hitRate == 1:
                        print("Enemy commited a critical miss!")
                        dealtDMG = int((random.randint(1, playerInfo["WeaponDmg"])) / 2)
                        if dealtDMG < 1:
                            dealtDMG = 1
                        print(enemy["EnemyName"], f" hurt itself for {dealtDMG}!")
                        enemy["EnemyHp"] -= dealtDMG

                    else:
                        print("The ", enemy["EnemyName"], " missed.")
                        time.sleep(2)

                if not (playerCurrentHP > 0):
                    playerG = int(playerG / 2)
                    TextFunctions.red_message("You have been defeated!")
                    TextFunctions.red_message("Half your gold has been lost in the dungeon.")
                    if playerG < 1:
                        playerG = 0

            else:
                TextFunctions.green_message("The enemy has been defeated")
                goldEarned = random.randint(1, enemy["EnemyGoldDropMax"])
                TextFunctions.yellow_message(f"{goldEarned} gold earned!")
                playerG += goldEarned
                if currentAC > playerInfo["Player AC"]:
                    currentAC = playerInfo["Player AC"]

    print("")
    return playerG, playerCurrentHP, playerCurrentMP


def display_inventory(playerInventory, playerCurrentHP, playerCurrentMP):
    print("")
    while True:
        for i in playerInventory:
            print(f"{i}")

        print("Type \"RETURN\" to return")
        command = str.upper(input("Command: "))
        if command == "RETURN":
            break

        elif command in playerInventory:
            print("")
            if not (len(playerInventory) > 0):
                TextFunctions.player_speech("Nothing in this section.")
            else:
                while True:
                    print(command)
                    for i in playerInventory[command]:
                        print(f"{i}:{playerInventory[command][i]}")
                    print("Type \"RETURN\" to return")
                    invcommand = str.upper(input("Command: "))

                    if invcommand == "RETURN":
                        break

                    elif invcommand in playerInventory[command]:
                        print(f"{invcommand} {command} used!")
                        if playerInventory[command][invcommand] > 0:
                            playerInventory[command][invcommand] -= 1

                        if invcommand == "HEALING":
                            playerCurrentHP += 5

                        elif invcommand == "MANA":
                            playerCurrentMP += 2

                    else:
                        TextFunctions.player_speech("\nI don't think i own that.\n")

        else:
            TextFunctions.player_speech("\nI don't think i have a section for that.\n")


def treasure_room(playerG):
    loot_type = random.randint(1, 2)
    if loot_type == 1:
        gold_gain = random.randint(15, 30)
        TextFunctions.write_n_wait("You walk into a room with a chest in the center.")
        TextFunctions.write_n_wait("You open the chest to find it partially full of coins!")
        print(f"You have found {gold_gain} coins")
        playerG += gold_gain

    elif loot_type == 2:
        print("Not yet implemented.")
