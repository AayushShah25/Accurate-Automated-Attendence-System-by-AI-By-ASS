

a = [ 1,2,3,2,2,2,1]


count = {}

for i in a:

	count[i] = a.count(i)


count = dict( (v,k) for k,v in count.items() )

print(count)
print(count[max(count)])

