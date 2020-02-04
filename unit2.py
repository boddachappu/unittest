import unittest

class Example:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        return (self.name,self.salary)

class ExampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('u r in setup class')
    def setUp(self):
        print('u r in setup')
    ob = Example('vinod',1272000)
    def testsalary(self):
        self.assertEqual(1272000, self.ob.salary)
    def testname(self):
        self.assertEqual('vinod', self.ob.name)
    @classmethod
    def tearDownClass(cls):
        print('u r in teardown class')
    def tearDown(self):
        print('u r in teardown')
if __name__ == '__main__':
    unittest.main()
