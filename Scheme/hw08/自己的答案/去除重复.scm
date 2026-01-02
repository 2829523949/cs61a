实现 no-repeats 函数，该函数接受一个数字列表 s 作为输入。
它会返回一个新列表，其中包含 s 中所有不重复的元素，并按照它们首次出现的顺序排列。
例如，(no-repeats (list 5 4 5 4 2 2)) 的计算结果为 (5 4 2)。
提示： 你可能会发现使用带有 lambda 过程的 filter 函数来过滤重复项很有帮助。要测试两个数字 a 和 b 是否不相等，请使用 (not (= a b))。
注意：Scheme 标准（如 R5RS）中，不能在if的分支内直接用define重定义变量（define应在函数 /begin块的顶层定义）。
注意：递归时，要把改变的量box传入结果中
(define (no-repeats s)
        (define (container s box)
                (cond 
                    ((null? s) box)
                    ((member (car s) box) (container (cdr s) box))
                    (else (container (cdr s) (append box (list(car s)))))))
        (container s ()))            