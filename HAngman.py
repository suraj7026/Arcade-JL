from time import sleep
from random import choice

categories = ("1. Prime Ministers of India ", "2. Phone Company", "3. Marvel characters")
characters = ("Iron man", "spiderman", "black widow", "hawkeye", "vision", "captian america","hulk","thor","black panther","wanda")
primeMinisters = ("Jawaharlal Nehru", "Rajiv Gandhi" , "Indira gandhi", "Vajpayee", "Narendra Modi", "Manmohan Singh")
companies = ("Google", "Redmi", "Apple", "Samsung", "moto", "Oppo","one plus","Nokia")
encourage = ("Good Job!!", "Yay!!", "Great work!")
w, h = 6, 3;
categories_matrix = [["" for x in range(w)] for y in range(h)] 
guessingword = "Samsung"
categories_matrix[0] = primeMinisters
categories_matrix[1] = companies
categories_matrix[2] = characters


hangManImageList = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """)

class HangmanGame:
    def __init__(self):
        self.typed_letters = []
        self.wrong_word_so_far = 0

    def play_hang_man(self):
        self.reset_game()
        self.begin_game()
        while self.wrong_word_so_far < len(hangManImageList) and self.word_till_now != guessingword:
            self.print_till_now()
            guess = self.guess_letter()
            if guess in guessingword:
                print(choice(encourage), "...Updating word so far...")
                for i in range(len(guessingword)):
                    if guess == guessingword[i]:
                        self.word_till_now = self.word_till_now[:i] + guess + self.word_till_now[i+1:]
            else:
                print(":( Wrong, Try again (HINT: Space is also a dash)")
                self.wrong_word_so_far += 1
        self.final_result()
        self.play_again()

    def begin_game(self):
        print("\nWelcome to Hangman")
        print(*categories, sep = "\n")
        option = input("Enter (1/2/3) to start")
        global guessingword
        guessingword = choice(categories_matrix[int(option)-1]).upper()
        self.word_till_now = "-" * len(guessingword)

    def play_again(self):
        print("Would you like to play again?")
        user_input = input("Enter Y/N ").upper()
        if user_input == "Y":
            self.play_hang_man()
        else:
            print()
            print("Bye, see you again")

    def final_result(self):
        if self.wrong_word_so_far == len(hangManImageList):
            print("Oops, game over!")
        else:
            print("Yay! You won, congrats!")

    def print_till_now(self):
        print(hangManImageList[self.wrong_word_so_far])
        print("Remaining word", self.word_till_now)
        print("Letters guessed", sorted(self.typed_letters))

    def reset_game(self):
        self.__init__()

    def guess_letter(self):
        guess = input("Type a letter: ")[0].upper()
        sleep(1)  
        while guess in self.typed_letters:
            print("Letter already guessed")
            guess = input("Type a letter: ")[0].upper()
            sleep(1)

        self.typed_letters.append(guess)

        return guess

if __name__ == '__main__':
    hang_man = HangmanGame()
    hang_man.play_hang_man()


