from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.prediction import router as prediction_router
from app.api.routes.analysis import router as analysis_router

app = FastAPI(

    title="TradeIntel API",

    version="1.0.0"

)

# -----------------------------
# CORS Configuration
# -----------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173",

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

# -----------------------------
# Routes
# -----------------------------

app.include_router(

    prediction_router

)

app.include_router(

    analysis_router

)


@app.get("/")
def home():

    return {

        "message": "TradeIntel API Running"

    }