import c_functions
import os.path


def validate_file_name(message):
    """ (str) -> str

    Prompt user the message to type the name of a file. Keep re-prompting
    until a valid filename that exists in the same directory as the current
    code file is supplied.
    Return the name of the file.
    """

    file_name = input(message)
    while not os.path.exists(file_name):
        print("Invalid filename! Please try again.")
        file_name = input(message)
    return file_name


def choose_encrypt_decrypt():
    """ () -> str

    Prompt user to enter if they choose the encryption or decryption process.
    Keep re-prompting until a valid process is given.
    Return the process chosen.
    """

    message = 'Shall we encrypt %s or decrypt %s? ' %(
             c_functions.ENCRYPT, c_functions.DECRYPT)
    process = input(message)
    while not (process == c_functions.ENCRYPT or
               process == c_functions.DECRYPT):
        print('Invalid process! I will ask again...')
        process = input(message)
    if process == c_functions.ENCRYPT:
        print("Okay! Let's Encrypt this message into absolute gibberish!")
    elif process == c_functions.DECRYPT:
        print("Let's Decrypt this puzzle and see what secret lies ahead!")
    return process


def main_operation():
    """ () -> NoneType

    Perform the chosen process using a deck supplied and a message supplied.
    If the process is 'e', encrypt; if 'd', decrypt.
    Stop the process if a valid card is not supplied.

    """

    prompt_user = 'Enter the filename of the card deck: '
    access_deck_file = open(validate_file_name(prompt_user), 'r')
    deck_to_use = c_functions.read_deck(access_deck_file)
    access_deck_file.close()
    if not (c_functions.validate_deck(deck_to_use)):
        print('This is not a valid card deck.')
        print('Stopping the process.')
        return

    prompt = 'Enter the filename of the message: '
    access_message_file = open(validate_file_name(prompt), 'r')
    messages = c_functions.read_message(access_message_file)
    access_message_file.close()
    # validating a message file is not needed as anything will be
    # encrypted or decrypted if it is an alphabet, numerals will be ignored.

    process = choose_encrypt_decrypt()

    for message in c_functions.process_message(deck_to_use, messages, process):
        print(message)

if __name__ == "__main__":
    main_operation()
