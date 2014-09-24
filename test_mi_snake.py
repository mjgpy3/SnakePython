#!/usr/bin/env python

import unittest
import mi_snake

class TestRandomPlace(unittest.TestCase):
    def test_random_places_width_is_between_0_and_width(self):
        some_width = 24

        place = mi_snake.random_place(some_width, 99)

        self.assertTrue(place.width >= 0 and place.width < some_width)

    def test_random_places_height_is_between_0_and_height(self):
        some_height = 24

        place = mi_snake.random_place(99, some_height)

        self.assertTrue(place.height >= 0 and place.height < some_height)

    def test_list_of_place_is_width_height(self):
        place = mi_snake.Place(42, 35)

        list_of_place = list(place)

        self.assertEqual([42, 35], list_of_place)

    def test_a_whole_bunch_of_food_locations_are_not_at_the_same_location_as_a_snake(self):
        snake = [[1, 2], [1, 3], [1, 4]]
        food_locations = []

        for _ in xrange(1000):
            food_locations.append(mi_snake.generate_food_location(snake, 42, 42))

        for location in food_locations:
            self.assertFalse(location in snake)

if __name__ == '__main__':
    unittest.main()
