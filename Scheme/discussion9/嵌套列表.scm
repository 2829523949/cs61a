用三种不同的方式创建下面描述的嵌套列表：使用 list、quote 和 cons。
注意，使用list时如果没有'会评估，而使用'创建则直接是字面量。
此外，(cons a (cons b nil))结果是(a b)(在scheme里面默认链接的要是链表形式)，需要(cons a (cons (cons b nil) nil))才是(a (b))
(cons (cons a (cons (cons b nil) nil)) (cons c (cons d (cons (cons e nil) nil))))
(list (list 'a (list 'b)) 'c 'd (list 'e))
'((a (b)) c d (e))
