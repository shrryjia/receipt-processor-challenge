# Receipt Processor

## How to run?

To run the application, ensure Docker and Docker Compose are installed on your system. Then, navigate to the root directory of the project and run:

```bash
docker-compose up --build
```

This command builds the Docker image (if necessary) and starts the application. Once running, the Flask application will be accessible at `http://localhost:80/` or `http://127.0.0.1`.

## Project Structure

This section provides an overview of the project's directory structure and its key components. Our project is structured to separate the core application logic from testing to ensure clarity and maintainability.

### Directory Layout

```
/
|- app/
|  |- main.py            # Entry point of the Flask application
|  |- utils.py           # Utility functions, including receipt processing logic
|
|- test/                 # tests for the application
|  |- test_api.py     # Tests related to API endpoints
|  |- test_calculate_points.py  # Tests for the points calculation logic
|
|- Dockerfile            # Dockerfile for building the application container
|- docker-compose.yml    # Docker Compose configuration for orchestrating services
```

### Key Components

#### app/

- `main.py`: This is the entry point of my Flask application. It defines the API endpoints and includes the primary business logic for processing requests and generating responses.

- `utils.py`: Contains utility functions that support the main application logic. This includes the `calculate_points` function, which implements the rules for calculating points based on receipt data.

#### test/

- Contains unit tests for our application, ensuring the reliability and correctness of both the API endpoints and the utility functions.

  - `test_api.py`: Tests the API endpoints defined in `main.py`, ensuring they handle requests and generate responses as expected.
  
  - `test_calculate_points.py`: Tests the logic within `utils.py` for calculating points, verifying correctness across a range of scenarios.

### Docker Configuration

- `Dockerfile`: Defines the Docker image for the application, specifying the base image, dependencies, and commands to run the application.

- `docker-compose.yml`: Orchestrates the setup of the application and its services, making it easy to build, run, and manage the application containers.



## Testing

While automated tests run within the container setup, you can also perform manual tests using Postman or `curl` to interact directly with the API. This can be useful for exploratory testing, debugging, or verifying specific use cases.

### Using Postman

[Postman](https://www.postman.com/) is a popular GUI tool for API testing that allows you to easily send requests to APIs and inspect the responses. Here's how you can test the API endpoints with Postman:

1. **Launch Postman**: Start Postman on your machine. If you haven't installed Postman yet, download it from the official website and follow the installation instructions.

2. **Create a New Request**: Click the "New" button or use the "+" tab to create a new request.

3. **Set Up the Request**:
    - For the request method, select `POST` from the dropdown menu next to the URL field.
    - Enter the URL for your API endpoint. For testing the `/receipts/process` endpoint, use `http://localhost:80/receipts/process`.
    - Go to the "Body" tab, select "raw", and then choose "JSON" from the dropdown menu that initially displays "Text".
    - Enter the JSON data for the receipt you wish to process in the request body. For example:
        ```json
        {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                }
            ],
            "total": "35.35"
        }   
        ```

4. **Send the Request**: Click the "Send" button to send the request to your Flask application.

5. **Inspect the Response**: View the response in the lower section of the Postman window. You should see the generated ID for the receipt if the request was successful.

5. **Create a New Request** in Postman as before.
6. **Set Up the Request**:
- Change the request method to `GET`.
- Enter the URL for your API endpoint, replacing `<receipt_id>` with the actual ID of the receipt you want to query. The URL should look like `http://localhost:80/receipts/<receipt_id>/points`.
- There's no need to set a request body for a `GET` request.
7. **Send the Request**: Click the "Send" button.
8. **Inspect the Response**: The response should include the points awarded for the receipt. It will be displayed in the lower section of the Postman window.

### Using `curl`

`curl` is a command-line tool available on most Unix-like operating systems (Linux, macOS) and Windows 10 & later. It allows you to send requests and receive responses via the command line.

Here's how you can use `curl` to test the `/receipts/process` endpoint:

- Open a terminal or command prompt.
- Use the `curl` command with the `-X` flag to specify the request method (`POST`), `-H` to add headers, and `-d` to include the JSON data as the request body. For example:

    ```bash
    curl -X POST http://localhost:80/receipts/process \
         -H "Content-Type: application/json" \
         -d '{
              "retailer": "Target",
              "purchaseDate": "2022-01-01",
              "purchaseTime": "13:01",
              "items": [
                  {
                  "shortDescription": "Mountain Dew 12PK",
                  "price": "6.49"
                  },{
                  "shortDescription": "Emils Cheese Pizza",
                  "price": "12.25"
                  },{
                  "shortDescription": "Knorr Creamy Chicken",
                  "price": "1.26"
                  },{
                  "shortDescription": "Doritos Nacho Cheese",
                  "price": "3.35"
                  },{
                  "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                  "price": "12.00"
                  }
              ],
              "total": "35.35"
            }'
    ```

- Press Enter to send the request. The response will be output directly in the terminal. If successful, you should see the generated ID for the receipt.

Here's how you can use `curl` to test the `/receipts/<receipt_id>/points` endpoint:

- Execute the following curl command, making sure to replace `<receipt_id>` with the actual receipt ID:
     ```bash
     curl -X GET http://localhost:80/receipts/<receipt_id>/points
     ```
- Press Enter. The response, which should include the points awarded to the receipt, will be displayed in your terminal.

For both Postman and curl, ensure you replace <receipt_id> with the ID returned from the /receipts/process endpoint after you've successfully submitted a receipt for processing. This ID is crucial for querying the points associated with that specific receipt.

These instructions should guide you through manually testing your Flask application's endpoints using either Postman or `curl`. Adjust the URL and port as necessary to match your application's configuration.