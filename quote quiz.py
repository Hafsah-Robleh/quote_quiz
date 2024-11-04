# A quote quiz created from python
# a program that asks question and provides a quote that would resonate

print("Hey there! Welcome to the quote quiz. I'm gonna ask you 5 questions and based on each of your answers, I'll give you a quote I think will resonate, I hope you enjoy ")
name = input("Whats your name? ") 
print("Welcome " + name + " Lets begin!")
quote1 = "Life shrinks or expands in proportion to one’s courage. ― Anaïs Nin"
quote2 = """ By believing passionately in something that still does not exist, we create it. The nonexistent is whatever we have not sufficiently desired. ― Franz Kafka """
quote3 = "Don't bend; don't water it down; don't try to make it logical; don't edit your own soul according to the fashion. Rather, follow your most intense obsessions mercilessly. ― Franz Kafka"
quote4 = "It is better to be hated for what you are than to be loved for what you are not. ― André Gide"
quote5 = "You do not just wake up and become the butterfly. Growth is a process ― Rupi Kaur"


values = print(input("Which one do you value most? A. Peace , B. Resilience, C. Purpose, D. Inspiration "))
if values == "A": 
    print(quote1)
# Change if statement to while loop 
elif values == "B":
    print(quote2)
elif values == "C":
    print(quote3)
elif values == "D":
    print(quote4)
else:
    print("Invalid choice, please capitalize your letter choice")


approach = print(input("how do you aproach new opppurtunities? A. Go right in, B. Carefully consider options, C. I wait to see if its right for me "))

success = print(input("How do you define success? A. Achieving personal goals , B. Feeling contetn and fulfilled, C. Making a positive impact, D. Being true to myself "))
fear = print(input("What do you believe is holding you back most? A. Fear of failure, B. Lack of motivation, C. Self- doubt "))




