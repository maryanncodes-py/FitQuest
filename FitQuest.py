#Maryann Pike
#FitQuest

import time

playAgain = "yes"

while playAgain == "yes":

    print("\n===================================")
    print("      FITQUEST: FITNESS ADVENTURE")
    print("===================================\n")

    print("Instructions:")
    print("Answer the five questions to personalize your story.")
    print("When making decisions, type 'yes' or 'no'.")
    print("Your choices will determine the ending.\n")

    time.sleep(1)

    # QUESTION 1
    playerName = ""
    while playerName == "":
        playerName = input("What is your name, hero of this fitness journey? ").strip()

    # QUESTION 2
    workoutType = ""
    while workoutType not in ["cardio", "strength", "yoga"]:
        workoutType = input("What’s your favorite type of workout? (cardio/strength/yoga): ").lower()

    # QUESTION 3
    favoriteSnack = ""
    while favoriteSnack == "":
        favoriteSnack = input("What’s your favorite post-workout snack? ").strip()

    # QUESTION 4
    fitnessGoal = ""
    while fitnessGoal not in ["endurance", "strength", "flexibility"]:
        fitnessGoal = input("What’s your biggest fitness goal? (endurance/strength/flexibility): ").lower()

    # QUESTION 5
    challengeChoice = ""
    while challengeChoice not in ["early run", "hiit", "hike"]:
        challengeChoice = input("Which challenge are you ready to try today? (early run/HIIT/hike): ").lower()

    print("\n===================================")
    print("         YOUR STORY BEGINS")
    print("===================================\n")

    time.sleep(1)

    print(f"{playerName} wakes up early in the morning.")
    time.sleep(1)

    print("A yoga mat rests on the floor, a water bottle sits nearby.")
    time.sleep(1)

    print("Running shoes wait by the door.")
    time.sleep(1)

    print(f"Today {playerName} feels ready for a {workoutType} workout.")
    time.sleep(1)

    print(f"The goal today is improving {fitnessGoal}.")
    time.sleep(1)

    print(f"Maybe even attempting a {challengeChoice} challenge.\n")
    time.sleep(1)

    # DECISION 1
    decision1 = ""
    while decision1 not in ["yes", "no"]:
        decision1 = input("Do you want to head to the gym for your workout? (yes/no): ").lower()

    if decision1 == "yes":
        print("\nYou grab your gear and head to the gym.")
        print("The energy inside the gym is motivating!")
    else:
        print("\nYou decide to stay home.")
        print("Your living room becomes your training ground.")

    time.sleep(2)

    # DECISION 2
    print("\nHalfway through the workout, a challenge appears.")
    print("The treadmill is busy... or your workout space feels cramped.")

    decision2 = ""
    while decision2 not in ["yes", "no"]:
        decision2 = input("Do you push through the obstacle anyway? (yes/no): ").lower()

    if decision2 == "yes":
        print("\nYou push harder and keep going.")
        print("Your determination grows stronger.")
    else:
        print("\nYou adjust your workout.")
        print("Balance and smart decisions keep you moving forward.")

    time.sleep(2)

    print("\nCalculating your fitness outcome...")
    time.sleep(2)

    print("\n===================================")
    print("            FINAL OUTCOME")
    print("===================================\n")

    # ENDINGS
    if decision1 == "yes" and decision2 == "yes":
        print(f"{playerName} chose the toughest path today.")
        print("The workout was intense, but determination paid off.")
        print("Confidence is sky high and the progress feels real.")
        print(f"To celebrate, {playerName} enjoys a well-earned {favoriteSnack}.")

    elif decision1 == "no" and decision2 == "no":
        print(f"{playerName} chose balance and mindfulness.")
        print("The workout stayed steady and controlled.")
        print("Listening to the body is part of a strong fitness journey.")

    else:
        print(f"{playerName} balanced determination with smart choices.")
        print("The workout was productive and progress was made.")
        print(f"After finishing, {playerName} relaxes with a {favoriteSnack}.")

    print("\nGreat work today! Your fitness journey continues.\n")

    # PLAY AGAIN
    playAgain = ""
    while playAgain not in ["yes", "no"]:
        playAgain = input("Would you like to play again? (yes/no): ").lower()

print("\nThanks for playing FitQuest!")
print("Stay active and keep chasing your goals!")