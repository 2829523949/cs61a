实现函数 interleave，它接收两个列表 lst1 和 lst2 作为参数。
interleave 函数应该返回一个新列表，这个列表由 lst1 和 lst2 的元素交替组成。
也就是说，新列表的元素应该在 lst1 和 lst2 之间交替出现，并且从 lst1 的元素开始。
如果 interleave 函数的其中一个输入列表比另一个短，那么它应该交替地从两个列表中取元素，直到其中一个列表用完为止，
然后将较长列表中剩余的元素添加到新列表的末尾。
(define (interleave lst1 lst2)
        (cond 
             ((null? lst1) lst2)
             ((null? lst2) lst1)
             (else (append (list (car lst1)) (list (car lst2)) (interleave (cdr lst1) (cdr lst2))))))
最后也可以用cons代替append list，豆包认为这样效率更高