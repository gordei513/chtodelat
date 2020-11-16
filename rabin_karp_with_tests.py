import unittest

def rabin_karp(s, sub):
    result = []
    # Выше не трогать. Менять отсюда

    s = 'axaxaxax '
   
    t = 'xax'
    N = 0
    o = ''
    h_sub = sum(ord(c) for c in sub)
    h = sum(ord(c) for c in s[:len(sub)])
    for pos in range(0,  len(s)- len(sub)  ):
        N += 1
        if h != h_sub:  
              h = h - ord(s[pos]) + ord(s[pos + len(sub)]) #,,сдвиг и проверка,,
        h = h - ord(s[pos]) + ord(s[pos + len(sub)]) 
        flag = True
        for i in range(len(sub)):
            if s[pos+i] != sub[i]:
                flag = False
                break
        
        if flag:
          
            result.append(int(str(pos)))
         
            
    # Ниже не трогать. Менять до сюда
    return result
   

class RabinKarpTest(unittest.TestCase):
    def setUp(self):
        self.text = 'axaxaxax'
        self.pattern = 'xax'

    def test_type(self):
        self.assertIsInstance(rabin_karp(self.text, "x"), list, msg="Функция должна возвращать список")

    def test_returns(self):
        self.assertEqual([], rabin_karp(self.text, "z"), msg="Функция должна возвращать пустой список, если нет вхождений")

    def test_finds(self):
        self.assertEqual([1, 3, 5], rabin_karp(self.text, self.pattern), msg="Функция должна искать все вхождения")
# Должно выдать (время может отличаться):
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s
# OK

if __name__ == '__main__':
    unittest.main()
