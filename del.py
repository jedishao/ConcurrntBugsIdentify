# @Time    : 4/2/22 8:23 PM
# @Author  : Shuai S
# @File    : del.py
import labelOfdata

re = []
for c in labelOfdata.redisson_exc:
    if c not in labelOfdata.ste_exc:
        re.append(c)
print(labelOfdata.redisson_exc)
