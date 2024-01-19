from typing import Sequence

from uniflow.node import Node
from uniflow.op.op import Op

class ReduceOp(Op):
    Exception()
    def __call__(self, nodes: Sequence[Node]) -> Node:
        """Reduce Operation. 

        Args:
            Sequence[Node]: Input two nodes

        Returns:
            Node: Output one node.
        """
        expand1 = list(nodes[0].value_dict.items())
        expand2 = list(nodes[1].value_dict.items())
        value_dict = {}
        if len(expand1) != len(expand2):
            raise ValueError('Node Expand1 and Expand2 should in same length.')
        
        for i in range(len(expand1)):
            key = expand1[i][0] + ' ' + expand2[i][0]
            value_dict[key] = expand1[i][1] + ' ' + expand2[i][1]
        
        return Node(self.unique_name(), value_dict, nodes)