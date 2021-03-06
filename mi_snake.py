#!/usr/bin/env python

import curses, random

def generate_food_location(snake, width, length):
    """ Loops through slots on the map and finds one where the snake is not """
    place = random_place(width, length)
    while place in snake:
        place = random_place(width, length)
    return place

class Pair(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __iter__(self):
        yield self.left
        yield self.right

    def __getitem__(self, index):
        return list(self)[index]

    def __eq__(self, other):
        return list(self) == list(other)

class Place(Pair):
    def __init__(self, w, h):
        self.width = w
        self.height = h
        Pair.__init__(self, w, h)

class Vector(Pair):
    def __init__(self, y, x):
        self.y = y
        self.x = x
        Pair.__init__(self, y, x)

    def opposite_of(self, other_vector):
        return self.x == -other_vector.x and self.y == -other_vector.y

def random_place(width, height):
    return Place(random.randrange(0, width), random.randrange(0, height))

def directions_are_opposite(dir_1, dir_2):
    """ Checks if two passed vectors are opposite in direction """
    return dir_1[0] == -dir_2[0] and dir_1[1] == -dir_2[1]

if __name__ == '__main__':
    snake = []	        # The snake which is a list of locations occupied
    direction = list(Vector(0, 1))
    points = 0	        # The number of eaten objects
    key = 0 	        # Holds the pressed key
    delay = 100
    key_to_vector = {65:[-1,0], 66:[1,0], 68:[0,-1], 67:[0,1]}

    # Make a new screen object
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    # Get and set the maximum y (Width) and x (Length) of the screen
    screen_width, screen_length = screen.getmaxyx()[0], screen.getmaxyx()[1]

    # Turn echo off so that input is not displayed
    curses.noecho()
    # Clear and refresh the screen
    screen.clear()

    # Give the snake it's first node at the middle of the screen
    snake.append([screen_width / 2, screen_length / 2])

    food_location = generate_food_location(snake, screen_width, screen_length)

    screen.nodelay(True)

    while key != 101:
        key = screen.getch()

        # If a valid key was entered
        if key in key_to_vector and not directions_are_opposite(direction, key_to_vector[key]):
            direction = key_to_vector[key]

        last = [0, 0]

        # Moves the snake, loops through each element in the snake moving it to
        # the element in front of it's location. Also saves the last location
        for i in xrange(len(snake)):
            if i == 0:
                last = [snake[i][0], snake[i][1]]
                snake[i][0] += direction[0]
                snake[i][1] += direction[1]
            else:
                snake[i], last = last, snake[i]

        # If the snake bites food
        if snake[0] == food_location:
            snake.append(last)
            food_location = generate_food_location(snake, screen_width, screen_length)

        screen.clear()

        # If the snake hits a wall
        if snake[0][0] >= screen_width or snake[0][1] >= screen_length or snake[0][0] < 0 or snake[0][1] < 0:
            break

        # If the snake hits itself
        for i in xrange(1, len(snake)):
            if snake[0] == snake[i]:
                key = 101

        # Adds characters to view
        for i in xrange(len(snake)):
            screen.addch(snake[i][0], snake[i][1], "X", curses.color_pair(1))

        screen.addch(food_location[0], food_location[1], "O", curses.color_pair(2))
        screen.move(0, 0)
        screen.refresh()

        # If we are going left or right
        if direction[1] != 0:
            curses.napms(delay / 2)
        else:
            curses.napms(delay)

    curses.endwin()
