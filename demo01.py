# import os
# import sys
# import uuid
# o_dir = os.path.join(sys.path[0],'exp6')
# if not os.path.exists(o_dir):
#     os.mkdir(o_dir)
# o_path = os.path.join(o_dir,'test.txt')
# with open(o_path,'w+') as f:
#     f.write(uuid.uuid1().__str__())
#
# t_dir = os.path.join(o_dir, 'copied')
# if not os.path.exists(t_dir):
#     os.mkdir(t_dir)
# t_path = os.path.join(t_dir, 'duplicated.txt')
# with open(o_path, 'w+', encoding="utf-8") as f1, open(t_path, 'r', encoding="utf-8") as f2:
#         f2.write(f1.read())
# with open(o_path, 'r', encoding="utf-8") as f1, open(t_path, 'r', encoding="utf-8") as f2:
#         print(f1.read())
#         print(f2.read())

import os
import sys
import uuid
o_dir = os.path.join(sys.path[0],'exp6')
if not os.path.exists(o_dir):
    os.mkdir(o_dir)
o_path = os.path.join(o_dir,'test.txt')


with open(o_path,'w+') as f:
    f.write(uuid.uuid1().__str__())

t_dir  = os.path.join(o_dir,'copied')
os.mkdir(t_dir)
t_path = os.path.join(t_dir,'duplicated.txt')
with open(o_path,'r',encoding = "utf-8") as f1,open(t_path,'w+',encoding ="utf-8") as f2:
    f2.write(f1.read())
with open(o_path,'r',encoding = "utf-8") as f1,open(t_path,'r',encoding ="utf-8") as f2:
    print(f1.read())
    print(f2.read())




