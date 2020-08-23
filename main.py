# A small text adventure game to get back to python

print("Welcome to my little text adventure game!")
name = input("What is your name? ")
age = int(input("How old are you? "))
health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice...left or right? (left/right) ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake."
                        "Do you swim across the lake or go around? (across/around) ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to? (house/river) ")
            if ans == "house":
                print("You go to the house and are greeted by the owner. He doesn't like you and you lose 5 health.")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game.")
                else:
                    print("You have survived, you win!")
            else:
                print("You fell in the river and lost.")
        else:
            print("You fell down and lost.")
    else:
        print("See you.")
else:
    print("You are not old enough to play.")

