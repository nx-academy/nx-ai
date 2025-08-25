from openai import OpenAI


client = OpenAI()


def list_openai_vector_stores():
    vector_stores = client.vector_stores.list()
    return vector_stores


def create_openai_vector_store(name: str):
    vector_store = client.vector_stores.create(
        name=name
    )
    return vector_store


def get_openai_vector_store(id: str):
    vector_store = client.vector_stores.retrieve(
        vector_store_id=id
    )
    return vector_store


def delete_openai_vector_store(id: str):
    vector_store = client.vector_stores.delete(
        vector_store_id=id
    )
    return vector_store


def search_vector_store(id: str, query: str):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=query,
        tools=[{
            "type": "file_search",
            "vector_store_ids": [id]
        }]
    )
    return response


def upload_files_to_vector_store(id: str, files_path: list[str]):
    print(files_path)
    # file_streams = [open(path, "rb") for path in file_path]
    
    # print("====")
    # print(file_streams)
    # print("====")
