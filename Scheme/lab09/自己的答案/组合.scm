(define (composed f g )
        (define (inner x)
                (f (g x)))
        inner)
'编写函数 composed，它接受函数 f 和 g 并输出一个新函数。 这个新函数接受一个数字 x 并输出对 x 应用 g 之后再应用 f 的结果。'