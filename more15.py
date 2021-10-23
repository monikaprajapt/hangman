def find_in_list(query, mainlist):

# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None

    mainlist_len = len(query)

    range_for_loop = range(mainlist_len)

    index = None

    for i in range_for_loop:

        element = mainlist[i]

        if element == query:

            index = i

    return i
