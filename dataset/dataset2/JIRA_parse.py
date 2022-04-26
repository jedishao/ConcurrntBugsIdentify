# @Time    : 4/21/22 9:02 PM
# @Author  : Shuai S
# @File    : JIRA_parse.py
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("zookeeper/lock.xml")
collection = DOMTree.documentElement

title = collection.getElementsByTagName("type")
description = collection.getElementsByTagName("description")
for t in title:
    print(t.childNodes[0].data)

# for t in title:
#     print(t.childNodes[0].data)
# for t in description:
#     for h in t.getElementsByTagName('p'):
#         if str(type(h.childNodes[0])) == "<class 'xml.dom.minidom.Text'>":
#             print(h.childNodes[0].data, end='')
#     print()

# to = open('zookeeper/title.txt', 'r')
# co = open('zookeeper/content.txt', 'r')
# ro = open('zookeeper/lock.txt', 'w')
# tlist = []
# clist = []
# for line1 in to.readlines():
#     tlist.append(line1)
#
# for line2 in co.readlines():
#     clist.append(line2)
#
# for i in range(len(clist)):
#     ro.write(tlist[i])
#     ro.write(clist[i])
#     ro.write('\n')
