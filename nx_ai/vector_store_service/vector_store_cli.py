import os
import click

from nx_ai.vector_store_service.vector_store_api import (
    list_openai_vector_stores,
    create_openai_vector_store,
    get_openai_vector_store,
    delete_openai_vector_store,
    search_vector_store,
    upload_files_to_vector_store
)

# For now, I've created an env variable for the Vector Store ID
VECTOR_STORE_ID = os.environ.get("VECTOR_STORE_ID")


@click.group()
def vector_store_group():
    """Set of commands related to OpenAI Vector Store"""
    pass


@vector_store_group.command()
def list():
    """Retrieve all the vectors stored"""
    vector_stores = list_openai_vector_stores()
    print(vector_stores)


@vector_store_group.command()
@click.option("--name", prompt="Name of the vector store",
              help="The name of the OpenAI Vector Store you'd like to create")
def create(name: str):
    """Create a new vector store"""
    vector_store = create_openai_vector_store(name=name)
    print(vector_store)


@vector_store_group.command()
@click.option("--id",
              help="The ID of the Vector Store you're searching for")
def get(id: str):
    """Search for a Specific Vector Store by ID"""
    vector_store = get_openai_vector_store(id=id)
    print(vector_store)


@vector_store_group.command()
@click.option("--id",
              prompt="You are about to delete a Vector Store. Type its ID to confirm",
              help="Delete a Vector Store with its ID")
def delete(id: str):
    """Delete a Specific Vector Store with its ID"""
    vector_store = delete_openai_vector_store(id=id)
    print(vector_store)


@vector_store_group.command()
@click.option("--id", prompt="ID of the Vector Store",
               help="The ID of the Vector Store you Want to Perform a Research Against")
@click.option("--query", prompt="Query for the LLM",
               help="a Query Input that will be used in the LLM to perform the search")
def search(id: str, query: str):
    """Search In a OpenAI Vector Store"""
    response = search_vector_store(id=id, query=query)
    
    print(response)


@vector_store_group.command()
def upload_files():
    """Upload a Batch of Files to a Choosen Vector Store"""
    # For now, I've hardcoded texts to send to Vector Store
    files = [
        "data/stylistic_samples/decouverte_docker.md",
        "data/stylistic_samples/point_nx_2025.md",
        "data/stylistic_samples/welcome_v2.md"
    ]
    
    vector_store = upload_files_to_vector_store(
        id=VECTOR_STORE_ID,
        files_path=files
    )
    
    print(vector_store.status)
    print(vector_store.file_counts)
