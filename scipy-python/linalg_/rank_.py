#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np

m = np.matrix(\
    [\
        [1, -1, -1, 2, 1],\
        [2, -2, -1, 3, 3],\
        [-1, 1, -1, 0, -3]\
    ]\
)
result = np.linalg.matrix_rank(m)
print(result)