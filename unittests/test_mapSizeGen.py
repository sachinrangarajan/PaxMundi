import unittest
from map.world_map import WorldMap

class TestMapSizeGeneration(unittest.TestCase):

    def test_map_size_generation(self):
        # Start with a small map size
        width, height = 3, 3
        max_width, max_height = 120, 40

        while width <= max_width or height <= max_height:
            with self.subTest(width=width, height=height):
                test_map = WorldMap(width, height)
                test_map.display()  # Assuming WorldMap has a display method
                print(f"Generated {width}x{height} map successfully.\n")

                # Increment the size for the next iteration
                if width <= max_width:
                    width += 1
                if height <= max_height:
                    height += 1

        # The test passes if it reaches this point without errors
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
