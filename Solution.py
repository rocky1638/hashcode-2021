from Intersection import Intersection
from collections import defaultdict
import math
import numpy as np

class Solution:
  def __init__(self, duration, num_intersections, num_streets, num_cars, bonus):
    self.duration = duration
    self.num_intersections = num_intersections
    self.num_streets = num_streets
    self.num_cars = num_cars
    self.bonus = bonus
    self.intersections = {}
    self.t = 0

  def __str__(self):
    return(f"""
    Solution:
      duration: {self.duration}
      num_intersections: {self.num_intersections}
      num_streets: {self.num_streets}
      num_cars: {self.num_cars}
      bonus: {self.bonus}
      intersections: {str(self.intersections)}
    """)

  def round_robin(self, testcase, streets, cars, intersections):
    filename = testcase.rsplit('.', 1)[0] + '.out'
    with open("out/" + filename, 'w') as file:
      file.write(f"{len(intersections)}\n")
      for intersection in intersections.values():
        file.write(f"{intersection.id}\n")
        
        file.write(f"{(len(intersection.incoming.values()))}\n")
        for strt in intersection.incoming.values():
          file.write(f'{strt.name} 1\n')

  def simple_load(self, testcase, streets, cars, intersections):
    filename = testcase.rsplit('.', 1)[0] + '.out'
    loads = self.calc_load(cars)
    with open("out/" + filename, 'w') as file:
      valid_ints = []
      for i in intersections.values():
        d = loads[i.id]
        if any(d.values()):
          valid_ints.append(i)
      file.write(f"{len(valid_ints)}\n")
      
      for intersection in valid_ints:
        file.write(f"{intersection.id}\n")
        
        file.write(f"{len([ strt for strt in intersection.incoming.values() if (loads[intersection.id][strt.name] > 0)] )}\n")
        for strt in intersection.incoming.values():
          if loads[intersection.id][strt.name] > 0:
            file.write(f'{strt.name} {max(1, min(self.duration, int(math.sqrt(loads[intersection.id][strt.name]))))}\n')
    
  def ln_load(self, testcase, streets, cars, intersections):
    filename = testcase.rsplit('.', 1)[0] + '.out'
    loads = self.calc_load(cars)
    with open("out/" + filename, 'w') as file:
      valid_ints = []
      for i in intersections.values():
        d = loads[i.id]
        if any(d.values()):
          valid_ints.append(i)
      file.write(f"{len(valid_ints)}\n")
      
      for intersection in valid_ints:
        file.write(f"{intersection.id}\n")
        
        file.write(f"{len([ strt for strt in intersection.incoming.values() if (loads[intersection.id][strt.name] > 0)] )}\n")
        for strt in intersection.incoming.values():
          if loads[intersection.id][strt.name] > 0:
            file.write(f'{strt.name} {max(1, min(self.duration, int(np.math.log(loads[intersection.id][strt.name], 2.86))))}\n')

  def calc_load(self, cars):
    loads = defaultdict(lambda: defaultdict(int))
    interest_rate = 1
    for c in cars:
      for i, s in enumerate(c.streets):
        loads[s.end_intersection.id][s.name] += 1

    return loads
    