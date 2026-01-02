(define (repeated_cube n x)
        (if (= n 0)
            x
            (let ((cube (repeated_cube (- n 1) x)))
                 (* cube cube cube))))
实现 repeatedly-cube 函数，它接受一个数字 x，并对其进行 n 次立方运算。
补充：这里的立方运算指代在计算结果上再次取立方