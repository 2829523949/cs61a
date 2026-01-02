#定义 print_evals，它接受一个 Scheme 表达式 expr，该表达式仅包含数字、+、* 和括号。
#它会打印出在求值 expr 过程中所有被求值的表达式。打印顺序与 scheme_eval 的调用顺序一致。
def print_evals(expr):
    if not isinstance(expr,Pair):
        print expr
    else:
        current=expr
        print current
        while not current is nil:
            if isinstance(current.first,Pair):
                print_evals(current.first)
            else:
                print current.first
            current=current.rest