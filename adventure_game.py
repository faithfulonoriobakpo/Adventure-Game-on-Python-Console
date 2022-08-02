import time
import random


def print_delay(text_to_print):
    print(text_to_print)
    time.sleep(2)


def intro(enemy):
    print_delay("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {enemy} is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_delay("In front of you is a house.")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand you hold your trusty "
                "(but not very effective) dagger. \n")


def open_field(enemy, weapon, selected_weapon, player_health, enemy_health):
    print_delay("Enter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    print_delay("What would you like to do?")
    while True:
        decision = input("(Please enter 1 or 2.) \n")
        if decision == "1":
            house(enemy, weapon, selected_weapon, player_health, enemy_health)
            break
        elif decision == "2":
            cave(selected_weapon, weapon, enemy, player_health, enemy_health)
            break


def house(enemy, weapon, selected_weapon, player_health, enemy_health):
    print_delay("You approach the door of the house.")
    print_delay("You are about to knock when the door opens and "
                f"out steps the {enemy}.")
    print_delay(f"Eep! This is the {enemy}'s house!")
    print_delay(f"The {enemy} tries to attack you!")
    while True:
        fight_decision = input("Would you like to (1) fight or (2) "
                               "run away? \n")
        if fight_decision == "1":
            fight(enemy, weapon, selected_weapon, player_health, enemy_health)
            break
        elif fight_decision == "2":
            print_delay("You run back into the field. Luckily, you don't "
                        "seem to have been followed.")
            open_field(enemy, weapon, selected_weapon, player_health,
                       enemy_health)
            break


def cave(selected_weapon, weapon, enemy, player_health, enemy_health):
    print_delay("You peer cautiously into the cave.")
    if selected_weapon == []:
        print_delay("It turns out to be an abandoned cave.")
        print_delay("Your eye catches a glint of metal behind a rock.")
        print_delay(f"You have found a {weapon}!")
        print_delay("You discard your silly old dagger and "
                    f"take the {weapon} and other valuables with you.")
        selected_weapon.append(weapon)
    else:
        print_delay("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
    print_delay("You walk back out to the field.\n")
    open_field(enemy, weapon, selected_weapon, player_health, enemy_health)


def fight(enemy, weapon, selected_weapon, player_health, enemy_health):
    if selected_weapon != []:
        weapon_fight(enemy, selected_weapon, player_health, enemy_health)
    else:
        dagger_fight(enemy, weapon, selected_weapon,
                     player_health, enemy_health)


def weapon_fight(enemy, selected_weapon, player_health, enemy_health):
    while True:
        health_meter(enemy_health, player_health, enemy)
        print_delay(f"The {enemy} attacks you but fortunately, your "
                    f"{selected_weapon[0]} protects you from most "
                    "of the attack.")
        player_health -= random.randint(5, 10)
        input("Press any key & enter or just enter to attack back\n")
        print_delay(f"You strike the {enemy} with your {selected_weapon[0]}.")
        enemy_health -= random.randint(8, 25)
        if enemy_health <= 0:
            print_delay(f"You've defeated the {enemy}!")
            break
        elif player_health <= 0:
            print_delay("You have been defeated!")
            print_delay("GAME OVER!")
            break
    play_again()


def dagger_fight(enemy, weapon, selected_weapon, player_health, enemy_health):
    health_meter(enemy_health, player_health, enemy)
    print_delay(f"The {enemy} attacks you.")
    player_health -= random.randint(8, 25)
    input("Press any key & enter or just enter to attack back\n")
    print_delay(f"You attack the {enemy} with your dagger.")
    print_delay(f"but your dagger is no match for the {enemy}"
                " and just little damage is done.")
    enemy_health -= random.randint(5, 10)
    if player_health <= 0:
        print_delay("You have been defeated!")
        print_delay("GAME OVER!")
        play_again()
    elif player_health < 55 and player_health > 35:
        # A recursive function was used to avoid recurssion error
        # from while loop
        def continue_fight(enemy, weapon, selected_weapon, player_health,
                           enemy_health):
            continue_fight_decision = input("You've been beaten bad! "
                                            "Do you want to keep"
                                            " fighting?(y/n)\n").lower()
            if continue_fight_decision == "y":
                dagger_fight(enemy, weapon, selected_weapon,
                             player_health, enemy_health)
            elif continue_fight_decision == "n":
                print_delay("You run back to the field. Perhaps"
                            " you can get a better weapon somewhere.\n")
                open_field(enemy, weapon, selected_weapon,
                           player_health, enemy_health)
            else:
                continue_fight(enemy, weapon, selected_weapon,
                               player_health, enemy_health)
        continue_fight(enemy, weapon, selected_weapon,
                       player_health, enemy_health)
    else:
        dagger_fight(enemy, weapon, selected_weapon,
                     player_health, enemy_health)


def health_meter(enemy_health, player_health, enemy):
    print_delay(f"Your Health Score: {round((player_health/100) * 100)}%")
    print_delay(f"{enemy}'s Health Score: {round((enemy_health/100) * 100)}%")


def play_again():
    play_again_decision = input("Would you like to play again? "
                                "(y/n) \n").lower()
    if play_again_decision == "y":
        print_delay("Restarting Game...\n")
        play_game()
    elif play_again_decision == "n":
        print_delay("Quiting Game...\n")
    else:
        play_again()


def play_game():
    enemies = ["griffin", "dragon", "werewolf", "ghoul", "troll"]
    enemy = random.choice(enemies)
    weapons = ["magic sword", "magic staff", "magic axe"]
    weapon = random.choice(weapons)
    selected_weapon = []
    player_health = 100
    enemy_health = 100
    intro(enemy)
    open_field(enemy, weapon, selected_weapon, player_health, enemy_health)


play_game()
