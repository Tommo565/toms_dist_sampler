import numpy as np
from distribution_sampler import DistributionSampler as DS
from distribution_sampler import distribution_sampler as ds


# Testing the distribution_sampler function

def test_distribution_sampler():
    '''
    Unit Test for the distribution_sampler function. This tests:
        * That the type is np.ndarray
        * That the length of the array is 20
        * That the first and last items in the array equal 1
    '''

    test = distribution_sampler(dist='Normal', size=20, mean=1, sd=0)

    assert isinstance(test, np.ndarray) is True
    assert len(test) == 20
    assert test[0] == 1
    assert test[19] == 1


# Testing the DistributionSampler class

def test_DistributionSampler():
    '''
    Unit Test for the DistributionSampler class. This tests:
        * That the type is np.ndarray
        * That the length of the array is 20
        * That the first and last items in the array equal 1
    '''

    Instance = DS()
    test = Instance.draw(dist='Normal', size=20, mean=1, sd=0)

    assert isinstance(test, np.ndarray) is True
    assert len(test) == 20
    assert test[0] == 1
    assert test[19] == 1
