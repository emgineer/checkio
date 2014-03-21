'''
Dicipher a password from a 4x4 matrix of lower case characters using a second
matrix with 4 "windows" which display 4 characters at a time. After noting each
displayed character, row by row from left to right, we rotate the masking matrix
90 degrees clockwise. Once we have made a full circle we have completed the
decryption.

'''

def rotate(matrix):
    new  = [['','','',''],['','','',''],['','','',''],['','','','']]
    rows = 3 # hard coded
    for i,row in enumerate(matrix):
        for j,char in enumerate(row):
            new[j][rows-i] = char

    return new

def checkio(input_data):
    'Return password of given cipher map'

    maskChars, passChars = input_data
    password = ''

    rotations = 0
    while rotations < 4:
        for i,row in enumerate(maskChars):
            maskChars[i] = list(row)

            for j,char in enumerate(maskChars[i]):
                if char == 'X':
                    password += passChars[i][j]

        maskChars = rotate(maskChars)
        rotations += 1

    return password

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'

    print('All ok')