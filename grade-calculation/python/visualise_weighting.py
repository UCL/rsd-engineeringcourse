from linear_weighting import linear_weighting
from weighted_phi import WeightedPhi

# This is the function psi as it appears in the tex document
inner = linear_weighting(0.2, 0.825)
# This is the function mathcal{P} as it appears in the tex document
weighting = WeightedPhi(min_value=0.4, max_value=1.1, inner=inner)

weighting.plot()
