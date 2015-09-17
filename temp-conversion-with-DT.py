def CtoF(x):
    '''
    >>> CtoF(5)
    41.0
    '''
    return x*(9.0/5)+32
    
if __name__ == "__main__":
    import doctest
    import argparse
    #doctest.testmod()

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type = float)
    args = parser.parse_args()
    x = args.x

    y = CtoF(x)
    print x, 'degrees Celsius is', y, 'degrees Fahrenheit'