# Instagram API

An Instagram-inspired REST API built with **FastAPI, Python, SQLAlchemy, and SQLite**.

This project provides backend functionality for user accounts, JWT authentication, posts, comments, and image uploads. It is also designed to integrate with Flutter applications.

## Features

### User Management
- User registration with password hashing.
- List and search users.
- Retrieve public user profiles.
- Retrieve and update your own profile.
- Delete your own account.
- Track post and comment counts.

### Authentication
- OAuth2 password authentication.
- JWT access tokens.
- Secure password hashing with `pwdlib`.
- Protected endpoints with ownership validation.

### Post Management
- Create posts with image URLs or uploaded images.
- Retrieve all posts.
- Retrieve individual posts.
- Retrieve posts by user.
- Update post captions.
- Delete your own posts.

### Comment Management
- Create comments on posts.
- Retrieve comments for a post.
- Edit your own comments.
- Delete your own comments or comments on your own posts.

### Image Handling
- Support for external image URLs.
- Upload JPG, JPEG, PNG, GIF, and WebP files.
- Serve uploaded images through FastAPI static files.

### Frontend Integration
- CORS middleware.
- RESTful endpoints.
- Flutter application integration.
- JSON request and response handling.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database operations |
| SQLite | Database |
| Pydantic | Data validation |
| OAuth2 | Authentication |
| JWT | Token-based authentication |
| pwdlib | Password hashing |
| Uvicorn | ASGI server |

## Project Structure

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

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ARK13-org/FastAPI-Instagram-API.git

cd FastAPI-Instagram-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
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

### 4. Configure the JWT secret

Set a secure secret key before running the application.

PowerShell:

```powershell
$env:SECRET_KEY = "your-secure-secret-key"
```

macOS/Linux:

```bash
export SECRET_KEY="your-secure-secret-key"
```

The application currently has a development fallback secret. Always configure a secure secret before deployment.

### 5. Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

The SQLite database is created automatically when the application starts.

## API Documentation

FastAPI automatically generates interactive documentation.

| Documentation | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

## API Endpoints

Protected endpoints require a valid JWT bearer token.

### Authentication

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/token` | Authenticate and generate an access token | No |

### Users

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/user` | Register a new user | No |
| GET | `/user` | List users, optionally search with `q` | No |
| GET | `/user/me` | Retrieve your own profile | Yes |
| PATCH | `/user/me` | Update your email or bio | Yes |
| GET | `/user/by_username/{username}` | Retrieve a user by username | No |
| GET | `/user/{id}` | Retrieve a user by ID | No |
| DELETE | `/user/delete/{id}` | Delete your own account | Yes |

The user listing endpoint supports `q` and `limit` query parameters.

### Posts

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/post/create_post` | Create a post | Yes |
| GET | `/post/` | Retrieve all posts | No |
| GET | `/post/{id}` | Retrieve a post by ID | No |
| GET | `/post/user_posts?user_id={id}` | Retrieve posts by user | No |
| PATCH | `/post/update_caption/{id}` | Update your post caption | Yes |
| DELETE | `/post/delete_post/{id}` | Delete your post | Yes |
| POST | `/post/upload_file` | Upload an image | Yes |

### Comments

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/comment/create_comment` | Create a comment | Yes |
| GET | `/comment/{id}` | Retrieve comments for a post | No |
| PATCH | `/comment/update_comment/{id}` | Update your comment | Yes |
| DELETE | `/comment/delete_comment?id={id}` | Delete an authorized comment | Yes |

## Authentication

The API uses OAuth2 password authentication with JWT access tokens.

### 1. Register

Send a POST request to:

```text
/user
```

Example JSON body:

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "your-password"
}
```

### 2. Login

Send a POST request to:

```text
/token
```

Use form data with:
- `username`
- `password`

The response includes an access token and user information.

### 3. Authorize requests

For protected endpoints, include the token in the request header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Image Uploads

The API supports external image URLs and uploaded image files.

To upload an image:

```text
POST /post/upload_file
```

Use `multipart/form-data` with a field named `file`.

The response includes the uploaded file path and its URL.

Uploaded images can be accessed through:

```text
http://127.0.0.1:8000/files/filename.jpg
```

When creating a post, `image_url_type` must be either `url` or `uploaded`.

## Database

The project uses SQLite with SQLAlchemy ORM.

The main database entities are:

- **User:** Account information, email, hashed password, and profile bio.
- **Post:** Image URL, image type, caption, timestamp, and author.
- **Comment:** Comment text, timestamp, author, and associated post.

Relationships connect users to their posts and comments, and posts to their comments.

The database file is generated locally and excluded from version control.

## Flutter Integration

This backend is connected to a separate Flutter frontend project:

[Instagram Posts - Flutter](https://github.com/ARK13-org/Instagram-Posts-Flutter)

The integration provides practice with:
- Fetching and displaying posts.
- Creating and managing posts.
- User authentication.
- Connecting Flutter models to FastAPI responses.
- Sending authenticated API requests.

For Android emulator testing, use `10.0.2.2` instead of `127.0.0.1` to access the API running on your computer.

For physical-device testing, use your computer's local network IP address.

## Security Notes

- Passwords are hashed before being stored.
- Protected endpoints use JWT authentication.
- Users can only modify or delete their own posts and profiles.
- Users can only edit their own comments.
- Comment authors and post owners can delete comments.
- Configure a secure `SECRET_KEY` before deployment.
- Restrict CORS origins before production deployment.

## What I Learned

Through this project, I practiced:

- Building REST APIs with FastAPI.
- Structuring applications with routers and modules.
- SQLAlchemy ORM and relational databases.
- CRUD operations.
- Pydantic schemas and validation.
- OAuth2 and JWT authentication.
- Password hashing.
- File uploads and static file serving.
- CORS configuration.
- Integrating backend APIs with Flutter.

## Project Goal

The goal of this project is to build a practical Instagram-inspired backend while strengthening my Python and FastAPI skills and applying backend concepts through Flutter integration.
