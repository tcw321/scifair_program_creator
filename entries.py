__author__ = 'tcw321'

import unittest

class Entries2:
    data = []

    def _processData(self):
        listByTeacher = {}
        for line in self.data:
            number_of_students = 1
            print line
            splitData = self.splitEntry(line)
            entity = {}
            entity['title'] = splitData[10]
            entity['first_name'] = splitData[1].strip()
            entity['last_name'] = splitData[2].strip()
            entity['first_name1'] = splitData[3].strip()
            entity['last_name1'] = splitData[4].strip()
            if entity['last_name1'] != '':
                number_of_students = 2
            entity['first_name2'] = splitData[5].strip()
            entity['last_name2'] = splitData[6].strip()
            if entity['last_name2'] != '':
                number_of_students = 3
            print number_of_students
            if listByTeacher.has_key(splitData[11]) == False:
                listByTeacher[splitData[11]] = []
            listByTeacher[splitData[11]].append(entity)
            teachers_in_project =[]
            teachers_in_project.append(splitData[11])
            if number_of_students > 1:
                if splitData[17] != '':
                   if splitData[17] not in teachers_in_project:
                      listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 17,3,4,1,2 )
                      teachers_in_project.append(splitData[17])
            if number_of_students > 2:
                if splitData[18] != '':
                    if splitData[18] not in teachers_in_project:
                        listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 18,5,6,1,2,3,4)
                        teachers_in_project.append(splitData[18])
        #            try:
#                if splitData[19] not in teachers_in_project:
#                    listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 19, 11, 14)
#            except IndexError:
#                print line
        return listByTeacher

    def findOtherTeachers(self, listByTeacher, current_line, teacher_column_number, first_name_num, last_name_num,first_name2_num, last_name2_num, first_name3_num=0, last_name3_num=0):
        next_teacher = current_line[teacher_column_number]
        entity = {}
        last_name = current_line[last_name_num]
        if (last_name != "") and (next_teacher != ""):
                entity['first_name'] = current_line[first_name_num]
                entity['last_name'] = current_line[last_name_num]
                entity['first_name1'] = current_line[first_name2_num]
                entity['last_name1'] = current_line[last_name2_num]
                if first_name3_num != 0:
                    entity['first_name2'] = current_line[first_name3_num]
                    entity['last_name2'] = current_line[last_name3_num]
                entity['title'] = current_line[10]
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
            projects.append(split_line[10])
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
           #if len(entry) not in [19,20,21]:
           #    print len(entry), entry
           #    raise ValueError('The entry is not the correct length')
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



