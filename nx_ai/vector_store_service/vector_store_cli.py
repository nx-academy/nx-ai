import click

from nx_ai.vector_store_service.vector_store_api import (
    list_openai_vector_stores,
    create_openai_vector_store,
    get_openai_vector_store,
    delete_openai_vector_store,
    search_vector_store
)


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
    
    print("====")
    print(response)
    print("====")
