def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    initial_petr, raise_petr, initial_driver, reduction_driver = offers

    # if their price is less than ours, accept theirs
    if initial_driver <= initial_petr:
        print ("Decided to pay: %s \n" % initial_petr)
        return initial_petr

    # if the amount we are raising by is greater than the price we have now,
    # just accept what we're offered.
    initial_petr   += raise_petr

    if initial_petr >= initial_driver:
        print ("May as well take %s\n" % initial_driver)
        return initial_driver

    # Otherwise go through a round of haggling
    initial_driver -= reduction_driver
    return checkio([initial_petr, raise_petr, initial_driver, reduction_driver])

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    assert checkio([500, 300, 700, 50]) == 700, 'Third'
    print('All is ok')