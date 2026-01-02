(define (repeat f n)
        (define (work x)
                 (if (= n 1) 
                     (f x)
                     (f ((repeat f (- n 1))x))))
        work)
编写一个名为 repeat 的过程, 它接受一个过程 f 和一个数字 n, 并返回一个新的过程
这个新过程接收一个数字 x, 并将 f 应用于 x，总共 n 次，并输出结果。