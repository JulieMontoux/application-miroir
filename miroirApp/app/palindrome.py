MESSAGES = {
    "fr": {
        "hello": "Bonjour",
        "goodbye": "Au revoir",
        "well_said": "Bien dit !"
    },
    "en": {
        "hello": "Hello",
        "goodbye": "Goodbye",
        "well_said": "Well said!"
    }
}

class OHCE :
    def __init__(self, language="fr"):
        self.language = language
        self.messages = MESSAGES.get(language, MESSAGES[language])

    def palindrome(self, input: str) -> str:
        response = f"{self.messages['hello']}\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        if self.is_palindrome(input):
            response += f"{self.messages['well_said']}\n"

        response += self.messages["goodbye"]
        return response

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]