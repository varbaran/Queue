from queue import Queue


def neighbours(v, moves):
    n = []
    x_v = v[0]
    y_v = v[1]
    for i in range(len(moves)):
        move = moves[i]
        x_m = move[0]
        y_m = move[1]
        if 0 <= x_m + x_v <= 7 and 0 <= y_m + y_v <= 7:
            n.append((x_m + x_v, y_m + y_v))
    return n


moves = [
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1)
]

visited = {}
visited_2 = {}

r = int(input(f"please enter th a_hors's row (0-7): "))
c = int(input(f"please enter th a_hors's column (0-7): "))
r_2 = int(input(f"please enter th a_hors's row (0-7): "))
c_2 = int(input(f"please enter th a_hors's column (0-7): "))

first_source = (r , c)
seceund_source= (r_2 , c_2)

destination = (5, 7)
q = Queue()
q.put(first_source)
visited[first_source] = (0 , None)
visited_2[seceund_source] = (0 , None)

while not q.empty():
    v = q.get()
    for e in neighbours(v, moves):
        if e not in visited.keys():
            q.put(e)
            visited[e] = v
    if destination in visited.keys():
        break

while not q.empty():
    q.get()

q.put(seceund_source)
while not q.empty():
    v = q.get()
    for e in neighbours(v, moves):
        if e not in visited_2.keys():
            q.put(e)
            visited_2[e] = v
    if destination in visited_2.keys():
        break


def get_route(source , destination , visited):
    route = []
    route.append(destination)
    corrent = destination
    while source not in route:
        route.append(visited[corrent])
        corrent = visited[corrent]
    route.reverse()
    return len(route) - 1, route


steps_1, route_1 = get_route(first_source, destination, visited)
steps_2, route_2 = get_route(seceund_source, destination, visited_2)
print(route_1)
print(route_2)
print(steps_1)
print(steps_2)


if steps_1 < steps_2:
    print(" the first horse is faster")
elif steps_1 > steps_2:
    print(" the seceund horse is faster")
else:
    print("equal")
