import numpy as np
from numpy import uint8

fastiecm_IS = np.array([[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[255, 0, 0]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]],
[[49, 127, 67]]], dtype=uint8)
