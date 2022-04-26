from lxml import etree
import requests


# 获取一个issue的内容及评论
def get_issue_content(issue_name):
    # 拼接issue地址
    # url = 'https://github.com/redisson/redisson/issues/' + issue_name
    # url = 'https://github.com/jedishao/FineLock/issues/' + issue_name
    url = 'https://github.com/grpc/grpc-java/issues/' + issue_name

    # print(url)
    issue_content = []
    issue_title = []
    response = requests.get(url)
    if str(response) == '<Response [404]>':
        return None
    page_source = response.text
    tree = etree.HTML(page_source)
    # 获取issue内容
    if len(tree.xpath('//table//td')) > 0:
        issue_content = tree.xpath('//table//td')[0].xpath('string(.)')

    if len(tree.xpath('//div[@id="ticket_content"]')) > 0:
        issue_title = \
            tree.xpath('//h1[@class="gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word"]/span')[
                0].xpath('string(.)')

    return issue_title, issue_content


if __name__ == '__main__':
    url = 'https://github.com/redisson/redisson/issues/1079'

    # print(url)
    issue_content = []
    issue_title = []
    response = requests.get(url)
    page_source = response.text
    tree = etree.HTML(page_source)
    # print(tree.xpath('//div[@id="ticket_content"]')[0].xpath('string(.)'))
    print(page_source)
    # tree = etree.HTML(page_source)
