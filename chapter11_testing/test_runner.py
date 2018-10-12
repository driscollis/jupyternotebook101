import unittest

import runner


class TestNotebook(unittest.TestCase):
    
    def test_runner(self):
        nb, errors = runner.run_notebook('Testing.ipynb')
        self.assertEqual(errors, [])
        
        
if __name__ == '__main__':
    unittest.main()