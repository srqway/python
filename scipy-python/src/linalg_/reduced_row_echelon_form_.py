#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

from sympy import Matrix

m = Matrix(\
    [\
        [1, 2, -4, -4, 5],\
        [2, 4, 0, 0, 2],\
        [2, 3, 2, 1, 5],\
        [-1, 1, 3, 6 ,5]
    ]
)
result = m.rref()
print(result)
