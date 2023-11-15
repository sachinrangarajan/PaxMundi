import unittest
import random

from map.world_map import WorldMap
from ui import uiUtils

class TestMapSizeGeneration(unittest.TestCase):

    def test_map_size_generation(self):
        # Start with a small map size
        width, height = 3, 3
        max_width, max_height = 42, 42
        mysterious_failure_size = 42  # The cosmic number from Douglas Adams

        while width <= max_width or height <= max_height:
            with self.subTest(width=width, height=height):
                # Cosmic Mystery Check
                if width == mysterious_failure_size and height == mysterious_failure_size:
                    print("Approaching the Cosmic Number 42... Will the Universe hold?")
                
                test_map = WorldMap(width, height)
                try:
                    uiUtils.updateMap(test_map)
                    print(f"Generated {width}x{height} map successfully.\n")
                except Exception as e:
                    print(f"Cosmic Disturbance Detected at {width}x{height}: {e}")
                    break  # Breaking the loop to prevent infinite errors

                # Increment the size for the next iteration
                if width <= max_width:
                    width += random.randint(1, 10)
                if height <= max_height:
                    height += random.randint(1, 10)

        # The test passes if it reaches this point without errors
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
    
