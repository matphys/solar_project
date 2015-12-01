import matplotlib.pyplot as plt
status=open('status.txt','a')
print('the end',file=status)
status.close()
input=open('status.txt','r')                    #append
name=['grey','orange','blue','green','red','yellow','white','gray']
skorost=[[]for i in range(8)]
radius=[[]for i in range(8)]
strt=''
strt=input.readlines()
for i in rag
    ind=name.index(strt[:strt.find(' ')])
    strt=strt[strt.find(' ')+1:]
    x=float(strt[:strt.find(' ')])
    strt=strt[strt.find(' ')+1:]
    y=float(strt[:strt.find(' ')])
    strt=strt[strt.find(' ')+1:]
    vx=float(strt[:strt.find(' ')])
    strt=strt[strt.find(' ')+1:]
    vy=float(strt[:strt.find(' ')])
    strt=strt[strt.find(' ')+1:]
    skorost[ind].append((vx**2+vy**2)**0.5)
    radius[ind].append((x**2+y**2)**0.5)
plt.plot(radius[0],skorost[0])
plt.show
