class OHCE :
    def Palindrome(self, input: str) -> str:
        response = "Bonjour\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        response += "Au revoir"
        return response