class Operation:
  def __init__ (self, operation_id, machines, processing_times):
    self.operation_id = operation_id
    self.machines = machines
    self.processing_times = processing_times

class Job:
  def __init__ (self, job_id, operations):
    self.job_id = job_id
    self.operations = operations

class Instance:
  def __init__ (self, num_jobs, num_machines, jobs):
    self.num_jobs = num_jobs
    self.num_machines = num_machines
    self.jobs = jobs

#creating an instance
op1 = Operation(1, [1, 2], [10, 15])
op2 = Operation(2, [2], [20])

job1 = Job(1, [op1, op2])

op3 = Operation(1, [1], [12])
op4 = Operation(2, [1, 2], [8, 14])

job2 = Job(2, [op3, op4])

inst = Instance(2, 2, [job1, job2])
