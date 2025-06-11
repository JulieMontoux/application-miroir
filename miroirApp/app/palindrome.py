from datetime import datetime

MESSAGES = {
    "fr": {
        "salutation": {
            "matin": "Bonjour",
            "après-midi": "Bonjour",
            "soirée": "Bonsoir",
            "nuit": "Bonsoir"
        },
        "revoir": {
            "matin": "Au revoir, bonne journée !",
            "après-midi": "Au revoir, bonne fin d'après-midi !",
            "soirée": "Bonne soirée, à bientôt !",
            "nuit": "Bonne nuit !"
        },
        "well_said": "Bien dit !"
    },
    "en": {
        "salutation": {
            "matin": "Good morning",
            "après-midi": "Good afternoon",
            "soirée": "Good evening",
            "nuit": "Good night"
        },
        "revoir": {
            "matin": "Goodbye, have a nice day!",
            "après-midi": "Goodbye, enjoy your afternoon!",
            "soirée": "Good night, see you soon!",
            "nuit": "Goodbye, sleep well!"
        },
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

    def get_period(self):
        hour = self.get_hour()
        if 5 <= hour < 12:
            return "matin"
        elif 12 <= hour < 18:
            return "après-midi"
        elif 18 <= hour < 22:
            return "soirée"
        else:
            return "nuit"


    def is_evening(self):
        return self.get_hour() >= 18

    def salutation(self):
        return self.messages["salutation"][self.get_period()]

    def au_revoir(self):
        return self.messages["revoir"][self.get_period()]

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