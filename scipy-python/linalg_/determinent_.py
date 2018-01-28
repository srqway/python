#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
from scipy import linalg

array_0 = np.array([[0,2,3],[4,5,6],[7,8,9]])
result = linalg.det(array_0)
print(result)