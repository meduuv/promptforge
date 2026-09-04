import unittest
from promptforge import template
class Tests(unittest.TestCase):
 def test_template(self): self.assertEqual(template("Hi {name}",{"name":"Medu"}),"Hi Medu")
if __name__=="__main__":unittest.main()
