#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import scipy as scipy
from scipy import linalg

A = scipy.array([[0,0,6],[1,2,3],[2,1,4]])
P, L, U = linalg.lu(A)

print("A:")
print(A)

print("P:")
print(P)

print("L:")
print(L)

print("U:")
print(U)
