__author__ = 'tcw321'

import unittest

class Entries2:
    data = []

    def _processData(self):
        listByTeacher = {}
        for line in self.data:
            print line
            splitData = line.split(',')
            entity = {}
            entity['title'] = splitData[4]
            entity['first_name'] = splitData[1]
            entity['last_name'] = splitData[2]
            number_of_students = int(splitData[9])
            if (number_of_students > 1):
                entity['first_name1'] = splitData[10]
                entity['last_name1'] = splitData[11]
            if (number_of_students > 2):
                entity['last_name2'] = splitData[14]
                entity['first_name2'] = splitData[13]
            if (number_of_students == 4):
                entity['first_name3'] = splitData[16]
                entity['last_name3'] = splitData[17]
            if listByTeacher.has_key(splitData[3]) == False:
                listByTeacher[splitData[3]] = []
            listByTeacher[splitData[3]].append(entity)
            teachers_in_project =[]
            teachers_in_project.append(splitData[3])
            if splitData[12] not in teachers_in_project:
               listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 12, 13,16 )
               teachers_in_project.append(splitData[12])
            if splitData[15] not in teachers_in_project:
                listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 15, 10, 16)
                teachers_in_project.append(splitData[15])
            if splitData[18] not in teachers_in_project:
                listByTeacher = self.findOtherTeachers(listByTeacher, splitData, 18, 10, 13)
        return listByTeacher

    def findOtherTeachers(self, listByTeacher, current_line, teacher_column_number, next_first_name, last_first_name):
        next_teacher = current_line[teacher_column_number]
        entity = {}
        if (next_teacher != ""):
                entity['first_name'] = current_line[teacher_column_number-2]
                entity['last_name'] = current_line[teacher_column_number-1]
                entity['first_name1'] = current_line[1]
                entity['last_name1'] = current_line[2]
                entity['first_name2'] = current_line[next_first_name]
                entity['last_name2'] = current_line[next_first_name+1]
                entity['first_name3'] = current_line[last_first_name]
                entity['last_name3'] = current_line[last_first_name+1]
                entity['title'] = current_line[4]
                if (listByTeacher.has_key(next_teacher) == False):
                    listByTeacher[next_teacher] = []
                listByTeacher[next_teacher].append(entity)
        return listByTeacher




    def find(self, teacher_name):
            listByTeacher = self._processData()
            projects = sorted(listByTeacher[teacher_name], key=lambda k: k['last_name'])  #*****
            return projects


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    def testReadData(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Diane,,,,,,",
                "12/1/2012 20:39:32,Billy,Bob,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Gotts,Diane,,,,,,"]
        teacher = entries.find('Heidi')
        self.assertEqual(teacher[0]['last_name'], 'Bob' )
        self.assertEqual(teacher[0]['first_name1'], 'Peaches' )
        self.assertEqual(teacher[0]['title'], 'How much is too much?')
        self.assertFalse(teacher[0].has_key('first_name2'))
        teacher = entries.find('Diane')
        self.assertEqual(teacher[0]['last_name'], 'Gotts')

    def testProjectWithFourStudents(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                        "12/1/2012 20:39:32,Billy,Bob,Heidi,How much is too little?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        teacher = entries.find('Heidi')
        self.assertEqual(teacher[0]['last_name'], 'Bob' )
        self.assertEqual(teacher[0]['first_name'], 'Billy' )
        self.assertEqual(teacher[0]['first_name1'], 'Midnight' )

        self.assertEqual(teacher[0]['title'], 'How much is too little?')
        self.assertFalse(teacher[0].has_key('first_name2'))
        self.assertEqual(teacher[1]['title'], 'How much is too much?')

    def testProjectWithFourStudentsFourTeachers(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Mario,Jamie,A,Z,Todd,B,Y,Bette",]

        listByTeacher = {}
        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 12,13,16)
        self.assertEqual(teacher['Jamie'][0]['last_name'], 'Mario')
        self.assertEqual(teacher['Jamie'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Jamie'][0]['last_name2'], 'Z')
        self.assertEqual(teacher['Jamie'][0]['last_name3'], 'Y')

        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 15,10,16)
        self.assertEqual(teacher['Todd'][0]['last_name'], 'Z')
        self.assertEqual(teacher['Todd'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Todd'][0]['last_name2'], 'Mario')
        self.assertEqual(teacher['Todd'][0]['last_name3'], 'Y')

        teacher = entries.findOtherTeachers(listByTeacher, entries.data[0].split(','), 18,10,13)
        self.assertEqual(teacher['Bette'][0]['last_name'], 'Y')
        self.assertEqual(teacher['Bette'][0]['last_name1'], 'Wright')
        self.assertEqual(teacher['Bette'][0]['last_name2'], 'Mario')
        self.assertEqual(teacher['Bette'][0]['last_name3'], 'Z')




