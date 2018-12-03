import random #Allows for me to use the random function throughout my code
'''The gameshow function is the function that controls the entire code for the whole game. It is a number fo functions\n
put together that allows for the program to run. By grouping these functions together it allows for me to write \n
less code for each category, while being more efficient. '''

def gameshow(cat, score, read, index): #defines the gameshow and has the parimeters the game must run through
    def evenrandom(a): #a function that can be called on later that only lets you select even lines
        x = 0 #gives x an original value of 0
        while x % 2 == 0: #only can pick the lines that will have no remainder if it is divided by 2
            x = random.randint(0, a) #will select a random line that can be divided by 2
        return x #stores the value of x

    yscore = score #sets your score equal to zero before you start the game.

    questions_asked = [] #is a blank list that allows for you to add the questions you have asked to the list

    def any_line(catergory1):
        pick_line = open(catergory1).read().splitlines() #a random line will be picked, read and then the rest will be ignored do to the splitlines function
        index = evenrandom(len(pick_line) - 1)
        return [pick_line[index]], pick_line[index + 1] #stores the value of the line it selects and teh line below which will contain the answer

    for x in range(len(cat) - 1):
        holder = any_line(cat) #the holder value is equal to a random line selected by the any_line function
        question = holder[0] #the question is then then equal to that holder and the holder will get a set value of 0
        while question in questions_asked:#looks to see if the question was already asked
            holder = any_line(cat) #if it was already asked it will select a new question from the text file
            question = holder[0] #will store that holder as the new value of the question
        questions_asked.append(question) #appends the questions asked to a list so it can only be asked once
        answer = holder[1] #The answer is then the line below the question, since the holder value increases by 1
        print(question[0]) #prints the question, that was stored in the holder value
        user_answer = input("What is your answer").lower() #asks for the user to input an answer and makes there answer lowercase
        if user_answer == answer: #determines if the user answer is the same as the correct answer
            print("Congratulations you have received 100 points") #tells the user what they recieved for answering the questions right
            yscore = yscore + 100 #adds 100 points to your score is the question is right
        else:
            print("I am sorry that is incorrect. Better luck with the next question.") #tells the user they got the answer wrong
            yscore = yscore + 0 #adds 0 points to your score if the question is wrong

    l = open("usernames.txt", "r")  #will then open the file and read to see if that username already exists
    l.seek(0)
    read1 = l.readlines()
    read1[index] = (str(yscore))
    q = open("usernames.txt", "w")

    q.writelines(read1)
    q.close()
    print("Your total score is " + (str(yscore))) #will print your final score at the end of the game


'''This part here will introduce the game, define the rules and how the point system works. It acts as an introduction\n
to my game. Without it users would be lost. It will then tell you what all of the category's are, so you can \n
 choose which one you would like to play'''

print("Welcome to Jeopardy. There are four categories. Category 1 iss ports teams, category 2 is the most popular\n"
      "boys names, category 3 is the most popular girls names, and category 4 is the most popular fish.")
print("    ") #Spacing for visual purposes
print("Before we begin, or if you are a returning player lets recap the rules. You get to select a category and \n"
      "will be asked 10 questions in a random order. for each correct answer you will receive points. The aim \n"
      "is to get as many points as possible. Your results will be ranked overall and in your just your category. \n"
      "Remember different questions are worth different amounts of points")
print("    ") #Spacing for visual purposes
print("If you are a retuning user when you enter your username it will give you the option to continue your \n"
      "previous quiz, or start a new one. Now lets start playing jeopardy!")
print("    ") #Spacing for visual purposes
abc = 0 #is a set value for abc
while abc == 0: #allows you to run the game as long as abc = 0
    usernames = input("what is your username?") #asks the user to provide the game with a username
    l = open("usernames.txt", "r")  #will then open the file and read to see if that username already exists
    read = l.readlines()

    '''This part here will read all of the lines 1 by 1. If the username is found to be in the file, the program will \n
    then go down one more line to determine the previous value of the score. Once that is determined it will print \n
    out your old score to tell you what you previously had. You can then pick to continue or start again. '''

    for x in range(len(read)-1):
        if usernames+"\n" == read[x]: #try to find the username in the file
            score = str(read[x + 1]) #will pick the line below the username and define it as the score
            print(score) #will print the score if there is one
            cont = input("Would you like to continue your previous game.") #allows you continue your previous game or restart a new one
            if cont == "no" or cont == "No": #if the answer is no you will restart
                score = 0 #The game will reset your score to 0
            category = input("hello " + usernames + " what category would you like to select today?") #Asks you to input what category you would like to select
            if category == "category 1" or category == "1":#determinnes what category the user selected
                gameshow("catergory 1", score, read, x + 1) #calls on the gameshow function and runs it through the parameters
            elif category == "category 2" or category == "2":#determinnes what category the user selected
                gameshow("catergory 2", score, read, x + 1) #calls on the gameshow function and runs it through the parameters
            elif category == "category 3" or category == "3": #determinnes what category the user selected
                gameshow("catergory 3", score, read, x + 1) #calls on the gameshow function and runs it through the parameters
            elif category == "category 4" or category == "4":#determinnes what category the user selected
                gameshow("catergory 4", score, read, x + 1) #calls on the gameshow function and runs it through the parameters


                ''' Please note there is a more detailed explanation on the parameters at the bottom.'''

        elif x == len(read)-2:
            f = open("usernames.txt", "a") #if the usernames is not in the file it will then add it to the file.
            f.write("\n" + usernames+ "\n"+"0") #does the same thing as the line above
            f.close()
            category = input("hello " + usernames + " what category would you like to select today?") #Allows the user to select what catergory they would like to play
            if category == "category 1" or category == "1": #determinnes what category the user selected
                gameshow("catergory 1", 0, read, x+3) #calls on the gameshow function and runs it through the parameters
            elif category == "category 2" or category == "2": #determinnes what category the user selected
                gameshow("catergory 2", 0, read, x+3) #calls on the gameshow function and runs it through the parameters
            elif category == "category 3" or category == "3": #determinnes what category the user selected
                gameshow("catergory 3", 0, read, x+3) #calls on the gameshow function and runs it through the parameters
            elif category == "category 4" or category == "4": #determinnes what category the user selected
                gameshow("catergory 4", 0, read, x+3) #calls on the gameshow function and runs it through the parameters
    cont = input("would you like to play again").lower() #asks if you would like to play the game again
    if cont == "no": #is the answer a user must answer to break the game
        abc = abc + 1 #adds 1 to abc, breaking the game, making it no longer have a value of 0
        print("Thank you for playing the game I hope you will come back and play again soon. the current list of high scores is")
        l = open("usernames.txt", "r") #opens the textfile
        scores = [] #a blank list the text file can be added to.
        lines = l.readlines() #will read the lines in the text file
        for x in range(0, len(lines), 2): #selects the lines in groups of 2
            scores.append(lines[x].strip() + " " + lines[x + 1].strip())#appends the text file to the list and deltes the /n
        scores = sorted(scores) #sorts the scores alphabetically
        print(scores) #prints the list by alphabetical order
    else:
        abc = abc + 0 #has abc add no value allowing for you to continue
        print("before we continue lets look to see how you compare to the other high scores")
        l = open("usernames.txt", "r") #opens the textfile
        scores = [] #a blank list the text file can be added to.
        lines = l.readlines() #will read the lines in the textfile
        for x in range(0, len(lines), 2): #selects the lines in groups of 2
            scores.append(lines[x].strip() + " " + lines[x + 1].strip()) #appends the text file to the list and deltes the /n
        scores = sorted(scores) #sorts the scores alphabetically
        print(scores) #prints the list by alphabetical order


    ''' The perimeters include 4 things. The first parameter decided what text file it will select the questions \n
    from. The second parameter is the score. In this case since you are a new user your score is automatically set to 0. \n
    The next two parts work together. They will write your score in the line below the username, read it and then print \n
    it eventually when that is called upon in the function. '''






