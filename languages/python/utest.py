import unittest


class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setUpClass()"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass()"
    
    def setUp(self):
        print "setUp()"
        self.seq = range(10)

    def tearDown(self):
        print "tearDown()"

    def test_test01(self):
        self.assertEqual(self.seq, range(10))
    
    @unittest.skip("This is a skipped test")
    def test_test02(self):
        self.assertEqual(self.seq, range(10))
    
    def test_test03(self):
        self.assertEqual(1, 0)

    def test_test04(self):
        self.assertEqual(1, 0, "Note that with comment you don't see actual vs expected values")


# pip install nose
# nosetests file.py
