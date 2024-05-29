import sys
import unittest

sys.path.append("../ThaiAddressParser")

loader = unittest.TestLoader()
testSuite = loader.discover("tests")
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)