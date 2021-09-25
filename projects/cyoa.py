"""Create Your Own Adventure!"""

__author__ = "730402784"


player: str = ""
HEART_EMOJI: str = "\U0001F497"
PARTY_EMOJI: str = "\U0001F389"
points: int = 0


def greet() -> None:
    """Greeting."""
    global player
    player = input("What is your name? ")
    print(f"{player}, welcome to Ainsley's Choose Your Own Adventure - maze addition!! For each question, choose one of the options presented and try to reach the end of the maze!!")


def q2() -> int:
    """Question 2."""
    global player
    global points
    points = 25
    ask_again: str = str(input(f"{player}, you come across another intersection, would you like to go left, right, center, or quit now?"))
    left2: bool = bool(ask_again == str("left"))
    center2: bool = bool(ask_again == str("center"))
    quit2: bool = bool(ask_again == str("quit"))
    if left2 is True or center2 is True:
        print(f"Oh no! Try again! Your points: {points}")
        q2()
    else: 
        if quit2 is True:
            print(f"Come back when you are ready to play. Your points: {points}")
            points += 76
        else:
            points += 25

    return points


def q3() -> int:
    """Question 3."""
    global points
    global player
    points = 50
    ask_again2: str = str(input(f"{player}, once again, you come across another intersection, would you like to go left, right, center, or quit now?"))
    left3: bool = bool(ask_again2 == str("left"))
    right3: bool = bool(ask_again2 == str("right"))
    quit3: bool = bool(ask_again2 == str("quit"))
    if left3 is True or right3 is True:
        print(f"Try again! Your points: {points}")
        q3()
    else:
        if quit3 is True:
            print(f"Come back when you are ready to play. Your points: {points}")
            points += 100
        else:
            points += 25
          
    return points


def end() -> None:
    """You win."""
    question: str = str(input("Do you want to play again or quit?"))
    quit: bool = bool(question == str("quit"))
    if quit is True:
        print("Come again later!")
    else:
        main()


def main() -> None:
    """Main."""
    global points
    from random import randint
    greet()
    q1: str = str(input(f"{player}, as you first enter the maze, you can go left, right, center, or end game, which do you choose?"))
    left: bool = bool(q1 == str("left"))
    center: bool = bool(q1 == str("center"))
    right: bool = bool(q1 == str("right"))
    sum: str = str(points)

    while points < 75:
        print(q1)
        if center is True or right is True:
            points = points + 25
            q2()
            if points == 50:
                q3()
        else:
            if left is True:
                print(f"You hit a dead end, try again!! Your point total: {sum}")
                points += 101
            else:
                print(f"Come again when you're ready to play!! {HEART_EMOJI}")
                points += 101
            
    if points == 75:
        answer: int = int(randint(1, 3))
        if answer == 1:
            print(f"YAY you win! Congrats!! {HEART_EMOJI}")
            print(f"Your points: {points} {PARTY_EMOJI}")
        else:
            if answer == 2:
                print(f"WOOHOO you got through the maze! {HEART_EMOJI}")
                print(f"Your points: {points} {PARTY_EMOJI}")
            else:
                print(f"You are so smart and made it to the finish! {HEART_EMOJI}")
                print(f"Your points: {points} {PARTY_EMOJI}")
        points = points + 1

    if points > 75:
        end()


if __name__ == "__main__":
    main()