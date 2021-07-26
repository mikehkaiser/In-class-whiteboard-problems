
def numberToLetter(colstr):

    reference = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    title = ''
    for digit in colstr:
        title += reference[i]
        i += 1
        return title.upper()


numberToLetter(1234)
