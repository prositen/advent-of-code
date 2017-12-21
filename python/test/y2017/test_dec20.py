import unittest

from python.src.y2017 import dec20

class TestSwarm(unittest.TestCase):

    def test_closest_particle(self):
        puzzle_input = ["p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>",
                        "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"]
        s = dec20.Swarm(puzzle_input)
        self.assertEqual(0, s.get_closest())

    def test_collide(self):
        puzzle_input = ["p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>",
                        "p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>",
                        "p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>",
                        "p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"
                        ]
        s = dec20.Swarm(puzzle_input)
        self.assertEqual(1, s.get_particle_count())