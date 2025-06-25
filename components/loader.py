import json
from typing import List
from pathlib import Path


from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.schema import TextNode


def load_and_parse_markdown(source_path: str) -> List[TextNode]:
    """
    Loads and parses markdown files into TextNodes.
    """
    reader = DoclingReader()
    documents = reader.load_data(source_path)

    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents(documents)

    return nodes


def save_nodes_to_json(nodes: List[TextNode], output_path: str = "nodes.json"):
    """
    Serializes and saves nodes to a JSON file.
    """
    data = [
        {
            "id": node.node_id,
            "text": node.text,
            "metadata": node.metadata,
        }
        for node in nodes
    ]
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(nodes)} nodes to {output_path}")


def load_nodes_from_json(input_path: str = "nodes.json") -> List[TextNode]:
    """
    Loads and reconstructs TextNodes from a JSON file.
    """
    with open(input_path, "r") as f:
        data = json.load(f)

    nodes = [
        TextNode(text=item["text"], metadata=item["metadata"], id_=item["id"])
        for item in data
    ]

    print(f"Loaded {len(nodes)} nodes from {input_path}")
    return nodes



