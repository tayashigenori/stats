#!/bin/python
# -*- coding: shift-jis -*-

SAMPLE_BORDER = 100

import sys
import math

class nDistribution:
    def __init__(self,
                 ):
        self._table = False # TODO
        return
    def find_p(self, obs):
        return

class tDistribution:
    def __init__(self, v, # degree of freedom
                 ):
        self._v = v
        self._table = False # TODO
        return
    def find_p(self, obs):
        try:
            table = self._tables[self._v]
        except IndexError:
            sys.stderr.write("v (degree of freedom) not found.\n")
            sys.exit()
        return

class NormalDistribution:
    def __init__(self, data, parent_mean, parent_var = False):
        self._n = len(data)
        if parent_var != False: # 母分散が既知
            self._dist = nDistribution()
            self._obs = self.compute_z(data, parent_mean, parent_var)
        else: # 母分散が未知
            if self._n >= SAMPLE_BORDER:
                self._dist = nDistribution()
                self._obs = self.compute_z(data, parent_mean, False)
            else:
                self._dist = tDistribution(v = n-1)
                self._obs = self.compute_t(data, parent_mean)
        return
    def is_significant(self, significant_level, both_sided = True):
        p = self._dist.find_p(self._obs)
        if both_sided:
            return p > (significant_level / 2.0)
        return p > significant_level


def main():
    return

if __name__ == '__main__':
    main()
