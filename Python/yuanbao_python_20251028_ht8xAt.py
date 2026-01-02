def feline_fixes(typed, source, limit):
    """ 计算将 typed 转换为 source 所需的最小替换次数 + 长度差异，不超过 limit """
    def recursion(typed, source, total):
        # 终止条件：替换次数已超过 limit，返回 limit+1
        if total > limit:
            return limit + 1
        # 处理其中一个字符串已遍历完的情况：剩余长度即为需要补充的差异
        if not typed:
            return total + len(source)
        if not source:
            return total + len(typed)
        # 比较当前首字符：不同则替换次数+1，相同则不变
        if typed[0] != source[0]:
            total += 1
            # 若已超限，提前返回
            if total > limit:
                return limit + 1
        # 递归处理剩余字符
        return recursion(typed[1:], source[1:], total)
    
    # 初始化替换次数为 0，启动递归
    return recursion(typed, source, 0)