from random import randint, randrange

def main():
    index = randint(0, 801) # There are 802 pokemon
    pokemon = ''
    with open('pokemon.txt') as fp:
        for i, line in enumerate(fp):
            if i == index:
                pokemon = line.strip()
    gameloop(pokemon)

def gameloop(pokemon):
    progress = ['_' for char in pokemon]
    win = False
    time = 5
    while time > 0 and not win:
        print(''.join(progress))
        guess = input('> ')[0]
        for i, char in enumerate(pokemon):
            if guess == char:
                progress[i] = pokemon[i]
        if guess not in pokemon:
            time -= 1

        win = ''.join(progress) == pokemon

    if win:
        print('That\'s right! It\'s' + pokemon + '.')
        print('Your father and I are so proud of you.')
    else:
        print('You took too long.')
        print('It was ' + pokemon + ' all along.')

if __name__ == '__main__':
    main()
