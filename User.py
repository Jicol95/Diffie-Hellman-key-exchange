import random
from encode_decode import encode
from encode_decode import decode


class User(object):

    # A user with Diffie-Hellman key exchange methods

    def __init__(self, name, prime_number, generator):
        self.name = name
        self.prime_number = prime_number
        self.generator = generator
        self.private_number = random.randint(0,20)
        self.key = None
        self.public_self_result = None
        self.public_partner_result = None
        print "User %s has been created." % self.name

    # One way function that takes the (public generator to the power of the users private random number) mod (public prime)
    def one_way_function (self):
        if (self.public_self_result is None):
            self.public_self_result = (self.generator^self.private_number)%(self.prime_number)
        else:
            print "Public Result is already generated"

    # Takes the result of the (2nd user's one way function to the power of the 1st user's private random number) mod (public prime)
    def key_calculation (self):
        if (self.key is None):
            self.key = (self.public_partner_result^self.private_number)%(self.prime_number)
        else:
            print "You already have the key"

    #Test funciton that prints the agreed key
    def print_key (self):
        print self.key



















