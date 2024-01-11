import logging


# debug, info, warning, error, critical

logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y

var1 = 20
var2 = 10

add_total = add(var1, var2)
logging.debug('Add: {} + {} = {}'.format(var1, var2, add_total))
