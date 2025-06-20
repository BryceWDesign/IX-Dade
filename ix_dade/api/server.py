"""
IX-Dade REST API Server

Provides HTTP endpoints for biomedical knowledge queries,
enabling integration with other IX-Gibson AI modules.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXDadeQueryProcessor

app = FastAPI()
query_processor = IXDadeQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def process_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        result = query_processor.process_query(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8050)
