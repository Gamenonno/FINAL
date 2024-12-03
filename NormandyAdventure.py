import random
import time
Name_Rank = [ "Pvt.","Cpl.", "Sgt.", "Spl." ]
Name_First = ["John", "Chris", "Leeroy", "Charles", "Kenny", "Jimmy", "Harper", "Gordon", "David", "Martin", "Elijah", "William", "Sebastian", "Jack", "Michael", "Leo", "Hudson"]
Name_Last = ["Smith", "Freeman", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Lopez", "Taylor", "Moore", "Anderson", "Lee", "Clark", "Carter", "Wright"]
Name_Role = ["Rifleman", "Scout","Machine gunner","Assitant Machine gunner", "Medic", "Combat Engineer", "Assitant Squad leader","Squad leader"]
Name_Division = ["1st Infantry", "29th Infantry"]
print("All answers must be in lowercase")
time.sleep(1)
print("You are", random.choice(Name_Rank) + " " + random.choice(Name_First) + " " + random.choice(Name_Last), "the " + random.choice(Name_Role) + " of the " + random.choice(Name_Division) + ".")
time.sleep(2)
print("You have been loaded onto a landingcraft, and are bound for normandy.")
time.sleep(1)
print("As you draw near, your commander orders you to get off the beach as soon as possible")
print("There is a hard crash as you hit the beach, the door of the landing craft swings open, and you are ordered to run.")
print("You are ordered to run, but your terrified mind tells you to hide in the landing craft.")
time.sleep(2)
print(" ")
print("run or hide?")

FirstChoice = input("> ")

if(FirstChoice == "hide"):
    print("You hide in the back of the landing craft, as the other infantry run off, you find that you are alone for a moment, and an aterllery shell blasts the landing craft. You were never recovered.")
    print("Mission Failed.")
    
elif(FirstChoice == "run"):
    print("You run like hell, you plunge into the water. You are weighed down by the weight of your pack, but it is full of useful supplies, drop the pack? (yes or no)")
    
    SecondChoice = input("> ")
    
    if(SecondChoice == "no"):
        print("The weight of your entire kit and the added weight of the water was too much, you were dragged under with a dozen other soldiers, machine gun rounds hit you while underwater, sealing your fate.")
        print("Mission Failed.")
        
    elif(SecondChoice == "yes"):
        print("You quickly shake the heavy bag off your back, and watch it sink to the depths. You pull yourself to the surface of the water and you see other soldiers struggle in the water, but if you stop now you will surely be shot, so you contuine to run..")
        time.sleep(3)
        print(" ")
        print("You take cover behind a tank trap, You are breathing heavy as the sounds of gunshots and explosions fill your ears, you look to your left and see an M4 sherman tank rolling its way to the enemy, some of your fellow infatry and using it as mobile cover.")
        time.sleep(2)
        print(" ")
        print("Looking to your right, you see a friendly combat engineer setting a mortar, If you help him you could destroy an enemy bunker, and allow your fellow soldiers to gain ground.")
        time.sleep(1.5)
        print(" ")
        print("left(Push with the tank) or right(Help the Combat Engineer)?")
        
        
        
        LeftOrRight = input("> ")
        if(LeftOrRight == "right"):
            print("You sprint to the Combat Engineer, and begin to help him set up, however an enemy shock trooper has spotted you, but he is alone.")
            time.sleep(2)
            print("Do you shoot the trooper(shoot), or demand him to surrdener?(demand)")
            
            RightC1 = input(">")
            if(RightC1 == "shoot"):
                time.sleep(1.5)
                print("You raise your weapon and fire, there is no time for hesitation.")
                time.sleep(2.5)
                print("The Combat Engineer finishes his mortar set up, and he aims the mortar, under his commands, you load and watch the mortar rounds blow up the enemy poisiton.")
                time.sleep(2.5)
                print("Another squad of infantry flood infront of you, you contuine to support the Combat Engineer, until you have recived news that the enemy lines have been breached, with this puncture you helped created, you played a role in the victory.")
                time.sleep(2)
                print("Mission Success!")
            elif(RightC1 == "demand"):
                print("You demand for the shock trooper to drop his weapon, and point your rifle.")
                time.sleep(1.5)
                print("The Soldier doesnt understand you at first, but after He sees your rifle not being fired. He raises his arms and falls to his knees.")
                time.sleep(1)
                print("You didn't notice the Combat Engineer finish setting up the mortar, nor were you able to stop him from taking his weapon and killing the surrendering trooper.")
                time.sleep(1.5)
                print("The horrors of war will haunt you until the end of your days, but you dont have time to think about what just happened..")
                time.sleep(1)
                print("The Combat Engineer called you over to load the mortar after he aimed it.")
                time.sleep(1)
                print("You load the mortar,and watch the rounds blow up the enemy poisiton.")
                time.sleep(1)
                print("Another squad of infantry flood infront of you, you contuine to support the Combat Engineer, until you have recived news that the enemy lines have been breached, with this puncture you helped created, you played a role in the victory.")
                time.sleep(2)
                print("Mission Success!")
            
            else:
                print("Your choices are 'shoot' or 'demand'.")
            
            

        elif(LeftOrRight == "left"):
            print("You rush over to the tank, you hear the sounds of rounds bouncing off the armor of the tank. The tanks rolls up the beach, and you notice it has had it's tracks destroyed by an explosion. You see the crew climb out of the tank to fix it, but they are only armed with handguns.")
            print("defend tankers or attempt to fix tracks?")
           
            LeftC1 = input("> ")
            if(LeftC1 == "attempt to fix tracks"):
                time.sleep(1)
                print("You run over to the tracks, you realize you have no knowldege or tools of tanks, and because you exposed yourself, you have been shot down by a machine gun.")
                print("Mission Failed.")
                
            elif(LeftC1 == "defend tankers"):
                print("You risk your own life for your brothers in arms, You lift your service weapon and begin firing at the enemy machine gunner that had targeted the vulnerable tankers.")
                time.sleep(2)
                print("You wound the enemy machine gunner, Just as another enemy was about to mount the machine gun, the gunner of the tank noticed your actions, and turned the tank's turret to the bunker, destroying it, and all the enemies inside.")
                time.sleep(2.5)
                print("With the tank repaired, you keep pushing forward, you see that the sand is turning to grass, and that the enemy are now attempting to scramble a defense.")
                time.sleep(1.5)
                print("You made it.")
                time.sleep(1)
                print("Mission success!")
            
                        
            else:
                print("The two choices are 'attempt to fix tracks' or 'defend tankers'.")
                
        else:
            print("Your choices are 'left' or 'right'.")
        
            
    
    else:
        print("The choices are 'yes' or 'no'.")
    
else:
    print("Your choices are either 'run' or 'hide'")