### "model"
class Model(object):
    def simulation_step():
        # Maths Here
        pass
### "view"
class View(object):
    def __init__(self, model):
        from matplotlib import pyplot as plt
        self.figure=plt.figure()
        axes=plt.axes()
        self.model=model
        self.scatter=axes.scatter(model.agent_locations()[:,1],
                model.agent_locations()[:,2])
    def update(self):
        self.scatter.set_offsets(model.agent_locations())
### "controller"
def Controller(object):
    def __init__(self):
        self.model=Model() # Or use Builder
        self.view=View(self.model)
        def animate():
            self.model.simulation_step()
            self.view.update()
        self.animator=animate
    def go(self):
        from matplotlib import animation
        animation.FuncAnimation(self.view.figure, self.animator)
