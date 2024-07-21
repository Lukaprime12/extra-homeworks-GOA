def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print('--------------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('enter A,B,C or D: ')
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guess)





def check_answer(answer,guess):
    if answer != guess:
        print('WRONG!')
        return 0
    else:
        print('CORRECT!')
        return 1




def display_score(correct_guesses, guesses):
    print('--------------------------------')
    print('RESULTS!')
    print('--------------------------------')
    print('Guesses', end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = (correct_guesses//len(questions)*100)
    print('you score is ' + str(score) + '%')



def play_again():
    response = input('Do you want to play again? (YES or NO): ')
    response = response.upper()
    if response == 'YES':
        return True
    else:
        return False




questions = {
    'who created python?':'D',
    'what year was python created?':'B',
    'is python created by me?':'C',
    'is Goa best Academy?' : 'A'
}

options = [['A) Badri Tabatadze', 'B) Elon Musk', 'C) Giorgi Sanikidze', 'D) Guido Van Rossum'],
           ['A) Yesterday', 'B) 1991','C) right now', 'D) 1977' ],
           ['A) Yes', 'B) of course', 'C) No', 'D) you are planning'],
           ['A) Yes!!!', 'B) what is goa?', 'C) No', 'D) Nope']]


new_game()


while play_again():
    new_game()


print('BYE!')