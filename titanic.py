print(r'''
                   ,:',:`,:'
                __||_||_||_||___
           ____[""""""""""""""""]___
           \  --------------------- /
    ~~^~^~^~^~^^~^~^~^~^~^~^~^~~^~^~^~^~~^~^''')
print("Welcome to the Titanic.")
print("Your mission is to survive.")

response1 = input("You see a hot rich girl about to throw herself off the ship. Do you try to stop her? ").lower()
if response1 == "yes":
    print("You fall madly in love with this woman and it leads to your demise. RIP.")
elif response1 == "no":
    print("Wow! You are a terrible person, but you have good survival instincts. Carry on.")
    response2 = input("How will you spend the evening? Partying, sleeping, or a moonlit stroll? ").lower()
    if response2 == "partying":
        print("When the ship hits the iceberg, you are trampled by a troupe of Irish dancers. RIP.")
    elif response2 == "sleeping":
        print(
            "Wow! What a nightmare! You dreamt that the ship was going down and you got stuck in your cabin- oh wait. RIP.")
    elif response2 == "moonlit stroll":
        print("When the ship hits the iceberg, you are able to quickly scramble to (temporary) safety!")
        response3 = input("There are three lifeboats left. Which one do you attempt to board? Left, right, or middle? ").lower()
        if response3 == "right":
            print("While this was the right choice, it was not the correct choice. This boat is full. RIP.")
        elif response3 == "middle":
            print("As you are attempting to step onto the boat, you trip and fall to your death. RIP.")
        elif response3 == "left":
            age = int(input("The crew member asks for your age. "))
            if age <= 18:
                print(
                    "The crew member looks at you skeptically, but nevertheless lets you on board. Congrats! You survive the Titanic!")
            else:
                print("They only have space left for children- which you are not. You go down with the ship. RIP.")
        else:
            print("Why did you type that? That doesn't make sense. Restart.")
    else:
        print("Why did you type that? That doesn't make sense. Restart.")
else:
    print("Why did you type that? That doesn't make sense. Restart.")
