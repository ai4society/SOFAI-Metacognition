import random

class Metacognition:
    def __init__(self, system1_solver, system2_solver, probability_repeat):
        self.system1 = system1_solver
        self.system2 = system2_solver
        self.probability_repeat = probability_repeat
        self.repeat_task_pool = []

    def solve_task(self, task):
        solution, time_taken, from_case_base = self.system1.solve(task)
        if from_case_base:
            return solution, time_taken, "System 1"

        solution, time_taken = self.system2.solve(task)
        self.system1.update_case_base(task, solution)
        return solution, time_taken, "System 2"

    def repeat_or_new_task(self, task_generator):
        if random.random() < self.probability_repeat and self.repeat_task_pool:
            return random.choice(self.repeat_task_pool)
        else:
            task = task_generator()
            self.repeat_task_pool.append(task)
            return task
