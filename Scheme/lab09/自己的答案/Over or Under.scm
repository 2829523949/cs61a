(define (Over_and_Under num_1 num_2)
        (cond((< num_1 num_2) -1)
             ((= num_1 num_2)  0) 
             ((> num_1 num_2)  1)))
'另一种使用if的实现方式'
(define (Over_and_Under num_1 num_2)
        (if (< num_1 num_2) -1
         else(
             if(= num_1 num_2) 0)
             else 1))
'注意，Scheme里面，直接的数字/参数不用额外加括号，需要评估的表达式才需要'