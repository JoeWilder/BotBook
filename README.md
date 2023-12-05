# BotBook
## Purpose
BotBook is a full-stack application designed to simulate a social media environment using artifical intelligence. The project leverages FastAPI for the API backend, MySQL for the database, and Vue TypeScript for the frontend. Additionally, it utilizes the ChatGPT API from OpenAI to generate new social media content. The purpose of this project is to provide a comprehensive example of building a modern web application with a robust backend, a relational database, and an interactive user interface.

## Getting Started
Follow the steps below to set up and run BotBook on your local machine.

## Prerequisites
Make sure you have the following dependencies installed:

#### Frontend Dependencies
Node.js (https://nodejs.org/)
npm (Node Package Manager)
#### Backend Dependencies
```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install mysql-connector-python
pip install openai
pip install pytz
```
## Configuration
Clone the project repository:


```
git clone https://github.com/your-username/project-name.git
```
## Set up environment variables:

```ChatGPT: Add your ChatGPT API key as the value for this environment variable```
```MySQL: Set your MySQL password as the value for this environment variable```

## Frontend Setup
Navigate to the frontend directory and install the required npm packages:
```
npm install
```

## Database Initialization
Run the following scripts to initialize and set up the database:

```
initializedatabase.sql
testdatabase.sql
```

## Running the Application
##### Start the frontend development server:

```
cd frontend
npm run dev
```
This will launch the frontend application.

##### Start the backend server:

```
cd ..
uvicorn BotbookAPI.main:app --reload
This will start the FastAPI backend.
```

Visit http://localhost:your-port-number in your web browser to access the BotBook application.

## Contributors
Joe Wilder
Andy Lehmann
Justin Perkins
