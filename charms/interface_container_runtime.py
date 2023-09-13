from ops import CharmBase, Relations, Unit
from typing import List, Optional


class ContainerRuntimeProvides:
    """Implements the Provides side of the container-runtime interface."""

    def __init__(self, charm: CharmBase, endpoint: str):
        self.charm = charm
        self.endpoint = endpoint

    @property
    def relations(self) -> List[Relations]:
        return self.charm.model.relations[self.endpoint]

    def set_sandbox_image(self, sandbox_image: str) -> None:
        """Set the sandbox image."""
        for relation in self.relations:
            relation.data[self.unit]["sandbox_image"] = sandbox_image

    @property
    def socket(self) -> Optional[str]:
        for relation in self.relations:
            for unit in relation.units:
                if socket := relation.data[unit].get("socket"):
                    return socket

    @property
    def unit(self) -> Unit:
        return self.charm.unit
