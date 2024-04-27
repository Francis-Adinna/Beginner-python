import os

"""
●	Build a quiz game, Ask the user questions and check if the users answer is same your answer
"""
print("Welcome to The quiz game! \nWe have three sections in this quiz game.")
print(" 1. Enter your name.\n 2. Choose the section you want to participate in. \n 3. Answer the questions to your best knowledge. \n 4. Note when choosing your answer select the letter in front of your chioce, like a, b, c, d \n 5. After playing your result will show. \nENJOY THE RIDE!!")


player_name = input("Name: ")
game_starts = True
print()


while game_starts:
    quiz_chioce = input("Type in the quiz game you want to participate in, Entertainment, History, Bible: ")
    quiz_chioce = quiz_chioce.title()
    if quiz_chioce == "Entertainment":
        print("1. Which actor portrayed the iconic character, James Bond, in the film 'Casino Royale?\na) Pierce Brosnan \nb) Daniel Craig \nc) Roger Moore \nd) Sean Connery")
        ent_first_ans = input("Your answer: ")
        ent_first_ans = ent_first_ans.lower()
        ent_correct1 = 0
        ent_wrong1 = 0
        print()
        if ent_first_ans == "b":
            print("⭐CORRECT⭐")
            ent_correct1 = +1
            
        else:
            print("❌Buzz!! Wrong!!❌")
            ent_wrong1 = +1   
        print()
        print("2. Who won the FIFA Men's world cup in 2018?\na) Germany\nb) Nigeria\nc) France\nd) Brazil")
        ent_second_ans = input("Your answer: ")
        ent_second_ans = ent_second_ans.lower()
        ent_correct2 = 0
        ent_wrong2 = 0
        print()
        if ent_second_ans == "c":
            print("⭐CORRECT⭐")
            ent_correct2 = +1
            
        else:
            print("❌Buzz!! Wrong!!❌")
            ent_wrong2 = +1
        print()
        print("3. Which album is the best selling of all time?\na)'Thriller' by Michael Jackson\nb)'Back in Black' by AC/DC\nc) 'The dark side of the moon' by Pink Floyd\nd) 'Abbey Road' by The Beatles")
        ent_third_ans = input("Your answer: ")
        ent_third_ans = ent_third_ans.lower()
        ent_correct3 = 0
        ent_wrong3 = 0
        print()
        if ent_third_ans == "a":
            print("⭐CORRECT⭐")
            ent_correct3 = +1
            
        else:
            print("❌Buzz!! Wrong!!❌")
            ent_wrong3 = +1
        print()
        print("4. Who is the highest-scoring NBA player of all time?\na) LeBron James\nb) Kobe Bryant\nc) Michael Jordon\nd) Kareem Abdul-Jabber ")
        ent_fourth_ans = input("Your answer: ")
        ent_fourth_ans = ent_fourth_ans.lower()
        ent_correct4 = 0
        ent_wrong4 = 0
        print()
        if ent_fourth_ans == "d":
            print("⭐CORRECT⭐")
            ent_correct4 = +1
            
        else:
            print("❌Buzz!! Wrong!!❌")
            ent_wrong4 = +1
        print()
        ent_correct = ent_correct1 + ent_correct2 + ent_correct3 + ent_correct4
        ent_wrong = ent_wrong1 + ent_wrong2 + ent_wrong3 + ent_wrong4 
        print(f"Hello {player_name}!\nYou got {ent_correct}answers correctly, and {ent_wrong} answers wrongly.")
        decision = input("Do you wish to play again? (Yes/No): ")
        if decision.lower() == "yes":
            decision = game_starts
            os.system('cls')

        elif decision.lower() == 'No':
            print("Thank you for playing")
            os.system('cls')
            break

    elif quiz_chioce == "History":
        print("1. What year did Christopher Columbus first reach the Americas?\na) 1492 \nb) 1520 \nc) 1555 \nd) 1607")
        his_first_ans = input("Your answer: ")
        his_first_ans = his_first_ans.lower()
        his_correct1 = 0
        his_wrong1 = 0
        print()
        if his_first_ans == "a":
            print("⭐CORRECT⭐")
            his_correct1 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            his_wrong1 = +1
        print()
        print("2. Who was the first President of the United states?\na) Thomas Jefferson \nb) Abraham Lincoln \nc) George Washington \nd) John Adams")
        his_second_ans = input("Your answer: ")
        his_second_ans = his_second_ans.lower()
        his_correct2 = 0
        his_wrong2 = 0
        print()
        if his_second_ans == "c":
            print("⭐CORRECT⭐")
            his_correct2 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            his_wrong2 = +1
        print()
        print("3. The Magna Carta, signed in 1215, is considered a cornerstone of modern what?\na) Democracy \nb) Aechitecture \nc) Medicine \nd) Literature")
        his_third_ans = input("Your answer: ")
        his_third_ans = his_third_ans.lower()
        his_correct3 = 0
        his_wrong3 = 0
        print()
        if his_third_ans == "a":
            print("⭐CORRECT⭐")
            his_correct3 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            his_wrong3 = +1
        print()
        print("4. Which ancient civilization built the pyramids at Giza? \na) Roman \nb) Egyptian \nc) Greek \nd) Mesopotamian")
        his_fourth_ans = input("Your answer: ")
        his_fourth_ans = his_fourth_ans.lower()
        his_correct4 = 0
        his_wrong4 = 0
        print()
        if his_fourth_ans == "b":
            print("⭐CORRECT⭐")
            his_correct4 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            his_wrong4 = +1
        print()
        his_correct = his_correct1 + his_correct2 + his_correct3 + his_correct4
        his_wrong = his_wrong1 + his_wrong2 + his_wrong3 + his_wrong4
        print(f"Hello {player_name}!\nYou got {his_correct}answers correctly, and {his_wrong} answers wrongly.")
        decision = input("Do you wish to play again? (Yes/No): ")
        if decision.lower() == "yes":
            decision = game_starts
            os.system('cls')
        elif decision.lower() == 'no':
            print("Thank you for playing")
            os.system('cls')
            break

    elif quiz_chioce == "Bible":
        print("1. Who was the oldest man in the bible?\na) Abraham \nb) Noah \nc) Methuselah \nd) Adam")
        bib_first_ans = input("Your answer: ")
        bib_first_ans = bib_first_ans.lower()
        bib_correct1 = 0
        bib_wrong1 = 0
        print()
        if bib_first_ans == "c":
            print("⭐CORRECT⭐")
            bib_correct1 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            bib_wrong1 = +1
        print()
        print("2. Who was the first king of Israel?\na) Saul \nb) David \nc) Solomon \nd) Moses")
        bib_second_ans = input("Your answer: ")
        bib_second_ans = bib_second_ans.lower()
        bib_correct2 = 0
        bib_wrong2 = 0
        print()
        if bib_second_ans == "a":
            print("⭐CORRECT⭐")
            bib_correct2 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            bib_wrong2 = +1
        print()
        print("3. Which prophet is known as the weeping prophet?\na) Jeremiah \nb) Isaiah \nc) Ezekiel \nd) Daniel")
        bib_third_ans = input("Your answer: ")
        bib_third_ans = bib_third_ans.lower()
        bib_correct3 = 0
        bib_wrong3 = 0
        print()
        if bib_third_ans == "a":
            print("⭐CORRECT⭐")
            bib_correct3 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            bib_wrong3 = +1
        print()
        print("4. What is the shortest verse in the bible?\na) John 3:16 \nb) Genesis 1:1 \nc) Exodus 20:3 \nd) John 11:35")
        bib_fourth_ans = input("Your answer: ")
        bib_fourth_ans = bib_fourth_ans.lower()
        bib_correct4 = 0
        bib_wrong4 = 0
        print()
        if bib_fourth_ans == "d":
            print("⭐CORRECT⭐")
            bib_correct4 = +1
        else:
            print("❌Buzz!! Wrong!!❌")
            bib_wrong4 = +1
        print()
        bib_correct = bib_correct1 + bib_correct2 + bib_correct3 + bib_correct4
        bib_wrong = bib_wrong1 + bib_wrong2 + bib_wrong3 + bib_wrong4
        print(f"Hello {player_name}!\nYou got {bib_correct}answers correctly, and {bib_wrong} answers wrongly.")
        decision = input("Do you wish to play again? (Yes/No): ")
        if decision.lower() == "yes":
            decision = game_starts
            os.system('cls')
        elif decision.lower() == 'no':
            print("Thank you for playing")
            os.system('cls')
            break

    else:
        print(f"Hi {player_name}!\nKindly choose correct quiz game.\nThank you.")
        decision = input("Do you wish to play again? (Yes/No): ")
        if decision.lower() == "yes":
            decision = game_starts
            os.system('cls')
        elif decision.lower() == 'no':
            print("Thank you for playing")
            os.system('cls')
            break

        