

# AWS Lambda API

This project is a serverless API created using AWS Lambda and API Gateway.

## Description

This project is a serverless API created using AWS Lambda and API Gateway. The API is capable of processing HTTP requests, demonstrating how to build and deploy a cloud service without the need to manage servers. This project is ideal for developers who want to learn about serverless computing and using AWS services to create scalable, low-cost APIs.

## Usage Examples

### 1. GET Request

To make a `GET` request and receive a welcome message:

```bash
curl -X GET https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/

### 2. POST Request
To make a POST request and send data to the API:
curl -X POST https://0jb6p52778.execute-api.eu-north-1.amazonaws.com/dev/data -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}'

Expected Response:
{
  "status": "success",
  "message": "Dados recebidos com sucesso!"
}

### **3. Add a Known Issues Section**

Here is a suggestion for the **Known Issues** section:

```markdown
## Known Issues

- **CORS Limitations**: The API is currently not configured to handle all CORS scenarios, which may cause issues when trying to access the API directly from some browsers.
- **Data Validation**: There is no robust data validation implemented in the `POST` endpoint. Data sent without the correct format may cause errors.   

## Technologies Used

- **AWS Lambda**: For serverless computing.
- **AWS API Gateway**: For managing RESTful endpoints.
- **Python**: Programming language used for the Lambda function.
- **AWS IAM**: For permissions and security management.

## How to Execute

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SeuUsuario/aws-lambda-api.git
   cd aws-lambda-api

## Endpoints

- **GET /dev/**: Returns a welcome message.
- **POST /dev/data**: Receives data and processes it.

  ## Next Steps

- Add authentication with AWS Cognito.
- Implement data persistence with DynamoDB.

  ## Contributions

Contributions are welcome! To contribute to this project:

1. **Fork the repository** to your own GitHub.
2. **Clone** the forked repository to your local environment.
3. Create a new **branch** for your modifications: `git checkout -b feature/name-of-your-branch`.
4. **Commit** your changes: `git commit -m 'Add new functionality'`.
5. **push** to the branch: `git push origin feature/name-of-your-branch`.
6. **Open a Pull Request** on the original repository.

Feel free to open issues if you find bugs or have suggestions for improvements!

## License

This project is under the MIT license. See the LICENSE file for more information.
