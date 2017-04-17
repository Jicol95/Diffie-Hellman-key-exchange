from User import User
from generate_Public_Values import generate_Public_Values
from diffie_hellman import diffie_Hellman_Crude

if __name__ == '__main__':

    print "Generating Public Prime..."
    print "Generating Public Primitive Root..."
    public_Numbers = generate_Public_Values()
    p = public_Numbers.prime
    print "Prime number is %d" % p
    g = public_Numbers.generator
    print "Primitive Root is %d" % g

    Alice = User("Alice", p, g)
    Bob = User ("Bob", p, g)

    diffie_Hellman_Crude(Alice,Bob)

    Bob.receive_Message(Alice.send_Message())
