import datetime

st = datetime.datetime.now()
s = []
for i in range(0, 10000):
    s += str(i)

et = datetime.datetime.now()
print(et - st)

st = datetime.datetime.now()
s = []
for i in range(0, 10000):
    s.append(str(i))
"".join(s)

et = datetime.datetime.now()
print(et - st)
