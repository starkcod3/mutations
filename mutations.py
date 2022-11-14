def mutate_string(string, position, character):
    '''Changes a character at a given index'''
    return string[:position] + character + string[position + 1:]
