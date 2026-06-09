# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Students will learn how to build a small REST API with FastAPI. They will define routes, return JSON responses, and use path and query parameters to make the API interactive.

## 📝 Tasks

### 🛠️ Build a Basic API

#### Description
Create a FastAPI application with a few simple endpoints that return JSON data about a sample resource, such as books, students, or tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /` route that returns a welcome message
- Define at least one additional `GET` route that returns a JSON object or list


### 🛠️ Add Dynamic Routes and Validation

#### Description
Extend the API so it can respond differently based on path parameters, query parameters, or request data.

#### Requirements
Completed program should:

- Define a route that uses a path parameter, such as an item ID
- Define a route that uses a query parameter to filter or customize the response
- Use Pydantic models or type hints to validate incoming data
- Return clear JSON responses for both successful and invalid requests
