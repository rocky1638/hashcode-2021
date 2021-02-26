from collections import deque

class Street:
  def __init__(self, name, length, start_intersection, end_intersection):
    self.name = name
    self.length = length
    self.start_intersection = start_intersection
    self.end_intersection = end_intersection
    self.queue = deque([])

  def __str__(self):
    return (f"""
    Street:
      name: {self.name}
      length: {self.length}
      start_intersection: {self.start_intersection.id}
      end_intersection: {self.end_intersection.id}
      queue: {[str(car) for car in self.queue]}
    """)