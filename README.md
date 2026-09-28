# 📸 FastAPI Instagram API

An Instagram-style REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

This project provides user authentication, posts, comments, image uploads, JWT-based authorization, and relational database management.

## ✨ Features

* 🔐 User registration and JWT authentication
* 🔑 Password hashing with `pwdlib`
* 👤 User management
* 📝 Create and delete posts
* 💬 Create, retrieve, and delete comments
* 🖼️ Image/file uploads
* 📁 Static file serving
* 🛡️ Protected endpoints using OAuth2 Bearer tokens
* 🗄️ SQLAlchemy ORM
* 🔗 User, post, and comment relationships
* 📦 Pydantic request and response schemas
* 💾 SQLite database

## 🛠️ Tech Stack

* **Python 3**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **JWT**
* **OAuth2**
* **pwdlib**
* **Uvicorn**

## 🏗️ Project Structure

```text
fastapi-instagram-api/
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

## 🔐 Authentication

The API uses **OAuth2 Bearer authentication** with JWT access tokens.

The authentication flow is:

```text
User Login
    ↓
Validate Credentials
    ↓
Generate JWT
    ↓
Client Sends Bearer Token
    ↓
Validate JWT
    ↓
Get Current User
    ↓
Access Protected Endpoint
```

Passwords are hashed before being stored in the database.

## 🗄️ Database Relationships

The project uses SQLAlchemy ORM to model the relationships between users, posts, and comments.

```text
User
 │
 ├── 1 ──── N ──── Post
 │                  │
 │                  └── 1 ──── N ──── Comment
 │
 └── 1 ──── N ──── Comment
```

### Models

**User**

* `id`
* `username`
* `email`
* `password`

**Post**

* `id`
* `image_url`
* `image_url_type`
* `caption`
* `timestamp`
* `user_id`

**Comment**

* `id`
* `text`
* `timestamp`
* `user_id`
* `post_id`

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ARK13-org/fastapi-instagram-api.git
cd fastapi-instagram-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 📡 Main Endpoints

### Users

```text
POST /user
```

Create a new user.

### Authentication

```text
POST /token
```

Authenticate a user and receive a JWT access token.

### Posts

```text
POST /post/create_post
GET  /post/
POST /post/delete/{id}
POST /post/upload_file
```

### Comments

```text
POST /comment/create_comment
GET  /comment/{id}
POST /comment/delete/{id}
```

## 🖼️ File Uploads

The API supports uploading image files.

Uploaded files are stored in the:

```text
uploaded_file/
```

directory and exposed through FastAPI's static file handling.

## 🧠 What I Explored

This project helped me practice:

* Building REST APIs with FastAPI
* Dependency injection with `Depends`
* OAuth2 Bearer authentication
* JWT access tokens
* Password hashing and verification
* SQLAlchemy ORM
* Foreign keys and relationships
* Pydantic schemas
* CRUD operations
* File uploads with `UploadFile`
* Static file serving
* API response models
* Organizing a FastAPI project into routers, database logic, authentication, and schemas

## 🔮 Future Improvements

* PostgreSQL support
* Alembic database migrations
* Refresh tokens
* Better authentication and authorization
* User profile endpoints
* Like and follow functionality
* Pagination
* Search and filtering
* Image validation and processing
* Automated tests with Pytest
* Docker support
* Environment-based configuration
* Improved error handling

## 📚 Project Purpose

This project was built as a practical backend project to learn how different FastAPI components work together in a real-world style application.

It focuses on **API design, authentication, database relationships, and backend architecture** rather than reproducing the complete Instagram platform.
