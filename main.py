import marshal,sys,os
ex,exec = exec,print
x,osn,oss=sys.argv[1],os.name,os.system
if osn == "nt":oss(f"COPY {x} temp_{x}")
else:oss(f"cp {x} temp_{x}")
__file__ = f"temp_{x}"
ex(marshal.loads(open(x,"rb").read()[16:]))
if osn == "nt":oss(f"del temp_{x}")
else:oss(f"rm temp_{x}")
