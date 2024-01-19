from typing import Any, Dict, Sequence

from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.constants import FLOW_DICT
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.op.prompt import PromptTemplate

class ExpandReduceFlow(Flow):
    """Expand & Reduce flow class.
    """

    TAG = FLOW_DICT

    def __init__(
        self,
        prompt_template: PromptTemplate,
        model_config: Dict[str, Any],
    ) -> None:  # pylint: disable=useless-parent-delegation
        """Initialize Expand Reduce class."""
        self.expand = ExpandOp(name="expand_op")
        self.reduce = ReduceOp(name="reduce_op")
        super().__init__()

    def run(self, node: Node) -> Sequence[Node]:
        """Run Expand Flow.
        Args:
            nodes (Node): Input a root node.

        Returns:
            Sequence[Node]: Output two nodes.
        """
        return self.expand(node)
    def run(self, nodes: Sequence[Node]) -> Node:
        """Run Reduce Flow.

        Args:
            Sequence[Node]: Input two nodes

        Returns:
            Node: Output one node.
        """
        return self.reduce(nodes)