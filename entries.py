__author__ = 'tcw321'

import unittest

class Entries2:
    data = []

    def _processData(self):
        listByTeacher = {}
        for line in self.data:
            #print line
            splitData = self.splitEntry(line)
            entity = {}
            entity['title'] = splitData[5]
            entity['first_name'] = splitData[2]
            entity['last_name'] = splitData[3]
            number_of_students = splitData[10]
            if number_of_students != '':
                try:
                    number_of_students = int(number_of_students)
                except ValueError:
                    print line
                    raise
            else:
                number_of_students = 1
            if (number_of_students > 1):
                entity['first_name1'] = splitData[11]
                entity['last_name1'] = splitData[12]
            if (number_of_students > 2):
                entity['last_name2'] = splitData[15]
                entity['first_name2'] = splitData[14]
            if (number_of_students == 4):
                entity['first_name3'] = splitData[17]
                entity['last_name3'] = splitData[16]
            if listByTeacher.has_key(splitData[4]) == False:
                listByTeacher[splitData[4]] = []
            listByTeacher[splitData[4]].append(entity)
            teachers_in_project =[]
            teachers_in_project.append(splitData[4])
            if splitData[13] not in teachers_in_project:
               listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 13, 14,17 )
               teachers_in_project.append(splitData[13])
            if splitData[16] not in teachers_in_project:
                listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 16, 11, 17)
                teachers_in_project.append(splitData[16])
            try:
                if splitData[19] not in teachers_in_project:
                    listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 19, 11, 14)
            except IndexError:
                print line
        return listByTeacher

    def findOtherTeachers(self, listByTeacher, current_line, teacher_column_number, next_first_name, last_first_name):
        next_teacher = current_line[teacher_column_number]
        entity = {}
        last_name = current_line[teacher_column_number-1]
        if (last_name != "") and (next_teacher != ""):
                entity['first_name'] = current_line[teacher_column_number-2]
                entity['last_name'] = last_name
                entity['first_name1'] = current_line[2]
                entity['last_name1'] = current_line[3]
                entity['first_name2'] = current_line[next_first_name]
                entity['last_name2'] = current_line[next_first_name+1]
                entity['first_name3'] = current_line[last_first_name]
                entity['last_name3'] = current_line[last_first_name+1]
                entity['title'] = current_line[5]
                if (listByTeacher.has_key(next_teacher) == False):
                    listByTeacher[next_teacher] = []
                listByTeacher[next_teacher].append(entity)
        return listByTeacher

    def find(self, teacher_name):
            listByTeacher = self._processData()
            if listByTeacher.has_key(teacher_name) == False:
                return {}
            else:
                projects = sorted(listByTeacher[teacher_name], key=lambda k: k['last_name'])  #*****
                return projects

    def number_of_projects(self):
        return len(self.data)

    def list_projects(self):
        projects = []
        for line in self.data:
            split_line = line.split(',')
            projects.append(split_line[5])
        projects = sorted(projects)
        return projects

    def projects_resubmitted(self):
        projects = []
        for line in self.data:
            split_line = line.split(',')
            if (split_line[1] == "Yes" ):
                projects.append(split_line[5])
        projects = sorted(projects)
        return projects

    def number_of_active_and_disabled_projects(self):
        active = 0
        disabled = 0
        for line in self.data:
            split_line = line.split(',')
            if (len(split_line) == 21) and (split_line[20] == "No" ):
                disabled+=1
            else:
                active+=1
        return (active, disabled)

    def splitEntry(self, entry):
        left_index = entry.find('"')
        if left_index != -1:
           right_index = entry.rfind('"')
           left_side = entry[0:left_index]
           right_side = entry[right_index+1:]
           entry = left_side.split(',')[0:-1] + [entry[left_index:right_index+1]] + right_side.split(',')[1:]
        else:
           entry = entry.split(',')
           if len(entry) not in [19,20,21]:
               print len(entry), entry
               raise ValueError('The entry is not the correct length')
        return entry


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    def testReadData(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Diane,,,,,,",
                "12/1/2012 20:39:32,No,Billy,Bob,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Gotts,Diane,,,,,,"]
        teacher = entries.find('Heidi')
        self.assertEqual(teacher[0]['last_name'], 'Bob' )
        self.assertEqual(teacher[0]['first_name1'], 'Peaches' )
        self.assertEqual(teacher[0]['title'], 'How much is too much?')
        self.assertFalse(teacher[0].has_key('first_name2'))
        teacher = entries.find('Diane')
        self.assertEqual(teacher[0]['last_name'], 'Gotts')

    def testProjectWithFourStudents(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                        "12/1/2012 20:39:32,No,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        teacher = entries.find('Heidi')
        self.assertEqual(teacher[0]['last_name'], 'Bob' )
        self.assertEqual(teacher[0]['first_name'], 'Billy' )
        self.assertEqual(teacher[0]['first_name1'], 'Midnight' )

        self.assertEqual(teacher[0]['title'], 'How much is too little?')
        self.assertFalse(teacher[0].has_key('first_name2'))
        self.assertEqual(teacher[1]['title'], 'How much is too much?')

    def testProjectWithFourStudentsFourTeachers(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Mario,Jamie,A,Z,Todd,B,Y,Bette",]

        listByTeacher = {}
        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 13,14,17)
        self.assertEqual(teacher['Jamie'][0]['last_name'], 'Mario')
        self.assertEqual(teacher['Jamie'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Jamie'][0]['last_name2'], 'Z')
        self.assertEqual(teacher['Jamie'][0]['last_name3'], 'Y')

        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 16,11,17)
        self.assertEqual(teacher['Todd'][0]['last_name'], 'Z')
        self.assertEqual(teacher['Todd'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Todd'][0]['last_name2'], 'Mario')
        self.assertEqual(teacher['Todd'][0]['last_name3'], 'Y')

        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 19,11,14)
        self.assertEqual(teacher['Bette'][0]['last_name'], 'Y')
        self.assertEqual(teacher['Bette'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Bette'][0]['last_name2'], 'Mario')
        self.assertEqual(teacher['Bette'][0]['last_name3'], 'Z')

    def testNumberOfProjects(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                        "12/1/2012 20:39:32,No,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        self.assertEqual(entries.number_of_projects(), 2)
        self.assertEqual(entries.list_projects(), ["How much is too little?", "How much is too much?"])

    def testNumberOfResubmittedProjects(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                    "12/1/2012 20:39:32,No,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi",
                    "12/1/2012 20:39:32,Yes,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        projects = entries.projects_resubmitted()
        self.assertEqual(projects, ["How much is too little?"])

    def testNumberOfActiveProjects(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,No,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                        "12/1/2012 20:39:32,No,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi,No",
                        "12/1/2012 20:39:32,Yes,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        active, disabled = entries.number_of_active_and_disabled_projects()
        self.assertEqual(active, 2)
        self.assertEqual(disabled, 1)

    def testTitleContainsComas(self):
        entries = Entries2()
        data = "12/1/2012 20:39:32,No,Comet,Wright,Heidi,\"When, if possible, is much is too much?\",Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi"
        data = entries.splitEntry(data)
        print data
        self.assertEqual(data,['12/1/2012 20:39:32', 'No', 'Comet', 'Wright', 'Heidi', '"When, if possible, is much is too much?"', 'Yes', '', 'Karen', 'karen', '2', 'Peaches', 'Wright', 'Heidi', 'AF', 'BL', 'Heidi', 'CF', 'DL', 'Heidi'] )
        data = "12/1/2012 20:39:32,No,Comet,Wright,Heidi,\"When, \"\"if possible\"\", is much is too much?\",Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi"
        print data
        data = entries.splitEntry(data)
        self.assertEqual(data[5], "\"When, \"\"if possible\"\", is much is too much?\"")



