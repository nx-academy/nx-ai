import click

from nx_ai.openai import configure_engine


@click.group()
def chroma_group():
    """Set of commands related to ChromaDB"""
    pass


@chroma_group.command()
def list_documents():
    """List of the documents stored locally"""
    engine = configure_engine()
    db = engine["db"]
    
    documents = db.get()
    for i, doc_id in enumerate(documents["ids"]):
        print(f"{i + 1}. ID: {doc_id} - Metadata: {documents["metadatas"][i]}")


@chroma_group.command()
@click.argument("id")
def read_chunk(id):
    """Retrieve if exists a chunk with the id ${id}"""
    engine = configure_engine()
    db = engine["db"]
    
    chunk = db.get(ids=[id])
    print(f"Chunk: {chunk['documents'][0]}")
    print(f"Metadata: {chunk['metadatas'][0]}")


@chroma_group.command()
@click.argument("document_name")
def read_doc(document_name):
    """Retrieve a set of chunks, a document in other words"""
    engine = configure_engine()
    db = engine["db"]
    
    document = db.get(where={"content": document_name})
    if len(document["documents"]) == 0:
        print("Unable to find the document in Chroma.")
        return
    
    full_context = "\n\n".join(document["documents"])
    print(full_context)
