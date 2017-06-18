#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------------
# RangeIteratorT.py
# -----------------

from unittest import main, TestCase

from RangeIterator import \
    Range_Iterator,       \
    range_iterator_yield

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            Range_Iterator,
            range_iterator_yield]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 2)
                self.assertIs(p, iter(p))
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 3)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 4)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertEqual(next(p), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 5)
                self.assertEqual(list(p), [2, 3, 4])
                self.assertEqual(list(p), [])

if __name__ == "__main__" :
    main()
