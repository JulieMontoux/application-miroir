from datetime import datetime

MESSAGES = {
    "fr": {
        "hello_day": "Bonjour",
        "hello_evening": "Bonsoir",
        "goodbye_day": "Au revoir, bonne journée !",
        "goodbye_evening": "Bonne soirée, à bientôt !",
        "well_said": "Bien dit !"
    },
    "en": {
        "hello_day": "Good morning",
        "hello_evening": "Good evening",
        "goodbye_day": "Goodbye, have a nice day!",
        "goodbye_evening": "Good night, see you soon!",
        "well_said": "Well said!"
    }
}

class OHCE :
    def __init__(self, language="fr"):
        self.language = language
        self.messages = MESSAGES.get(language, MESSAGES[language])

    @staticmethod
    def get_hour():
        return datetime.now().hour

    def is_evening(self):
        return self.get_hour() >= 18

    def salutation(self):
        return self.messages["hello_evening"] if self.is_evening() else self.messages["hello_day"]

    def au_revoir(self):
        return self.messages["goodbye_evening"] if self.is_evening() else self.messages["goodbye_day"]

    def palindrome(self, input: str) -> str:
        hello = self.salutation()
        goodbye = self.au_revoir()

        response = hello + "\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        if self.is_palindrome(input):
            response += f"{self.messages['well_said']}\n"

        response += goodbye
        return response

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]