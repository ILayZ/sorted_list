from sortedcontainers import SortedList
sl = SortedList([10, 9, 8, 6, 7, 5, 4, 3, 2, 1])
print( sl )
sl.add(11)
print( sl )
del sl[5]
print( sl )
del sl[0]
print( sl )
del sl[len(sl)-1]
print( sl )
