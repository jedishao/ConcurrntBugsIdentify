# 导入minidom
from xml.dom import minidom

# 1.创建DOM树对象
dom = minidom.Document()
# 2.创建根节点。每次都要用DOM对象来创建任何节点。
root_node = dom.createElement('root')
# 3.用DOM对象添加根节点
dom.appendChild(root_node)

# 用DOM对象创建元素子节点
book_node = dom.createElement('book')
# 用父节点对象添加元素子节点
root_node.appendChild(book_node)
# 设置该节点的属性
book_node.setAttribute('price', '199')

name_node = dom.createElement('name')
root_node.appendChild(name_node)
# 也用DOM创建文本节点，把文本节点（文字内容）看成子节点
name_text = dom.createTextNode('计算机程序设计语言 第1版')
# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
name_node.appendChild(name_text)

# 每一个结点对象（包括dom对象本身）都有输出XML内容的方法，如：toxml()--字符串, toprettyxml()--美化树形格式。

try:
    with open('../dataset/dom_write.xml', 'w', encoding='UTF-8') as fh:
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
        print('OK')
except Exception as err:
    print('错误：{err}'.format(err=err))
