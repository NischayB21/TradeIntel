from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed(self, text):

        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()

    def embed_documents(self, documents):

        return self.model.encode(
            documents,
            normalize_embeddings=True
        ).tolist()