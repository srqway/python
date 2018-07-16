#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
from scipy import linalg

m = np.matrix(\
    [\
        [5, -3, 2],\
        [1, 0, 2],\
        [2, -1, 3]
    ]\
)
result = linalg.det(m)
print(result)