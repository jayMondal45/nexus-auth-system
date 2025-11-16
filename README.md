# 🌟 Nexus Authentication System

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-2.0%2B-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-success)

**A modern, beautiful, and feature-rich authentication system built with Flask**

*Complete user authentication flow with registration, login, and password recovery*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Demo](#-screenshots) • [Contributing](#-contributing)

</div>

---

## ✨ Features

### Core Functionality
- 🔐 **User Registration** - Create new accounts with email validation
- 🔑 **Secure Login** - Authenticate users with email and password
- 📧 **Password Recovery** - Reset passwords via email notification
- 💾 **SQLite Database** - Lightweight and efficient user data storage
- ✉️ **Email Integration** - SMTP email sending for password recovery

### User Experience
- 📱 **Fully Responsive** - Mobile-friendly interface that works on all devices
- 🎨 **Modern UI/UX** - Beautiful gradient design with floating animations
- 💬 **Flash Messages** - Real-time feedback for user actions (success/error)
- 👁️ **Password Visibility Toggle** - Show/hide password functionality
- 🔄 **Smooth Transitions** - Animated form switching between login/register/forgot
- 🎯 **Navigation Dots** - Easy visual navigation between forms

### Design Elements
- 🌈 Stunning gradient purple background with animated floating elements
- ✨ Glassmorphism effect on the main container
- 🎭 Custom-styled input fields with Font Awesome icons
- 🎪 Interactive hover effects and animations
- 🎨 Clean, professional Poppins font typography
- 🔵 Social login placeholders (Facebook, Twitter, Google) - Ready for OAuth integration

## 🚀 Quick Start

### Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- pip (Python package installer)
- A Gmail account (or other SMTP email provider) for password recovery feature

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jayMondal45/nexus-auth-system.git
   cd nexus-auth-system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install flask flask-sqlalchemy
   
   # Or use requirements.txt if available
   pip install -r requirements.txt
   ```

4. **Configure email settings**
   
   Open `main.py` and update these variables:
   ```python
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_PORT = 587
   EMAIL_ADDRESS = "your_email@gmail.com"      # Your email
   EMAIL_PASSWORD = "your_app_password"        # Your app password
   ```

   **For Gmail users:**
   - Enable 2-Factor Authentication on your Google account
   - Generate an App Password: Visit [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Use the 16-character app password (not your regular Gmail password)

5. **Update secret key** (Important for security)
   ```python
   app.secret_key = "your-super-secret-random-key-here"
   ```

6. **Run the application**
   ```bash
   python main.py
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:5000/
   ```

That's it! Your authentication system is now running locally. 🎉

## 🔒 Security Notes

> ⚠️ **IMPORTANT DISCLAIMER**: This project is designed for **educational and demonstration purposes**. It contains several security vulnerabilities that must be addressed before using in production.

### Current Security Issues:

| Issue | Risk Level | Description |
|-------|-----------|-------------|
| 🔴 Plain Text Passwords | **CRITICAL** | Passwords stored without hashing |
| 🔴 Password via Email | **CRITICAL** | Sends actual passwords instead of reset tokens |
| 🟡 No CSRF Protection | **HIGH** | Vulnerable to cross-site request forgery |
| 🟡 No Rate Limiting | **HIGH** | Susceptible to brute force attacks |
| 🟡 No Email Verification | **MEDIUM** | Users can register with any email |
| 🟡 No Session Management | **MEDIUM** | Lacks proper user session handling |
| 🟡 Hardcoded Secret Key | **MEDIUM** | Uses weak secret key in code |

### 🛡️ Recommended Security Improvements

**For Production Use, Implement:**

1. **Password Hashing**
   ```python
   from werkzeug.security import generate_password_hash, check_password_hash
   
   # When storing password
   hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
   
   # When verifying
   if check_password_hash(user.password, provided_password):
       # Login successful
   ```

2. **Password Reset Tokens**
   ```python
   from itsdangerous import URLSafeTimedSerializer
   
   # Generate reset token instead of sending password
   serializer = URLSafeTimedSerializer(app.secret_key)
   token = serializer.dumps(user.email, salt='password-reset-salt')
   ```

3. **Additional Security Packages**
   ```bash
   pip install flask-login        # Session management
   pip install flask-wtf          # CSRF protection
   pip install flask-limiter      # Rate limiting
   pip install email-validator   # Email validation
   ```

4. **Environment Variables**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   app.secret_key = os.getenv('SECRET_KEY')
   EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
   ```

### Best Practices Checklist

- [ ] Hash all passwords using bcrypt or werkzeug
- [ ] Implement token-based password reset
- [ ] Add CSRF protection on all forms
- [ ] Enable rate limiting on login attempts
- [ ] Verify email addresses before activation
- [ ] Use environment variables for sensitive data
- [ ] Implement proper session management
- [ ] Add input validation and sanitization
- [ ] Enable HTTPS in production
- [ ] Set up proper logging and monitoring

## 📁 Project Structure

```
nexus-auth-system/
│
├── 📄 main.py                      # Main Flask application with routes
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # Project documentation
├── 📄 .gitignore                   # Git ignore file
│
├── 📁 templates/
│   └── 📄 login.html               # HTML template for all forms
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css            # Complete styling
│   └── 📁 js/
│       └── 📄 app.js               # JavaScript functionality
│
└── 📁 instance/
    └── 📄 users.db                 # SQLite database (auto-generated)
```

## 🎮 How to Use

### Registration
1. Click on **"Create account"** link
2. Enter your full name, email, and password
3. Confirm your password
4. Click **"Create Account"** button
5. Success! You can now login

### Login
1. Enter your registered email
2. Enter your password
3. Optional: Check "Remember me"
4. Click **"Sign In"** button

### Forgot Password
1. Click **"Forgot password?"** link
2. Enter your registered email address
3. Click **"Send Password"** button
4. Check your email inbox for password recovery

## 📸 Screenshots

### Login Interface
The main login screen features:
- Clean gradient background (purple to violet)
- Animated floating elements
- Email and password input fields
- Remember me checkbox
- Forgot password link
- Social login buttons (Facebook, Twitter, Google)

### Registration Form
- Full name field
- Email validation
- Password with visibility toggle
- Confirm password field
- Smooth transition animation

### Password Recovery
- Simple email input
- Clear instructions
- Email confirmation message
- Back to login option

## 🛠️ Built With

### Backend
- **[Flask 2.0+](https://flask.palletsprojects.com/)** - Micro web framework
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** - ORM for database management
- **[SQLite](https://www.sqlite.org/)** - Lightweight database
- **[smtplib](https://docs.python.org/3/library/smtplib.html)** - Email sending functionality

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **JavaScript (ES6+)** - Client-side interactivity
- **[Font Awesome 6.4.0](https://fontawesome.com/)** - Icon library
- **[Google Fonts (Poppins)](https://fonts.google.com/specimen/Poppins)** - Typography

### Design Features
- CSS Variables for theming
- Flexbox & Grid layouts
- CSS Animations & Transitions
- Glassmorphism effects
- Responsive design principles

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**! 

### How to Contribute

1. **Fork the Project**
   ```bash
   # Click the 'Fork' button at the top right of this page
   ```

2. **Clone your Fork**
   ```bash
   git clone https://github.com/your-username/nexus-auth-system.git
   cd nexus-auth-system
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make your Changes**
   - Write clean, readable code
   - Follow existing code style
   - Add comments where necessary
   - Test your changes thoroughly

5. **Commit your Changes**
   ```bash
   git add .
   git commit -m "Add some AmazingFeature"
   ```

6. **Push to your Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Provide a clear description of your changes

### Contribution Guidelines

- ✅ Write clear commit messages
- ✅ Update documentation if needed
- ✅ Add comments to complex code
- ✅ Test your code before submitting
- ✅ Keep pull requests focused on a single feature/fix
- ✅ Be respectful and constructive in discussions

### Areas for Contribution

- 🔐 Security improvements
- 🎨 UI/UX enhancements
- 📝 Documentation updates
- 🐛 Bug fixes
- ✨ New features
- 🧪 Test coverage
- 🌍 Internationalization (i18n)

## 📋 Future Roadmap

### High Priority
- [ ] 🔐 Implement password hashing (bcrypt/werkzeug)
- [ ] 🎫 Add password reset tokens instead of sending passwords
- [ ] 🔑 Integrate Flask-Login for session management
- [ ] 🛡️ Add CSRF protection with Flask-WTF
- [ ] ⏱️ Implement rate limiting to prevent brute force
- [ ] ✉️ Add email verification for new accounts

### Medium Priority
- [ ] 👤 Create user profile page with edit functionality
- [ ] 🔄 Implement actual "Remember Me" functionality
- [ ] 💪 Add password strength indicator
- [ ] 🌐 Integrate OAuth (Google, Facebook, Twitter)
- [ ] 📱 Add mobile app support (API endpoints)
- [ ] 🎨 Add theme switcher (Light/Dark mode)

### Low Priority
- [ ] 👑 Create admin dashboard for user management
- [ ] 🎭 Add user roles and permissions system
- [ ] 📊 Implement analytics and logging
- [ ] 🔍 Add advanced search and filtering
- [ ] 🌍 Multi-language support (i18n)
- [ ] 📧 Email templates customization
- [ ] 🧪 Add comprehensive test suite
- [ ] 🐳 Docker containerization
- [ ] 📚 API documentation with Swagger

### Nice to Have
- [ ] 2FA (Two-Factor Authentication)
- [ ] Social profile integration
- [ ] Activity log for user actions
- [ ] Export user data feature
- [ ] Password history
- [ ] Account deletion feature
- [ ] Email notifications for login from new device

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Jay Mondal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Author

<div align="center">

### **Jay Mondal**

[![GitHub](https://img.shields.io/badge/GitHub-jayMondal45-181717?style=for-the-badge&logo=github)](https://github.com/jayMondal45)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/jay-mondal)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:your.email@example.com)

</div>

## 🙏 Acknowledgments

Special thanks to:

- **[Flask](https://flask.palletsprojects.com/)** - The amazing Python web framework
- **[Font Awesome](https://fontawesome.com/)** - For the beautiful icon library
- **[Google Fonts](https://fonts.google.com/)** - For the Poppins typeface
- **Stack Overflow Community** - For countless solutions and inspirations
- **GitHub Community** - For hosting and version control
- **All Contributors** - Who help improve this project

## 📞 Support & Feedback

### Found a Bug? 🐛
If you encounter any bugs or issues, please:
1. Check if it's already reported in [Issues](https://github.com/jayMondal45/nexus-auth-system/issues)
2. If not, create a [New Issue](https://github.com/jayMondal45/nexus-auth-system/issues/new)
3. Provide detailed information about the bug

### Have Questions? ❓
- Open a [Discussion](https://github.com/jayMondal45/nexus-auth-system/discussions)
- Check existing discussions for similar questions
- Create a new discussion if needed

### Want to Help? 💪
- Star ⭐ this repository if you find it helpful
- Share it with others who might benefit
- Contribute by fixing bugs or adding features
- Improve documentation

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ by [Jay Mondal](https://github.com/jayMondal45)**

*Happy Coding! 🚀*

---

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=jayMondal45.nexus-auth-system)
![Last Commit](https://img.shields.io/github/last-commit/jayMondal45/nexus-auth-system)
![Repo Size](https://img.shields.io/github/repo-size/jayMondal45/nexus-auth-system)

</div>
