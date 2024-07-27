## Live Deployed Link
http://my-image-analysis-app-junaid.s3-website-us-east-1.amazonaws.com/

# Image Analysis Web Application

## Project Overview

This project is a web-based image analysis application that leverages several AWS services to provide real-time image recognition capabilities. Users can upload images through a clean, intuitive interface, and receive instant analysis results, including detected objects, scenes, and their confidence levels.

## Features

- User-friendly web interface for image upload
- Real-time image analysis using AWS Rekognition
- Dynamic visualization of analysis results with confidence bars

## Technologies Used

- Frontend: HTML5, CSS3, JavaScript (ES6+)
- Backend: AWS Serverless Architecture

## AWS Services Utilized

1. **Amazon S3 (Simple Storage Service)**
   - Hosts the static website files (HTML, CSS, JS)
   - Provides scalable object storage for uploaded images

2. **Amazon API Gateway**
   - Creates and manages the RESTful API that connects the frontend to the backend services
   - Handles request/response management and API versioning

3. **AWS Lambda**
   - Executes serverless functions to process API requests
   - Integrates with other AWS services to perform image analysis

4. **Amazon Rekognition**
   - Performs advanced image analysis to detect labels, objects, and scenes
   - Provides confidence scores for detected elements

5. **AWS Identity and Access Management (IAM)**
   - Manages secure access to AWS services and resources
   - Defines and enforces fine-grained permissions for Lambda functions and other AWS resources
## Architecture //

1. User uploads an image through the web interface hosted on S3.
2. The JavaScript client sends the image data to API Gateway.
3. API Gateway triggers a Lambda function.
4. The Lambda function uses Amazon Rekognition to analyze the image.
5. Analysis results are returned through API Gateway to the client.
6. The web interface dynamically displays the results.

This project demonstrates proficiency in cloud computing, serverless architectures, and integration of various AWS services to create a scalable, efficient web application. It showcases skills essential for cloud computing roles, including working with serverless technologies, API development, and leveraging AI services in cloud environments.
