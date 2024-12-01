from diagrams import Diagram, Cluster
from diagrams.gcp.api import Endpoints
from diagrams.azure.compute import OsImages
from diagrams.aws.general import Users
from diagrams.aws.management import SystemsManagerAutomation
from diagrams.onprem.compute import Server
from diagrams.programming.language import Rust
from diagrams.onprem.container import Docker
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
        wasi = OsImages("WASI (Optional)")

    with Cluster("Hosting Infrastructure", graph_attr=graph_attr_cluster):
        api_service = Endpoints("API/Service Layer")
        container = Docker("Container")

    client = Users("Client Application", fontcolor="white")

    # Connections
    ide >> compiler >> wasm_binary >> runtime
    runtime >> wasi
    runtime >> api_service >> container
    container >> client
