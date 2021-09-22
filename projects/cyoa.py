"""Create Your Own Adventure!"""

author = "730402784"


points: int = 0
player: str
HEART_EMOJI: str = "\U0001F497"
ask_again: str = str("You come across another intersection, would you like to go left, right, or center now?")


def greet() -> None:
    player: str = str(input("What is your name? "))
    print(f"{player}, welcome to Ainsley's Choose Your Own Adventure - maze addition!! For each question, choose one of the options presented and try to reach the end of the maze!!")


def q2() -> None:
    print(ask_again)
    


def left() -> None:
    print(ask_again)


def right() -> None:
    print(ask_again)


def main() -> None:
    greet()
    q1: str = str(input("As you first enter the maze, you can go left, right, center, or end game, which do you choose?"))
    left: bool = bool(q1 == str("left"))
    center: bool = bool(q1 == str("center"))
    right: bool = bool(q1 == str("right"))
    points: int = 0
    sum: str = str(points)
    
    print(q1)
    if center is True or right is True:
        q2()
    else:
        if left is True:
            print(f"You hit a dead end, try again!! Your point total: {sum}")
        else:
            print(f"Come again when you're ready to play!! {HEART_EMOJI}")


if __name__ == "__main__":
    main()
