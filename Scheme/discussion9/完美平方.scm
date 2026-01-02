写一个函数 fit(total, n)，输入两个非负整数 total 和 n，判断是否存在 n 个不同的正完全平方数，加起来等于 total。
思路：从小往大递归，如果当前最小的平方比当前n大，那么直接#f 
补充：调用函数时，像定义函数时一样即可
(define (fit total n)
        (define (add_k total n k)
                (cond ((or (< n 1) (< total (* k k))) #f)
                      ((and (= n 1)(= total (* k k))) #t)
                      (else (or (add_k (- total (* k k)) (- n 1) (+ k 1))
                                (add_k total n (+ k 1))))))
        (add_k total n 1))