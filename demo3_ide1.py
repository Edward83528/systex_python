def getdigit(x):
    """

    :param x:
    :return:
    """
    returns = 0
    while x > 0:
        x/=10
        returns += 1
    return returns
def test(x):
    return 'ss'

print (getdigit(2*512));
