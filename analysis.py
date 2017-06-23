import os
import json

fn = 'C302_20170610-1.txt'
f = open(fn).read()
jl = []
jd = {}
fa = 0
dap = {}
for nn, i in enumerate(f.split('\r')):
	i = i.split('\t')
	al, yr, ti, jn = i[0], i[1], i[2], i[3]
	dap[nn]={'al':al.strip('"').strip().split(';'), 'year':yr, 'title':ti, 'jn':jn}


for n in dap:
	print dap[n]['al']



"""	
	if al.lstrip().startswith('Ip') or al.lstrip().startswith('"Ip') :
		fa +=1
		print al, jn
	if jn not in jl:
		jl.append(jn) 
	if jn not in jd:
		jd[jn] = 1
	else:
		jd[jn] = jd[jn] + 1

#print jl
jl.sort()

pprint.pprint(jl)
pprint.pprint(jd)
"""
