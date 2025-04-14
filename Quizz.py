

total_score = 2
score = 0

def ask_question(question, correct_option):
    print(question)
    while True:
        answer = input('> ').lower()
        if answer in ['a', 'b', 'c']:
            if answer == correct_option:
                print('Correct ✅\n')
                return 1
            else:
                print('Incorrect ❌\n')
                return 0
        else:
            print("Invalid input. Please enter 'a', 'b', or 'c'.")

# Question 1
q1 = '''1) Who wrote the famous play Romeo and Juliet?
a. William Shakespeare
b. Leonardo da Vinci
c. Leonardo Di Caprio'''
score += ask_question(q1, 'a')

# Question 2
q2 = '''2) What is the chemical symbol for Gold?
a. Ag
b. Au
c. Ug'''
score += ask_question(q2, 'b')

print(f'Your score is {score}/{total_score}')
