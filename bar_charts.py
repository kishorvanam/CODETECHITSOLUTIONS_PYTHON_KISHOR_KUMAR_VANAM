import matplotlib.pyplot as plt
x = ["2017","2018","2019","2020","2021","2022"]
y=[200,220,310,400,450,100]
c=["red","blue","green","black"]
plt.bar(x,y,color=c,width=0.4)
plt.xlabel("Year")
plt.ylabel("Placement")
plt.show()