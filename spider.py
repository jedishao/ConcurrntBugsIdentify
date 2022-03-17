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

    if len(tree.xpath('//h1[@class="gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word"]/span')) > 0:
        issue_title = \
            tree.xpath('//h1[@class="gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word"]/span')[
                0].xpath('string(.)')

    return issue_title, issue_content


if __name__ == '__main__':
    # 测试
    # get_repos_list('ML pipeline')
    # get_issues('/combust/mleap')
    # get_issue_content('/combust/mleap/issues/716')
    '''
    issue="/rust-lang/rust/issues/76833"
    content=get_issue_content(issue)
    print(content)

    '''
    with open(r'./results/projects/grpc.txt', 'w+', encoding='utf-8') as f:
        # key_words = input('please input a keyword：')
        # 获取项目列表
        # repos_list = get_repos_list(key_words)
        # 格式：/combust/mleap
        # for repo in repos_list:
        # repo = 'redisson/redisson'
        # repo = 'jedishao/FineLock'
        # repo = 'eclipse-vertx/vert.x'
        repo = 'grpc/grpc-java'
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
        for i in range(4186):
            i = i + 1
            issues_list.append(str(i))
        # 格式：/combust/mleap/issues/716
        for issue in issues_list:
            # 获取issue的内容
            issue_url = 'https://github.com/grpc/grpc-java/issues/' + issue
            # issue_url = 'https://github.com/redisson/redisson/issues/' + issue
            # issue_url = 'https://github.com/grpc/grpc-java/issues/' + issue
            title, content = get_issue_content(issue)
            # content=filter_emoji(content)
            if content is None:
                print('S')
                continue
            print(issue_url)
            f.write(issue_url)
            f.write('\n')
            f.write(title+'\n')
            f.write('>' * 100)
            f.write('\n')
            f.write(str(content).strip())
            f.write('\n')
            f.write('<' * 100)
            f.write('\n\n')
            f.flush()
            # print(content)
            # print(issue)
