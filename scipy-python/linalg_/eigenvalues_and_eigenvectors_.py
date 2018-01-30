#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
from scipy import linalg


m = np.matrix(\
    [\
        [7, 1, -2],\
        [-3, 3, 6],\
        [2, 2, 2]
    ]\
)
w, vl = linalg.eig(m)
print(w)
print(vl)
