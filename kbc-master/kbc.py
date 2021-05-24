from questions import QUESTIONS

def isAnswerCorrect(question, answer):
    
    return True if question['answer']==answer else False


def lifeLine(ques):
    correctOption = int(ques['answer'])
    delopt1 = 0
    delopt2 = 0

    if correctOption == 1:
        delopt1 = 3
        delopt2 = 4
    elif correctOption == 2:
        delopt1 = 3
        delopt2 = 4
    elif correctOption == 3:
        delopt1 = 1
        delopt2 = 2
    else:
        delopt1 = 1
        delopt2 = 2

    del ques["option"+str(delopt1)]
    del ques["option"+str(delopt2)]

    return ques,correctOption


def kbc():
    print("Please enter your name")
    username = input().strip()
    print("Welcome " + username + "! Let's start Kaun Banega Crorepati!")
    roundno = 0
    prize = 0
    minPrize = 0
    lifeline = 1
    while(roundno<=14):
        print(f'\tQuestion : {QUESTIONS[roundno]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[roundno]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[roundno]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[roundno]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[roundno]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        if ans.lower()=="lifeline":
            if lifeline==1:
                lifeline = 0
                q,c = lifeLine(QUESTIONS[roundno])
                print("Two incorrect options have been deleted, the remaining options are: ")
                print(f'\tQuestion : {QUESTIONS[roundno]["name"]}')
                if c==1 or c==2:
                    print(f'\t\t\tOption 1: {QUESTIONS[roundno]["option1"]}')
                    print(f'\t\t\tOption 2: {QUESTIONS[roundno]["option2"]}')
                    ans = input("Your choice 1/2 : ")
                else:
                    print(f'\t\t\tOption 3: {QUESTIONS[roundno]["option3"]}')
                    print(f'\t\t\tOption 4: {QUESTIONS[roundno]["option4"]}')
                    ans = input("Your choice 3/4 : ")
            else:
                print("\t\t\tSorry you have already used your lifeline")
                continue

        elif ans == "quit":
            finalans = input("Are you sure? y/n: ")
            if finalans.lower() == "y":
                print("You recieve "+ str(prize) + " Rupees, Congratulations!")
                break
            else:
                continue

        if isAnswerCorrect(QUESTIONS[roundno], int(ans) ):

            print('\nCorrect !')
            prize = QUESTIONS[roundno]["money"]
            if roundno!=14:
                print("You have earned " + str(prize) + " rupees till now")
            else:
                print("\t\t\tCongratulations " + username + " you have won Kaun Banega Crorepati!!!")
                break
            roundno += 1
            if roundno==5:
                minPrize = 10000
            elif roundno==10:
                minPrize = 320000

        elif isAnswerCorrect(QUESTIONS[roundno], int(ans) ) == False:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print("You will recieve " + str(minPrize) + " rupees!")
            break



    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

kbc()
