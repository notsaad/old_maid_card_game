# Family Name: Saad Mazhar
# Student Number: 300249820
# Course: ITI 1120C
# Assignment Number 4
import random


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''

    random.shuffle(deck)


#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)
    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = []
    other = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for idx, val in enumerate(deck):
        if idx % 2 == 0:
            dealer.append(val)
        else:
            other.append(val)

    return (dealer, other)



def remove_pairs(l):
    '''
    (list of str)->list of str
    Returns a copy of list l where all the pairs from l are removed AND
    the elements of the new list shuffled
    Precondition: elements of l are cards represented as strings described above
    '''
    no_pairs = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    l.sort()

    for i, v in enumerate(l):
        if i + 1 < len(l):
            if l[i][0] != l[i + 1][0]:
                if l[i][0] != l[i - 1][0]:
                    no_pairs.append(v)
                elif l[i][0] == l[i - 1][0] and l[i][0] == l[i - 2][0]:
                    no_pairs.append(v)
        else:
            if l[i][0] != l[i-1][0]:
                no_pairs.append(v)

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for x in deck:
        print(x, end=' ')
    print('')


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE


def play_game():
    '''()->None
    This function plays the game'''

    winner = False
    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    print('******************************\n')

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
    while winner == False:
        if len(dealer) == 0:
            print('I do not have any more cards, I win!')
            winner = True
        elif len(human) == 0:
            print('You do not have any more cards')
            print('Congratulations! You, Human, win!')
            winner = True
        else:
            print('Your turn.')
            print('Your current deck of cards is:')
            print_deck(human)
            print('I have', str(len(dealer)), 'cards. If 1 stands for my first card and', str(len(dealer)), 'for my last card, which of my cards would you like?')
            hChoice = int(input('Give me an integer between 1 and ' + str(len(dealer)) + ': '))
            if hChoice < 1 or hChoice > len(dealer):
                while hChoice < 1 or hChoice > len(dealer):
                    hChoice = int(input('Invalid number. Please enter an integer between 1 and ' + str(len(dealer)) + ': '))
            print('You asked for my ', str(hChoice), 'position card.')
            print('Here it is. It is ' + dealer[hChoice - 1])
            print('With ' + dealer[hChoice - 1] + ' added, your current deck is: ')
            human.append(dealer.pop(hChoice - 1))
            print_deck(human)
            print('And after discarding pairs and shuffling, your deck is: ')
            human = remove_pairs(human)
            print_deck(human)
            wait_for_player()
            print('******************************\n')
            print('My turn.')
            x = random.randint(1, len(human))
            print('I took your', str(x), 'position card.')
            dealer.append(human.pop(x - 1))
            dealer = remove_pairs(dealer)
            wait_for_player()
            print('******************************\n')




# main
play_game()
