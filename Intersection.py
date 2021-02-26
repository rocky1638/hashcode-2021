class Intersection:
  def __init__(self, id):
    self.id = id
    self.incoming = {}
    self.outgoing = {}
    self.light = None

  def __str__(self):
    return(f"""
    Intersection:
      id: {self.id}
      incoming: {self.incoming}
      outgoing: {self.outgoing}
      light: {self.light}
    """)

  def add_incoming(self, street):
    self.incoming[street.name] = street
  
  def add_outgoing(self, street):
    self.outgoing[street.name] = street
