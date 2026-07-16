from app.services.document_loader import DocumentLoader
from app.services.vector_store_service import VectorStoreService
from app.services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.vector_db = VectorStoreService()

        self.llm = LLMService()

    def ask(
        self,
        ticker,
        question,
    ):

        # ----------------------------------
        # Load latest documents
        # ----------------------------------

        documents = self.loader.load_news_documents(
            ticker
        )

        # ----------------------------------
        # Index into ChromaDB
        # ----------------------------------

        self.vector_db.index_documents(
            documents
        )

        # ----------------------------------
        # Retrieve only top 3 documents
        # ----------------------------------

        results = self.vector_db.search(
            query=question,
            top_k=3,
        )

        retrieved_docs = results["documents"][0]

        # ----------------------------------
        # Reduce prompt size
        # ----------------------------------

        context = "\n\n".join(

            [
                doc[:500]
                for doc in retrieved_docs
            ]

        )

        # ----------------------------------
        # Optimized Prompt
        # ----------------------------------

        prompt = f"""
You are TradeIntel AI, an expert financial analyst.

Use ONLY the context provided.

If the answer cannot be determined from the context, clearly say so.

Keep your answer under 200 words.

Context
========

{context}

Question
========

{question}

Return in this format:

Summary:
...

Key Insights:
- ...

Risks:
- ...

Recommendation:
...
"""

        response = self.llm.llm.invoke(
            prompt
        )

        return {

            "Question": question,

            "Answer": response.content,

            "Retrieved Documents": retrieved_docs,

        }