#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

from sympy import Point3D, Plane
plane_0 = Plane(Point3D(3, 0, 0), normal_vector=(1, 2, -1))
plane_1 = Plane(Point3D(0, 0, 1), normal_vector=(2, 3, 1))
plane_0.intersection(plane_1)
