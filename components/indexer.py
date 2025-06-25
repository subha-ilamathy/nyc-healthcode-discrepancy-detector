from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.schema import TextNode
from typing import List

def build_and_persist_index(
    nodes: List[TextNode],
    persist_dir: str = "./storage"
) -> VectorStoreIndex:
    
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    index = VectorStoreIndex(nodes, embed_model=embed_model)
    index.storage_context.persist(persist_dir=persist_dir)
    
    print(f"Index stored at: {persist_dir}")
    
    return index



def load_index(persist_dir: str = "./storage"):
    """
    Loads a VectorStoreIndex from the local storage directory.

    Args:
        persist_dir (str): Directory where index was persisted.

    Returns:
        VectorStoreIndex
    """
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
    print(f"Index loaded from: {persist_dir}")
    return index