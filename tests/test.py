from main import main
import unittest

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(),'news')
        print('Tested')

if __name__=='__main__':
    unittest.main()