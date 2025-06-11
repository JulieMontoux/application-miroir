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

    def palindrome(self, input: str) -> str:
        if self.is_evening():
            hello = self.messages['hello_evening']
            goodbye = self.messages['goodbye_evening']
        else:
            hello = self.messages['hello_day']
            goodbye = self.messages['goodbye_day']

        response = f"{hello}\n"
        reversed_input = input[::-1]
        response += reversed_input + "\n"

        if self.is_palindrome(input):
            response += f"{self.messages['well_said']}\n"

        response += goodbye
        return response

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]