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
            if (splitData[9] >= 2):
                entity['first_name1'] = splitData[10]
                entity['last_name1'] = splitData[11]
            if (splitData[9] >= 3):
                entity['last_name2'] = splitData[14]
                entity['first_name2'] = splitData[13]
            if (splitData[9] ==4):
                entity['first_name3'] = splitData[16]
                entity['last_name3'] = splitData[17]
            if listByTeacher.has_key(splitData[3]) == False:
                listByTeacher[splitData[3]] = []
            listByTeacher[splitData[3]].append(entity)
        return listByTeacher


    def find(self, key_value):
        listByTeacher = self._processData()
        return listByTeacher[key_value]


class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    def testreadData(self):
        entries = Entries2()
        entries.data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Diane,,,,,,",
                "12/1/2012 20:39:32,Billy,Bob,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Gotts,Diane,,,,,,"]
        teacher = entries.find('Heidi')
        print teacher
        self.assertEqual(teacher[0]['last_name'], 'Wright' )
        self.assertEqual(teacher[0]['first_name1'], 'Peaches' )
        self.assertEqual(teacher[0]['title'], 'How much is too much?')


