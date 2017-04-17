def diffie_Hellman_Crude(Alice, Bob):

    Alice.one_way_function()
    print "Alice's result is: %d" % Alice.public_self_result

    Bob.one_way_function()
    print "Bob's result: %d" % Bob.public_self_result

    Bob.public_partner_result = Alice.public_self_result
    Bob.key_calculation()

    Alice.public_partner_result = Bob.public_self_result
    Alice.key_calculation()
