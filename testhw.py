from unittest import TestCase, main
from homework import move_zeros



class MoveZerosTestCase(TestCase):

    def test_1_base(self):
        self.assertEqual(move_zeros([0, 1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0, 0])
    
    def test_2_no_zeros(self):
        self.assertEqual(move_zeros([1, 2 ,3]), [1, 2, 3])
    
    def test_3_double_didgets(self):
        self.assertEqual(move_zeros([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])
    
    def test_4_double_zeros(self):
        self.assertEqual(move_zeros([00, 2, 4, 0, 9]), [2, 4, 9, 00, 0])
    