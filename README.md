\# Isaac AI



\*\*An AI-powered chatbot built with FastAPI, Groq, PostgreSQL, and JavaScript.\*\*



Isaac AI is a full-stack AI chatbot that allows users to create accounts, interact with an AI assistant, and manage their conversations. It uses the Groq API to generate responses and PostgreSQL to store user accounts, conversations, and messages.



\## Features



\- \*\*User Authentication\*\* — Register and log in securely using email and password.

\- \*\*AI Chat\*\* — Generate AI responses using the Groq API.

\- \*\*Conversation History\*\* — Save and retrieve previous conversations.

\- \*\*Conversation Management\*\* — Create, rename, and delete conversations.

\- \*\*Edit and Resend\*\* — Edit previous messages and generate a new response.

\- \*\*Regenerate Responses\*\* — Generate a new answer to the latest prompt.

\- \*\*Stop Generation\*\* — Stop waiting for an ongoing response from the frontend.

\- \*\*Markdown Support\*\* — Display formatted text, code blocks, and syntax highlighting.

\- \*\*Export Conversations\*\* — Download conversations as TXT or PDF files.

\- \*\*Responsive Interface\*\* — Chat interface designed for different screen sizes.



\## Tech Stack



\### Backend

\- Python

\- FastAPI

\- Groq API

\- PostgreSQL

\- SQLAlchemy

\- Pydantic

\- JWT Authentication

\- Argon2 Password Hashing



\### Frontend

\- HTML

\- CSS

\- JavaScript

\- Marked.js

\- DOMPurify

\- Highlight.js

\- jsPDF



\### Deployment and Tools

\- Render

\- Git

\- GitHub

\- VS Code



\## Project Structure



```text

Isaac-AI/

│

├── backend/

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── requirements.txt

│   ├── test\_main.py

│   └── README.md

│

├── frontend/

│   ├── index.html

│   ├── style.css

│   ├── script.js

│   ├── favicon.svg

│   └── BACKEND\_PATCH.md

│

├── screenshots/

│

├── .gitignore

└── README.md

```



\## Getting Started



\### 1. Clone the Repository



```bash

git clone https://github.com/y2man/Isaac-AI.git

cd Isaac-AI

```



\### 2. Set Up the Backend



```bash

cd backend

py -m venv venv

```



Activate the virtual environment on Windows:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

py -m pip install -r requirements.txt

```



\### 3. Configure Environment Variables



Create a `.env` file inside the `backend` folder:



```env

GROQ\_API\_KEY=your\_groq\_api\_key

DATABASE\_URL=your\_postgresql\_database\_url

JWT\_SECRET=your\_secret\_key

```



Replace the example values with your own credentials. Never commit your `.env` file or expose your API keys.



\### 4. Run the Backend



From the `backend` directory:



```bash

py -m uvicorn main:app --reload

```



The API will be available at:



`http://127.0.0.1:8000`



Interactive API documentation:



`http://127.0.0.1:8000/docs`



\### 5. Run the Frontend



Open the `frontend` folder in VS Code and launch `index.html` using the Live Server extension.



Make sure the frontend API configuration points to your running backend.



\## Live Demo



\*\*Backend API:\*\*  

https://python-practice-4cx5.onrender.com



\*\*API Documentation:\*\*  

https://python-practice-4cx5.onrender.com/docs



\## Screenshots



\### Main Chat Interface



!\[Isaac AI Main Chat](screenshots/main-chat.png)





\## What I Learned



Building Isaac AI helped me gain practical experience with:



\- Building REST APIs using FastAPI.

\- Integrating external AI APIs into Python applications.

\- Managing relational databases with PostgreSQL and SQLAlchemy.

\- Implementing authentication and password security.

\- Connecting a JavaScript frontend to a Python backend.

\- Managing conversation history and database relationships.

\- Testing API endpoints and handling errors.

\- Deploying a full-stack application.



\## Future Improvements



\- Streaming AI responses.

\- Improved conversation search.

\- More customization options.

\- Additional AI features and tools.



\## Author



\*\*Isaac\*\*



Software Engineering Student | Python Developer | AI Integration Learner



GitHub: \[@y2man](https://github.com/y2man)



\---



\*Built as a hands-on project to explore AI integration and full-stack application development.\*

