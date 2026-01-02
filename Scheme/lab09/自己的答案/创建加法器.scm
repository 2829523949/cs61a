(define (make_adder num)
        (lambda (inc) (+ num inc)))
'另一种写法'
(define (make_adder num)
        (define (inner inc) (+ num inc))
        inner)
'注意，是(+ num inc)而不是(num+inc)'