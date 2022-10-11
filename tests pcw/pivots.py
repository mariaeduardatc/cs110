indices = [(0, len([1,2,4]))]
while indices:
    (frm, to) = indices.pop()
    print(frm, to)
    print(indices.pop())
