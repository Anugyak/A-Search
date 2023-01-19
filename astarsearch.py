
#Input Graph
graph = {"S": ["A", "D"], "A": ["S", "B", "C"],
          "B": ["A", "C", "D", "E"], "C": ["A", "B", "G"],
          "D": ["S", "B", "E"], "E": ["B", "D", "G"], "G": ["C", "E"]}
#Input Heiristic
heuristic = {"S": 7, "A": 9, "B": 4, "C": 2, "D": 5, "E": 3, "G": 0}
#Path Cost
pathcost = {"AS": 3, "DS": 4, "AB": 2, "AC": 5, "BD": 1, "BC": 2, "BE": 1, "CG": 4, "DE": 5, "EG": 13}
#Initializing Empty Queue
queue = []
#Initializing Cost List
cost = []

def PC(path):
    he = 0
    for i in heuristic:
        if i in path:
            he = he + heuristic[i]
    for i in range(len(path) - 1):
        val1 = path[i]
        val2 = path[i + 1]
        temp = [val1, val2]
        temp.sort()
        sn = ""
        for j in temp:
            sn = sn + j
        if sn in pathcost:
            he = he + pathcost[sn]
        del sn
        del temp
    return he
def add_path(path):
    temp = []
    for i in path:
        temp.append(i)
    queue.append(temp)
def r(node, trace, goal):
    if goal in trace:
        #print("returned ",trace)
        add_path(trace)
        cost.append(PC(trace))
        return
    if node not in trace:
        trace.append(node)
    child = graph[node]
    for i in child:
        if i not in trace:
            r(i, trace, goal)
    trace.remove(node)
def A_star_search():
    r("S", [], "G")
    re_p = []
    c = 100
    for i in range(len(queue)):
        print(queue[i], "cost = ",cost[i])
        if cost[i] < c:
            c = cost[i]
            re_p = queue[i]
    return re_p, c

print("Possible path and cost are: ")
print("\nThe path and cost are returned by A* search as:-\n", A_star_search())






