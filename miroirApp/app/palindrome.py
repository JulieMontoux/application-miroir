class OHCE :
    def palindrome(self, input: str) -> str:
        response = "Bonjour\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        if self.is_palindrome(input):
            response += "Bien dit !\n"

        response += "Au revoir"
        return response

    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]