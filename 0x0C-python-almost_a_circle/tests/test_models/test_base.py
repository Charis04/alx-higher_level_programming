#!/usr/bin/python3
"""Tests for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_exist(self):
        b1 = Base()
        self.assertTrue(b1.id)
        self.assertEqual(b1.id, 1)

    def test_id_plus(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == "__main__":
    unittest.main()
