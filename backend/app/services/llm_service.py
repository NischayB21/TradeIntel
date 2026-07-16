import json

from langchain_ollama import ChatOllama


class LLMService:

    def __init__(self):

        self.llm = ChatOllama(

            model="qwen2.5:7b",

            temperature=0.2,

            num_ctx=2048,

            num_predict=400,

        )

    def analyze(

        self,

        prediction,

        sentiment,

        retrieved_context,

        question,

    ):

        prompt = f"""
You are TradeIntel AI.

You are a professional Financial Analyst.

Your task is to analyze the stock using ONLY the supplied information.

Do NOT make up facts.

If something is unavailable, say "Not enough information."

====================================================
Prediction
====================================================

{json.dumps(prediction, indent=2)}

====================================================
News Sentiment
====================================================

{json.dumps(sentiment, indent=2)}

====================================================
Retrieved Financial Context
====================================================

{retrieved_context}

====================================================
User Question
====================================================

{question}

====================================================
Instructions
====================================================

Return ONLY valid JSON.

Do not return markdown.

Do not wrap the JSON inside ```.

Use this exact schema:

{{
    "summary": "",

    "recommendation": "",

    "risk": "",

    "confidence": 0,

    "reasoning": [

        "",

        ""

    ],

    "pros": [

        "",

        ""

    ],

    "cons": [

        "",

        ""

    ]
}}

Rules:

1. recommendation must be one of:
   BUY
   HOLD
   SELL

2. risk must be one of:
   LOW
   MEDIUM
   HIGH

3. confidence must be between 0 and 100.

4. reasoning must contain 3 concise bullet points.

5. pros must contain 2 points.

6. cons must contain 2 points.

Return JSON only.
"""

        response = self.llm.invoke(prompt)

        content = response.content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()

        elif content.startswith("```"):
            content = content.replace("```", "").strip()

        try:

            return json.loads(content)

        except Exception:

            return {

                "summary": content,

                "recommendation": prediction.get(
                    "Final Recommendation",
                    "HOLD",
                ),

                "risk": prediction.get(
                    "Risk Level",
                    "MEDIUM",
                ),

                "confidence": int(
                    prediction.get(
                        "Confidence (%)",
                        0,
                    )
                ),

                "reasoning": [

                    "Unable to parse structured JSON from the LLM."

                ],

                "pros": [],

                "cons": [],

            }