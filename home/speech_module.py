def checkio(number):
    # define string container
    wordedNumber = []

    # define a few special cases
    numberLookup = {
         '1': 'one'     ,  '2':'two'      ,  '3':'three'   ,  '4':'four'   ,
         '5':'five'     ,  '6':'six'      ,  '7':'seven'   ,  '8':'eight'  ,
         '9':'nine'     , '10':'ten'      , '11':'eleven'  , '12':'twelve' ,
        '13':'thirteen' , '14':'fourteen' , '15':'fifteen' , '16':'sixteen',
        '17':'seventeen', '18':'eighteen' , '19':'nineteen', '20':'twenty' ,
        '30':'thirty'   , '40':'forty'    , '50':'fifty'   , '60':'sixty'  ,
        '70':'seventy'  , '80':'eighty'   , '90':'ninety'
    }

    print ('The raw number: %d' % number)

    # if we are in the thousands, translate the number of thouands we have and
    # append the 'thousand' string to it
    thousands = int(number / 1000)
    if thousands > 0:
        wordedNumber.append(numberLookup[str(thousands)] + " thousand")
        number -= thousands * 1000

    # if we are in the hundreds, translate the number of hundreds we have and
    # append the 'hundred' string to it
    hundreds = int(number / 100)
    if hundreds > 0:
        wordedNumber.append(numberLookup[str(hundreds)] + " hundred")
        number -= hundreds * 100

    # if we are in the tens, translate the number if we are between 10 and 20
    # since those numbers are special cases. Otherwise translate only the tens
    # digit (twenty, thirty, forty, ...)
    tens = int(number / 10)
    if tens > 0:
        if 10 <= number <= 20:
            # set number to 0 after this since this finishes our translations
            wordedNumber.append(numberLookup[str(number)])
            number = 0
        else:
            wordedNumber.append(numberLookup[str(tens * 10)])
            number -= tens * 10

    # finally, translate the final one's digits
    if number > 0:
        wordedNumber.append(numberLookup[str(number)])

    # combine the list with whitespace and return
    number = ' '.join(wordedNumber)
    print ('The worded number: '+number)
    return number

if __name__ == '__main__':
    assert checkio(4)   == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)  == 'twelve', "Third"
    assert checkio(101) == 'one hundred one', "Fifth"
    assert checkio(212) == 'two hundred twelve', "Sixth"
    assert checkio(40)  == 'forty', "Seventh"
    # for fun
    assert checkio(999) == 'nine hundred ninety nine', "Eigth"
    assert checkio(9999) == 'nine thousand nine hundred ninety nine', 'Nineth'
    print('All ok')