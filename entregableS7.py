"""
for i in range(10):
    for j in range(10):
        print("Ciclo externo:", i, "Ciclo interno", j)
    print()
"""

################################
"""
0 x 0 = 0
0 x 1 = 0
...
...
10 x 9 = 90
10 x 10 = 100
"""
for i in range(11): 
     for j in range(11):
         num = i*j
         print(i,"x", j, "=", num)
     print()     
else: 
    print (' Felicidades') 