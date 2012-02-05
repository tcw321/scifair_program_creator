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
            project = {}
            names = self.values['Student Name'][i]
            first_name, last_name = names.split()
            second_name = self.values['Second Student Name'][i].split()
            if (len(second_name) > 0):
              first_name1, last_name1 = self.values['Second Student Name'][i].split()
              project['first_name1'] = first_name1
              project['last_name1'] = last_name1
            project['title'] = self.values['Project Name'][i]
            project['first_name'] = first_name
            project['last_name'] = last_name
            results.append(project)
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
        self.assertEqual(project, [{'title':"DeniseProject", 'first_name':'D.', 'last_name':'Dump'}, {'title':"DeniseProject2", 'first_name':'D.', 'last_name':'Dail', 'first_name1':'E.','last_name1':'Elbert'}])

    def testFindOneStudent(self):
        project = self.entries.find({"Teacher": "Chad"})
        self.assertEqual(project, [{'title':'ChadProject', 'first_name':'C.', 'last_name':'Cod'}])
    
        
if __name__ == '__main__':
    unittest.main()
