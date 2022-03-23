# @Time    : 3/21/22 4:01 PM
# @Author  : Shuai S
# @File    : spider_redisson.py

import requests
from lxml import etree


def get_404():
    # 拼接issue地址
    issue_404 = []
    issue_content = []
    issue_title = []
    for issue_name in range(4189):
        issue_name = issue_name + 1
        url = 'https://github.com/redisson/redisson/issues/' + str(issue_name)
        print(url)
        response = requests.get(url)
        if str(response) == '<Response [404]>':
            issue_404.append(issue_name)
            return issue_404, issue_title, issue_content
        page_source = response.text
        tree = etree.HTML(page_source)
        # 获取issue内容
        if len(tree.xpath('//table//td')) == 0:
            issue_content.append(url)
            return issue_404, issue_title, issue_content
        # if len(tree.xpath('//table//td')) > 0:
        #     issue_content = tree.xpath('//table//td')[0].xpath('string(.)')

        # if len(tree.xpath('//h1[@class="gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word"]/span')) > 0:
        #     issue_title = \
        #         tree.xpath('//h1[@class="gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word"]/span')[
        #             0].xpath('string(.)')


def get_content():
    # 拼接issue地址
    issue_404 = []
    issue_content = []
    issue_divp = []
    issue_tdp = []
    for issue_name in range(4189):
        issue_name = issue_name + 1
        url = 'https://github.com/redisson/redisson/issues/' + str(issue_name)
        print(url)
        response = requests.get(url)
        if str(response) == '<Response [404]>':
            issue_404.append(issue_name)
        page_source = response.text
        tree = etree.HTML(page_source)
        # 获取issue内容
        if len(tree.xpath('//table//td')) == 0:
            if len(tree.xpath(
                    '//div[@class="comment-body markdown-body js-comment-body soft-wrap user-select-contain '
                    'd-block"]//p')) != 0:
                issue_divp.append(url)
                continue
            elif len(tree.xpath('//td//p')) != 0:
                issue_tdp.append(url)
                continue
            else:
                issue_content.append(url + "ss")
            return issue_divp, issue_tdp, issue_content


if __name__ == '__main__':
    issue_content = get_content()
    print(issue_content)
    # url = 'https://github.com/redisson/redisson/issues/' + str(86)
    # response = requests.get(url)
    # page_source = response.text
    # tree = etree.HTML(page_source)
    # print(tree.xpath('//td//p')[0].xpath('string(.)'))
    # print(tree.xpath(
    #     '//div[@class="comment-body markdown-body js-comment-body soft-wrap user-select-contain d-block"]//p')[0].xpath(
    #     'string(.)'))
    # print(page_source)
