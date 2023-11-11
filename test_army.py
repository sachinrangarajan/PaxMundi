import unittest
from tribes.army import Army
from map.world_map import WorldMap

class TestArmy(unittest.TestCase):
    def test_move(self):
        #creates a worldmap and an army
        test_map = WorldMap(5, 5)
        test_army = Army("Ghost Army", 0, 0)

        #move the army
        test_army.move(1, 0, test_map) #move right

        #check if the army position is updated correctly
        self.assertEqual((test_army.x, test_army.y), (1, 0))

if __name__ == '__main__':
    unittest.main()
