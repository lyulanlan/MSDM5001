import re
f=open('blocklist.xml', 'r')
for line in f.readlines():
    if re.search("emItem blockID=\"[ig]\\d+\"", line):
        print(line)
        
import re        
f=open("blocklist.xml","r")
for line in f.readlines():
    if re.search(r"id=\"\w+@\w+(\.\w+)+", line):
        print(line)
