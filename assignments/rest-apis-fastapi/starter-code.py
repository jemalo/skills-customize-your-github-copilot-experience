"""
FastAPI REST API Starter Code
Build a Todo API or similar resource management API

TODO: Implement the tasks according to the assignment requirements
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="My REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define a Pydantic model for your resource
# Example: 
# class Item(BaseModel):
#     id: Optional[int] = None
#     name: str
#     description: Optional[str] = None


# TODO: Create an in-memory database (list or dictionary)
# Example:
# items_db = []


# TODO: Task 1 - Create your first GET endpoint
@app.get("/")
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to My REST API"}


# TODO: Task 2 - CRUD Operations
# Implement GET (retrieve all items or by ID)
# Implement POST (create new item)
# Implement PUT (update existing item)
# Implement DELETE (remove item)

# TODO: Task 3 - Response models and automatic documentation
# Use Pydantic models for request/response validation
# Your endpoints should be properly typed for auto-documentation


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
