### "setup"
from mock import Mock
array=[]
agt=[]
ws=[]
agents=[]
counter=0
x=Mock()
agent=Mock()



### "obvious"
counter=counter+1 # Increment the counter
for element in array: # Loop over elements
    pass

### "style1"
for i in range(len(agt)): #for each agent
  agt[i].theta+=ws[i]     # Increment the angle of each agent
                          #by its angular velocity
  agt[i].x+=r*sin(agt[i].theta) #Move the agent by the step-size
  agt[i].y+=r*cos(agt[i].theta) #r in the direction indicated

### "style2"
for agent in agents:
  agent.turn()
  agent.move()

class Agent(object):
   def turn(self):
        self.direction+=self.angular_velocity;
   def move(self):
       self.x+=Agent.step_length*sin(self.direction)
       self.y+=Agent.step_length*cos(self.direction)

### "issues"
x.clear()# Code crashes here sometimes
class Agent(object):
    pass
    # TODO: Implement pretty-printer method
### "issuesOK"
if x.safe_to_clear(): # Guard added as temporary workaround for #32
   x.clear()
### "selfish"
agent.turn() # Turtle Power!
agent.move()
agents[:]=[]# Shredder!
### "rude"
# Stupid supervisor made me write this code
# So I did it while very very drunk.
### "teaching"
# This is how you define a decorator in python
def double(decorated_function):
   # Here, the result function forms a closure over 
   # the decorated function
   def result_function(input):
       return decorated_function(decorated_function(input))
   # The returned result is a function
   return result_function

@double
def try_me_twice():
    pass
### "docstring"
def complex(real=0.0, imag=0.0):
    """Form a complex number.
    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    # code here

### "other"
def __init__(self):
    self.angle=0 # clockwise from +ve y-axis
    nonzero_indices = [] # Use sparse model as memory constrained
