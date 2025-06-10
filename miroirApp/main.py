from app.miroir import miroir_mot

def main():
    while True:
        texte = input("> ")
        mots = texte.split()
        for mot in mots:
            print(miroir_mot(mot), end=' ')
        print()

if __name__ == "__main__":
    main()
