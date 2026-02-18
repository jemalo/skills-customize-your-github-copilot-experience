# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework. You'll create an API that manages resources with HTTP endpoints, implementing best practices for modern API development.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Create a basic FastAPI application with proper project structure and dependencies.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn
- Create a main application file with a FastAPI instance
- Define at least one GET endpoint that returns a welcome message
- Successfully run the server using uvicorn


### 🛠️ Create CRUD Endpoints

#### Description
Implement Create, Read, Update, and Delete operations for a resource (e.g., a todo item, book, or product).

#### Requirements
Completed program should:

- Implement a GET endpoint to retrieve all items or a specific item by ID
- Implement a POST endpoint to create a new item
- Implement a PUT endpoint to update an existing item
- Implement a DELETE endpoint to remove an item
- Use appropriate HTTP status codes for each operation


### 🛠️ Add Data Validation and Documentation

#### Description
Implement request/response validation and automatic API documentation.

#### Requirements
Completed program should:

- Use Pydantic models for request and response validation
- Define clear data types for all endpoints
- Access the automatic Swagger UI documentation at `/docs`
- Handle validation errors gracefully with appropriate error messages
