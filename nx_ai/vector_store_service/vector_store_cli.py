import click


@click.group()
def vector_store_group():
    """Set of commands related to OpenAI Vector Store"""
    pass


@vector_store_group.command()
def list():
    """Retrieve all the vectors stored"""
    pass


@vector_store_group.command()
@click.option("--name", prompt="Name of the vector store",
              help="The name of the OpenAI Vector Store you'd like to create")
def create(name: str):
    """Create a new vector store"""
    pass


