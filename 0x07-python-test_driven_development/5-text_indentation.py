#!/usr/bin/python3
"""

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Arguments:
        text {String} -- [anything string]

    Raises:
        TypeError: [when text != str]
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    aux = 0
    for i in text:
        if i in characters:
            print(i, end="\n\n")
            aux = 1
        else:
            if aux == 0:
                print(i, end="")
            else:
                if i == ' ' or i == '\t':
                    pass
                else:
                    print(i, end="")
                    aux = 0
