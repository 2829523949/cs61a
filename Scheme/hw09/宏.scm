switch 是一个宏，它接受一个表达式 expr 和一个由数对 options 组成的列表。
每个数对的第一个元素是一个值，第二个元素则是一个表达式。
switch 会计算 options 列表中，与 expr 的计算结果相匹配的表达式。
scm> (switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b)) ; (print 'b) is evaluated because (+ 1 1) evaluates to 2
                      (3 (print 'c))))
b
switch 在其实现中使用另一个名为 switch-to-cond 的过程：
scm> (define-macro (switch expr options)
                   (switch-to-cond (list 'switch expr options))
     )
你的任务是定义 switch-to-cond，这是一个过程（而非宏），它接受一个带引号的 switch 表达式，并将其转换为行为相同的 cond 表达式。
例如：
scm> (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))

(define-macro (switch expr options) (switch-to-cond (list 'switch expr options)))
注意，这里将expr和options的字面量传入后在求值阶段是把整体都当作switch-to-cond的参数传入

(define (switch-to-cond switch-expr)
  (cons _________
    (map
      (lambda (option) (cons _______________ (cdr option)))
      (car (cdr (cdr switch-expr))))))