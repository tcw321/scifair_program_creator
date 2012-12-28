__author__ = 'tcw321'

import unittest



class TestEntriesClass(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    def testreadData(self):
        data = ["12/1/2012 20:39:32,Comet,Wright,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Wright,Diane",
                "12/1/2012 20:39:32,Billy,Bob,Heidi,How much is too much?,Yes,,Karen,karen,2,Peaches,Gotts,Diane"]
        listByTeacher = {}
        for line in data:
            print line
            splitData = line.split(',')
            entity = []
            entity.append(splitData[2])
            entity.append(splitData[1])
            entity.append(splitData[4])
            if listByTeacher.has_key(splitData[3]) == False:
                listByTeacher[splitData[3]] = []
            listByTeacher[splitData[3]].append(entity)
        self.assertEqual(listByTeacher[splitData[3]][0][0], 'Wright' )
        self.assertEqual(listByTeacher[splitData[3]][1][0], 'Bob' )


