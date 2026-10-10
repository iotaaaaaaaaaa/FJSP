import random

#adding reproducibility
random.seed(42)

class MachineOption:
  def __init__ (self, machine_id, processing_time):
    self.machine_id = machine_id
    self.processing_time = processing_time

class Operation:
  def __init__ (self, operation_id, available_machines):
    self.operation_id = operation_id
    self.available_machines = available_machines
    self.eligible_machines = random.sample(self.available_machines, random.randint(1, len(self.available_machines)))
    self.machine_options = []

    for i in self.eligible_machines:
      self.machine_options.append(MachineOption (i, random.randint(1,15)))

class Job:
  def __init__ (self, job_id, num_operations, machines):
    self.job_id = job_id
    self.num_operations = num_operations
    self.operations = []
    self.machines = machines

    for i in range (1, self.num_operations+1):
      self.operations.append(Operation(i, self.machines))

class Instance:
  def __init__ (self, num_jobs, num_machines):
    self.num_machines = num_machines
    self.machines = list(range(1, self.num_machines + 1))
    self.num_jobs = num_jobs
    self.jobs = []
    
    for i in range(1, self.num_jobs+1):
      self.jobs.append(Job(i, random.randint(1, 10), self.machines))

  #displaying an instance
  def display (self):
    print (f"Number of Machines: {self.num_machines}")
    print (f"Number of Jobs: {self.num_jobs}")
    for i in self.jobs:
      print (f"Job ID: {i.job_id}")
      for j in i.operations:
        print (f"Operation ID: {j.operation_id}")
        for k in j.machine_options:
          print (f"Machine ID: {k.machine_id}")
          print (f"Processing Time: {k.processing_time}")
      print()

#creating an instance
num_jobs = random.randint(1, 20)
num_machines = random.randint(1, 25)

inst = Instance(num_jobs, num_machines)

inst.display()
