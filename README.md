# Instagram Posts – Flutter

A modern Instagram-inspired social media application built with **Flutter** and **Dart**, integrated with a custom **FastAPI REST API**.

This project started as a simple posts application and has grown into a more complete social media UI. It focuses on Flutter app architecture, API integration, authentication, navigation, and managing posts and comments.

## 📱 Screenshots

### Posts Feed
![Posts Feed](screenshots/posts-feed.png)

### Add Post
![Add Post](screenshots/add-post.png)

### Update Post
![Update Post](screenshots/update-post.png)

## ✨ Features

- **Authentication:** Sign in and manage an authenticated user session.
- **Home Feed:** Fetch and browse posts from the backend.
- **Explore:** Browse available posts in the explore section.
- **Post Details:** Open individual posts and view their details.
- **Create Posts:** Create posts using an image URL and caption.
- **Edit Posts:** Update existing post captions.
- **Delete Posts:** Remove posts.
- **Comments:** View and interact with post comments.
- **User Profiles:** View user profile information and posts.
- **Pull to Refresh:** Refresh feed content.
- **Navigation:** Navigate between the main application sections.
- **API Integration:** Communicate with the FastAPI backend using HTTP requests.
- **Session Management:** Maintain authentication information across app usage.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Flutter | Cross-platform UI development |
| Dart | Application programming language |
| FastAPI | Backend REST API |
| HTTP | API communication |
| JSON | Data exchange and serialization |
| Shared Preferences | Local session data storage |
| File Picker | File selection dependency |

## 📂 Project Structure

```text
lib/
├── api/
│   ├── config.dart
│   ├── dart_api.dart
│   └── session.dart
│
├── models/
│   ├── post_model.dart
│   └── user_model.dart
│
├── screens/
│   ├── add_post.dart
│   ├── auth_screen.dart
│   ├── explore_screen.dart
│   ├── feed_screen.dart
│   ├── main_shell.dart
│   ├── post_detail_screen.dart
│   ├── profile_screen.dart
│   └── update_post.dart
│
├── theme/
│   └── app_theme.dart
│
├── utils/
│   └── format.dart
│
├── widgets/
│   ├── avatar.dart
│   ├── brand.dart
│   ├── comments_panel.dart
│   ├── post_card.dart
│   └── state_views.dart
│
└── main.dart
```

## 🔗 Backend Integration

This application connects to a separate FastAPI backend.

**Backend Repository:**  
[FastAPI-Instagram-API](https://github.com/ARK13-org/FastAPI-Instagram-API)

The backend provides REST API functionality for authentication, users, posts, and comments.

The API base address is configured in:

```text
lib/api/config.dart
```

Make sure the backend is running and accessible before using the application.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ARK13-org/Instagram-Posts-Flutter.git
```

### 2. Navigate to the Project

```bash
cd Instagram-Posts-Flutter
```

### 3. Install Dependencies

```bash
flutter pub get
```

### 4. Configure the Backend

Open:

```text
lib/api/config.dart
```

Set the API address according to your environment.

Common examples:

- **Android Emulator:** `10.0.2.2` to access the host computer.
- **Physical Android Device:** Your computer's local network IP address.
- **Web/Desktop:** An address accessible from your environment.

Ensure the backend URL and port match your FastAPI configuration.

### 5. Run the Application

```bash
flutter run
```

## 📚 What I Learned

Through this project, I practiced:

- Building multi-screen Flutter applications.
- Organizing Flutter projects into reusable components.
- Managing application state and navigation.
- Creating and using Dart model classes.
- Parsing JSON responses.
- Integrating Flutter with a FastAPI backend.
- Sending HTTP requests and handling API responses.
- Implementing authentication and session management.
- Working with asynchronous operations.
- Building reusable widgets and application themes.
- Managing data across different screens.

## 🎯 Project Goal

The goal of this project is to improve my Flutter and Dart development skills by building a practical social media application and integrating it with a custom backend.

It is part of my ongoing portfolio development, combining **Flutter frontend development** with **Python and FastAPI backend development**.

---

**Developer:** [ARK13-org](https://github.com/ARK13-org)
