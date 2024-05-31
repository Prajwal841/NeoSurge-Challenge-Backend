# -Neosurge-Investment-Insight-Backend-App-Development-Challenge-
# Python(Django) Project README

## Project Overview

This project utilizes Django, a high-level Python web framework, for backend development. The primary database used is MongoDB and for security JWT Webtokens is Used. The README provides an overview of the project setup, key libraries utilized, design choices made, integration of GPT-4, and any additional features implemented.

## Setup Instructions

1. **Clone Repository:**
2. **Install Dependencies:**

   - `django`: A high-level Python web framework for backend development. It provides tools for building web applications quickly and efficiently.

   - `djangorestframework`: A powerful and flexible toolkit for building Web APIs in Django. It provides serializers and views to create RESTful APIs.

   - `django-rest-framework-simplejwt`: A JSON Web Token authentication plugin for Django REST Framework. It provides secure authentication using JWT tokens.

   - `requests`: A simple and elegant HTTP library for Python. Used for making HTTP requests to external APIs, such as the OpenAI GPT-4 API in this project.

   - `pymongo`: A Python driver for MongoDB. Used for interacting with MongoDB, such as inserting, updating, and querying documents in the database.

   - `jwt`: A Python library for encoding and decoding JSON Web Tokens (JWT). Used for authentication and authorization purposes, particularly in the `jwt_middleware` and `login_required` decorators.

   - `secrets`: A module in Python's standard library used for generating secure random numbers and strings. Used for generating unique user IDs.

   - `json`: A built-in Python module for encoding and decoding JSON data. Used for handling JSON data in various parts of the application.

   - `datetime`: A module in Python's standard library for working with dates and times. Used for handling timestamps and time-related operations.

   - `pathlib`: A module in Python's standard library for working with file system paths. Used for defining the base directory path in the Django settings.

   - `corsheaders`: A Django application for handling Cross-Origin Resource Sharing (CORS) headers. Used for allowing cross-origin requests in the application.

   These dependencies are essential for the proper functioning of the Django project and its integration with external services like MongoDB and OpenAI's GPT-4 API.
   
## Task 2: GPT-4 Integration

### Overview
In Task 2, we integrate the GPT-4 API to process and analyze financial data, providing insightful content based on user preferences and market trends.

### Integration Details
We utilize the GPT35Service class to interact with the GPT-4 API. Here's how the integration works:

1. **Initialization**: 
   - The `GPT35Service` class is initialized with the base API URL for the GPT-4 endpoint (`https://api.openai.com/v1/chat/completions`).

2. **Generating Insights**:
   - The `generate_insight` method takes a prompt and an API key as input parameters.
   - It constructs the request payload containing the prompt, model details (in this case, "gpt-3.5-turbo" for GPT-4 we just need to change model version for testing purpose to cost less i have used GPT3.5), and maximum tokens for response.
   - The request is sent to the GPT-4 API endpoint using the `requests.post` method with appropriate headers (Authorization and Content-Type).
   - Upon receiving a successful response (status code 200), the method extracts the generated insight from the API response and returns it.
   - In case of any error, it returns an error message.

3. **Usage**:
   - This integration enables the backend logic to generate insightful content by providing prompts related to financial data or market trends.
   - Users can input their queries or preferences, and the system leverages GPT-4 to generate relevant and informative responses.

### Benefits
- **Efficiency**: GPT-4 automates the process of analyzing financial data and generating insights, saving time and resources.
- **Accuracy**: By leveraging advanced natural language processing capabilities, the system produces accurate and contextually relevant insights.
- **Personalization**: Users can receive tailored insights based on their specific preferences and queries, enhancing user experience and engagement.

### Future Enhancements
- **Fine-tuning**: Continuously train and fine-tune the GPT-4 model to improve the quality and relevance of generated insights.
- **Integration with External Data Sources**: Integrate with external financial data sources to enrich the analysis and provide more comprehensive insights.
- **Real-time Updates**: Implement real-time analysis and insights generation to reflect the latest market trends and developments.

This integration significantly enhances the capabilities of our application, empowering users with valuable insights into the financial landscape.
## Task 3: Database Management

### Overview
Task 3 focuses on choosing and integrating a suitable database for storing user preferences and generated investment insights. We'll be implementing database schemas and handling database operations within the Django framework.

### Database Choice
For this project, we've chosen MongoDB as the database solution due to its flexibility, scalability, and compatibility with our Django application.

### Database Schema
We'll be using MongoDB collections to store user preferences and investment insights. Here's an overview of the database schema:

1. **User Preferences Collection**:
   - Stores user preferences such as investment strategies, risk tolerance, etc.
   - Each document contains a user ID and corresponding preferences.

2. **Investment Insights Collection**:
   - Stores generated investment insights for each user.
   - Each document contains a user ID, insight content, and timestamp.

### Signup and Login Functionality
We've implemented signup and login functionality to manage user authentication and authorization. Here's how it works:

- **Signup**:
  - Users can register by providing their email and password.
  - Upon successful registration, a unique user ID is generated, and the user's information is stored in the database.
  - Returns a success message upon successful registration.

- **Login**:
  - Users can log in using their registered email and password.
  - If the credentials are valid, a JSON Web Token (JWT) is generated and returned as a response.
  - The JWT token can be used for subsequent authenticated requests to the API.
  - Returns a JWT token upon successful authentication.

### Implementation Details
- We've utilized Django's built-in authentication system for signup and login functionality.
- The `User` model provided by Django is used to store user information.
- MongoDB is integrated using the PyMongo library to perform database operations.

### Next Steps
- Further database optimizations and indexing to enhance performance.
- Implement additional CRUD operations for managing user data and insights.
- Implement data validation and error handling for robustness.

By integrating MongoDB and implementing signup/login functionality, we've laid the foundation for managing user data and generating investment insights effectively.

## Task 4: RestAPI Implementation

### Overview
Task 4 involves developing RestAPIs to handle user input, preferences, and generate investment insights. These APIs will serve as endpoints for client applications to interact with the backend server.

### Implemented APIs
We've implemented the following RestAPIs:

1. **Signup API**:
   - Endpoint: `/signup`
   - Method: POST
   - Description: Allows users to register by providing their email and password.
   - Upon successful registration, a unique user ID is generated, and the user's information is stored in the database.
   - Returns a success message upon successful registration or an error message if the email is already taken.

2. **Login API**:
   - Endpoint: `/login`
   - Method: POST
   - Description: Allows users to log in using their registered email and password.
   - If the credentials are valid, a JSON Web Token (JWT) is generated and returned as a response.
   - Returns a JWT token upon successful authentication or an error message if the credentials are incorrect.

3. **Generate Insight API**:
   - Endpoint: `/generate_insight`
   - Method: POST
   - Description: Generates investment insights based on user input prompts.
   - Users can provide prompts related to financial data or market trends.
   - Utilizes the GPT-3.5 API to generate insights and stores them in the database.
   - Requires authentication using the JWT token.

4. **Save User Preference API**:
   - Endpoint: `/save_user_preference`
   - Method: POST
   - Description: Allows users to save their preferences such as investment strategies, risk tolerance, etc.
   - Stores user preferences in the database for future reference.
   - Requires authentication using the JWT token.

5. **Get User Preference API**:
   - Endpoint: `/get_user_preference/<user_id>`
   - Method: GET
   - Description: Retrieves the saved preferences of a specific user.
   - Returns the user's preferences stored in the database.
   - Requires authentication using the JWT token.

6. **Save Insight API**:
   - Endpoint: `/save_insight`
   - Method: POST
   - Description: Allows users to save generated investment insights.
   - Stores the insights in the database for future reference.
   - Requires authentication using the JWT token.

7. **Get Insights API**:
   - Endpoint: `/get_insights/<user_id>`
   - Method: GET
   - Description: Retrieves all the saved insights of a specific user.
   - Returns a list of insights stored in the database.
   - Requires authentication using the JWT token.

8. **Update Preferences API**:
   - Endpoint: `/update_preferences`
   - Method: POST
   - Description: Allows users to update their saved preferences.
   - Updates the user preferences in the database with the new values.
   - Requires authentication using the JWT token.

### Implementation Details
- We've implemented these APIs using Django and Django Rest Framework.
- Authentication is enforced using JWT tokens for secure access to protected endpoints.
- User input and preferences are validated before processing to ensure data integrity.
- Database operations are performed using MongoDB to store and retrieve user data and insights.

### Next Steps
- Implement additional error handling and validation for robust API behavior.
- Enhance security measures such as rate limiting, input sanitization, etc.
- Optimize API performance and scalability to handle increased traffic and user load.

By implementing these RestAPIs, we've provided a robust backend infrastructure for managing user input, preferences, and generating investment insights efficiently.
## Task 5: Security and Scalability

### Overview

Task 5 focuses on enhancing the security of the backend system to protect user data and ensuring scalability to handle potential growth in user base and traffic.

### Implementation Details

#### JWT (JSON Web Token)

JSON Web Tokens (JWTs) are used for secure authentication and authorization. JWTs are compact, URL-safe tokens that encode a JSON payload containing information about the user.

#### Token Generation

- Tokens are generated when users sign up or log in.
- Upon successful authentication, a JWT token is generated containing the user's unique identifier (user_id) and signed with a secret key.
- The token is then returned to the client and included in subsequent requests for authentication.

#### Middleware

- Middleware intercepts incoming requests and processes them before passing them to the views.
- The JWT middleware verifies the authenticity and validity of JWT tokens included in the request headers.
- If the token is valid, the corresponding user is retrieved from the database and attached to the request object for further processing.
- If the token is invalid or expired, appropriate error responses are returned.

#### Decorators

- Decorators are used to enforce authentication requirements on views.
- The `login_required` decorator ensures that only authenticated users can access certain views by checking if the user object exists in the request.
- If the user is not authenticated, a 403 Forbidden error is returned.

### Next Steps

- Regularly review and update security measures to mitigate potential vulnerabilities.
- Implement rate limiting, input validation, and other security best practices to prevent attacks such as SQL injection, CSRF, etc.
- Monitor system performance and scalability to anticipate and address potential bottlenecks as the user base grows.
- Consider using additional security tools and services such as HTTPS, firewalls, intrusion detection systems, etc., for comprehensive protection.

By implementing these security measures and designing the backend system for scalability, we ensure that user data remains secure and the system can handle increased demand without compromising performance.
![Screenshot (116)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/c212ddb6-d1d9-40c8-86ea-a4cd51abaa75)

![Screenshot (117)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/46bf73a1-f19e-4d68-926c-4f1bef341432)

![Screenshot (118)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/e309deb6-db27-4855-af40-d6c77c2d8c3e)

![Screenshot (119)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/920dac07-f123-4db8-a14a-6bb3324b41db)

![Screenshot (120)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/663b5125-9b4e-40b8-81f8-f5794e7d8d6c)


![Screenshot (121)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/2e5b485e-6a77-4cef-af6c-66a1597ac61a)

![Screenshot (122)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/c56a3206-2b04-4318-a207-b1f151add5e0)

![Screenshot (123)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/1c7b7eaa-fc80-4fe9-8b61-81cfcf5de4ae)

![Screenshot (124)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/c0db0ceb-eba1-471e-8760-ec8c7e06fb52)

![Screenshot (125)](https://github.com/Prajwal841/-Neosurge-Investment-Insight-Backend-App-Development-Challenge-/assets/74364347/bdee09f0-d987-4b3a-a24b-808746c57b37)



# NeoSurge-Challenge-Backend
