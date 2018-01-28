#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
from scipy import linalg

array_0 = np.array([[1,2,-1],[2,2,4],[1,3,-3]])
result = linalg.inv(array_0)
print(result)