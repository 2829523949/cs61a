实现一个名为 ascending? 的函数，它接收一个数字列表 s 作为参数。如果列表中的数字按非降序排列，函数返回 True，否则返回 False。
提示： 内置函数 null? 用于判断参数是否为 nil。
注意： ascending? 里的问号只是函数名的一部分，在 Scheme 语法中没有特殊含义。Scheme 习惯用问号结尾来命名返回布尔值的函数。
(define (ascending? s)
        (cond 
             ((null? (cdr s)) #t)
             ((> (car s) (car (cdr s))) #f)
             (else (ascending? (cdr s)))))