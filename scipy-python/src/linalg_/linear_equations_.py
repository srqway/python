#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np

#3 * x0 + x1 = 9 and x0 + 2 * x1 = 8:
x = np.array([[3,1], [1,2]])
c = np.array([9,8])
result = np.linalg.solve(x, c)
print(result)
