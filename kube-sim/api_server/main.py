from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import uuid
from .node_manager import NodeManager


app = FastAPI()
node_manager = NodeManager()

class NodeCreateRequest(BaseModel):
    cpu_cores: int

@app.post("/add_node")
def add_node(request: NodeCreateRequest):
    node_id = str(uuid.uuid4())
    success = node_manager.register_node(node_id, request.cpu_cores)
    if not success:
        raise HTTPException(status_code=400, detail="Node already exists")
    
    subprocess.Popen(["docker", "run", "--rm", "-d",
                      "--name", f"node_{node_id}",
                      "-e", f"NODE_ID={node_id}",
                      "-e", f"API_URL=http://host.docker.internal:8000",
                      "kube-node"])  # 'kube-node' is the image you'll build
    return {"message": "Node added", "node_id": node_id}
