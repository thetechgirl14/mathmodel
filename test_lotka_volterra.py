import os
import unittest
from math_model import Lotka_Volterra


class LotkaVolterraTestCase(unittest.TestCase):
    def test_lotka_volterra_initialization(self):
        iv_x = 10
        iv_y = 2
        alpha = 2
        beta = 1
        dt = 0.01
        time = 1000
        L = Lotka_Volterra(iv_x, iv_y, alpha, beta, dt, time)
        assert L.alpha == alpha
        assert L.beta == beta
        assert L.dt == dt
        assert L.time == time

    def test_logistic_sys(self):
        iv_x = 10
        iv_y = 2
        alpha = 2
        beta = 1
        dt = 0.01
        time = 1000
        L = Lotka_Volterra(iv_x, iv_y, alpha, beta, dt, time)
        L.initial_value(iv_x, iv_y)
        L.logistic_sys()
        assert L.x[0] == 10
        assert L.y[0] == 2

    def test_plots(self):
        iv_x = 10
        iv_y = 2
        alpha = 2
        beta = 1
        dt = 0.01
        time = 1000
        L = Lotka_Volterra(iv_x, iv_y, alpha, beta, dt, time)
        L.initial_value(iv_x, iv_y)
        L.logistic_sys()
        L.plot_system()
        assert os.path.exists("./Dynamic Systems and Phase Plot.png")

    def test_equilibrium(self):
        iv_x = 10
        iv_y = 2
        alpha = 2
        beta = 1
        dt = 0.01
        time = 1000
        L = Lotka_Volterra(iv_x, iv_y, alpha, beta, dt, time)
        L.initial_value(iv_x, iv_y)
        L.logistic_sys()
        equilibria = L.find_equilibrium(10)
        assert type(equilibria) is list
        assert len(equilibria) == 3
        assert equilibria == [(0, 0), (1, 1), (2, 0)]


if __name__ == '__main__':
    unittest.main()
