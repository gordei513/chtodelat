def rabin_karp(s, sub):
    N = 0
    K = 0
    T = ' '
    
    h_sub = sum(ord(c) for c in sub)
    h = sum(ord(c) for c in s[:len(sub)])
    for pos in range(0,  len(O)- len(sub)  ):
        N += 1
        if h != h_sub:  
            h = h - ord(O[pos]) + ord(O[pos + len(sub)]) #,,сдвиг и проверка,,
        h = h - ord(O[pos]) + ord(O[pos + len(sub)]) 
        flag = True
        for i in range(len(sub)):
            if s[pos+i] != sub[i]:
                flag = False
                break
         
            K += 1 
        if flag:
            T = T  + ', ' + str(pos)
            T = T[1:] 
            
    return(T)
   
        

s = 'abababab' #Сама строка, в которой ищем подсктроку.
t = 'bab' #Подстрока, которую ищем в строке
O = s + '+' #Когда была длина s, то когда у подстроки не было справо других елементо, ее не считывало
rabin_karp(s, t)
if(rabin_karp(s, t) == "1, 3, 5"):
    print('Проверка успешна')
else:
  print('Проверка прошла неудачно')




