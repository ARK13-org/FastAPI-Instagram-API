# 📸 FastAPI Instagram API

An Instagram-inspired REST API built with **FastAPI, SQLAlchemy, and SQLite**. This project provides backend functionality for user management, authentication, post management, comments, and image uploads.

Originally developed to practice backend development fundamentals, the project has evolved with additional API endpoints, improved frontend integration, and support for Flutter UI development.

## 🔄 Project Evolution

This project has gone through several improvements since its initial version.

| Feature | Original Version | Updated Version |
|---|---|---|
| User registration | ✅ | ✅ |
| JWT authentication | ✅ | ✅ |
| Password hashing | ✅ | ✅ |
| User retrieval | Basic | Expanded |
| Post creation | ✅ | ✅ |
| Fetch all posts | ✅ | ✅ |
| Fetch individual posts | — | ✅ |
| Fetch posts by user | — | ✅ |
| Update post captions | — | ✅ |
| Delete posts | ✅ | ✅ |
| Image uploads | ✅ | ✅ |
| Comment creation | ✅ | ✅ |
| Fetch comments | ✅ | ✅ |
| Comment deletion | ✅ | ✅ |
| CORS middleware | — | ✅ |
| Flutter frontend integration | — | Added as current development focus |

The updated version focuses on making the API more flexible and suitable for frontend applications.

## ✨ Features

### 👤 User Management
- User registration.
- Retrieve user information.
- Retrieve users by specific identifiers.
- User account deletion.

### 🔐 Authentication
- OAuth2 authentication.
- JWT access token generation.
- Password hashing using pwdlib.

### 📝 Post Management
- Create new posts.
- Retrieve all posts.
- Retrieve individual posts.
- Retrieve posts belonging to a specific user.
- Update post captions using PATCH.
- Delete posts.

### 🖼️ Image Handling
- Support for external image URLs.
- Upload image files to the backend.
- Serve locally uploaded images using FastAPI static files.

### 💬 Comment Management
- Create comments.
- Retrieve comments belonging to a post.
- Delete comments.

### 🌐 Frontend Integration
- CORS middleware configuration.
- REST API endpoints designed for frontend consumption.
- Flutter integration for practicing real-world API communication.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database operations |
| SQLite | Relational database |
| Pydantic | Data validation |
| OAuth2 | Authentication framework |
| JWT | Token-based authentication |
| pwdlib | Password hashing |
| Uvicorn | ASGI server |

## 📂 Project Structure

```text
FastAPI-Instagram-API/
│
├── auth/
│   ├── authentication.py
│   └── oauth2.py
│
├── db/
│   ├── database.py
│   ├── models.py
│   ├── db_user.py
│   ├── db_post.py
│   ├── db_comment.py
│   └── hash.py
│
├── routers/
│   ├── user.py
│   ├── post.py
│   └── comment.py
│
├── uploaded_file/
│
├── main.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ARK13-org/FastAPI-Instagram-API.git

cd FastAPI-Instagram-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the upload directory

Make sure the `uploaded_file` directory exists in the project root.

```bash
mkdir uploaded_file
```

### 5. Start the server

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 6. API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 📡 API Endpoints

The following table summarizes the main API operations.

### Users

| Method | Endpoint | Description |
|---|---|---|
| POST | `/user` | Register a user |
| GET | `/user/{id}` | Retrieve a user by ID |
| GET | User lookup route | Retrieve a user by username |
| DELETE | `/user/delete/{id}` | Delete a user |

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/token` | Generate a JWT access token |

### Posts

| Method | Endpoint | Description |
|---|---|---|
| POST | `/post/create_post` | Create a post |
| GET | `/post/` | Retrieve all posts |
| GET | `/post/{id}` | Retrieve a specific post |
| GET | `/post/user_posts?user_id={id}` | Retrieve posts by user |
| PATCH | `/post/update_caption/{id}` | Update a post caption |
| POST | `/post/delete_post/{id}` | Delete a post |
| POST | `/post/upload_file` | Upload an image |

### Comments

| Method | Endpoint | Description |
|---|---|---|
| POST | `/comment/create_comment` | Create a comment |
| GET | `/comment/{id}` | Retrieve comments for a post |
| DELETE | `/comment/delete_comment?id={id}` | Delete a comment |

*Note: Check the actual router definitions in Swagger UI for exact paths, HTTP methods, and request parameters.*

## 🔐 Authentication Status

JWT authentication and OAuth2 functionality are implemented in the project.

For the current Flutter UI development and testing phase, authentication dependencies have intentionally been disabled on selected post and comment routes.

This allows frontend operations to be tested without implementing the login interface first.

**Security note:** These routes are currently intended for local development and UI practice. Authentication and ownership validation should be enabled before public deployment.

## 🗄️ Database Design

The application uses SQLAlchemy ORM to manage relationships between users, posts, and comments.

```text
User
 │
 ├── Posts (One-to-Many)
 │     │
 │     └── Comments (One-to-Many)
 │
 └── Comments (One-to-Many)
```

Main database entities:

- **User:** Stores user account information.
- **Post:** Stores image information, captions, timestamps, and user relationships.
- **Comment:** Stores comment text, timestamps, and relationships with users and posts.

## 📱 Flutter Integration

The updated backend is also being used for Flutter frontend development.

The current frontend practice focuses on the Posts section, including:

- Displaying posts from the API.
- Creating posts with images and captions.
- Updating post captions.
- Retrieving individual posts.
- Connecting Flutter models to FastAPI responses.

For Android emulator testing, use `10.0.2.2` instead of `127.0.0.1` to access a FastAPI server running on your computer.

For physical-device testing, use your computer's local network IP address and configure CORS and network access appropriately.

## 🧠 What I Learned

During the development of this project, I practiced:

- Building REST APIs with FastAPI.
- Structuring applications using routers and modules.
- SQLAlchemy ORM and relational database management.
- Implementing CRUD operations.
- Pydantic schemas and data validation.
- OAuth2 and JWT authentication.
- Password hashing.
- Handling file uploads and static files.
- Configuring CORS for frontend integration.
- Connecting backend APIs with Flutter.

## 🎯 Project Goal

The goal of this project is to strengthen my backend development skills using FastAPI while building a foundation for an Instagram-inspired application.

It has evolved from a basic backend learning project into a more feature-rich REST API that I can use alongside Flutter to practice full-stack application development.
