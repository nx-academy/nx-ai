import click

from nx_ai.openai import configure_engine


def get_db():
    engine = configure_engine()
    return engine["db"]


@click.group()
def chroma_group():
    """Set of commands related to ChromaDB"""
    pass


@chroma_group.command()
def list_chunks():
    """List all chunks stored locally"""
    db = get_db()
    
    chunks = db.get()
    for i, chunk_id in enumerate(chunks["ids"]):
        print(f"{i + 1}. ID: {chunk_id} - Metadata: {chunks["metadatas"][i]}")


@chroma_group.command()
@click.argument("id")
def read_chunk(id):
    """Read a single chunk by its ID"""
    db = get_db()
    
    chunk = db.get(ids=[id])
    print(f"Chunk: {chunk['documents'][0]}")
    print(f"Metadata: {chunk['metadatas'][0]}")


@chroma_group.command()
@click.argument("document_name")
def read_doc(document_name):
    """Read all chunks associated with a document name"""
    db = get_db()
    
    document = db.get(where={"content": document_name})
    if len(document["documents"]) == 0:
        print("Unable to find the document in Chroma.")
        return
    
    full_context = "\n\n".join(document["documents"])
    print(full_context)
    

@chroma_group.command()
@click.argument("id")
def delete_chunk(id):
    """Delete a single chunk by its ID"""
    db = get_db()
    
    db.delete(ids=[id])
    print(f"Chunk with id {id} deleted.")
    

@chroma_group.command()
@click.argument("document_name")
def delete_document(document_name):
    """Delete all chunks associated with a document name"""
    db = get_db()   
    
    db.delete(where={"content": document_name})
    print(f"Document with name {document_name} deleted.")
