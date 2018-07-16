#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np

# projection v onto u
v = np.array([-1, 3])
u = np.array([2, 1])
result = (np.dot(v, u) / np.dot(u, u)) * u
print(result)
