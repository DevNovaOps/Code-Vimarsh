# Code Vimarsh Website

A dynamic, modern website for Code Vimarsh - a college technical club. Built with Django and MySQL, featuring a cyberpunk-themed UI.

## 🚀 Features

- **Home Section**: Hero section with club logo and introduction
- **About Us**: Information about the club's mission and activities
- **Upcoming Events**: Dynamic event listing with registration links
- **Meet the Team**: Team member showcase
- **Authentication**: User login/signup system using Django's built-in authentication
- **Admin Panel**: Content management via Django Admin
- **API Endpoints**: Simple JSON APIs for events and team data (no DRF)

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Theme**: Cyberpunk/Futuristic with custom color scheme

## 📋 Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Code Vimarsh"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   - Create a MySQL database named `cv`
   - Update database credentials in `codevimarsh/settings.py` if needed:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'cv',
             'USER': 'root',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load initial data (Demo Day event)**
   ```bash
   python manage.py load_initial_data
   ```

8. **Place the logo**
   - Place `logo.webp` in the `static/images/` directory
   - The logo should be the Code Vimarsh logo provided

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the website**
    - Website: http://127.0.0.1:8000/
    - Admin Panel: http://127.0.0.1:8000/admin/

## 🎨 Design & Theme

The website features a **cyberpunk/futuristic** theme with the following color palette:

- **Gunmetal Gray**: `#48514b` - Borders and accents
- **Tan**: `#e18222` - Secondary highlights
- **Orange**: `#f0a529` - Primary highlights and glow effects
- **Black**: `#000000` - Background

Key design elements:
- Dark background with neon orange highlights
- Glowing borders and text shadows
- Smooth animations and hover effects
- Responsive design for all devices

## 📁 Project Structure

```
Code Vimarsh/
├── codevimarsh/          # Django project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── core/                 # Main Django app
│   ├── models.py         # Event and TeamMember models
│   ├── views.py          # View functions
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Admin configuration
│   └── management/       # Management commands
├── templates/            # HTML templates
│   ├── base.html
│   └── core/
│       ├── home.html
│       ├── login.html
│       └── signup.html
├── static/              # Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.webp    # Place logo here
├── manage.py
├── requirements.txt
└── README.md
```

## 🔐 Authentication Design

**Why Django's Built-in Authentication?**

1. **Simplicity**: Django's authentication system is battle-tested and requires minimal code
2. **Security**: Built-in password hashing, CSRF protection, and session management
3. **Interview-Friendly**: Easy to explain and modify during assessment
4. **No Over-engineering**: Avoids unnecessary complexity (no JWT, no custom roles)

**Session-Based Authentication Implementation:**
- **Sessions**: Django uses database-backed sessions (`django.contrib.sessions`)
- **How it works**: 
  - User logs in → `login(request, user)` creates a session
  - Session ID stored in cookie, user ID stored in session database
  - Each request checks session to identify authenticated user
  - `request.user` automatically populated from session
- **Session Configuration**:
  - Stored in database (default Django behavior)
  - Session cookie age: 2 weeks
  - HttpOnly cookies for security
  - SameSite=Lax for CSRF protection
- **No Tokens**: Uses server-side sessions, not JWT or token-based auth
- **Simple login/logout views**: Django's built-in views handle session creation/destruction
- **Logged-in users**: See "Registered Member" badge on homepage via `user.is_authenticated`

**Authentication Endpoints:**
- `/login/` - User login
- `/signup/` - User registration
- `/logout/` - User logout

## 🔌 API Endpoints

Simple JSON APIs (no Django REST Framework):

- **GET `/api/events/`**: Returns all events as JSON
  ```json
  {
    "events": [
      {
        "id": 1,
        "title": "Event Title",
        "date": "January 20, 2026",
        "description": "Event description",
        "registration_link": "https://..."
      }
    ]
  }
  ```

- **GET `/api/team/`**: Returns all team members as JSON
  ```json
  {
    "team": [
      {
        "id": 1,
        "name": "Member Name",
        "role": "Role",
        "bio": "Bio text"
      }
    ]
  }
  ```

## 📝 Admin Panel

Access the admin panel at `/admin/` to:
- Add/edit/delete events
- Add/edit/delete team members
- Manage users

## 🎯 Key Features Explained

### 1. Dynamic Content Loading
- Events and team members are loaded via JavaScript from API endpoints
- No page refresh required
- Easy to update content through Django Admin

### 2. Responsive Design
- Mobile-first approach
- Works on all screen sizes
- Touch-friendly navigation

### 3. Cyberpunk Theme
- Custom CSS with glow effects
- Smooth animations
- Dark theme with neon accents

### 4. Easy to Modify
- Clean, commented code
- Simple structure
- No complex dependencies

## 🚀 Scalability Plan

**Current Architecture:**
- Single Django app (`core`)
- Simple models (Event, TeamMember)
- Basic JSON APIs

**Future Enhancements (if needed):**
1. **Caching**: Add Redis for API response caching
2. **Media Storage**: Use AWS S3 or similar for images
3. **Email Notifications**: Django email backend for event reminders
4. **Blog Section**: Add a blog model for announcements
5. **Event Categories**: Extend Event model with categories/tags
6. **User Profiles**: Extend User model with profile information
7. **Comments/Feedback**: Add feedback system for events

**Why This Approach:**
- Start simple, scale when needed
- Easy to understand and modify
- No premature optimization
- Interview-friendly architecture

## 🧪 Testing

To test the website:

1. **Create a test user**: Use the signup page
2. **Login**: Test authentication flow
3. **View events**: Check if Demo Day event appears
4. **Add team members**: Use admin panel to add team members
5. **Test responsiveness**: Resize browser window

## 📦 Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Set a secure `SECRET_KEY`
4. Configure production database
5. Set up static file serving (e.g., WhiteNoise or CDN)
6. Use environment variables for sensitive data

## 🤝 Contributing

This is a Web Team selection project. The codebase is designed to be:
- Easy to understand
- Easy to modify during assessment
- Professional and production-ready

## 📄 License

This project is created for Code Vimarsh Web Team selection.

## 👤 Author

Built for Code Vimarsh Web Team onboarding task.

---

**Note**: Make sure to place `logo.webp` in the `static/images/` directory before running the server.

