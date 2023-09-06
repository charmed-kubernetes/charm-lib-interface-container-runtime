class ContainerRuntimeProvides:
    """Implements the Provides side of the container-runtime interface."""

    def __init__(self, charm, endpoint):
        self.charm = charm
        self.endpoint = endpoint

    @property
    def relations(self):
        return self.charm.model.relations[self.endpoint]

    def set_sandbox_image(self, sandbox_image):
        """Set the sandbox image."""
        for relation in self.relations:
            relation.data[self.unit]["sandbox_image"] = sandbox_image

    @property
    def socket(self):
        for relation in self.relations:
            for unit in relation.units:
                socket = relation.data[unit].get("socket")
                if socket:
                    return socket

    @property
    def unit(self):
        return self.charm.unit
