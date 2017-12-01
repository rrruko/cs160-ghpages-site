"""A hangman game with pokemon"""

from random import randint

def main():
    """Choose a pokemon and start/restart the game"""
    replay = True
    while replay:
        index = randint(0, 801) # There are 802 pokemon
        pokemon = ''
        with open('pokemon.txt') as file:
            for i, line in enumerate(file):
                if i == index:
                    pokemon = line.strip()
        gameloop(pokemon)
        print('Would you like to play again? (y/N)')
        replay = input('> ') in ['y', 'yes']


def gameloop(pokemon):
    """Main game loop"""
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
        print('That\'s right! It\'s ' + pokemon + '.')
        print('Your father and I are so proud of you.')
    else:
        print('You took too long.')
        print('It was ' + pokemon + ' all along.')

if __name__ == '__main__':
    main()
