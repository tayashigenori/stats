#!/bin/python
# -*- coding: shift-jis -*-

import sys
import math

DISTRIBUTION_Z = 'z'
DISTRIBUTION_T = 't'

class zDistribution:
    def __init__(self,
                 ):
        self._name = DISTRIBUTION_Z
        self._table = False # TODO
        return
    def get_distribution_name(self,):
        return self._name
    def find_p(self, obs):
        return

class tDistribution:
    def __init__(self, v, # degree of freedom
                 ):
        self._name = DISTRIBUTION_T
        self._v = v
        self._table = False # TODO
        return
    def get_distribution_name(self,):
        return self._name
    def find_p(self, obs):
        try:
            table = self._tables[self._v]
        except IndexError:
            sys.stderr.write("v (degree of freedom) not found.\n")
            sys.exit()
        return

class NormalDistribution:
    SAMPLE_BORDER = 100

    def __init__(self, samples, parent_mean, parent_var = False):
        n = len(samples)
        self._dist = self.get_dist(parent_var, n)
        self._ktr = self.compute_ktr(samples, parent_mean, parent_var)
        return
    def get_distribution(self, parent_var, n):
        if parent_var != False: # 母分散が既知
            return zDistribution()
        # 母分散が未知
        if n >= self.SAMPLE_BORDER:
            # 正規分布で近似可能
            return zDistribution()
        return tDistribution()
    def compute_ktr(self,): # ktr: Kentei Toukei Ryou
        if self._dist.get_distribution_name() = DISTRIBUTION_Z:
            return self.compute_z(samples, parent_mean, parent_var)
        else if self._dist.get_distribution_name() = .DISTRIBUTION_T:
            return self.compute_t(samples, parent_mean, False)
        else:
            sys.stderr.write("unknown distribution!\n")
            sys.exit()
    def is_significant(self, significant_level, both_sided = True):
        p = self._dist.find_p(self._obs)
        if both_sided:
            return p > (significant_level / 2.0)
        return p > significant_level


def main():
    return

if __name__ == '__main__':
    main()
