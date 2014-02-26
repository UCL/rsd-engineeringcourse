"""  Simplistic 1-dimensional diffusion model """
def energy(density, coefficient=1):
  """ Energy associated with the diffusion model

      :Parameters:
        density: array of positive integers
           Number of particles at each position i in the array/geometry
  """
  from numpy import array, any, sum

  # Make sure input is an array
  density = array(density)

  # of the right kind (integer). Unless it is zero length, in which case type does not matter.
  if density.dtype.kind != 'i' and len(density) > 0:
    raise TypeError("Expected array of *integers*.")
  # and the right values (positive or null)
  if any(density < 0): raise ValueError("Expected array of *positive* integers.")
  
  if False:
    print "hello, I'm not covered"

  return coefficient * 0.5 * sum(density * (density - 1))

def this_is_a_fake_routine(something):
  print "hello, I'm not covered"
