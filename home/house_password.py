from re import search

def checkio(data):
    '''
    Return True if password strong and False if not

    Password is "Strong" if:
        1) Password is >= 10 Characters
        2) Contains at least one upper, one lower, and one numeral
    '''

    # check legth first
    if len( data ) >= 10:
        # positive lookahead FTW
        if search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$', data):
            return True
        else:
            print ('Password should contain at least on lower case letter, ' +\
                   'one upper case character, and one numeral')
            return False
    else:
        print("Password should be at least 10 characters")
        return False

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print('All ok')