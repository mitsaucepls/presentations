from diagrams import Diagram, Cluster
from diagrams.gcp.api import Endpoints
from diagrams.azure.compute import OsImages
from diagrams.aws.general import Users
from diagrams.aws.management import SystemsManagerAutomation
from diagrams.onprem import security
from diagrams.onprem.compute import Server
from diagrams.programming.language import Rust
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Postgresql
from diagrams.onprem.security import Vault
from diagrams.custom import Custom

wasm_binary_icon = "./WebAssembly_Logo.png"
graph_attr = {
    "bgcolor": "transparent",
    "fontcolor": "white"
}

graph_attr_cluster = {
    "fontcolor": "black"
}

with Diagram("Wasm Backend Service Architecture", show=False, graph_attr=graph_attr):
    with Cluster("Development Environment", graph_attr=graph_attr_cluster):
        ide = Rust("Source Code")
        compiler = SystemsManagerAutomation("Compiler")

    wasm_binary = Custom("Wasm Binary", wasm_binary_icon, fontcolor="white")

    with Cluster("Runtime Environment", graph_attr=graph_attr_cluster):
        runtime = Server("Wasm Runtime")
        runtime - [Docker("Containerization")]

    with Cluster("Capabilities (WASI and more)", graph_attr=graph_attr_cluster):
        postgres = Postgresql("PostgreSQL")
        api_service = Endpoints("HTTP")
        secrets = Vault("Secrets")


    # Connections
    ide >> compiler >> wasm_binary >> runtime
    runtime >> api_service
    api_service - postgres
    api_service - secrets
