import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(0) == 0)

    def test_volume2(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_volume3(self):
        assert(sphere.volume(2) == 33.510321638291124)

    def test_surfacearea1(self):
        assert(sphere.surfaceArea(0) == 0)

    def test_surfaceare2(self):
        assert(sphere.surfaceArea(10) == 1256.6370614359173)

    def test_surfacearea3(self):
        assert(sphere.surfaceArea(2) == 50.26548245743669)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(30) == 0)

    #failing test
    #def test_surfacearea(self):
        #assert(sphere.surfaceArea(100) == 0)


if __name__ == '__main__':
    unittest.main()
