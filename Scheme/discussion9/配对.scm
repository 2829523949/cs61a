实现 pair-up 函数，该函数接收列表 s 作为输入，并返回一个列表的列表，其中包含 s 的所有元素，且顺序不变。
结果列表中，每个子列表应包含 2 个元素，最后一个子列表最多可包含 3 个元素。
注意，cons要求cdr也必须是cons格式，而list则不用
(define (pair-up s)
        (if (< (length s) 4) 
            (list s)
            (append (list (car s) (car (cdr s))) (pair-up (cdr (cdr s))))))