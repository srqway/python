#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
from sklearn.preprocessing import normalize

array_0 = np.array([3, 4])
result = normalize(array_0[np.newaxis,:]).ravel()
print(result)
