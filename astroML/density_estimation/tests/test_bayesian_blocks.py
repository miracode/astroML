import numpy as np
from  numpy.testing import assert_allclose, assert_
from astroML.density_estimation import bayesian_blocks


def test_single_change_point():
    # make sure the correct change point is found for a simple distribution
    np.random.seed(0)
    x = np.concatenate([np.random.random(100),
                        1 + np.random.random(200)])

    bins = bayesian_blocks(x)

    assert_(len(bins) == 3)
    assert_allclose(bins[1], 1, rtol=0.02)


def test_duplicate_events():
    t = np.random.random(100)
    t[80:] = t[:20]

    x = np.ones_like(t)
    x[:20] += 1

    bins1 = bayesian_blocks(t)
    bins2 = bayesian_blocks(t[:80], x[:80])

    assert_allclose(bins1, bins2)


def test_measures_fitness():
    np.random.seed(0)
    t = np.linspace(0, 1, 11)
    x = np.exp(-0.5 * (t - 0.5) ** 2 / 0.01 ** 2)
    sigma = 0.05
    x = np.random.normal(x, sigma)

    bins = bayesian_blocks(t, x, sigma, fitness='measures')

    assert_allclose(bins, [0, 0.45, 0.55, 1])
