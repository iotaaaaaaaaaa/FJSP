class MachineOption:
  def __init__ (self, machine_id, processing_time):
    self.machine_id = machine_id
    self.processing_time = processing_time

class Operation:
  def __init__ (self, operation_id, machine_option):
    self.operation_id = operation_id
    self.machine_option = machine_option

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
op1 = Operation(1, [MachineOption(1, 10), MachineOption(2, 15)])
op2 = Operation(2, [MachineOption(2, 20)])

job1 = Job(1, [op1, op2])

op3 = Operation(1, MachineOption(1, 12))
op4 = Operation(2, [MachineOption(1, 8), MachineOption(2, 14)])

job2 = Job(2, [op3, op4])

inst = Instance(2, 2, [job1, job2])
