import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
file=open('Abhishek_1.txt','r')#Esta es una onda que significa "Like"
infile=file.read().rsplit('\n')

tempString = ' '.join(infile)
infile = tempString.rsplit(' ')
infile.remove('')
infile=list(map(float, infile))
#print(infile)

#plt.plot(infile)
#plt.show()

file2 = open('Abhishek_3.txt','r')#Esta es una onda que significa "Dislike"
infile2 = file2.read().rsplit('\n')

tempString2 = ' '.join(infile2)
infile2 = tempString2.rsplit(' ')
infile2.remove('')
infile2 = list(map(float, infile2))
#print(infile2)

plt.figure(1)
plt.subplot(211)
plt.plot(infile, 'b', label='Like')
plt.legend()
plt.subplot(212)
plt.plot(infile2, 'r', label='Dislike')
plt.legend()
#plt.plot(infile, infile2)
plt.show()


             