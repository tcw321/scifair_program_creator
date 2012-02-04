import unittest

class Entries(object):
    values = ""
    def find(self, key_value):
        name = key_value.values()[0]
        names = self.values['Teacher']
        for i in range(len(names)):
            if names[i] == name:
                break
        return self.values['Project'][i]


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = {'Teacher': ['Chad', 'Mike', 'Denise'],
                               'Project': ['ChadProject', 'MikeProject', 'DeniseProject']}

    def testFind(self):
        project = self.entries.find({"Teacher" : "Denise"})
        self.assertEqual(project, "DeniseProject")
        
if __name__ == '__main__':
    unittest.main()
