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
        """Gets text input from the user.
        
        Args:
            self (Console): an instance of Console.
            prompt(string): The prompt to be displayed.

        Returns:
            integer: the user's input as a number.
        """
        return int(input(prompt))

    def write(self, text):
        """Gets text input from the user.
        
        Args:
            self (Console): an instance of Console.
            text(string): The output to be displayed.
        """
        print(text)