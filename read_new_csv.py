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

    def testProjectWithFourStudents(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Heidi,AF,BL,Heidi,CF,DL,Heidi",
                        "12/1/2012 20:39:32,Billy,Bob,Heidi,How much is too much?,Yes,,Karen,karen,2,Midnight,Gotts,Diane,EF,FL,Heidi,GF,HL,Heidi"]
        teacher = entries.find('Heidi')
        self.assertEqual(teacher[0]['last_name'], 'Bob' )
        self.assertEqual(teacher[0]['first_name'], 'Billy' )
        self.assertEqual(teacher[0]['first_name1'], 'Midnight' )

        self.assertEqual(teacher[0]['title'], 'How much is too much?')
        self.assertFalse(teacher[0].has_key('first_name2'))

