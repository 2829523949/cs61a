编写一个函数 my-filter，它接收一个谓词函数 pred 和一个列表 s 作为参数，并返回一个新列表，其中只包含 s 中满足 pred 条件的元素。
返回的列表应该保持元素在原列表中的顺序。
注意： 请不要直接调用 Scheme 内置的 filter 函数，我们需要你自己实现一个！此外，判断是否为nil应该用null?而不是=
技巧：使用append可以实现列表拼接
(defiine (my-filter pred s)
         (cond 
              ((null? s) nil)
              ((pred (car s)) (append (list (car s)) (my-filter pred (cdr s))))
              (else (my-filter pred (cdr s)))))