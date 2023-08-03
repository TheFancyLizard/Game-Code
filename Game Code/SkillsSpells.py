import random
import TextFunctions


def fury(playerCurrentHp, playerCurrentMP):
    playerCurrentHp += 5
    fury_active = True

    playerCurrentMP -= 1

    return playerCurrentMP, playerCurrentHp, fury_active


def heal(playerCurrentHp, playerInfo, playerCurrentMP):
    value = random.randint(1, 6)
    if (playerCurrentHp + value) > playerInfo["Player Hp"]:
        print("Your health is now full")
        playerCurrentHp = playerInfo["Player Hp"]

    else:
        TextFunctions.green_message(f"You heal yourself for {value} health points!")
        playerCurrentHp += value

    playerCurrentMP -= 1

    return playerCurrentHp, playerCurrentMP


def smite(enemy, playerCurrentMP):
    value = random.randint(1, 8)
    TextFunctions.write_n_wait(f"You smote the enemy, dealing {value} points of holy damage!")
    enemy["EnemyHp"] -= value

    playerCurrentMP -= 1

    return enemy, playerCurrentMP


def castArmour(currentAC, playerCurrentMP):
    TextFunctions.pink_message("You increase your defense by 2!")
    currentAC += 2
    playerCurrentMP -= 1

    return currentAC, playerCurrentMP


def runicSlash(enemy, playerCurrentMP):
    value = random.randint(2, 10)
    TextFunctions.write_n_wait(f"You slash at the enemy with a magic blade, dealing {value} points of damage!")
    enemy["EnemyHp"] -= value

    playerCurrentMP -= 1

    return enemy, playerCurrentMP


def shadowCloak(currentAC, playerCurrentMP):
    TextFunctions.pink_message("You increase your defense by 2!")
    currentAC += 2
    playerCurrentMP -= 1

    return currentAC, playerCurrentMP


def feignAttack(playerCurrentMP):
    hitrate_bonus = True
    playerCurrentMP -= 1

    return playerCurrentMP, hitrate_bonus


def check_skill(command, playerCurrentHp, playerInfo, playerCurrentMP, enemy, currentAC, fury_active, hitrate_bonus):
    if playerCurrentMP >= 1:

        if command == "HEAL":
            playerCurrentHp, playerCurrentMP = heal(playerCurrentHp, playerInfo, playerCurrentMP)

        elif command == "SMITE":
            enemy, playerCurrentMP = smite(enemy, playerCurrentMP)

        elif command == "CAST ARMOUR":
            currentAC, playerCurrentMP = castArmour(currentAC, playerCurrentMP)

        elif command == "SHADOW CLOAK":
            currentAC, playerCurrentMP = shadowCloak(playerInfo, playerCurrentMP)

        elif command == "FURY":
            playerCurrentMP, playerCurrentHp, fury_active = fury(playerCurrentHp, playerCurrentMP)

        elif command == "RUNIC SLASH":
            enemy, playerCurrentMP = runicSlash(enemy, playerCurrentMP)

        elif command == "FEIGN ATTACK":
            playerCurrentMP, hitrate_bonus = feignAttack(playerCurrentMP)

        spell_cast = True
        return spell_cast, playerCurrentMP, playerCurrentHp, enemy, currentAC, fury_active, hitrate_bonus

    else:
        print("Insufficient Mana")
