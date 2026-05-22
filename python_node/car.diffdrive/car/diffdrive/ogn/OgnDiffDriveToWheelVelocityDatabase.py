"""Support for simplified access to data on nodes of type car.diffdrive.OgnDiffDriveToWheelVelocity."""

import sys
import traceback

import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn


class OgnDiffDriveToWheelVelocityDatabase(og.Database):
    """Helper class providing access to data on car.diffdrive.OgnDiffDriveToWheelVelocity."""

    GENERATOR_VERSION = (1, 79, 1)
    TARGET_VERSION = (0, 0, 0)
    PER_NODE_DATA = {}

    INTERFACE = og.Database._get_interface([
        ("inputs:angularZ", "double", 0, None, "cmd_vel.angular.z [rad/s]", {ogn.MetadataKeys.DEFAULT: "0.0"}, True, 0.0, False, ""),
        ("inputs:execIn", "execution", 0, None, "", {}, True, None, False, ""),
        ("inputs:linearX", "double", 0, None, "cmd_vel.linear.x [m/s]", {ogn.MetadataKeys.DEFAULT: "0.0"}, True, 0.0, False, ""),
        ("inputs:wheelRadius", "double", 0, None, "Wheel radius R [m]", {ogn.MetadataKeys.DEFAULT: "0.05"}, True, 0.05, False, ""),
        ("inputs:wheelSeparation", "double", 0, None, "Wheel separation L [m]", {ogn.MetadataKeys.DEFAULT: "0.4"}, True, 0.4, False, ""),
        ("outputs:leftDegPerSec", "double", 0, None, "", {}, True, None, False, ""),
        ("outputs:rightDegPerSec", "double", 0, None, "", {}, True, None, False, ""),
    ])

    @classmethod
    def _populate_role_data(cls):
        role_data = super()._populate_role_data()
        role_data.inputs.execIn = og.AttributeRole.EXECUTION
        return role_data

    class ValuesForInputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {
            "angularZ",
            "execIn",
            "linearX",
            "wheelRadius",
            "wheelSeparation",
            "_setting_locked",
            "_batchedReadAttributes",
            "_batchedReadValues",
        }

        def __init__(self, node, attributes, dynamic_attributes):
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedReadAttributes = [
                self._attributes.angularZ,
                self._attributes.execIn,
                self._attributes.linearX,
                self._attributes.wheelRadius,
                self._attributes.wheelSeparation,
            ]
            self._batchedReadValues = [0.0, None, 0.0, 0.05, 0.4]

        @property
        def angularZ(self):
            return self._batchedReadValues[0]

        @angularZ.setter
        def angularZ(self, value):
            self._batchedReadValues[0] = value

        @property
        def execIn(self):
            return self._batchedReadValues[1]

        @execIn.setter
        def execIn(self, value):
            self._batchedReadValues[1] = value

        @property
        def linearX(self):
            return self._batchedReadValues[2]

        @linearX.setter
        def linearX(self, value):
            self._batchedReadValues[2] = value

        @property
        def wheelRadius(self):
            return self._batchedReadValues[3]

        @wheelRadius.setter
        def wheelRadius(self, value):
            self._batchedReadValues[3] = value

        @property
        def wheelSeparation(self):
            return self._batchedReadValues[4]

        @wheelSeparation.setter
        def wheelSeparation(self, value):
            self._batchedReadValues[4] = value

        def __getattr__(self, item):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            return super().__getattr__(item)

        def __setattr__(self, item, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _prefetch(self):
            read_attributes = self._batchedReadAttributes
            new_values = _og._prefetch_input_attributes_data(read_attributes)
            if len(read_attributes) == len(new_values):
                self._batchedReadValues = new_values

    class ValuesForOutputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {"leftDegPerSec", "rightDegPerSec", "_batchedWriteValues"}

        def __init__(self, node, attributes, dynamic_attributes):
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedWriteValues = {}

        @property
        def leftDegPerSec(self):
            value = self._batchedWriteValues.get(self._attributes.leftDegPerSec)
            if value is not None:
                return value
            return og.AttributeValueHelper(self._attributes.leftDegPerSec).get()

        @leftDegPerSec.setter
        def leftDegPerSec(self, value):
            self._batchedWriteValues[self._attributes.leftDegPerSec] = value

        @property
        def rightDegPerSec(self):
            value = self._batchedWriteValues.get(self._attributes.rightDegPerSec)
            if value is not None:
                return value
            return og.AttributeValueHelper(self._attributes.rightDegPerSec).get()

        @rightDegPerSec.setter
        def rightDegPerSec(self, value):
            self._batchedWriteValues[self._attributes.rightDegPerSec] = value

        def __getattr__(self, item):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            return super().__getattr__(item)

        def __setattr__(self, item, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _commit(self):
            _og._commit_output_attributes_data(self._batchedWriteValues)
            self._batchedWriteValues = {}

    class ValuesForState(og.DynamicAttributeAccess):
        def __init__(self, node, attributes, dynamic_attributes):
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)

    def __init__(self, node):
        super().__init__(node)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_INPUT)
        self.inputs = OgnDiffDriveToWheelVelocityDatabase.ValuesForInputs(node, self.attributes.inputs, dynamic_attributes)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_OUTPUT)
        self.outputs = OgnDiffDriveToWheelVelocityDatabase.ValuesForOutputs(node, self.attributes.outputs, dynamic_attributes)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = OgnDiffDriveToWheelVelocityDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    class abi:
        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "get_node_type", None)
            if callable(get_node_type_function):  # pragma: no cover
                return get_node_type_function()
            return "car.diffdrive.OgnDiffDriveToWheelVelocity"

        @staticmethod
        def compute(context, node):
            try:
                per_node_data = OgnDiffDriveToWheelVelocityDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get("_db")
                if db is None:
                    db = OgnDiffDriveToWheelVelocityDatabase(node)
                    per_node_data["_db"] = db
            except Exception:
                db = OgnDiffDriveToWheelVelocityDatabase(node)

            try:
                compute_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "compute", None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:  # pragma: no cover
                    return compute_function(context, node)

                db.inputs._prefetch()
                db.inputs._setting_locked = True
                with og.in_compute():
                    return OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:  # pragma: no cover
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f"Assertion raised in compute - {error}\n{stack_trace}", add_context=False)
            finally:
                db.inputs._setting_locked = False
                db.outputs._commit()
            return False

        @staticmethod
        def initialize(context, node):
            OgnDiffDriveToWheelVelocityDatabase._initialize_per_node_data(node)
            initialize_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "initialize", None)
            if callable(initialize_function):  # pragma: no cover
                initialize_function(context, node)

            per_node_data = OgnDiffDriveToWheelVelocityDatabase.PER_NODE_DATA[node.node_id()]

            def on_connection_or_disconnection(*args):
                per_node_data["_db"] = None

            node.register_on_connected_callback(on_connection_or_disconnection)
            node.register_on_disconnected_callback(on_connection_or_disconnection)

        @staticmethod
        def initialize_nodes(context, nodes):
            for node in nodes:
                OgnDiffDriveToWheelVelocityDatabase.abi.initialize(context, node)

        @staticmethod
        def release(node):
            release_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "release", None)
            if callable(release_function):  # pragma: no cover
                release_function(node)
            OgnDiffDriveToWheelVelocityDatabase._release_per_node_data(node)

        @staticmethod
        def init_instance(node, graph_instance_id):
            init_instance_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "init_instance", None)
            if callable(init_instance_function):  # pragma: no cover
                init_instance_function(node, graph_instance_id)

        @staticmethod
        def release_instance(node, graph_instance_id):
            release_instance_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "release_instance", None)
            if callable(release_instance_function):  # pragma: no cover
                release_instance_function(node, graph_instance_id)
            OgnDiffDriveToWheelVelocityDatabase._release_per_node_instance_data(node, graph_instance_id)

        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "update_node_version", None)
            if callable(update_node_version_function):  # pragma: no cover
                return update_node_version_function(context, node, old_version, new_version)
            return False

        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "initialize_type", None)
            needs_initializing = True
            if callable(initialize_type_function):  # pragma: no cover
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "car.diffdrive")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Diff Drive To Wheel Velocity")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "robotics")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Convert cmd_vel to differential-drive wheel velocity")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")
                OgnDiffDriveToWheelVelocityDatabase.INTERFACE.add_to_node_type(node_type)

        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(
                OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS, "on_connection_type_resolve", None
            )
            if callable(on_connection_type_resolve_function):  # pragma: no cover
                on_connection_type_resolve_function(node)

    NODE_TYPE_CLASS = None

    @staticmethod
    def register(node_type_class):
        OgnDiffDriveToWheelVelocityDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(OgnDiffDriveToWheelVelocityDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("car.diffdrive.OgnDiffDriveToWheelVelocity")
