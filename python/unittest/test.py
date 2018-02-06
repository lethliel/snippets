import unittest

class Test(unittest.TestCase):
  def test_assert(self):
     self.assertEqual('This is my test string 1', 'This is not equal')

if __name__ == '__main__':
    unittest.main() 
