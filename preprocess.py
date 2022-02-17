import json

FILE1 = './dataset/subtask1_training_part1.txt'
FILE2 = './dataset/subtask1_training_part2.txt'
FILE3 = './dataset/subtask1_test_set_with_answer.json'

PATH1 = './dataset/data/data1-'
PATH2 = './dataset/data/data2-'
PATH3 = './dataset/data_test/data-test-'


def Process_File(FILENAME, PATH, enc):
    with open(FILENAME, 'r', encoding=enc) as f:
        i = 0
        while True:
            txt = f.readline()
            if not txt: break  # end loop
            i += 1
            j = json.loads(txt)
            orig = j['originalText']  # original text
            entities = j['entities']  # entity part
            pathO = PATH + str(i) + '-original.txt'
            pathE = PATH + str(i) + '.txt'

            with open(pathO, 'w', encoding='utf-8') as o1:  # write the original text
                o1.write(orig)
                o1.flush

            with open(pathE, 'w', encoding='utf-8') as o2:  # wirte entity file
                for e in entities:
                    start = e['start_pos']  # extract start position
                    end = e['end_pos']  # extract end position
                    name = orig[start:end]  # entity content
                    ty = e['label_type']  # entity label type
                    label = '{0}\t{1}\t{2}\t{3}\n'.format(name, start, end, ty)
                    o2.write(label)
                    o2.flush


Process_File(FILE1, PATH1, 'utf-8-sig')
Process_File(FILE2, PATH2, 'utf-8-sig')
Process_File(FILE3, PATH3, 'utf-8')