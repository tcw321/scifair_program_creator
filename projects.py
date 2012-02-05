import unittest

class Entries(object):
    values = ""
    def find(self, key_value):
        name = key_value.values()[0]
        names = self.values['Teacher']
        resultIndexes = []
        for i in range(len(names)):
            if names[i] == name:
                resultIndexes.append(i)
        results = []
        for i in resultIndexes:
            names = []
            names.append(self.values['Student Name'][i])
            results.append([self.values['Project Name'][i], names])
        return results


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = {'Teacher': ['Chad', 'Mike', 'Denise', 'Denise'],
                               'Project Name': ['ChadProject', 'MikeProject', 'DeniseProject', 'DeniseProject2'],
                               'Student Name': ['C. Cod', 'M. Mad', 'D. Dump', 'D. Dail']} 

    def testFind(self):
        project = self.entries.find({"Teacher" : "Denise"})
        self.assertEqual(project, [["DeniseProject", ['D. Dump']], ["DeniseProject2", ['D. Dail']]])

        
if __name__ == '__main__':
    unittest.main()
