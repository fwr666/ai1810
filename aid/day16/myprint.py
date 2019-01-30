import sys
def myprint(*args,sep=' ',end='\n',file=sys.stdout,flush=False):
    flag=False
    L = [str(obj) for obj in args]
    file.write(sep.join(L))
    file.write(end)