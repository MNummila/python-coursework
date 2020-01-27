import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,6,7,8]
x2=[1,2,3,4]
y2=[3,5,7,9]
plt.bar(x,y  ,label='palkkejaaaa')
plt.bar(x2,y2,label='piikkee')
plt.xlabel('Kellonaika')
plt.ylabel('Matkamäärä')
plt.title('Matkoja eri kellonaikoina')
plt.legend()
plt.show()