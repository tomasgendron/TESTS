# TestApp2

This is a FastAPI application with CRUD operations for a `Person` table.

## Setup

1.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the application

```bash
uvicorn app:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

You can access the API documentation at `http://127.0.0.1:8000/docs`.

### Create a Person

*   **URL:** `/people/`
*   **Method:** `POST`
*   **Data:**

    ```json
    {
      "name": "string",
      "age": "integer"
    }
    ```

*   **Example:**

    ```bash
    curl -X 'POST' 
      'http://127.0.0.1:8000/people/' 
      -H 'accept: application/json' 
      -H 'Content-Type: application/json' 
      -d '{
      "name": "John Doe",
      "age": 30
    }'
    ```

### Get all People

*   **URL:** `/people/`
*   **Method:** `GET`
*   **Example:**

    ```bash
    curl -X 'GET' 
      'http://127.0.0.1:8000/people/' 
      -H 'accept: application/json'
    ```

### Get a specific Person

*   **URL:** `/people/{person_id}`
*   **Method:** `GET`
*   **Example:**

    ```bash
    curl -X 'GET' 
      'http://127.0.0.1:8000/people/1' 
      -H 'accept: application/json'
    ```

### Update a Person

*   **URL:** `/people/{person_id}`
*   **Method:** `PUT`
*   **Data:**

    ```json
    {
      "name": "string",
      "age": "integer"
    }
    ```

*   **Example:**

    ```bash
    curl -X 'PUT' 
      'http://127.0.0.1:8000/people/1' 
      -H 'accept: application/json' 
      -H 'Content-Type: application/json' 
      -d '{
      "name": "Jane Doe",
      "age": 31
    }'
    ```

### Delete a Person

*   **URL:** `/people/{person_id}`
*   **Method:** `DELETE`
*   **Example:**

    ```bash
    curl -X 'DELETE' 
      'http://127.0.0.1:8000/people/1' 
      -H 'accept: application/json'
    ```
