"""
OmniGraph core Python API:
  https://docs.omniverse.nvidia.com/kit/docs/omni.graph/latest/Overview.html

OmniGraph attribute data types:
  https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/ogn/attribute_types.html

Collection of OmniGraph code examples in Python:
  https://docs.omniverse.nvidia.com/kit/docs/omni.graph.docs/latest/dev/ogn/ogn_code_samples_python.html

Collection of OmniGraph tutorials:
  https://docs.omniverse.nvidia.com/kit/docs/omni.graph.tutorials/latest/Overview.html
"""


class OgnCarAddtestPyInternalState:
    """Convenience class for maintaining per-node state information"""

    def __init__(self):
        """Instantiate the per-node state information"""
        status = False


class OgnCarAddtestPy:
    """The Ogn node class"""

    @staticmethod
    def internal_state():
        """Returns an object that contains per-node state information"""
        return OgnCarAddtestPyInternalState()

    @staticmethod
    def compute(db) -> bool:
        """Compute the output based on inputs and internal state"""
        state = db.internal_state

        try:
            a = db.inputs.inputA
            b = db.inputs.inputB

            db.outputs.result = a + b

        except Exception as e:
            db.log_error(f"Computation error: {e}")
            return False
        return True
