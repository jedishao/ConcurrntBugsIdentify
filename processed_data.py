import numpy as np
import os
from sklearn.model_selection import train_test_split

label_dict = {'药物': 'DRUG',
              '解剖部位': 'BODY',
              '疾病和诊断': 'DISEASES',
              '影像检查': 'EXAMINATIONS',
              '实验室检验': 'TEST',
              '手术': 'TREATMENT'}

TRAIN = './dataset/processed_data/train_dataset.txt'
VALID = './dataset/processed_data/val_dataset.txt'
TEST = './dataset/processed_data/test_dataset.txt'


def sentence2BIOlabel(sentence, label_from_file):
    """ BIO Tagging """
    sentence_label = ['O'] * len(sentence)
    if label_from_file == '':
        return sentence_label

    for line in label_from_file.split('\n'):

        entity_info = line.strip().split('\t')
        start_index = int(entity_info[1])
        end_index = int(entity_info[2])
        entity_label = label_dict[entity_info[3]]
        # Frist entity: B-xx
        sentence_label[start_index] = 'B-' + entity_label
        # Other: I-xx
        for i in range(start_index + 1, end_index):
            sentence_label[i] = 'I-' + entity_label
    return sentence_label


def loadRawData(fileName):
    """ Loading raw data and tagging """
    sentence_list = []
    label_list = []

    for file_name in os.listdir(fileName):

        if '.DS_Store' == file_name:
            continue

        if 'original' in file_name:
            org_file = fileName + file_name
            lab_file = fileName + file_name.replace('-original', '')

            with open(org_file, encoding='utf-8') as f:
                content = f.read().strip()

            with open(lab_file, encoding='utf-8') as f:
                content_label = f.read().strip()

            sentence_label = sentence2BIOlabel(content, content_label)
            sentence_list.append(content)
            label_list.append(sentence_label)

    return sentence_list, label_list


def Save_data(filename, texts, tags):
    """ Processing to files in neeed format """
    with open(filename, 'w') as f:
        for sent, tag in zip(texts, tags):
            size = len(sent)
            for i in range(size):
                f.write(sent[i])
                f.write('\t')
                f.write(tag[i])
                f.write('\n')

# Training data
sentence_list, label_list = loadRawData('./dataset/data/')
# Test data
sentence_list_test, label_list_test = loadRawData('./dataset/data_test/')

# Split dataset
words = [list(sent) for sent in sentence_list]
t_words = [list(sent) for sent in sentence_list_test]
tags = label_list
t_tags = label_list_test
train_texts, val_texts, train_tags, val_tags = train_test_split(words, tags, test_size=.2)
test_texts, test_tags = t_words, t_tags

# Obtain training, validating and testing files
Save_data(TRAIN, train_texts, train_tags)
Save_data(VALID, val_texts, val_tags)
Save_data(TEST, test_texts, test_tags)