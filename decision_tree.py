
print("Welcome to Life Decision Simulator!")
while True:
    work = input("Do you use your pc/laptop for work(Y/N)?: ").upper()
    if work == 'Y':
        job = input("You're working in IT(Y/N)?: ").upper()
        if job == 'Y':
            remote = input("Do you work remotely(Y/N)?: ").upper()
            if remote == "Y":
                print("You're really lucky! I wish i could do that.")
                print("Thanks for playing.")
                break
            elif remote == "N":
                office = input("You're working in the office(Y/N)?: ").upper()
                if office == 'Y':
                    print("Oh man that's may be hard")
                    print("Thanks for playing")
                    break
                elif office == 'N':
                    print("I can't even think where you working")
                    print("Thanks for playing")
                    break
                else:
                    print("Invalid input. Please try again!")
            else:
                print("Invalid input. Please try again!")
        elif job == 'N':
            vehicle = input("How do you get to work(Car/Motorcycle/Bus use first letter of the word)?: ").upper()
            if vehicle == 'C' or 'M' or 'B':
                print("Okay thanks for playing!!!")
                break
        else:
            print("Invalid input. Please try again!")
    elif work == "N":
        job2 = input("Do you have a job(Y/N)?: ").upper()
        if job2 == 'Y':
            job3 = input("You're working in criminal justice(Y/N)?: ").upper()
            if job3 == 'Y':
                law = input("You're lawyer(Y/N)?: ").upper()
                if law == 'Y':
                    print("YEEES I guessed your job")
                    print("Thanks for playing")
                    break
                elif law == 'N':
                    print("I can't guess your job")
                    print("Thanks for playing")
                    break
                else:
                    print("Invalid input. Please try again!")
            elif job3 == 'N':
                print("I can't guess your job")
                print("Thanks for playing")
                break
            else:
                print("Invalid input. Please try again!")
        elif job2 == 'N':
            print("WHAT??")
            print("Bro...")
            print("You need to find a work")
            break
        else:
            print("Invalid input. Please try again!")
    else:
        print("Invalid input. Please try again!")

