class Console:
    """Code template for a computer console. This class
    is to get a text/numerical inputs and to display text outputs.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt(string): The prompt to display.
    """
    def read(self, prompt):
        """Gets text input from the user.
        
        Args:
            self (Console): an instance of Console.
            prompt(string): The prompt to be displayed.

        Returns:
            string: the user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets text input from the user. Validates input.
        
        Args:
            self (Console): an instance of Console.
            prompt(string): The prompt to be displayed.

        Returns:
            integer: the user's input as a number.
        """
        guess = input(prompt)
        while True:
            if guess.isnumeric():
                guess = int(guess)
                break
            else:
                print("Please enter a positive number.")
                guess = input(prompt)
        return guess
        

    def write(self, text):
        """Gets text input from the user.
        
        Args:
            self (Console): an instance of Console.
            text(string): The output to be displayed.
        """
        print(text)

"""TEST CASES:"""
# x = Console()
# name = x.read("What is your name? ")
# x.write(name)
# prompt = "Please enter your guess (1000-9999): "
# guess = x.read_number(prompt)
# while True:
#     if(guess < 1000):
#         print("Please enter a guess over 1000.")
#         guess = x.read_number(prompt)
#     elif(guess > 9999):
#         print("Please enter a guess under 9999.")
#         guess = x.read_number(prompt)
#     else:
#         break
# print(guess)