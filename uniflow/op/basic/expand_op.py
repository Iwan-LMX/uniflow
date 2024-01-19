import copy
from typing import Sequence

from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    def __call__(self, node: Node) -> Sequence[Node]:
        """Expand Operation. if root has value_dict has elements large than 1

        Args:
            nodes (Node): Input a root node.

        Returns:
            Sequence[Node]: Output two nodes.
        """
        if not node.value_dict or len(node.value_dict) ==1: return [node]
        output_nodes = []
        root_keys = list(node.value_dict.keys())
        root_half = len(root_keys) // 2
        #initial two nodes' value dict
        value_dict1 = {root_keys[i]: node.value_dict[root_keys[i]] for i in range(root_half)}
        value_dict2 = {root_keys[i]: node.value_dict[root_keys[i]] for i in range(root_half, len(root_keys))}

        #insert expand1
        output_nodes.append(
            Node(
                name = self.unique_name(),
                value_dict= value_dict1,
                prev_nodes=[node]
            )
        )
        #insert expand2
        output_nodes.append(
            Node(
                name = self.unique_name(),
                value_dict= value_dict2,
                prev_nodes=[node]
            )
        )
        return output_nodes