# AWS Lambda API

A serverless API created using AWS Lambda and API Gateway.

## Description

This project is a serverless API built with AWS Lambda and API Gateway. The API is publicly available at [this link](https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev). It demonstrates how to create and deploy a cloud-based service without the need to manage servers. This project is ideal for developers learning about serverless computing and how to use AWS services to create scalable, low-cost APIs.

**Main Features:**

- Processes HTTP requests.
- Easy integration with AWS services.
- Example of a serverless architecture.

## Technologies Used

- **AWS Lambda**: Serverless computing service that runs your code in response to events and automatically manages the underlying compute resources.
- **API Gateway**: Service for creating, publishing, maintaining, monitoring, and securing RESTful APIs at any scale.

## How to Run

1. Clone the repository to your local environment:
   ```bash
   git clone https://github.com/GustavoLVJardim/aws-lambda-api.git
Install the necessary dependencies:
bash

pip install -r requirements.txt
Deploy the Lambda function and configure API Gateway:
Log in to the AWS Console.
Navigate to the Lambda service and create a new function.
Deploy the Lambda function using the provided code.
Configure API Gateway to integrate with your Lambda function.
Endpoints
GET /dev/: Returns a welcome message.

URL: GET https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/
POST /dev/data: Receives data and processes it.

URL: POST https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/data
Usage Examples
1. GET Request
To make a GET request and receive a welcome message:

bash

curl -X GET https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/
Expected Response:
json

{
  "message": "Welcome to the serverless API!"
}
2. POST Request
To make a POST request and send data to the API:

bash

curl -X POST https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/data -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}'
Expected Response:
json

{
  "status": "success",
  "message": "Data received successfully!"
}
Known Issues
CORS Limitations: The API may have CORS issues when called from certain domains. This requires additional configuration in API Gateway.
Data Validation: There is no robust data validation on the POST endpoint. Incorrect data can cause errors.
Next Steps
Implement authentication with AWS Cognito to enhance API security.
Add data persistence using DynamoDB to store and retrieve data.
Improve error handling and add standardized responses.
Contributions
Contributions are welcome! To contribute to this project:

Fork the repository to your own GitHub.
Clone the forked repository to your local environment.
Create a new branch for your changes: git checkout -b feature/your-branch-name.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin feature/your-branch-name.
Open a Pull Request in the original repository.
Feel free to open issues if you find bugs or have suggestions for improvements!

License
This project is licensed under the MIT License. See the LICENSE file for more information.
