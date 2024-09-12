import time
from solvers.generic_solver import GenericSolver

class System1Solver(GenericSolver):
    def __init__(self):
        self.case_base = {}

    def solve(self, task):
        start_time = time.time()
        if task in self.case_base:
            elapsed_time = time.time() - start_time
            return self.case_base[task], elapsed_time, True
        return None, time.time() - start_time, False

    def update_case_base(self, task, solution):
        self.case_base[task] = solution
