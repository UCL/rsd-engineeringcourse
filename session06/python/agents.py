### "model"
class AgentModel(object):
  def simulate(self):
    for agent in agents:
      for target in agents:
        agent.interact(target)
      agent.simulate()
### "construct"
class AgentModel(object):
  def __init__(self, config):
    self.agents=[]
    for agent_config in config:
      self.agents.append(self.create(**agent_config))

### "boids"
class BirdModel(AgentModel):
  def create(self, species):
    return Boid(species)

### "web"
class WebAgentFactory(AgentModel):
  def __init__(self, url):
    self.url=url
    connection=AmazonCompute.connect(url)
    AgentModel.__init__(self)
  def create(self, species):
    return OnlineAnimal(species, connection)
