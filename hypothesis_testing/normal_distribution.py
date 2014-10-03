#!/bin/python
# -*- coding: shift-jis -*-

import sys
import math

DISTRIBUTION_Z = 'z'
DISTRIBUTION_T = 't'

class distribution:
    def get_distribution_name(self,):
        return self._name
    def find_p(self, obs):
        try:
            p = self._table[obs]
        except IndexError:
            sys.stderr.write("v (degree of freedom) not found.\n")
            sys.exit()
        return
    def compute_ktr(self, samples): # ktr Kentei Toukei Ryou
        # override me
        return
    def is_significant(self, ktr,
                       significant_level, both_sided = True):
        p = self.find_p(ktr)
        if both_sided:
            return p > (significant_level / 2.0)
        return p > significant_level

class zDistribution(distribution):
    def __init__(self,
                 ):
        self._name = DISTRIBUTION_Z
        self._table = False # TODO
        return
    def compute_ktr(self, samples,
                    parent_mean, parent_var): # ktr Kentei Toukei Ryou
        # TODO
        return

class tDistribution(distribution):
    def __init__(self, v, # degree of freedom
                 ):
        self._name = DISTRIBUTION_T
        self._v = v
        self._table = False # TODO
        return
    def compute_ktr(self, samples
                    parent_mean): # ktr Kentei Toukei Ryou
        # TODO
        return

class DistributionDispatcher:
    SAMPLE_BORDER = 100

    def __init__(self, samples, parent_mean, parent_var = False):
        n = len(samples)
        self._dist = self.get_dist(parent_var, n)
        self._ktr = self.compute_ktr(samples, parent_mean, parent_var)
        return
    def dispatch_distribution(self, parent_var, n):
        if parent_var != False: # 母分散が既知
            return zDistribution()
        # 母分散が未知
        if n >= self.SAMPLE_BORDER:
            # 正規分布で近似可能
            return zDistribution()
        return tDistribution()


def main():
    return

if __name__ == '__main__':
    main()
