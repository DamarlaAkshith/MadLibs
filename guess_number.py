import random
def get_range():
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            return start, end
def generate_number(start, end):
    return random.randint(start, end)
def get_guess():
    while True:
            guess = int(input("Guess the number: "))
            return guess
def check_guess(guess, number, hint_used):
    if guess < number:
        hint = f"Your guess is low. "
        if number % guess == 0:
            hint += f"The number is divisible by guess."
        elif number%2 == 0  and not hint_used['even']:
            hint_used['even'] = True
            hint += "Hint: The number is even."
        elif number % 3 == 0 and not hint_used['divisible_by_3']:
            hint_used['divisible_by_3'] = True
            hint += "Hint: The number is divisible by 3."
        elif number % 5 == 0 and not hint_used['divisible_by_5']:
            hint_used['divisible_by_5'] = True
            hint += "Hint: The number is divisible by 5."
        else:
            if abs(guess - number) == 1:
                hint += "You are one away from the number!"
            elif abs(guess - number) == 2:
                hint += "You are two away from the number!"
            elif guess < number - 5:
                hint += f"The number is between {guess} and {number}."
            else:
                hint += "The number is high."
        return hint, hint_used
    elif guess > number:
        hint = f"Your guess is too high. "
        if guess % number == 0:
            hint += f"Your guess is divisible by number."
        elif number%2==0 and not hint_used['even']:
            hint_used['even'] = True
            hint += "Hint: The number is even."
        elif number % 3 == 0 and not hint_used['divisible_by_3']:
            hint_used['divisible_by_3'] = True
            hint += "Hint: The number is divisible by 3."
        elif number % 5 == 0 and not hint_used['divisible_by_5']:
            hint_used['divisible_by_5'] = True
            hint += "Hint: The number is divisible by 5."
        else:
            if abs(guess - number) == 1:
                hint += "You are one away from the number!"
            elif abs(guess - number) == 2:
                hint += "You are two away from the number!"
            elif guess > number + 5:
                hint += f"The number is between {number} and {guess}."
            else:
                hint += "The number is low."
        return hint, hint_used
    else:
        return "Correct", hint_used
def play_game():
    start, end = get_range()
    number = generate_number(start, end)
    print(number)
    score = 100
    hint_used = {'even': False, 'divisible_by_3': False, 'divisible_by_5': False}
    while True:
        guess = get_guess()
        hint, hint_used = check_guess(guess, number, hint_used)
        print(hint)
        score -= 10
        if hint == "Correct":
            print("You win! Your score is", score)
            break
        if score==0:
            print("You chances are over")
            break

play_game()
