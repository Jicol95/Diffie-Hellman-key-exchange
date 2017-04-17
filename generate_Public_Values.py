import random
class generate_Public_Values(object):
    def __init__(self):
        self.n = 700
        self.prime = self.generate_Public_Prime_Number_List(self.n)
        self.prime = random.choice(self.prime)
        self.generate_generator()


    def generate_Public_Prime_Number_List (self, n):
        """
        Find all prime numbers between 0 and n
        Args:
            n (int): The input number to find primes up to.
        """
        primes = [True] * (n / 2)
        for i in range(int((n / 2 - 1) / 2) >> 1):
            for j in range((i * (i + 3) << 1) + 3, n / 2, (i << 1) + 3):
                primes[j] = False
        return [2] + [((i << 1) + 3) for i in range(n / 2) if (primes[i])]


    def generate_generator (self):
        num_to_check = 0
        primitive_roots = []
        for each in range(1, self.prime):
            num_to_check += 1
            candidate_prim_roots = []
            for i in range(1, self.prime):
                modulus = (num_to_check ** i) % self.prime
                candidate_prim_roots.append(modulus)
                cleanedup_candidate_prim_roots = set(candidate_prim_roots)
                if len(cleanedup_candidate_prim_roots) == len(range(1, self.prime)):
                    primitive_roots.append(num_to_check)
        self.generator = random.choice(primitive_roots)