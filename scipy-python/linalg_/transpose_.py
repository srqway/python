#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np

m = np.matrix(\
    [\
        [1, 2],\
        [3, 4]
    ]\
)
result = m.transpose()
print(result)