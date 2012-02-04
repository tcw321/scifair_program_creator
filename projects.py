import unittest

class Entries(object):
    values = ""
    def find(self, key_value):
        return self.values


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = "Leslie"

    def testFind(self):
        project = self.entries.find({"teacher" : "Leslie"})
        self.assertEqual(project, "Leslie")
        
if __name__ == '__main__':
    unittest.main()
