def rabin_karp(s, sub):
    N = 0
    K = 0

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
            for i in range(pos+1, pos+1+len(t)):
               print(i, end=" " )
            print ()
        
            
         


s = 'ABCDABCDABCDAA' #Сама строка, в которой ищем подсктроку.
t = 'ABCD' #Подстрока, которую ищем в строке
O = s + '+' #Когда была длина s, то когда у подстроки не было справо других елементо, ее не считывало
rabin_karp(s, t)
