#By UntossibleTrash007
#2023/11/27

import random

def write(*lines):
    for line in lines:
        print(line)
        input()

def kitchen():
    write(
        "Despite the horrors of dragging yourself out of bed, you manage to make it to the kitchen.",
        "You grab your favourite bowl from the cupboard and your favourite cereal from the pantry,\nbut even more horrors strike as you open the fridge to find out you have no milk!"
    )
    print("What do you do?\n- Head out to the store to buy milk (a)         - Cry on the floor (s)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            walk()
        elif choice == "s":
            cry2()
        elif choice == "d":
            drycereal()
        else:
            print("please enter a valid input")

def walk():
    write(
        "After taking a moment to get yourself ready, you take a giant step out into the world and grimace at the brightness of the outdoors.",
        "Despite that, you manage to make it to the end of your street without any issues.",
        "'Maybe this won't be so bad after all' you think to yourself",
        "Immediately as you think that, you take one large, confident step.",
        "Suddenly, your foot feels cold and wet...",
        "You now realize that you have stepped in a giant puddle of water.",
        "You let out a long sigh, all of your once born confidence suddenly leaving your body all at once.",
        "You continue walking, when you suddenly come across Tibbles, the neighbourhood cat!",
    )
    print("What do you do?\n - Pet Tibbles (a)              - Continue to the store (s)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            cat()
        elif choice == "s":
            cont()
        else:
            print("please enter a valid input")

def cat():
    write(
        "You let out the most obnoxious 'OMG TIBBLES HIIIIIII' before sprinting over to the poor cat.",
        "Tibbles is already used to your bullshit and sits there and stares at you as you rush towards him, but trip over your own feet before reaching and face plant the ground.",
        "This does not stop you, as you crawl over to Tibbles and give him a big hug and and a little kiss on his forehead.",
        "It seems you have pleased Lord Tibbles, and he has blessed you with much cereal blessings.",
        "After saying goodbye to Tibbles, you continue on with your perilous journey",
    )
    cont()

def cont():
    write(
        "The store is close, you can almost taste it.",
        "Or maybe that's just the stale gasoline in the air from all of the cars ¯\_(ツ)_/¯",
        "Either way, you are getting restless for the cereal.",
        "It is not a want, it's a need.",
        "But just as you can see the store in the distance, you come across a lemon tree.",
    )
    print("What do you do?\n - Interact (a)            - Ignore (s)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            lemon()
        elif choice == "s":
            ignore()
        else:
            print("please enter a valid input")


def lemon():
    write(
        "As you're passing by this lemon tree, it gives you a look.",
        "You're not sure if you appreciate the look, but engage with the tree anyways",
        "'Hey girl, hey'",
        "'sup'",
        "You feel heat rising in your cheeks, 'No no stop it, I have a boyfriend (nah jk jk I'm lonely *peepoShy*)'",
        "'k'",
        "You stare at each other for a solid two minutes before you blow the lemon tree a nice little kiss and continue on.",
    )
    ignore()

def ignore():
    write(
        "After a grueling (7 minute) walk to the closest supermarket, you burst through the front revolving doors like the Kool-Aid Man and demand to know where the milk is.",
        "The mortified cashier shakily raises his hand and points to the back of the store",
    )
    print("What do you do?\n - go to the back of the store (a)          - blow the cashier a kiss (s)          - make an intimidation check (d)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            store()
        elif choice == "s":
            kiss()
        elif choice == "d":
            intimidation()
        else:
            print("please enter a valid input")

def store():
    write(
        "You find your way to the back of the store, the wall lined with fridges containing various dairy products.",
        "You scan the wall carefully and spot the milk a little bit to the left from where you are standing.",
        "Excitement fills your bones.",
        "You can barely contain your excitement, and you begin doing the Cha Cha Slide in the middle of the aisle.",
        "After you're finished with your little jig, you grab a carton of 2% milk from the fridge and bring it up to the checkout"
    )
    checkout()

def checkout():
    write(
        "You pull up to the self checkout, as you are now too scared to look the cashier in the face, and quickly scan your milk.",
        "It is almost cereal o'clock, you can almost taste it.",
        "Once your payment goes through, you take your receipt and shove it into the deep dark depths of your pocket.",
        "With a spring in your step, you giddily walk out the door and basically sashay your way back home."
    )
    home()

def home():
    write(
        "As soon as you pull up to your apartment, you sprint into the kitchen and grab your favourite bowl.",
        "Once the bowl has been acquired, you must now grab your box of cereal.",
        "Now, you must make the most important decision of your entire life..."
    )
    print("Which do you put in your bowl first, milk (s) or cereal? (a)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            cereal()
        elif choice == "s":
            milk()
        else:
            print("please enter a valid input")

def milk():
    write(
        "You are a heathen. Literally.",
        "Despite this fact you continue preparing your bowl of cereal."
    )
    complete()

def complete():
    write("Once the bowl of cereal, is in fact, a bowl of cereal, you must now choose how you should eat it.")
    print("Eat the cereal like a dog (a), eat it with your hands (s), eat it like a normal functioning human being (d)")
    choice = " "
    choices = ["a", "s", "d"]
    while choice not in choices:
        choice = input()
        if choice == "a":
            dog()
        elif choice == "s":
            hands()
        elif choice == "d":
            normie()
        else:
            print("please enter a valid input")

def dog():
    write(
        "Without hesitation, you shove your face into the bowl of cereal and start munching away.",
        "eventually, there is no more cereal left to munch and cromch, so you start drinking the milk.",
        "Also like a dog.",
        "you are now covered in cereal and milk.",    
        "It was totally worth it.",
        "THE END"
    )
    exit()

def hands():
    write(
        "You take one look at the spoon in your hand and think 'Pfffft spoons are for normies!' and proceed to throw it on the ground.",
        "You then proceed to grab a handful of cereal, milk dripping down you hand as you shove the handful of cereal into your mouth.",
        "Once the cereal is gone, and milk drank, craving fulfilled, you wash your bowl like a civilized person and continue on with your day."
        "THE END"
    )
    exit()

def normie():
    write(
        "You pick up you favourite spoon from the table and now begin to eat your bowl of cereal that you worked so hard for.",
        "It doesn't take long for you to finish your little treat, and now you are ready to face the horrors of the day.",
        "THE END"
    )
    exit()

def cereal():
    write("You are a cultured person, so you decide to pour in the cereal before the milk.")
    complete()

def kiss():
    write("Upon realizing that you may have scarred this poor cashier for life, you blow them a little kiss as an apology before heading to the back of the store for your precious milk.")
    store()

def intimidation():
    print("Press 'i' to make an intimidation check")
    check = " "
    inputs = ["i"]
    while check not in inputs:
        check = input()
        if check == "i":
            roll = random.randint(1,20)
        else:
            print("I said press I >:((((((")
    
    if roll < 15:
        write(
            "The cashier's adreneline wore off and now you look like a silly little weirdo to them",
            "The cashier lets out a looooong drawn out sigh and thinks 'it's another one of *those* days huh?'",
        )
        store()
    elif roll > 15:
        write(
            "The cashier is shivering in their boots as you make direct eye contact with them. You are exerting some sort of unknown but extremely high pressure around you.",
            "The cashier faints as boss music starts playing in the background.",
            "In reality, it was just your phone going off."
        )
        store()


def cry2():
    write(
        "You sink to the floor, devastated that your craving cannot be filled. Your dissappointment is immesurable and your day is ruined.",
        "THE END"
    )
    exit()

def drycereal():
    write(
        "Out of pure desperation, you MUST fulfill your craving of eating cereal. No matter the cost.\nYou pry open the box, rip the bag out, tear it open and start pouring the cereal into your mouth.",
        "Sure you may be choking, but man it's well worth it. To your dismay, you reach the end of the bag, and you're faced with the decision; what now?",
        "You look down at the empty bag and box in your hands, until the little possum in your brain whispers to you: 'Do it'",
        "Following the possum's commands, you take the plastic bag and and take a large bite. At first, the texture throws you off guard, but oddly, you feel compelled to continue.",
        "Soon the bag is gone, and now all that's left is the cereal box. You feel an urge. You gingerly pick up the box and take a nice chomp out of it.",
        "Soon, the box is gone as well, and you are now downing a couple of antacid tablets and drinking tea on the couch as you feel sick from eating plastic and cardboard.",
        "Do you feel terrible now? Yes. But was it worth it? Only you know.",
        "THE END",
    )
    input()
    exit()

def cry():
    write("Instead of braving the horrors of the world, you sit in your bed, forever cereal-less, and cry yourself back to sleep. Are you ok? Do you need a hug?")
    exit()

if __name__ == "__main__":
    while True:
        write(
            "It is a dark and dreary Friday morning",
            "You find yourself craving a bowl of cereal",
            "You are currently lying in bed though. No cereal to be found unfortunately :(((("
        )
        print("What would you like to do? \n - go to the kitchen (a)      - Stay in bed cereal-less and sad (s)")
        choice = " "
        choices = ["a", "s"]
        while choice not in choices:
            choice = input()
        if choice == "a":
            kitchen()
        elif choice == "s":
            cry()
        else:
            print("please enter a valid input")
        
