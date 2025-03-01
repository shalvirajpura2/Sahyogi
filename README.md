# Sahyogi - Volunteer Management System

A web-based platform that connects volunteers with organizations, streamlining the process of finding and managing volunteer opportunities.

## 🌟 Features

### For Volunteers
- Browse available volunteer opportunities
- Easy application process for events
- Track application status
- Personalized dashboard
- Profile management

### For Recruiters
- Create and post volunteer events
- Manage volunteer applications
- Track event participation
- View volunteer profiles
- Event management dashboard

### For Administrators
- Comprehensive user management
- System-wide analytics
- Monitor all activities
- User activation/deactivation
- Platform oversight

## 🛠️ Tech Stack

- **Backend:** Django 4.2
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Database:** SQLite3
- **Authentication:** Django Authentication System
- **Icons:** Font Awesome

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shalvirajpura2/Sahyogi.git
   cd Sahyogi
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open browser and go to: `http://127.0.0.1:8000`
   - Admin interface: `http://127.0.0.1:8000/admin`

## 📁 Project Structure

```
Sahyogi/
├── accounts/                # User management app
│   ├── models.py           # User and event models
│   ├── views.py            # View logic
│   └── forms.py            # Form definitions
├── volunteer_system/       # Main project settings
├── templates/             # HTML templates
│   ├── admin/            # Admin templates
│   ├── volunteer/        # Volunteer templates
│   └── recruiter/        # Recruiter templates
└── static/               # Static files (CSS, JS)
```

## 💡 Key Features Implementation

- **Custom User Model**: Extended Django's base user model to include user types
- **Role-Based Access**: Different views and permissions for volunteers, recruiters, and admins
- **Event Management**: Complete CRUD operations for volunteer events
- **Application System**: Streamlined process for volunteer applications
- **Dashboard Analytics**: User-specific statistics and activity tracking
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5

## 🔐 Security Features

- CSRF Protection
- Secure Authentication
- Role-based Authorization
- Form Validation
- Secure Password Handling

## 🎨 UI Features

- Responsive Design
- Intuitive Navigation
- Clean and Modern Interface
- Consistent Color Scheme
- User-friendly Forms
- Interactive Elements

## 👥 User Types

1. **Volunteers**
   - Browse Events
   - Apply for Opportunities
   - Track Applications

2. **Recruiters**
   - Create Events
   - Manage Applications
   - Track Participation

3. **Administrators**
   - User Management
   - System Monitoring
   - Platform Administration

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👩‍💻 Author

**Shalvi Rajpura**
- GitHub: [@shalvirajpura2](https://github.com/shalvirajpura2)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- Open Source Community

---
© 2025 Sahyogi. Created with ❤️ by Shalvi Rajpura