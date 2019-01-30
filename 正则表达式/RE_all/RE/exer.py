import re 

f = open('test')
data = f.read() 

# pattern = r"\b[A-Z]+\w*" #单词

pattern = r"\b-?\d+\.?/?\d*%?\b" #数字

l = re.findall(pattern,data)
print(l)



