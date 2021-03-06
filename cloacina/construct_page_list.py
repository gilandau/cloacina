def construct_page_list(total_results):
    total_results = int(total_results)
    base_iter = total_results / 10
    remainder = total_results % 10

    iter_list = []
    
    if total_results == 0:
        return [(0, 0)]

    if total_results < 10:
        return [(1, total_results)]
    
    for i in range(base_iter):
        iter_list.append((i * 10 + 1, i * 10 + 10))

    if remainder:
        iter_list.append((range(base_iter)[-1] * 10 + 10 + 1, range(base_iter)[-1] * 10 + 10 + remainder))

    return iter_list
