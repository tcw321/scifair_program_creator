import unittest

# handle first and last names

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
            secondName = self.values['Second Student Name'][i]
            if secondName != '':
                names.append(secondName)
            results.append([self.values['Project Name'][i], names])
        return results


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = {'Teacher': ['Chad', 'Mike', 'Denise', 'Denise'],
                               'Project Name': ['ChadProject', 'MikeProject', 'DeniseProject', 'DeniseProject2'],
                               'Student Name': ['C. Cod', 'M. Mad', 'D. Dump', 'D. Dail'],
                               'Second Student Name': ['','','','E. Elbert']}

    def testFind(self):
        project = self.entries.find({"Teacher" : "Denise"})
        self.assertEqual(project, [["DeniseProject", ['D. Dump']], ["DeniseProject2", ['D. Dail', 'E. Elbert']]])

        
if __name__ == '__main__':
    unittest.main()
