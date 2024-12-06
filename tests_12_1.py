import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1=runner.Runner('Vasya')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance,50)

    def test_run(self):
        obj2 = runner.Runner('Kostya')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = runner.Runner('Alla')
        obj4 = runner.Runner('Alex')
        for i in range(10):
            obj3.walk()
            obj4.run()
        self.assertNotEqual(obj3,obj4)