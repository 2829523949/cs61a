实现函数 curry-cook，它接受一个 Scheme 列表 formals 和一个带引号的表达式 body。
curry-cook 应该生成一个程序，该程序作为一个列表，是 lambda 函数的柯里化版本。
输出的程序应为一个柯里化的 lambda 函数，其形式参数为 formals，函数体为 body。
你可以假设所有传入的函数都至少有一个形式参数（formals）；否则，无法进行柯里化。
例如，如果你想柯里化函数 (lambda (x y) (+ x y))，
你可以将 formals 设置为 '(x y)，将 body 设置为 '(+ x y)，并调用 curry-cook：(curry-cook '(x y) '(+ x y))。
注意：cdr lst只要存在，一定返回列表形式，不用在套上list
(define (curry-cook formals body)
        (if (= (length formals) 1)
            (list 'lambda formals body)
            (list 'lambda (list (car formals)) (curry-cook  (cdr formals) body))))

实现函数 curry-consume，它接受一个柯里化的 lambda 函数 curry，并将该函数应用于参数列表 args。
你可以做出以下假设：
1.如果 curry 是一个经过 n 次柯里化的函数，那么 args 中最多可以包含 n 个参数。
2.如果参数数量为 0（args 是一个空列表），则你可以假设 curry 已经完全应用了相关的参数；
在这种情况下，curry 现在包含一个表示 lambda 函数输出的值。返回它。
请注意，对于相应的 lambda 函数 curry，args 的数量可能少于 formals！ 
如果提供的参数数量少于所需，curry-consume 应该返回一个柯里化的 lambda 函数，该函数是 curry 函数部分应用了已提供的参数后的结果。
(define (curry-consume curry args)
        (if (= (length args) 0)
            curry
            (curry-consume (curry (car args)) (cdr args))))
补充：在将列表传递为参数时，要用引用。