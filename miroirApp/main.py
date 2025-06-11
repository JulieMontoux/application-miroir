from app.palindrome import OHCE


def main():
    print("Bienvenue dans l'application OHCE !")

    langue = input("Choisissez votre langue (fr/en) : ").strip().lower()
    ohce = OHCE(language=langue if langue in ["fr", "en"] else "fr")

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print(ohce.au_revoir())
            break

        result = ohce.palindrome(user_input)
        print(result)

if __name__ == "__main__":
    main()
