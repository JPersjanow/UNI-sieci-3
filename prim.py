import time
edge = [
        [1, ['A', 'B']],
        [2, ['A', 'C']],
        [2, ['A', 'D']],
        [6, ['A', 'E']],
        [4, ['B', 'D']],
        [5, ['B', 'E']],
        [3, ['C', 'D']],
        [3, ['D', 'E']],
        ]

#PRIM ALG
prime_starttime = time.clock()
vertex_amount = 5
x = ['A']
edge.sort()

start = 'A'
final_graf = []
sum_prim = 0
counter = 0

while len(x) < vertex_amount:
    edg = edge[counter]
    x1 = edg[1][0]
    x2 = edg[1][1]

    if x1 not in x and x2 not in x:
        counter = counter + 1

    elif x1 in x and x2 in x:
        edge.remove(edg)

    elif x1 in x and x2 not in x:
        final_graf.append(edg)
        x.append(x2)
        edge.remove(edg)
        sum_prim = sum_prim + edg[0]
        counter = 0

    elif x1 not in x and x2 in x:
        final_graf.append(edg)
        x.append(x1)
        edge.remove(edg)
        sum_prim = sum_prim + edg[0]
        counter = 0


print("PRIM ALGORITHM")
print("MST:")

for i in final_graf:
   print(i)

print("SUM: " + str(sum_prim))
prim_time = time.time() - prime_starttime
print("--%s sec--" % prim_time)
print("")
#KURSKAL
kurskal_starttime = time.clock()
edge = [
    [1, ['A', 'B']],
    [2, ['A', 'C']],
    [2, ['A', 'D']],
    [6, ['A', 'E']],
    [4, ['B', 'D']],
    [5, ['B', 'E']],
    [3, ['C', 'D']],
    [3, ['D', 'E']],
]
vertex = [['A'], ['B'], ['C'], ['D'], ['E']]

edge.sort()

final_graf = []
sum_kurskal = 0

while len(vertex[0]) < 5:
    edgg = edge[0]
    y1 = edgg[1][0]
    y2 = edgg[1][1]

    for i in vertex:
        if y1 in i:
            z1 = i
        if y2 in i:
            z2 = i
    if z1 != z2:
        vertex.remove(z1)
        vertex.remove(z2)
        vertex.append(z1 + z2)
        final_graf.append(edgg)
        sum_kurskal = sum_kurskal + edgg[0]
        edge.remove(edgg)
    else:
        edge.remove(edgg)

print("KURSKAL ALGORITHM")
print("MST:")
for i in final_graf:
    print(i)

print("SUM: " + str(sum_kurskal))
kurskal_time = time.time() - kurskal_starttime
print("--%s sec--" % kurskal_time)

print("")
print("estimated time difference: (PRIM/KURSKAL) " + str(prim_time/kurskal_time))