# 7-Segment Display Digit Recognition

## Introduction
This project is a prediction app that utilizes AI computer vision to recognize digits on a 7-segment display. The app is built using a FastAPI backend and a Nuxt 3 frontend. The backend receives images of 7-segment displays, processes them using a trained AI model, and sends the predictions to the frontend. The frontend displays the prediction and maintains a history of all previous predictions.

## Project Structure
The project is divided into two main folders:
- **ai**: Contains the AI model and FastAPI backend.
- **client**: Contains the Nuxt 3 frontend.

## AI Model
The AI model is trained on a dataset of images of 7-segment displays and is capable of recognizing digits (0-9). The model is implemented using the Ultralytics YOLOv8 library.

## FastAPI Backend
The FastAPI backend:
- Receives images of 7-segment displays.
- Processes them using the AI model.
- Sends the predictions to the frontend.
- Is implemented using the FastAPI framework and is deployed on a local server.

## Nuxt 3 Frontend
The Nuxt 3 frontend:
- Displays the prediction.
- Maintains a history of all previous predictions.
- Is implemented using the Nuxt 3 framework and is deployed on a local server.

## Features
- **Image Upload**: Users can upload images of 7-segment displays to the app.
- **Prediction**: The app displays the predicted digit on the 7-segment display.
- **Prediction History**: The app maintains a history of all previous predictions.

## Requirements
- Python 3.9+
- FastAPI
- Ultralytics YOLOv8
- Nuxt 3
- Node.js 14+

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required dependencies:
   ```bash
   cd client && npm i
   ```
3. Start the FastAPI backend:
   ```bash
   cd ai && fastapi dev main.py
   ```
4. Start the Nuxt 3 frontend:
   ```bash
   cd client && npm run dev
   ```

## Usage
1. Open the app in your web browser at `http://localhost:3000`
2. Upload an image of a 7-segment display.
3. The app will display the predicted digit.
4. The app will maintain a history of all previous predictions.

## API Documentation
The FastAPI backend provides a RESTful API for interacting with the app. The API is documented using Swagger and can be accessed at:
- `http://localhost:8000/docs`

## Commit Messages
Commit messages follow the conventional commit message format.

## Branching Strategy
The project uses a feature-branch workflow. New features are developed in separate branches and merged into the main branch when complete.

To check more over my workflow and the train of thoughts check out the diagrams i have drawn out while planning this small project: [Figjam Board](https://www.figma.com/board/TkoeqbAxCUhr7QwW1FrzCS/WorkFlow?node-id=0-1&t=1ofNXRnW7ehpLy9R-1)

## API Endpoints
The FastAPI backend provides the following API endpoints:
- `POST /predict`: Receives an image of a 7-segment display and returns the prediction consisting of x and y coordinates, class, and confidence level for each digit.

## Model Training
The AI model is trained on a dataset of images of 7-segment displays using the Ultralytics YOLOv8 library.

## Model Evaluation
The AI model is evaluated using metrics such as mAP50, mAP50-95.

## Model Deployment
The AI model is deployed on a local server using the FastAPI framework.

## Future Work
- Improve the accuracy of the AI model.
- Add support for recognizing multiple digits on a single 7-segment display.