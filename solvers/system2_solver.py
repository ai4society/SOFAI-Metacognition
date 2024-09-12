import time
from solvers.generic_solver import GenericSolver

# Odd-Even Solver
class OddEvenSolver(GenericSolver):
    def solve(self, task):
        start_time = time.time()
        solution = "even" if task % 2 == 0 else "odd"
        return solution, time.time() - start_time

# Prime Checker Solver
class PrimeCheckerSolver(GenericSolver):
    def solve(self, task):
        start_time = time.time()
        if task < 2:
            return "not prime", time.time() - start_time
        for i in range(2, int(task ** 0.5) + 1):
            if task % i == 0:
                return "not prime", time.time() - start_time
        return "prime", time.time() - start_time
