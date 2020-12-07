import networkx as nx

bags_and_contents = open("2020/inputs/input07.txt", "r").readlines()


# part 1

g = nx.DiGraph()

for s in bags_and_contents:
    s1, s2 = s.split(" bags contain ")
    s2a = s2.replace(".\n", "").replace(
        " bags", "").replace(" bag", "").split(", ")
    s2b = list(map(lambda x: x.split(" ", 1), s2a))
    g.add_node(s1)
    if(s2 != "no other bags.\n"):
        for n, b in s2b:
            g.add_node(b)
            g.add_edge(b, s1, num=int(n))

print(len(nx.descendants(g, "shiny gold")))


# part 2

gr = g.reverse()


def num_bags(g, bag):
    n = 0
    for d in g.successors(bag):
        n += g.edges[bag, d]["num"] * (num_bags(g, d) + 1)
    return n


print(num_bags(gr, "shiny gold"))
