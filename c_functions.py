# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def edit_message(message):
    """(str) -> str

    Return the message with only alphabets, all in uppercase.

    >>>edit_message("Good Day!")
    "GOODDAY"
    >>>edit_message("Make Me Encryptable")
    "MAKEMEENCRYPTABLE"

    """
    edited = ""
    for a in message:
        if a.isalpha():
            edited += a
    big = edited.upper()
    return big


def encrypt(letter, key):
    """(str, int) -> str

    Precondition: key > 0

    Return the resulting uppercase letter after encryption by adding the letter
    index in the alphabets and the key value.

    >>>encrypt("A", 3)
    "D"
    >>>encrypt("Z", 1)
    "A"

    """

    letter_index = ALPHABETS.find(letter)
    encrypted_index = letter_index + key
    if encrypted_index < len(ALPHABETS):
        return ALPHABETS[encrypted_index]
    else:
        looped_index = encrypted_index - len(ALPHABETS)
        return ALPHABETS[looped_index]


def decrypt(letter, key):
    """(str, int) -> str

    Precondition: key > 0

    Return the resulting uppercase letter after decryption by subtracting the
    key with the letter index in alphabets.

    >>>decrypt("D", 3)
    "A"
    >>>decrypt("A", 1)
    "Z"

    """
    letter_index = ALPHABETS.find(letter)
    decrypted_index = letter_index - key
    return ALPHABETS[decrypted_index]


def swap_cards(deck,i):
    """(list of int, int) -> NoneType

    Interchange the index associated with the card at i and the one after
    that.

    >>>deck = [1,2,3,4]
    >>>swap_cards(deck, 2)
    None
    >>>deck
    [1,2,4,3]

     >>>deck = [1,2,3,4]
    >>>swap_cards(deck, 3)
    None
    >>>deck
    [4,2,3,1]
    """
    taken_out = deck[i]
    if deck[i] == deck[(len(deck)-1)]:
        deck[i] = deck[0]
        deck[0] = taken_out
    else:
        deck[i] = deck[i+1]
        deck[i+1] = taken_out


def small_joker(deck):

    """(list of int) -> int

    Precondition: len(deck) >= 3

    Return the value of the small joker (the card with the second largest
    value)

    >>>small_joker([1,2,3,4])
    3
    >>>small_joker([4,5,2,1])
    4
    """

    max_value = []
    max_value.append(max(deck))
    max_index = deck.index(max(deck))
    deck.remove(max(deck))

    second_max = max(deck)

    deck.insert(max_index, max_value[0])

    return second_max


def big_joker(deck):
    """(list of int) -> int

    Precondition: len(deck) >= 3

    Return the value of the big joker (the card with the largest value)

    >>>big_joker([1,2,3,4])
    4
    >>>big_joker([4,5,2,1])
    5
    """
    return max(deck)


def shift_small_joker(deck):
    """(list of int) -> int

    Precondition: len(deck) >= 3

    shift the small joker with the card after it.
    Consider the deck to be circular.

    >>>deck = [1,2,3,4]
    >>>shift_small_joker(deck)
    None
    >>>deck
    [1,2,4,3]

    >>>deck = [3,4,2,6,5]
    >>>shift_small_joker(deck)
    None
    >>>deck
    [5,4,2,6,3]

    """

    small = small_joker(deck)
    index = deck.index(small)

    if index == len(deck) - 1:
        deck[index] = deck[0]
        deck[0] = small
    else:
        deck[index] = deck[index + 1]
        deck[index + 1] = small


def shift_big_joker(deck):
    """(list of int) -> NoneType

    Precondition: len(deck) >= 3

    Move the big joker down under the two cards after it.
    Consider the deck to be circular.

    >>>deck = [1,2,3,4]
    >>>shift_big_joker(deck)
    None
    >>>deck
    [2,4,3,1]

    >>>deck = [4,3,5,2,1]
    >>>shift_big_joker(deck)
    None
    >>>deck
    [4,3,2,1,5]

    """
    taken_out = []
    big = big_joker(deck)
    index = deck.index(big)

    taken_out.append(deck[index+2-len(deck)])

    deck[index] = deck[index+1 - len(deck)]
    deck[index+1 - len(deck)] = deck[index+2 - len(deck)]
    deck[index+2 -len(deck)] = big


def triple_cut_deck(deck):
    """(list of int) -> NoneType

    Perform a triple cut by finding the first joker and second joker, and
    swapping the stacks of index less than first joker index and greter than
    second joker index.

    >>>deck = [1,2,5,6,4,3]
    >>>triple_cut_deck(deck)
    None
    >>>deck
    [4,3,5,6,1,2]

    """
    index_s = deck.index(small_joker(deck))
    index_b = deck.index(big_joker(deck))

    if index_s < index_b:
        first_joker = index_s
        second_joker = index_b
    elif index_b < index_s:
        first_joker = index_b
        second_joker = index_s

    new_top = deck[second_joker+1 : ]
    middle = deck[first_joker : second_joker+1]
    new_bottom = deck[ : first_joker]

    new_deck = new_top + middle + new_bottom
    deck[0:len(deck)] = new_deck


def top_to_bottom(deck):
    """(list of int) -> NoneType

    Precondition: value of bottom card !> len(deck)

    After finding the value of the bottom card, take that many cards from
    the top of the deck and place them at the bottom above the last card.
    If the bottom card is the big joker, place the small joker value amount
    of cards on top of the big joker from the top.

    >>>deck = [1,2,3,6,5,4]
    >>>top_to_bottom(deck)
    None
    >>>deck
    [5,1,2,3,6,4]

    >>>deck = [1,2,5,6,4,3]
    >>>top_to_bottom(g)
    >>>deck
    [6, 4, 1, 2, 5, 3]

    """
    value = deck[len(deck) - 1]

    if value == big_joker(deck):
        value = small_joker(deck)

    pile = deck[:value]

    new_deck = deck[value:len(deck)-1] + pile + deck[len(deck)-1:]

    deck[0:len(deck)] = new_deck


def top_index_card(deck):
    """(list of int) -> int

    Precondition: value of top card !> len(deck)

    Return the value of the card - to be used as the keystream value - at the
    index of the value of the top card. If the value of the top card is the
    big joker, return the value of the card at the index of the small joker.

    >>>top_index_card([5,4,3,6,7,2,1])
    2
    >>>top_index_card([7,6,2,5,4,3,1])
    1

    """
    top = deck[0]
    if top == big_joker(deck):
        top = small_joker(deck)

    return deck[top]


def get_keystream_value(deck):
    """(list of int) -> int

    Return a valid keystream value after repeating all 5 steps of the
    algorithm. Repeat the 5 steps until a valid keystream value is produced.

    >>>deck=[1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,
    >>>      17,20,23,26]
    >>>get_keystream_value(deck)
    11

    >>>deck=[23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,5,8,11,
    >>>      14,17,20,6]
    >>>get_keystream_value(deck)
    9
    """
    shift_small_joker(deck)
    shift_big_joker(deck)
    triple_cut_deck(deck)
    top_to_bottom(deck)
    key = top_index_card(deck)
    while key >= small_joker(deck):

        shift_small_joker(deck)
        shift_big_joker(deck)
        triple_cut_deck(deck)
        top_to_bottom(deck)
        key = top_index_card(deck)

    return key


def process_message(deck, messages, task):
    """(list of int, list of str, str) -> list of str

    Return a list of encrypted or decrypted (as prompted) strings in the
    order presented.

    >>>deck = deck1.txt
    >>>messages = secret7.txt
    >>>process_message(deck, messages, DECRYPT)
    DOABARRELROLL

    >>>deck = deck2.txt
    >>>messages = secret2.txt
    >>>process_message(deck, messages, DECRYPT)
    HOUSTONWEHAVEAPROBLEM

    """
    after_process = []

    for message in messages:
        processed_message = ""
        new_message = edit_message(message)

        for l in new_message:
            key = get_keystream_value(deck)
            if task == ENCRYPT:
                letter = encrypt(l, key)
            elif task == DECRYPT:
                letter = decrypt(l, key)
            processed_message += letter
        after_process.append(processed_message)

    return after_process


def read_message(file):
    """(file open for reading) -> list of str

    Return a list of messages, whose items will be per line in the file
    and in the same order.


    No example given as a function to read the file is required.
    """
    messages = []

    for line in file:
        messages.append(line)

    return messages


def validate_deck(candidate_deck):
    """(list of int) -> bool

    Precondition: len(candidate_deck) >= 3

    Return True iff candidate deck has every integer from 1 to the number
    of cards in the deck. If it is not a valid deck, return False.

    >>>validate_deck([1,3,4,5,2,6,9,7,8])
    True
    >>>validate_deck([1,5,2,3])
    False

    """
    already_checked = []
    flag = True

    for number in candidate_deck:
        if (number > len(candidate_deck)) or (number in already_checked):
            flag = False
        else:
            already_checked.append(number)

    return flag


def read_deck(file):
    """(file open for reading) -> list of int

    Return the list of numbers that will be represented as the candidate
    deck that will be checked.

    No examples given as functions to read files are required.
    """
    deck_to_check = []

    for line in file:
        new_line = line.strip("\n")
        to_be_added = new_line.split(" ")
        for numbers in to_be_added:
            if numbers.isdigit():
                deck_to_check.append(int(numbers))

    return deck_to_check
