import unittest

# handle first and last names

# find teachers in second teacher list that does not equal primary teacher
# make that teacher's student first student and return with teacher, students and title

# Same with third student, fourth student
#

class Entries(object):
    values = ""
    results = []

    def getOtherStudents(self, project, index, suffix, key):
        names = self.values[key][index]
        if (len(names) > 0):
            first_name, last_name = names.split()
            project['first_name'+suffix] = first_name
            project['last_name'+suffix] = last_name
        return project
    
    def find(self, key_value):
        self.results = []
        name = key_value.values()[0]
        names = self.values['Teacher']
        titles = []
        resultIndexes = []
        for i in range(len(names)):
            if names[i] == name:
                resultIndexes.append(i)
        for i in resultIndexes:
            project = {}
            project = self.getOtherStudents(project, i, '', 'Student Name')
            project = self.getOtherStudents(project, i, '1', 'Second Student Name')
            project = self.getOtherStudents(project, i, '2', 'Third Student Name')
            project = self.getOtherStudents(project, i, '3', 'Fourth Student Name')
            project['title'] = self.values['Project Name'][i]
            titles.append(project['title'])
            self.results.append(project)
        names = self.values['Second Teacher Name']
        resultIndexes = []
        for i in range(len(names)):
            if names[i] == name:
                resultIndexes.append(i)
        for i in resultIndexes:
            title = self.values['Project Name'][i]
            if title not in titles:
                project = {}
                project['title'] = title
                titles.append(title)
                project = self.getOtherStudents(project, i, '', 'Second Student Name')
                project = self.getOtherStudents(project, i, '1', 'Student Name')
                project = self.getOtherStudents(project, i, '2', 'Third Student Name')
                project = self.getOtherStudents(project, i, '3', 'Fourth Student Name')
                self.results.append(project)        
        return self.results

class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    entries = Entries()
    def setUp(self):
        self.entries.values = {'Teacher': ['Chad', 'Mike', 'Denise', 'Denise', 'Leslie', 'Tracey'],
                               'Project Name': ['ChadProject', 'MikeProject', 'DeniseProject', 'DeniseProject2', 'LeslieProject', 'TraceyProject'],
                               'Student Name': ['C. Cod', 'M. Mad', 'D. Dump', 'D. Dail', 'Bob Smith', 'Howard Hughes'],
                               'Second Student Name': ['','','Tracey Zicker','E. Elbert', 'Tom Smoth',''],
                               'Second Teacher Name':['','','Tracey','Mike','',''],
                               'Third Student Name': ['','','Tracey Ann','','Henry Snot',''],
                               'Third Teacher Name':['','','','Mike','',''],                               
                               'Fourth Student Name': ['','','Tracey Cird','','Timmy Toon',''],
                               'Fourth Teacher Name':['','','','Mike','','']}                               

    def tearDown(self):
        entries = Entries()

    def testFindOneStudent(self):
        project = self.entries.find({"Teacher": "Chad"})
        self.assertEqual(project, [{'title':'ChadProject', 'first_name':'C.', 'last_name':'Cod'}])

    def testSortingProjectsbyFirstLastName(self):
        project = self.entries.find({"Teacher" : "Denise"})
        project = sorted(project, key=lambda k: k['last_name'])
        self.assertEqual(project, [{'title':"DeniseProject2", 'first_name':'D.', 'last_name':'Dail',  'first_name1':'E.','last_name1':'Elbert'}, {'title':"DeniseProject", 'first_name':'D.', 'last_name':'Dump','first_name1':'Tracey', 'last_name1':'Zicker','first_name2':'Tracey', 'last_name2':'Ann',
                                                                                    'first_name3':'Tracey', 'last_name3':'Cird'}])

    def testProjectWithFourStudents(self):
        project = self.entries.find({"Teacher" : "Leslie"})
        self.assertEqual(project, [{'title':"LeslieProject", 'first_name':'Bob', 'last_name':'Smith', 'first_name1':'Tom', 'last_name1':'Smoth',
                                    'first_name2':'Henry', 'last_name2':'Snot', 'first_name3':'Timmy', 'last_name3':'Toon'}])

    def testWithSecondStudentWithDifferentTeacher(self):
        project = self.entries.find({"Teacher" : "Mike"})
        self.assertEqual(project, [{'title':"MikeProject", 'first_name':'M.', 'last_name':'Mad'},
                                       {'title':'DeniseProject2', 'first_name':'E.', 'last_name':'Elbert',
                                        'first_name1':'D.', 'last_name1':'Dail'}])

    def testWithTeacherTwoProjectsSecondFromSecondaryNames(self):
        project = self.entries.find({"Teacher" : "Tracey"})
        self.assertEqual(project, [{'title':'TraceyProject', 'first_name':'Howard', 'last_name':'Hughes'},
        {'title':'DeniseProject', 'first_name':'Tracey', 'last_name':'Zicker','first_name2':'Tracey', 'last_name2':'Ann',
         'first_name3':'Tracey', 'last_name3':'Cird', 'first_name1':'D.', 'last_name1':'Dump'}])

if __name__ == '__main__':
    unittest.main()
