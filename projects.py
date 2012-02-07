import unittest

# handle first and last names

class Entries(object):
    values = ""
    results = []
    def find(self, key_value):
        name = key_value.values()[0]
        names = self.values['Teacher']
        resultIndexes = []
        for i in range(len(names)):
            if names[i] == name:
                resultIndexes.append(i)
        self.results = []
        for i in resultIndexes:
            project = {}
            names = self.values['Student Name'][i]
            first_name, last_name = names.split()
            second_name = self.values['Second Student Name'][i].split()
            if (len(second_name) > 0):
              first_name1, last_name1 = second_name
              project['first_name1'] = first_name1
              project['last_name1'] = last_name1

            third_name = self.values['Third Student Name'][i].split()
            if (len(third_name) > 0):
              first_name2, last_name2 = third_name
              project['first_name2'] = first_name2
              project['last_name2'] = last_name2
              
            fourth_name = self.values['Fourth Student Name'][i].split()
            if (len(fourth_name) > 0):
              first_name3, last_name3 = fourth_name
              project['first_name3'] = first_name3
              project['last_name3'] = last_name3
              
            project['title'] = self.values['Project Name'][i]
            project['first_name'] = first_name
            project['last_name'] = last_name
            self.results.append(project)
        return self.results

class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = {'Teacher': ['Chad', 'Mike', 'Denise', 'Denise', 'Leslie'],
                               'Project Name': ['ChadProject', 'MikeProject', 'DeniseProject', 'DeniseProject2', 'LeslieProject'],
                               'Student Name': ['C. Cod', 'M. Mad', 'D. Dump', 'D. Dail', 'Bob Smith'],
                               'Second Student Name': ['','','','E. Elbert', 'Tom Smoth'],
                               'Second Teacher Name':['','','','Mike',''],
                               'Third Student Name': ['','','','','Henry Snot'],
                               'Fourth Student Name': ['','','','','Timmy Toon']}


    def testFindOneStudent(self):
        project = self.entries.find({"Teacher": "Chad"})
        self.assertEqual(project, [{'title':'ChadProject', 'first_name':'C.', 'last_name':'Cod'}])

    def testSortingProjectsbyFirstLastName(self):
        project = self.entries.find({"Teacher" : "Denise"})
        project = sorted(project, key=lambda k: k['last_name'])
        self.assertEqual(project, [{'title':"DeniseProject2", 'first_name':'D.', 'last_name':'Dail',  'first_name1':'E.','last_name1':'Elbert'}, {'title':"DeniseProject", 'first_name':'D.', 'last_name':'Dump'}])

    def testProjectWithFourStudents(self):
        project = self.entries.find({"Teacher" : "Leslie"})
        self.assertEqual(project, [{'title':"LeslieProject", 'first_name':'Bob', 'last_name':'Smith', 'first_name1':'Tom', 'last_name1':'Smoth',
                                    'first_name2':'Henry', 'last_name2':'Snot', 'first_name3':'Timmy', 'last_name3':'Toon'}])

    def testWithSecondStudentWithDifferentTeacher(self):
        project = self.entries.find({"Teacher" : "Mike"})
        self.assertEqual(project, [{'title':"MikeProject", 'first_name':'M.', 'last_name':'Mad'},
                                   {'title':'DeniseProject2', 'first_name':'E.', 'last_name':'Elbert',
                                            'first_name1':'D.', 'last_name1':'Dail'}])

if __name__ == '__main__':
    unittest.main()
