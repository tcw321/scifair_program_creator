__author__ = 'tcw321'

import unittest

spreadsheet = open("entries.tsv", 'r')

def generateEntries(lines):
    headers = lines[0].split('\t')
    entries = []
    for line in lines[1:]:
        entries.append(line.split('\t'))

    good_indices = [1,2,3,4,9,10,11,12,13,14,15,16,17,18]
    teachers = ['Heidi', 'Edie', 'Diane', 'Jennifer', 'Tyra', 'Jamie', 'Tracey', 'Josh', 'Carl', 'Denise', 'Bette', 'Chad', 'Ko', 'Mike', 'Rick', 'Leslie', 'Peter', 'Adam', 'Mary', 'Aina']
    header_titles = ["name", "studentfirst1", "studentlast1", "teacher1", "total_students",
                     "studentfirst2", "studentlast2", "teacher2",
                     "studentfirst3", "studentlast3", "teacher3",
                     "studentfirst4", "studentlast4", "teacher4"]
    program = {}
    for teacher in teachers:
        program[teacher] = []
    for n in range(len(entries)):
        entry_array = [entries[n][i] for i in good_indices ]
        if entry_array[-1] == '\n':
            entry_array[-1] = ''
        entry = {}
        for i in range(len(entry_array)):
            entry[header_titles[i]] = entry_array[i]
        print(entry)
        current_teachers = [entry['teacher1']]
        program[entry['teacher1']].append([[entry['studentfirst1'], entry['studentlast1']],
                                          [entry['studentfirst2'], entry['studentlast2']],
                                          [entry['studentfirst3'], entry['studentlast3']],
                                          [entry['studentfirst4'], entry['studentlast4']]])
        if entry['teacher2'] != '' and entry['teacher2'] not in current_teachers:
            entry['studentfirst1'], entry['studentfirst2'] = entry['studentfirst2'], entry['studentfirst1']
            entry['studentlast1'], entry['studentlast2'] = entry['studentlast2'], entry['studentlast1']
            program[entry['teacher2']].append([[entry['studentfirst1'], entry['studentlast1']],
                                          [entry['studentfirst2'], entry['studentlast2']],
                                          [entry['studentfirst3'], entry['studentlast3']],
                                          [entry['studentfirst4'], entry['studentlast4']]])
            current_teachers.append(entry['teacher2'])
        if entry['teacher3'] != '' and entry['teacher3'] not in current_teachers:
            entry['studentfirst1'], entry['studentfirst3'] = entry['studentfirst3'], entry['studentfirst1']
            entry['studentlast1'], entry['studentlast3'] = entry['studentlast3'], entry['studentlast1']
            program[entry['teacher3']].append([[entry['studentfirst1'], entry['studentlast1']],
                                          [entry['studentfirst2'], entry['studentlast2']],
                                          [entry['studentfirst3'], entry['studentlast3']],
                                          [entry['studentfirst4'], entry['studentlast4']]])
            current_teachers.append(entry['teacher3'])
        if entry['teacher4'] != '' and entry['teacher4'] not in current_teachers:
            entry['studentfirst1'], entry['studentfirst4'] = entry['studentfirst4'], entry['studentfirst1']
            entry['studentlast1'], entry['studentlast4'] = entry['studentlast4'], entry['studentlast1']
            program[entry['teacher4']].append([[entry['studentfirst1'], entry['studentlast1']],
                                          [entry['studentfirst2'], entry['studentlast2']],
                                          [entry['studentfirst3'], entry['studentlast3']],
                                          [entry['studentfirst4'], entry['studentlast4']]])
    return program

class TestGenerateEntries(unittest.TestCase):
    def testhookup(self):
        self.assertEqual(0,0)

    def testOneTeacherTwoStudents(self):
        entry = ['','timestamp\tname\tstudentfirst\tstudentlast\tBette\tparent\tparent email\telectrical\tother\ttotal\t\t\t\t\t\t\t\t\t']
        program = generateEntries(entry)
        self.assertEqual(program,
                         {'Jennifer': [], 'Carl': [], 'Edie': [], 'Mike': [], 'Adam': [], 'Mary': [],
                          'Bette': [[['studentfirst', 'studentlast'], ['', ''], ['', ''], ['', '']]],
                          'Aina': [], 'Heidi': [], 'Rick': [], 'Josh': [], 'Tyra': [], 'Peter': [],
                          'Ko': [], 'Chad': [], 'Tracey': [], 'Jamie': [], 'Denise': [], 'Diane': [], 'Leslie': []})

    def testOneTeacherTwoStudents(self):
        entry = ['','timestamp\tname\tstudentfirst\tstudentlast\tBette\tparent\tparent email\telectrical\tother\ttotal\tBob\tSmith\tBette\t\t\t\t\t\t']
        program = generateEntries(entry)
        self.assertEqual(program,
                         {'Jennifer': [], 'Carl': [], 'Edie': [], 'Mike': [], 'Adam': [], 'Mary': [],
                          'Bette': [[['studentfirst', 'studentlast'], ['Bob', 'Smith'], ['', ''], ['', '']]],
                          'Aina': [], 'Heidi': [], 'Rick': [], 'Josh': [], 'Tyra': [], 'Peter': [],
                          'Ko': [], 'Chad': [], 'Tracey': [], 'Jamie': [], 'Denise': [], 'Diane': [], 'Leslie': []})

    def testTwoTeachersTwoStudents(self):
        entry = ['','timestamp\tname\tstudentfirst\tstudentlast\tBette\tparent\tparent email\telectrical\tother\ttotal\tBob\tSmith\tJosh\t\t\t\t\t\t']
        program = generateEntries(entry)
        self.assertEqual(program,
                         {'Jennifer': [], 'Carl': [], 'Edie': [], 'Mike': [], 'Adam': [], 'Mary': [],
                          'Bette': [[['studentfirst', 'studentlast'], ['Bob', 'Smith'], ['', ''], ['', '']]],
                          'Aina': [], 'Heidi': [], 'Rick': [], 'Josh': [[['Bob', 'Smith'], ['studentfirst', 'studentlast'], ['', ''], ['', '']]], 'Tyra': [], 'Peter': [],
                          'Ko': [], 'Chad': [], 'Tracey': [], 'Jamie': [], 'Denise': [], 'Diane': [], 'Leslie': []})

    def testThreeTeachersThreeStudents(self):
        entry = ['','timestamp\tname\tstudentfirst\tstudentlast\tBette\tparent\tparent email\telectrical\tother\ttotal\tBob\tSmith\tJosh\tTom\tDoe\tLeslie\t\t\t']
        program = generateEntries(entry)
        self.maxDiff = None
        self.assertEqual(program,
                         {'Jennifer': [], 'Carl': [], 'Edie': [], 'Mike': [], 'Adam': [], 'Mary': [],
                          'Bette': [[['studentfirst', 'studentlast'], ['Bob', 'Smith'], ['Tom', 'Doe'], ['', '']]],
                          'Aina': [], 'Heidi': [], 'Rick': [], 'Josh': [[['Bob', 'Smith'], ['studentfirst', 'studentlast'], ['Tom', 'Doe'], ['', '']]], 'Tyra': [], 'Peter': [],
                          'Ko': [], 'Chad': [], 'Tracey': [], 'Jamie': [], 'Denise': [], 'Diane': [], 'Leslie': [[['Tom', 'Doe'], ['studentfirst', 'studentlast'], ['Bob', 'Smith'], ['', '']]]})

if __name__ == '__main__':
    unittest.main()


