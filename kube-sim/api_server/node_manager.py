class NodeManager:
    def __init__(self):
        self.nodes = {}  # node_id: {cpu_cores, available_cores, status}

    def register_node(self, node_id, cpu_cores):
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = {
            "cpu_cores": cpu_cores,
            "available_cores": cpu_cores,
            "status": "healthy"
        }
        return True

    def list_nodes(self):
        return self.nodes
