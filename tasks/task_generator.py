import random

class TaskGenerator:
    @staticmethod
    def generate_odd_even_task():
        return random.randint(1, 100)
    
    @staticmethod
    def generate_prime_task():
        return random.randint(2, 1000)
