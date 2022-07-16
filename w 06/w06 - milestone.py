# https://byui-cse.github.io/cse110-course/lesson06/prove.html
# 06 Prove: Assignment - Adventure Game
print("---------WELCOME TO THE ADVENTURE GAME---------")
print("INSTRUCTIONS: As the story progresses you will have to make different decisions to create your own story. \nThe decisions to choose will be in capital letters.")
print()
print("Let's begin this adventure...")

#INTRO
scenario = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?: ").upper()
print()
while scenario != "MATCH" and scenario != "FLASHLIGHT":
    scenario = input("Wrong answer! Do you pick up the MATCH or the FLASHLIGHT?: ").upper()

#CONDITIONALS
if scenario == "MATCH": #DECISION MATCH
        scenario = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN or HIDE behind a tree?: ").upper()
        print()

        while (scenario != "RUN" and scenario != "HIDE"):
            scenario = input("Wrong answer! Do you RUN or HIDE?: ").upper()

        if  scenario == "RUN": #DECISION MATCH -> RUN -> 
            scenario = input("You start running but the bear has already saw you! Do you want ATTACK the bear, CLIMB a tree or SCARE the bear?: ").upper()
            print()

            while scenario != "ATTACK" and scenario != "CLIMB" and scenario != "SCARE":
                scenario = input("Wrong answer! Do you ATTACK, CLIMB or SCARE?: ").upper()

            if scenario == "ATTACK": #DECISION MATCH -> RUN -> ATTACK
                print("You were tired and the bear was really big. You died") #END 1
            
            elif scenario == "CLIMB": #DECISION MATCH -> RUN -> CLIMB
                print("The bear knows how to climb too. It has reached you. You died") #END 2

            elif scenario == "SCARE": #DECISION MATCH -> RUN -> SCARE 
                print("You started screaming and yelling to the bear, it seems He got scared and left. One of your friends heard you and came to help you... You survived!") #END 3
            
            else: 
             print("Invalid decision, GAME OVER!")

        elif scenario == "HIDE": #DECISION MATCH -> HIDE
            scenario = input("It seems that the bear didn't see you. You see a cavern where you could spend the night. Do you want the WAIT there until dawn or EXPLORE?: ").upper()
            print()

            while scenario != "WAIT" and scenario != "EXPLORE":
                scenario = input("Wrong answer! Do you WAIT or EXPLORE?: ").upper()

            if scenario == "WAIT": #DECISION MATCH -> HIDE -> WAIT
                print("You slept in the cavern. You see the dawn, it's time to go home... You survived!") #END 4

            elif scenario == "EXPLORE": #DECISION MATCH -> HIDE -> EXPLORE
                print("The bear wasn't that far. He caugth you. You died") #END 5
            
            else: 
                print("Invalid decision, GAME OVER!")
        else: 
            print("Invalid decision, GAME OVER!")

elif scenario == "FLASHLIGHT": #DECISION FLASHLIGHT
        scenario = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?: ").upper()
        print()

        while scenario != "LOOK" and scenario != "FOLLOW":
            scenario = input("Wrong answer! Do you LOOK or FOLLOW?: ").upper() 

        if scenario == "LOOK": #DECISION FLASHLIGHT -> LOOK
            scenario = input("You went to check that noise and found a dead rabbit near a trap, probably someone is hunting nearby. You hear a voice yeeling 'Hey don't move!'. Do you want to RUN or CHECK the voice?: ").upper()
            print()

            while scenario != "RUN" and scenario != "CHECK":
                scenario = input("Wrong answer! Do you RUN or CHECK?: ").upper()
            
            if scenario == "RUN": #DECISION FLASHLIGHT -> LOOK -> RUN
                print("You started running. It seems that someone was hunting indeed. You stepped on a bear trap. You died") #END 6

            elif scenario == "CHECK": #DECISION FLASHLIGHT -> LOOK -> CHECK
                print("It's Adam, one of your frinds! He is happy to find you and He takes you to his house nearby. You spent the night there. It's time to go home... You survived!") #END 7
           
            else: 
                print("Invalid decision, GAME OVER!")
    
        elif scenario == "FOLLOW": #DECISION FLASHLIGHT -> FOLLOW
            scenario = input("You followed the path. You see a small old house in the distance. Do you want to ENTER the house or EXPLORE the forest?: ").upper()
            print()

            while scenario != "ENTER" and scenario != "EXPLORE":
                scenario = input("Wrong answer! Do you ENTER or EXPLORE?: ").upper()  
            
            if scenario == "ENTER": #DECISION FLASHLIGHT -> FOLLOW -> ENTER
                print("You see hunting tools and clothes, probalby someone is hunting nearby. You spent the night there. It's time to go home... You survived!") #END 8

            elif scenario == "EXPLORE": #DECISION FLASHLIGHT -> FOLLOW -> EXPLORE
                print("You didn't find anything relevant. The night is dangerous and there are many wild animals. As you were walking you felt a bite on your ankle. It was a Cobra, it's too late for you. You died") #END 9
            
            else:
                print("Invalid decision, GAME OVER!")
        
        else: 
            print("Invalid decision, GAME OVER!")
else: 
    print("Invalid decision, GAME OVER!")

#END OF GAME
print("------------------------------------------------")
print("End of the game, thanks for playing! :)")



        
        

