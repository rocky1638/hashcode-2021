class Car:
  def __init__(self, streets):
    self.streets = streets
    self.num_streets = len(streets)
    self.next_street = 0
    self.time_to_intersection = 0
    self.finish_time = None
    # add to first intersection
    self.streets[self.next_street].queue.append(self)

  def __str__(self):
    return(f"""
    Car:
      next_intersection: {self.streets[self.next_street].end_intersection.id}
      time_to_intersection: {self.time_to_intersection}
      is_done: {self.is_done()}
    """)
