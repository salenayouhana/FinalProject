import pygame
import sys
import unittest
pygame.init()

class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = Topscore()

class TestTopscore(unittest.TestCase):
    """Tests for the class Topscore."""
    def test_top_score(self):
        def test_top_score(Topscore):
            self.assertEqual(Topscore, test_top_score)

class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIGHT/2
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity

class TestDragon(unittest.TestCase):
    """Tests for the class Dragon."""
    def test_dragon_img_rect_width(self):
        def test_dragon_img_rect_width(Dragon):
            self.assertEqual(10, test_dragon_img_rect_width)

    def test_dragon_img_rect_height(self):
        def test_dragon_img_rect_height(Dragon):
            self.assertEqual(10, test_dragon_img_rect_height())

class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('fireball.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30


    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity

class TestFlames(unittest.TestCase):
    """Tests for the class Flames."""

    def test_flames_img_rect_right(self):
        def test_flames_img_rect_right(flames):
            self.assertEqual(test_flames_img_rect_right.rect.right, (1))

class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = WINDOW_HEIGHT/2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10

class TestMario(unittest.TestCase):
    """Tests for the class Mario."""
    def SetUp(self):
        self.Mario = Mario("Mario")

    def test_mario_img_rect_top(self):
        def test_mario_img_rect_top(Mario):
            self.assertEqual(test_mario_img_rect_top(Mario))

    def test_mario_img_rect_bottom(self):
        def test_mario_img_rect_bottom(mario):
            self.assertEqual(test_mario_img_rect_bottom(Mario))


if __name__ == '__main__':
    unittest.main()