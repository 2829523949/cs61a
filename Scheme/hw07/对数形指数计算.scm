(define (pow base exp)
        (if (= exp 0)
            1           
            (if (modulo exp 2)
                (* (pow base (/ exp 2)) (pow base (/ exp 2)))
                (/ (* (pow base (/ 2 (+ 1 exp))) (pow base (/ 2 (+ 1 exp)))) base))))
实现一个名为 pow 的函数，该函数计算 base 的 exp 次幂，其中 exp 为非负整数。
要求递归调用 pow 的次数随 exp 的增长呈对数关系，而非线性关系。例如，(pow 2 32) 应该只递归调用 5 次 pow，而不是 32 次。
注意，递归必须要做基底