from alemanpyutils.random.RandomIntegerGenerator import RandomIntegerGenerator


def test_int_rand_gen():
    
    irg = RandomIntegerGenerator(100)

    for i in range(0,10):
        print(irg.generate())