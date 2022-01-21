# import os
# import sys
# def login(usr,pwd,data):
#     if usr in data and data[usr] == pwd:
#         return True
#     else:
#         return False
# path = os.path.join(sys.path[0],'data.txt')
# data = {}
# with open(path,'r') as f:
#     content = f.readlines()
#     for i in content:
#         _usr,_pwd = i.split(' ')
#         data[_usr] = _pwd.strip('\n')
# retry = 3
# while True:
#     retry -= 1
#     usr = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     a = login(usr,pwd,data)
#     if a == True:
#         print(f'登陆成功','\n')
#         break
#     elif retry != 0:
#         print(f'登陆失败，还有{retry:d}次机会','\n')
#         continue
#     elif retry == 0:
#         print('多次登陆失败，请稍后再试','\n')
#         break
# import os
# import sys
#
#
# def login(usr, pwd, data):
#     if usr in data and data[usr]==pwd:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#
#     data = {}
#     data_path = os.path.join(sys.path[0], 'data.txt')
#     with open(data_path, 'r') as f:
#         content = f.readlines()
#         for item in content:
#             _usr, _pwd = item.split(' ')
#             data[_usr] = _pwd.strip('\n')
#
#     retry = 3
#     while True:
#         retry -= 1
#         usr = input('name: ')
#         pwd = input('password: ')
#         if login(usr, pwd, data):
#             break
#         elif retry != 0:
#             continue
#         else:
#             break

# import re
# key=r"<html><body><h1>hello world</h1></body></html>"
# p1="<h1>(+)</h1>"
# pattern1 =re.compile(p1)
# matcher1=re.search(pattern1, key)
# print(matcher1.group(1))
