(define (gcd a b)
        (if (= a b)
            a
            (gcd (- (max a b) (min a b)) (min a b))))
这里也可以利用module: modulo（或者mod） a b 返回a对b取模，可以优化效率