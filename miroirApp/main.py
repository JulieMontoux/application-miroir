from app.miroir import miroir_mot, est_palindrome

def main():
    while True:
        texte = input("> ")
        if texte.lower() in ("exit", "quit"):
            break
        mots = texte.split()
        for mot in mots:
            print(miroir_mot(mot), end=' ')
            if est_palindrome(mot):
                print("→ Bien dit !", end=' ')
        print()

if __name__ == "__main__":
    main()
