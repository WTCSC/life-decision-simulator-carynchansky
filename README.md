## __Overview__

**Life Decision Simulator** is a simple, text-based Python game that asks the player a series of yes/no or single-letter questions to “guess” aspects of their working life.
Your answers guide the program through different branches until it makes a playful comment and ends.

## __How It Works__

1. The game greets the player and immediately starts asking questions.

2. Your responses (Y/N or first letters like C, M, B) determine the next question or the game’s ending.

3. Invalid input triggers a reminder to “try again,” keeping the loop running until a valid answer is given or the game finishes.

## __Requirements__

* Python 3.x

No external libraries are needed—just the built-in input() and print() functions.

## __How to Run__

1. Open a terminal or command prompt in the script’s directory. 
2. Create a clone of a git hub repository: 
    
    __git clone link-to-repository__ 
3. Open a repository:

    __cd life-decision-simulator__
4. Run:

    __python3 decision_tree.py__

5. Follow the on-screen prompts.

## __Notes__

All inputs are converted to uppercase to simplify comparisons.

Any response outside the expected letters results in an “Invalid input” prompt and restarts that question.

