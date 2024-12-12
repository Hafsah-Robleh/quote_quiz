# A quote quiz created from python
# a program that asks question and provides a quote that would resonate

def start_game(): 
        print("Hey there! Welcome to the quote quiz. I'm gonna ask you 5 questions and based on each of your answers, I'll give you a quote I think will resonate, I hope you enjoy ")
        name = input("Whats your name? ") 
        print("Welcome " + name + " Lets begin!\n")

        quote1 = "Life shrinks or expands in proportion to one’s courage. ― Anaïs Nin"
        quote2 = """ By believing passionately in something that still does not exist, we create it. The nonexistent is whatever we have not sufficiently desired. ― Franz Kafka """
        quote3 = "Don't bend; don't water it down; don't try to make it logical; don't edit your own soul according to the fashion. Rather, follow your most intense obsessions mercilessly. ― Franz Kafka"
        quote4 = "It is better to be hated for what you are than to be loved for what you are not. ― André Gide"
        quote5 = "You do not just wake up and become the butterfly. Growth is a process ― Rupi Kaur"

        tally = { 
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        }


        questions = [
        "Which one do you value most? A. Peace , B. Resilience, C. Purpose, D. Inspiration ",
        "how do you aproach new opppurtunities? A. Go right in, B. Carefully consider options, C. I wait to see if its right for me ",
        "How do you define success? A. Achieving personal goals , B. Feeling content and fulfilled, C. Making a positive impact, D. Being true to myself ",
        ]

        for question in questions:
            while True:
                answer= input(question).strip().upper()
                if answer in tally:  
                    tally[answer] += 1
                    break
                else:
                    print("Invalid choice, please choose A,B,C or D")
    
    

        result = max (tally, key = tally.get)
        if result == "A":
            print(quote1)
        elif result == "B": 
            print(quote2) 
        elif result == "C":
         print(quote3)       
        elif result == "D":
            print(quote4)               
        else: 
            print("Wrong input be for real")  

        play_again = input("Do you want play again? (yes/no)")
        if play_again == "yes":
            start_game()
        elif play_again == "no":
            print ("Thanks for playing!")
        else:
            print("please just write yes or no")
            input("Do you want to play again")

start_game()
