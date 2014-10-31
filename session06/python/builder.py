### "nobuilder"

class Model(object):
    def __init__(self, xsize, ysize,
                 agent_count, wind_speed,
                 agent_sight_range, eagle_start_location):
        pass

### "simplemodel"

Model=Mock()

### "builder"

class ModelBuilder(object):
    def start_model():
        self.model=Model()
    def set_bounds(xlim, ylim):
        self.model.xlim=xlim
        self.model.ylim=ylim
    def add_agent(xpos, ypos):
        pass # Implementation here
    def finished_model():
        return self.model

### "use"

builder=ModelBuilder()
builder.start_model()
builder.set_bounds(500,500)
builder.add_agent(40,40)
builder.add_agent(400,100)
model=builder.finish()
model.simulate()
