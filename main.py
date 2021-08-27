jogo = [["A","D","H","A"],
["B","C","E","D"],
["B","H","F","C"],
["F","E","G","G"]] 
views = [['[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]']]
print ("""
   X  0   1   2   3
 Y |-----------------|
 0 | [ ] [ ] [ ] [ ] |
 1 | [ ] [ ] [ ] [ ] |
 2 | [ ] [ ] [ ] [ ] |
 3 | [ ] [ ] [ ] [ ] |""")   
print (""" 
---------------------------------   
|       Seja bem vindo ao       |
|      - jOGO DA MEMÓRIA -       |
---------------------------------
     """)
print ("  ") 
cont = 0
for i in range (0,16):
  for i in range (0,1):
    cont += 1
    y = int (input("Informe a posição desejada (y): "))
    x = int (input("Informe a posição desejada (x): ")) 
    views [y][x] = jogo [y][x] 
    n1 = jogo [y][x] 
    print ("""
    X  0  1  2  3
    Y |--------------|
    0 | %s%s%s%s |
    1 | %s%s%s%s |
    2 | %s%s%s%s |
    3 | %s%s%s%s |""" % (views [0][0], views [0][1], views [0][2], views [0][3],views [1][0],views [1][1],views [1][2],views [1][3],views [2][0],views [2][1],views [2][2],views [2][3],views [3][0],views [3][1],views [3][2],views [3][3])) 
  y = int (input("Informe a posição desejada (y): "))
  x = int (input("Informe a posição desejada (x): ")) 
  views [y][x] = jogo [y][x] 
  n2 = jogo [y][x] 
  print ("""
  X  0  1  2  3
  Y |--------------|
  0 | %s%s%s%s |
  1 | %s%s%s%s |
  2 | %s%s%s%s |
  3 | %s%s%s%s |""" % (views [0][0], views [0][1], views [0][2], views [0][3],views [1][0],views [1][1],views [1][2],views [1][3],views [2][0],views [2][1],views [2][2],views [2][3],views [3][0],views [3][1],views [3][2],views [3][3])) 
  if n1 != n2: 
    import os
    os.system("clear")  