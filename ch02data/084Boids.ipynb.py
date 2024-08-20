# ---
# jupyter:
#   jekyll:
#     display_name: The Boids
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # The Boids!
#
# Now that we have covered the basics of both NumPy and Matplotlib, we will go through an extended example of using these libaries to run and visualise a simulation of flocking dynamics.
#
# ## Flocking
#
#
# > The aggregate motion of a flock of birds, a herd of land animals, or a school of fish is a beautiful and familiar
# part of the natural world... The aggregate motion of the simulated flock is created by a distributed behavioral model much
# like that at work in a natural flock; the birds choose their own course. Each simulated bird is implemented as an independent actor that navigates according to its local perception of the dynamic environment, the laws of simulated physics that rule its motion, and a set of behaviors programmed into it... The aggregate motion of the simulated flock is the result of the dense interaction of the relatively simple behaviors of the individual simulated birds. 
#
# &mdash; Craig W. Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model", *Computer Graphics* **21** _4_ 1987, pp 25-34 (see the [original paper](http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/))
#
# A basic model of flocking behaviour can be derived from [three basic rules](https://en.wikipedia.org/wiki/Boids)
#
# > * *Collision avoidance*: avoid collisions with nearby flockmates.
# > * *Velocity matching*: attempt to match velocity with nearby flockmates.
# > * *Flock centering*: attempt to stay close to nearby flockmates.
#
# We will use a simple two-dimensional model in which the state of the *n*<sup>th</sup> *boid* (short for *bird-oid* or flock member) is described by a position vector $\boldsymbol{x}_n = (x_{n,0}, x_{n,1})$ and velocity $\boldsymbol{v}_n = (v_{n,0}, v_{n,1})$. We will represent our flock state as NumPy arrays, implement our simulation dynamics using NumPy array operations and use the [animation capabilities of Matplotlib](https://matplotlib.org/stable/api/animation_api.html) to create animated simulations of our flying boids. We first import the relevant modules `numpy`, `matlotlib.pyplot` and `matplotlib.animation` and [set Matplotlib animations to default to being represented as interactive JavaScript widgets in the notebook interface](http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/).

# %%
import numpy as np
from matplotlib import pyplot as plt, animation
plt.rcParams['animation.html'] = 'jshtml'

# %% [markdown]
# ## Initialising the simulation
#
# We will represent the positions and velocities of all the boids as a pair of two-dimensional arrays, both with shape `(num_boids, 2)` where `num_boids` is an integer determining the number of boids. We need to set initial values for these arrays, representing the positions and velocities at the start of the simulation. Here we will use a NumPy random number generator object to sample random initial values for the positions and velocities from some distribution. 
#
# Generation of random number is a very common task in research software, but a topic with lots of important subtleties. A common pattern in many programming languages is to use a *global* random number generator which has a state which is updated by every call to random number generation routines. Use of global state like this breaks the usual expectation that for fixed inputs a function will produce fixed outputs, can lead to hard to diagnose bugs and make it difficult to ensure reproducibility of our research.
#
# To avoid these issues we will create an instance of [the NumPy `Generator` class](https://numpy.org/doc/stable/reference/random/generator.html), which encapsulates the state of a random number generator plus methods to produce random numbers from specified distributions, and explicitly pass this in to functions in which we wish to generate random numbers. We will also fix the initial state of the random number generator by explicitly specifying a *seed* value, meaning we can reproduce our results. The easiest way to produce a seeded `Generator` object is using the `np.random.default_rng` function and passing in integer `seed` argument

# %%
rng = np.random.default_rng(seed=21878533808081494313)


# %% [markdown]
# The `rng` object we just created provides methods for producing from various different probability distributions. Here we generate random values uniformly distributed over a specified interval using [the `Generator.uniform` method](https://numpy.org/doc/stable/reference/random/generator.html). We can inspect the docstring for this method by running `rng.uniform?` (if in a Jupyter notebook or IPython interpreter) or `help(rng.uniform)` (in any Python interpreter).
#

# %%
# rng.uniform?

# %% [markdown]
# Helpfully, `Generator.uniform` accepts a `size` argument allowing us to generate an array of random samples of a specified *shape* (the argument is named `size` rather than `shape` to avoid clashing with the usage of shape as the standard name for a parameter of some probability distributions). We can also specify array-like arguments for the `low` and `high` parameters specifying the lower and upper bounds of the interval the distribution is defined on, these should either match the shape specified by `size` or be of a compatible shape for *broadcasting*. Below we define a function which given a `Generator` object `rng` and optional arguments specifying the number of boids `num_boids`, minimum and maximum of the intervals to draw the positions (`min_position` and `max_position`) and velocities (`min_velocity` and `max_velocity`) from, outputs a pair of arrays `positions` and `velocities`, both of shape `(num_boids, 2)`, corresponding to the sampled position and velocities values respectively.

# %%
def initialise_boid_states(
    rng, 
    num_boids=100,
    min_position=(100, 900), 
    max_position=(200, 1100), 
    min_velocity=(0, -20), 
    max_velocity=(10, 20)
):
    """Generate random initial states for the boids.
    
    Args:
        rng: NumPy random number generator object.
        num_boids: Number of boids to generate states for.
        min_position: Length 2 sequence defining lower bounds for 
           interval to uniformly generate positions from.
        max_position: Length 2 sequence defining upper bounds for
           interval to uniformly generate position from.
        min_velocity: Length 2 sequence defining lower bounds for 
           interval to uniformly generate velocities from.
        max_velocity: Length 2 sequence defining upper bounds for
           interval to uniformly generate velocities from.
        
    Returns:
        Tuple of two arrays `(positions, velocities)`, both of shape
        `(num_boids, 2)` corresponding to respectively the positions and
        velocities of boids.
    """
    positions = rng.uniform(min_position, max_position, size=(num_boids, 2))
    velocities = rng.uniform(min_velocity, max_velocity, size=(num_boids, 2))
    return positions, velocities


# %% [markdown]
# We can call this function with our `rng` random number generator object (and default values for the other arguments) to generate random initial values for the `positions` and `velocities` arrays.

# %%
positions, velocities = initialise_boid_states(rng)


# %% [markdown]
# ## Visualising the boids
#
# Now that we have initialised the state of our simulation, we are ready to start visualising our boids. As we have assumed our boids exist in two-dimensions, we can use Matplolib's extensive range of plotting functions for two-dimensional data. Ideally we want to represent both the instantenous positions and velocities of the boids in our visualisation. We will use a [Matplotlib *quiver* plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html) to do this, representing each boid as an arrow located on the plot axes at a point corresponding to its simulated position, and with the direction of the arrow representing its current heading. While we could also represent its speed by the size of the arrow, we choose here to keep the arrows all the same size - this requires calculating the *unit vectors* (vectors of length one) corresponding to the velocity vectors, which can be done efficiently with broadcasted array operations in NumPy. We wrap the code for plotting the boids into a function to allow for easy reuse. We return the generated Matplotlib figure and axis (subplot) objects, along with *artist* object representing the quiver plot arrows returned by the `quiver` call, to allow us to make calls to these objects outside of the function.

# %%
def calculate_unit_vectors(vectors):
    """Calculate the length-one vectors corresponding to an array of vectors.
    
    Args:
        vectors: Array with last dimension corresponding to vector dimension.
    
    Returns:
        Array of same shape as `vectors` with Euclidean norm along last axis
        equal to one.
    """
    return vectors / (vectors**2).sum(-1)[..., np.newaxis]**0.5


def plot_boids(positions, velocities, figsize=(8, 8), xlim=(0, 2000), ylim=(0, 2000)):
    """Create visual representation of boids as quiver plot.
    
    Args:
        positions: Array of shape `(num_boids, 2)` defining positions of boids.
        velocities: Array of shape `(num_boids, 2)` defining velocities of boids.
        figsize: Tuple defining figure dimension `(width, height)` in inches.
        xlim: Tuple `(min, max)` defining extents of horizontal axis.
        ylim: Tuple `(min, max)` defining extents of vertical axis.
    
    Returns:
        Tuple containing Matplotlib figure, axis and artist corresponding to plot.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set(xlim=xlim, ylim=ylim, xlabel="$x_0$ coordinate", ylabel="$x_1$ coordinate")
    velocity_unit_vectors = calculate_unit_vectors(velocities)
    arrows = ax.quiver(
        positions[:, 0],  # horizontal coordinates for origin points for arrows
        positions[:, 1],  # vertical coordinates for origin points of arrows
        velocity_unit_vectors[:, 0],  # horizontal component of arrow vectors
        velocity_unit_vectors[:, 1],  # vertical component of arrow vectors
        scale=40,  # size of arrows
        angles='xy',  # convention used for specifying arrow directions
        color='C0',  # color of arrows - set to first value in default color cycle
        pivot='middle'  # plot middle of arrows at specified origin points
    )
    return fig, ax, arrows


# %% [markdown]
# We can now produce a (rather boring) visualisation of our boids in their initial state.

# %%
fig, ax, arrows = plot_boids(positions, velocities)


# %% [markdown]
# ## Simulating the model dynamics
#
# We will model the boids as being subject to forces corresponding to the three rules described above. Newton's second law of motion tells use that the acceleration of a body (rate of change of velocity) is proportional to the net force acting on it, with the velocity in turn being the rate in change of the position of the object. In mathematical notation, if $F_{k,n}$ is a function which calculates the value of the $k$th force on the $n$th boid given the positions and velocities of all the boids then we have that
#
#
# $$
#   \frac{\mathrm{d}\boldsymbol{x}_{0:N}}{\mathrm{d}t} = \boldsymbol{v}_{0:N}, \qquad
#   \frac{\mathrm{d}\boldsymbol{v}_{0:N}}{\mathrm{d}t} = \sum_{k=1}^K F_{k,n}(\boldsymbol{x}_{0:N}, \boldsymbol{v}_{0:N}).
# $$
#
# Note that it is not a problem if you are not familiar with the notation here - understanding the mathematics behind the model is non-essential! There are a variety of numerical approaches for approximately simulating dynamics of this form. Here we will use a particularly simple to implement numerical method which corresonds to the approximation that for a small timestep $\delta t$ that
#
# $$
#   \boldsymbol{x}_{0:N}(t + \delta t) \approx \boldsymbol{x}_{0:N}(t) + \delta t \boldsymbol{v}_{0:N}(t), \qquad
#   \boldsymbol{v}_{0:N}(t + \delta t) \approx \boldsymbol{x}_{0:N}(t) + \delta t \sum_{k=1}^K F_k(\boldsymbol{x}_{0:N}(t + \delta t), \boldsymbol{v}_{0:N}(t)).
# $$
#
# Using NumPy array operations we can implement this numerical scheme efficiently by updating the positions and velocities for all boids simulateneously. We wrap this into a function `simulate_timestep` below that updates the `positions` and `velocities` arrays in-place.

# %%
def simulate_timestep(positions, velocities, forces, timestep):
    """Simulate model dynamics forward one timestep, updating states in-place.
    
    Args:
        positions: Array of shape `(num_boids, 2)` defining positions of boids.
        velocities: Array of shape `(num_boids, 2)` defining velocities of boids.
        forces: Sequence of functions computing forces on boids given positions
            and velocities of all boids.
        timestep: Scalar timestep to use for numerical integrator.
    """
    positions += timestep * velocities
    velocities += timestep * sum(force(positions, velocities) for force in forces)


# %% [markdown]
# ## Creating an animation of the simulation
#
# Now that we have a function to update the boid states according to the model dynamics, we are ready to produce animations visualising the simulated dynamics over time. To do this we will use [the `FuncAnimation` class from the `matplotlib.animation` module](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html). We can inspect the docstring for the initialiser for this class:

# %%
# animation.FuncAnimation?

# %% [markdown]
# We see that `FuncAnimation` produces an animation by repeatedly calling a specified function to update the animation 'frame', which corresponds to a Matplotlib figure instance. As well as the figure object to use and function updating the frames, we need to specify the `frames` argument - here we do this with an integer corresponding to the number of frames to animate. Finally we specify an optional argument `interval` corresponding to the delay between each frame being shown in milliseconds. Again we wrap all of this into a function to allow for easy reuse.

# %%
def animate_flock(positions, velocities, forces=(), timestep=1., num_step=100):
    """Visualise the dynamics of the boids as a Matplotlib animation.
    
    Args:
        positions: Array of shape `(num_boids, 2)` defining positions of boids.
        velocities: Array of shape `(num_boids, 2)` defining velocities of boids.
        forces: Sequence of functions computing forces on boids given positions
            and velocities of all boids.
        timestep: Scalar timestep to use for numerical integrator.
        num_step: Number of timesteps to simulate in animation.
    
    Returns:
        Matplotlib animation of simulated boid dynamics.
    """
    fig, ax, arrows = plot_boids(positions, velocities)

    def update_frame(frame_index):
        simulate_timestep(positions, velocities, forces, timestep)
        velocity_unit_vectors = calculate_unit_vectors(velocities)
        arrows.set_offsets(positions)
        arrows.set_UVC(velocity_unit_vectors[:, 0], velocity_unit_vectors[:, 1])
        return [arrows]
    
    # Close Matplotlib figure object to avoid displaying static figure as well as animation
    plt.close(fig)
    return animation.FuncAnimation(fig, update_frame, num_step, interval=50)


# %% [markdown]
# We are now ready to produce our first animation! We generate initial positions and velocities using our `initialise_boid_states` function and then pass these to the `animate_flock` function, using the default values for the other arguments for now, with in particular we not specifying any forces acting on the boids for now.

# %%
positions, velocities = initialise_boid_states(rng)
animate_flock(positions, velocities)


# %% [markdown]
# Though our boids are now moving, we see that they have the rather uninteresting behaviour of moving perpetually in a straight line. To get more interesting flocking like behaviour we need to specify some forces.
#
# ## Specifying the flocking dynamics
#
# Now that we have our simulation and animation framework set up, we are ready to start defining the forces corresponding to the flocking behaviour rules we encountered at the start of the notebook.
#
# ### *Cohesion*: staying close to nearby flockmates
#
# <a title="Craig Reynolds, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Rule_cohesion.gif"><img width="217" alt="Rule cohesion" src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Rule_cohesion.gif"><br /><em>Credit: Craig Reynolds (public domain)</em></a>
#
# The first behaviour we consider is the tendency for flocks to remain close to flockmates, which we term *cohesion*. We represent this as a force which pushes the flock members towards the mean point of surrounding flock members, that is the force exerted is proportional to the difference between the mean flock position and the current flock members position. We can implement this efficiently using broadcasted NumPy array operations:

# %%
def cohesion_force(positions, velocities, cohesion_strength=0.01):
    return cohesion_strength * (positions.mean(axis=0)[np.newaxis] - positions)


# %% [markdown]
# Now that we have defined our first force function, we can create a new animation with this force applied:

# %%
positions, velocities = initialise_boid_states(rng)
animate_flock(positions, velocities, [cohesion_force])


# %% [markdown]
# Our boids now show a more interesting dynamic behaviour, staying together as one cohesive unit. We see however that a lot of the time boids appear to be in (near) collisions with each other.
#
# ### *Separation*: avoiding collisions with nearby flockmates
#
# <a title="Craig Reynolds, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Rule_separation.gif"><img width="217" alt="Rule separation" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Rule_separation.gif"><br /><em>Credit: Craig Reynolds (public domain)</em></a>
#
# The second behaviour that we consider it tendency of flockmates to avoid collisions with each other. We represent this as a force which for each pair of boids within a certain distance of each other, exerts a force which pushes the boids away from each other so that the displacement beween them increases, by acting along the line of displacement. To only sum the displacements over the pairs of boids within a specified distance of each other we can use [the `numpy.where` function](https://numpy.org/doc/stable/reference/generated/numpy.where.html). Calling 
# ```Python
# values = np.where(conditions, values_if_true, values_if_false)
# ```
# creates an array `values` such that for an index `i` (either a single integer for one-dimensional arrays or tuple of integers for multidimensional arrays) `values[i]` is equal to `values_if_true[i]` if `conditions[i]` is `True` and `values_if_false[i]` otherwise. All of the array arguments `conditions`, `values_if_true` and `values_if_false` should be of compatible shapes - that is of the same shape, or of shapes that can be broadcast (remember that a scalar is compatible for broadcasting with an array of any shape).

# %%
def separation_force(positions, velocities, separation_strength=1., separation_distance=10.):
    displacements = positions[np.newaxis] - positions[:, np.newaxis]
    are_close = (displacements**2).sum(-1)**0.5 <= separation_distance
    return separation_strength * np.where(are_close[..., None], displacements, 0).sum(0)


# %% [markdown]
# We can now run and animate a simulation with both the forces we have defined:

# %%
positions, velocities = initialise_boid_states(rng)
animate_flock(positions, velocities, [cohesion_force, separation_force])


# %% [markdown]
# ### *Alignment*: matching velocity with nearby flockmates
#
# <a title="Craig Reynolds, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Rule_alignment.gif"><img width="217" alt="Rule alignment" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Rule_alignment.gif"><br /><em>Credit: Craig Reynolds (public domain)</em></a>
#
# The final rule we consider is a little different in that it specifies a relationship between the *velocities* rather than *positions* of the boids. The *alignment* rule specifies that nearby flockmates should tend to match velocities with each other. We can implement this as a force which is negatively proportional to the velocity differences between pairs of boids within a certain distance of each other. We can use a similar implementation to that for `separation_force`:

# %%
def alignment_force(positions, velocities, alignment_strength=0.125, alignment_distance=100):
    displacements = positions[np.newaxis] - positions[:, np.newaxis]
    velocity_differences = velocities[np.newaxis] - velocities[:, np.newaxis]
    are_close = (displacements**2).sum(-1)**0.5 <= alignment_distance
    return -alignment_strength * np.where(are_close[..., None], velocity_differences, 0).mean(0)


# %% [markdown]
# Now we are finally ready to run and animate a simulation with forces for all three rules defined:

# %%
positions, velocities = initialise_boid_states(rng)
animate_flock(positions, velocities, [cohesion_force, separation_force, alignment_force])

# %% [markdown]
# ## Conclusion and extensions
#
# Hopefully this example has illustrated the power and convenience of NumPy. Implementing an equivalent model using native Python data structures such as lists to represent the states of the boids would both result in code that was slower to run and harder to read.
#
# If you are interested in exploring this model further here are some ideas for extensions
#
#   * Currently the cohesion force applies globally rather than only acting locally on boids within a certain distance of each other like the other two forces. Can you alter the implementation to have a similar behaviour of only acting over a finite distance?
#   * There are various model parameters such as the relative force strengths `cohesion_strength`, `separation_strength` and `alignment_strength` which are currently left as the default values specified in the force function definitions. Can you redesign the `simulate_timestep` and/or `animate_flock` to allow passing in a dictionary of these parameter values to override the default to allow easily visualising the behaviour for different parameters?
#   * Currently our boids exist in a two-dimensional world - can you alter the simulation to work in three-dimensions? You may find [Matplotlib's three-dimensional plotting toolkit](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) useful for the visualisation side.
#
#
