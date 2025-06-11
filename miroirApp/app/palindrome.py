class OHCE :
    def palindrome(self, input: str) -> str:
        response = "Bonjour\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        if input == reversed_input:
            response += "Bien dit !\n"

        response += "Au revoir"
        return response