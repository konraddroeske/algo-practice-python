from collections import defaultdict
from typing import Optional

from tqdm import tqdm


class BitsEdge:
    def __init__(self, tail: str, head: str, distance: int) -> None:
        self.tail = tail
        self.head = head
        self.distance = distance

    def __lt__(self, obj: "BitsEdge") -> bool:
        return self.distance < obj.distance

    def __eq__(self, obj: "BitsEdge") -> bool:
        return self.distance == obj.distance

    def __hash__(self) -> int:
        return hash(repr(self))

    def __repr__(self) -> str:
        return (
            f"BitsEdge(tail: {self.tail}, head: {self.head}, distance: {self.distance})"
        )


class BitsNode:
    def __init__(self, label: str, leader: str) -> None:
        self.label = label
        self.leader = leader

    def __repr__(self) -> str:
        return f"BitsNode(label: {self.label}, leader: {self.leader})"

    def update_leader(self, new_leader: str) -> None:
        self.leader = new_leader


class BitsGraph:
    def __init__(self) -> None:
        self.graph: dict[str, BitsNode] = {}
        self.groups: dict[str, list[str]] = defaultdict(list)

    def union(self, edge: BitsEdge) -> None:
        tail_node = self.graph.get(edge.tail)
        head_node = self.graph.get(edge.head)

        if tail_node is None:
            tail_node = BitsNode(edge.tail, edge.tail)
            self.graph[edge.tail] = tail_node
            self.groups[edge.tail] = [edge.tail]

        if head_node is None:
            head_node = BitsNode(edge.head, edge.head)
            self.graph[edge.head] = head_node
            self.groups[edge.head] = [edge.head]

        # merge smaller into larger
        tail_group = self.groups[tail_node.leader]
        head_group = self.groups[head_node.leader]

        if len(tail_group) == 0:
            print("Tail Group is 0 - Already Merged")
            return

        if len(head_group) == 0:
            print("Head Group is 0 - Already Merged")
            return

        if len(head_group) > len(tail_group):
            orig_tail_node_leader = tail_node.leader

            for cur_label in tail_group:
                self.graph[cur_label].leader = head_node.leader
                head_group.append(cur_label)

            self.groups[orig_tail_node_leader] = []

        else:
            orig_head_node_leader = head_node.leader

            for cur_label in head_group:
                self.graph[cur_label].leader = tail_node.leader
                tail_group.append(cur_label)

            self.groups[orig_head_node_leader] = []

    def is_cycle(self, edge: BitsEdge) -> bool:
        tail_leader = self.find_leader(edge.tail)

        if tail_leader is None:
            return False

        head_leader = self.find_leader(edge.head)

        if head_leader is None:
            return False

        return tail_leader == head_leader

    def find_leader(self, edge_label: str) -> Optional[str]:
        target_node = self.graph.get(edge_label)

        if target_node is None:
            return None

        return target_node.leader


nodes_hash = {}

with open("clustering_input_big.txt") as f:
    for input_index, line in enumerate(f):

        if input_index == 0:
            split_line = [int(val) for val in str.split(line)]
            input_nodes = split_line[0]
            bits_length = split_line[1]
        else:
            line = "".join(line.split())
            nodes_hash[line] = True

print(f"Input nodes w/ distance > 0: {len(nodes_hash)}")


def get_before_and_after(orig_node: str, index: int) -> tuple[str, str]:
    try:
        before = orig_node[:index]
    except IndexError:
        before = ""

    try:
        after = orig_node[index + 1 :]
    except IndexError:
        after = ""

    return before, after


def get_edges_from_node(
    orig_node: str, orig_nodes_hash: dict[str, bool]
) -> list[BitsEdge]:
    results = []

    # Distance 1
    for index_d1, char_d1 in enumerate(orig_node):
        before_d1, after_d1 = get_before_and_after(orig_node, index_d1)
        swapped_char_d1 = "1" if char_d1 == "0" else "0"
        merged_d1 = before_d1 + swapped_char_d1
        new_node_d1 = merged_d1 + after_d1

        if orig_nodes_hash.get(new_node_d1):
            results.append(BitsEdge(orig_node, new_node_d1, 1))

        # Distance 2
        for index_d2, char_d2 in enumerate(after_d1):
            before_d2, after_d2 = get_before_and_after(after_d1, index_d2)
            swapped_char_d2 = "1" if char_d2 == "0" else "0"
            new_node_d2 = merged_d1 + before_d2 + swapped_char_d2 + after_d2

            if orig_nodes_hash.get(new_node_d2):
                results.append(BitsEdge(orig_node, new_node_d2, 2))

    return results


total_input_edges = set()

for node in nodes_hash.keys():
    all_edges = get_edges_from_node(node, nodes_hash)

    for cur_edge in all_edges:
        total_input_edges.add(cur_edge)

print(f"Total input edges: {len(total_input_edges)}")


def get_min_clusters(input_edges: set[BitsEdge], total_nodes: int) -> int:
    sorted_edges = sorted(list(input_edges))
    tree = BitsGraph()

    cur_clusters = total_nodes

    for index in tqdm(range(len(sorted_edges))):
        input_edge = sorted_edges[index]

        is_cycle = tree.is_cycle(input_edge)

        if not is_cycle:
            tree.union(input_edge)
            cur_clusters -= 1

    return cur_clusters


print(f"Min clusters: {get_min_clusters(total_input_edges, len(nodes_hash))}")
