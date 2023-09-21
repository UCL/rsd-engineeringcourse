# ---
# jupyter:
#   jekyll:
#     display_name: The Boids
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## The Boids!
#
# This section shows an example of using NumPy to encode a model of how a group of birds or other animals moves. It is based on [a paper by Craig W. Reynolds](http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/). Reynolds calls the simulated creatures "bird-oids" or "boids", so that's what we'll be calling them here too.

# %% [markdown]
# ### Flocking

# %% [markdown]
#
# > The aggregate motion of a flock of birds, a herd of land animals, or a school of fish is a beautiful and familiar
# part of the natural world... The aggregate motion of the simulated flock is created by a distributed behavioral model much
# like that at work in a natural flock; the birds choose their own course. Each simulated bird is implemented as an independent
# actor that navigates according to its local perception of the dynamic environment, the laws of simulated physics that rule its
# motion, and a set of behaviors programmed into it... The aggregate motion of the simulated flock is the result of the
# dense interaction of the relatively simple behaviors of the individual simulated birds. 
#
# -- Craig W. Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model", *Computer Graphics* **21** _4_ 1987, pp 25-34

# %% [markdown]
# The model includes three main behaviours which, together, give rise to "flocking". In the words of the paper:
#
# * Collision Avoidance: avoid collisions with nearby flockmates
# * Velocity Matching: attempt to match velocity with nearby flockmates
# * Flock Centering: attempt to stay close to nearby flockmates

# %% [markdown]
# ### Setting up the Boids

# %% [markdown]
# Our boids will each have an x velocity and a y velocity, and an x position and a y position.

# %% [markdown]
# We'll build this up in NumPy notation, and eventually, have an animated simulation of our flying boids.

# %%
import numpy as np

# %% [markdown]
# Let's start with simple flying in a straight line.

# %% [markdown]
# Our positions, for each of our N boids, will be an array, shape $2 \times N$, with the x positions in the first row,
# and y positions in the second row.

# %%
boid_count = 10

# %% [markdown]
# We'll want to be able to seed our Boids in a random position.

# %% [markdown]
# We'd better define the edges of our simulation area:

# %%
limits = np.array([2000, 2000])

# %%
positions = np.random.rand(2, boid_count) * limits[:, np.newaxis]
positions

# %%
positions.shape

# %% [markdown]
# We used **broadcasting** with np.newaxis to apply our upper limit to each boid.
# `rand` gives us a random number between 0 and 1. We multiply by our limits to get a number up to that limit.

# %%
limits[:, np.newaxis]

# %%
limits[:, np.newaxis].shape

# %%
np.random.rand(2, boid_count).shape


# %% [markdown]
# So we multiply a $2\times1$ array by a $2 \times 10$ array -- and get a $2\times 10$ array.

# %% [markdown]
# Let's put that in a function:

# %%
def new_flock(count, lower_limits, upper_limits):
    width = upper_limits - lower_limits
    return (lower_limits[:, np.newaxis] + np.random.rand(2, count) * width[:, np.newaxis])


# %% [markdown]
# For example, let's assume that we want our initial positions to vary between 100 and 200 in the x axis, and 900 and 1100 in the y axis. We can generate random positions within these constraints with:
# ```python
# positions = new_flock(boid_count, np.array([100, 900]), np.array([200, 1100]))
# ```

# %% [markdown]
# But each bird will also need a starting velocity. Let's make these random too:
#
# We can reuse the `new_flock` function defined above, since we're again essentially just generating random numbers from given limits. This saves us some code, but keep in mind that using a function for something other than what its name indicates can become confusing!
#
# Here, we will let the initial x velocities range over $[0, 10]$ and the y velocities over $[-20, 20]$.

# %%
velocities = new_flock(boid_count, np.array([0, -20]), np.array([10, 20]))
velocities

# %% [markdown]
# ### Flying in a Straight Line

# %% [markdown]
# Now we see the real amazingness of NumPy: if we want to move our *whole flock* according to
#
# $\delta_x = \delta_t \cdot \frac{dv}{dt}$

# %% [markdown]
# we just do:

# %%
positions += velocities

# %% [markdown]
# ### Matplotlib Animations

# %% [markdown]
# So now we can animate our Boids using the matplotlib animation tools. All we have to do is import the relevant libraries:

# %%
from matplotlib import animation
from matplotlib import pyplot as plt
# %matplotlib inline

# %% [markdown]
# Then, we make a static plot, showing our first frame:

# %%
# create a simple plot
# initial x position in [100, 200], initial y position in [900, 1100]
# initial x velocity in [0, 10], initial y velocity in [-20, 20]
positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))

figure = plt.figure()
axes = plt.axes(xlim=(0, limits[0]), ylim=(0, limits[1]))
scatter = axes.scatter(positions[0, :], positions[1, :],
                       marker='o', edgecolor='k', lw=0.5)
scatter


# %% [markdown]
# Then, we define a function which **updates** the figure for each timestep

# %%
def update_boids(positions, velocities):
    positions += velocities


def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose())


# %% [markdown]
# Call `FuncAnimation`, and specify how many frames we want:

# %%
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

# %% [markdown]
# Save out the figure:

# %%
positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
anim.save('boids_1.mp4')

# %% [markdown]
# And download the [saved animation](http://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch02data/boids_1.mp4).

# %% [markdown]
# You can even view the results directly in the notebook.

# %%
from IPython.display import HTML
HTML(anim.to_jshtml())

# %% [markdown]
# ### Fly towards the middle

# %% [markdown]
# Boids try to fly towards the middle:

# %%
positions = new_flock(4, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(4, np.array([0, -20]), np.array([10, 20]))

# %%
positions

# %%
velocities

# %%
middle = np.mean(positions, 1)
middle

# %%
direction_to_middle = positions - middle[:, np.newaxis]
direction_to_middle

# %% [markdown]
# This is easier and faster than:
#
# ``` python
# for bird in birds:
#     for dimension in [0, 1]:
#         direction_to_middle[dimension][bird] = positions[dimension][bird] - middle[dimension]
# ```

# %%
move_to_middle_strength = 0.01
velocities = velocities - direction_to_middle * move_to_middle_strength


# %% [markdown]
# Let's update our function, and animate that:

# %%
def update_boids(positions, velocities):
    move_to_middle_strength = 0.01
    middle = np.mean(positions, 1)
    direction_to_middle = positions - middle[:, np.newaxis]
    velocities -= direction_to_middle * move_to_middle_strength
    positions += velocities


# %%
def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose())


# %%
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

# %%
positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
HTML(anim.to_jshtml())

# %% [markdown]
# ### Avoiding collisions

# %% [markdown]
# We'll want to add our other flocking rules to the behaviour of the Boids.

# %% [markdown]
# We'll need a matrix giving the distances between each bird. This should be $N \times N$.

# %%
positions = new_flock(4, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(4, np.array([0, -20]), np.array([10, 20]))

# %% [markdown]
# We might think that we need to do the X-distances and Y-distances separately:

# %%
xpos = positions[0, :]

# %%
xsep_matrix = xpos[:, np.newaxis] - xpos[np.newaxis, :]

# %%
xsep_matrix.shape

# %%
xsep_matrix

# %% [markdown]
# But in NumPy we can be cleverer than that, and make a $2 \times N \times N$ matrix of separations:

# %%
separations = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]

# %%
separations.shape

# %% [markdown]
# And then we can get the sum-of-squares $\delta_x^2 + \delta_y^2$ like this:

# %%
squared_displacements = separations * separations

# %%
square_distances = np.sum(squared_displacements, 0)

# %%
square_distances

# %% [markdown]
# Now we need to find birds that are too close:

# %%
alert_distance = 2000
close_birds = square_distances < alert_distance
close_birds

# %% [markdown]
# Find the direction distances **only** to those birds which are too close:

# %%
separations_if_close = np.copy(separations)
far_away = np.logical_not(close_birds)

# %% [markdown]
# Set `x` and `y` values in `separations_if_close` to zero if they are far away:

# %%
separations_if_close[0, :, :][far_away] = 0
separations_if_close[1, :, :][far_away] = 0
separations_if_close

# %% [markdown]
# And fly away from them:

# %%
np.sum(separations_if_close, 2)

# %%
velocities = velocities + np.sum(separations_if_close, 2)


# %% [markdown]
# Now we can update our animation:

# %%
def update_boids(positions, velocities):
    move_to_middle_strength = 0.01
    middle = np.mean(positions, 1)
    direction_to_middle = positions - middle[:, np.newaxis]
    velocities -= direction_to_middle * move_to_middle_strength

    separations = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]
    squared_displacements = separations * separations
    square_distances = np.sum(squared_displacements, 0)
    alert_distance = 100
    far_away = square_distances > alert_distance
    separations_if_close = np.copy(separations)
    separations_if_close[0, :, :][far_away] = 0
    separations_if_close[1, :, :][far_away] = 0
    velocities += np.sum(separations_if_close, 1)

    positions += velocities


# %%
def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose())


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
HTML(anim.to_jshtml())


# %% [markdown]
# ### Match speed with nearby birds

# %% [markdown]
# This is pretty similar:

# %%
def update_boids(positions, velocities):
    move_to_middle_strength = 0.01
    middle = np.mean(positions, 1)
    direction_to_middle = positions - middle[:, np.newaxis]
    velocities -= direction_to_middle * move_to_middle_strength

    separations = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]
    squared_displacements = separations * separations
    square_distances = np.sum(squared_displacements, 0)
    alert_distance = 100
    far_away = square_distances > alert_distance
    separations_if_close = np.copy(separations)
    separations_if_close[0, :, :][far_away] = 0
    separations_if_close[1, :, :][far_away] = 0
    velocities += np.sum(separations_if_close, 1)

    velocity_differences = velocities[:, np.newaxis, :] - velocities[:, :, np.newaxis]
    formation_flying_distance = 10000
    formation_flying_strength = 0.125
    very_far = square_distances > formation_flying_distance
    velocity_differences_if_close = np.copy(velocity_differences)
    velocity_differences_if_close[0, :, :][very_far] = 0
    velocity_differences_if_close[1, :, :][very_far] = 0
    velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

    positions += velocities


# %%
def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose())


anim = animation.FuncAnimation(figure, animate,
                               frames=200, interval=50)


positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
HTML(anim.to_jshtml())

# %% [markdown]
# Hopefully the power of NumPy should be pretty clear now. This would be **enormously slower** and harder to understand using traditional lists.
