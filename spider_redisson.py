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


def get_content(issue_name):
    # 拼接issue地址
    # 4189
    #url = 'https://github.com/redisson/redisson/issues/' + str(issue_name)
    url = 'https://github.com/eclipse-vertx/vert.x/issues/' + str(issue_name)
    response = requests.get(url)
    # if str(response) == '<Response [404]>':
    page_source = response.text
    tree = etree.HTML(page_source)
    if len(tree.xpath('//title')) > 0:
        issue_title = tree.xpath('//title')[0].xpath('string(.)')
    else:
        issue_title = []

        # 获取issue内容
    if len(tree.xpath('//table//td')) != 0:
        issue_content = tree.xpath('//table//td')[0].xpath('string(.)')
    elif len(tree.xpath(
            '//div[@class="comment-body markdown-body js-comment-body soft-wrap user-select-contain '
            'd-block"]//p')) != 0:
        issue_content = \
            tree.xpath('//div[@class="comment-body markdown-body js-comment-body soft-wrap user-select-contain '
                       'd-block"]//p')[0].xpath('string(.)')
    elif len(tree.xpath('//td//p')) != 0:
        issue_content = tree.xpath('//td//p')[3].xpath('string(.)')
    else:
        issue_content = []

    return issue_title, issue_content


if __name__ == '__main__':
    with open(r'./results/projects/grpc.txt', 'a+', encoding='utf-8') as f:
        #repo = 'redisson/redisson'
        repo = 'eclipse-vertx/vert.x'
        # 拼接项目url
        repos_url = 'https://github.com/' + repo
        # print(repos_url)
        f.write('\n\n')
        f.write(repos_url)
        f.write('\n')
        # 获取项目的issues列表
        # number, issues_list = get_issues_list(repo)
        # f.write(str(number))
        # f.write('\n')
        issues_list = []
        for i in range(1836):
            i = i + 2487
            issues_list.append(str(i))
        # 格式：/combust/mleap/issues/716
        for issue in issues_list:
            # 获取issue的内容
            #issue_url = 'https://github.com/redisson/redisson/issues/' + issue
            issue_url = 'https://github.com/eclipse-vertx/vert.x/issues/' + issue
            # issue_url = 'https://github.com/grpc/grpc-java/issues/' + issue
            title, content = get_content(issue)
            # content=filter_emoji(content)
            # if content is None:
            #     print('S')
            #     continue
            print(issue_url)
            f.write(issue_url)
            f.write('\n')
            f.write(str(title) + '\n')
            f.write('>' * 100)
            f.write('\n')
            f.write(str(content).strip())
            f.write('\n')
            f.write('<' * 100)
            f.write('\n\n')
            f.flush()
            # print(content)
            # print(issue)
