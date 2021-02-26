import unittest
import os

from Car import Car
from Intersection import Intersection
from Solution import Solution
from Street import Street

class TestSubmissionOutput(unittest.TestCase):
  def parse_input(self, filename):
    with open(filename, 'r') as file:
      solution = None
      cars = []
      streets = {}
      intersections = {}
      for i, line in enumerate(file.readlines()):
        if i == 0:
          [D, I, S, V, F] = line.strip().split(' ')
          solution = Solution(int(D),I,S,V,F)
        elif i <= int(S):
          # processing streets
          [start, end, name, length] = line.strip().split(' ')

          if start not in intersections:
            intersections[start] = Intersection(start)
          if end not in intersections:
            intersections[end] = Intersection(end)
          street = Street(name, length, intersections[start], intersections[end])
          streets[street.name] = street
          
          intersections[end].add_incoming(street)
          intersections[start].add_outgoing(street)

        else:
          # processing cars
          street_names = line.strip().split(' ')[1:]
          car_streets = [streets[street_name] for street_name in street_names]
          cars.append(Car(car_streets))

    return solution, cars, streets, intersections

  def test(self):
    with os.scandir("testcases") as input_files:
      for input_file in input_files:
        solution, cars, streets, intersections = self.parse_input(input_file.path)
        solution.ln_load(input_file.name, streets, cars, intersections)

    
if __name__ == '__main__':
    unittest.main()