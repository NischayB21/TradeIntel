import chromadb

from app.services.embedding_service import EmbeddingService


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="tradeintel_news"
        )

        self.embedding_service = EmbeddingService()

    def index_documents(self, documents):

        existing = self.collection.get()

        if len(existing["ids"]) > 0:

            self.collection.delete(
                ids=existing["ids"]
            )

        ids = []
        texts = []
        embeddings = []
        metadatas = []

        for doc in documents:

            ids.append(
                doc["id"]
            )

            texts.append(
                doc["text"]
            )

            embeddings.append(
                self.embedding_service.embed(
                    doc["text"]
                )
            )

            metadatas.append(
                doc["metadata"]
            )

        self.collection.add(

            ids=ids,

            documents=texts,

            embeddings=embeddings,

            metadatas=metadatas,

        )

    def search(

        self,

        query,

        top_k=5,

    ):

        query_embedding = self.embedding_service.embed(
            query
        )

        results = self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k,

        )

        return results