import click


@click.group()
def chroma_group():
    """Set of commands related to ChromaDB"""
    pass


@chroma_group.command()
def list_documents():
    """List of the documents stored locally"""
    print("List of the document")


@chroma_group.command()
@click.argument("doc_id")
def read_doc(doc_id):
    """Retrieve if exists the doc with the id ${doc_id}"""
    print(f"Getting the doc_id: {doc_id}")
