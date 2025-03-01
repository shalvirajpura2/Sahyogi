# Sahyogi - Together We Serve

A platform that brings hearts together for social good. Sahyogi connects passionate volunteers with meaningful causes, creating a community of change-makers.

## 🌟 Features

### For Change-Makers (Volunteers)
- Discover meaningful opportunities to make a difference
- Simple and intuitive application process
- Track your volunteering journey
- Personalized impact dashboard
- Build your volunteering portfolio

### For Impact Leaders (Recruiters)
- Create and manage social impact initiatives
- Connect with dedicated volunteers
- Track community engagement
- Measure social impact
- Streamlined event management

### For Community Guardians (Administrators)
- Comprehensive community oversight
- Impact analytics and insights
- Platform governance
- Quality assurance
- Community safety management

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
├── accounts/                # Core application logic
│   ├── models.py           # Data models
│   ├── views.py            # View controllers
│   └── forms.py            # Form definitions
├── sahyogi/               # Main project settings
├── templates/             # HTML templates
│   ├── admin/            # Administrator interface
│   ├── volunteer/        # Volunteer dashboard
│   └── recruiter/        # Recruiter workspace
└── static/               # Static assets
```

## 💡 Key Features Implementation

- **Smart User System**: Tailored experiences for different user roles
- **Intuitive Access Control**: Role-specific permissions and views
- **Impact Tracking**: Complete management of social initiatives
- **Engagement System**: Streamlined volunteer-organization matching
- **Impact Analytics**: Measure and visualize social impact
- **Modern Interface**: Responsive design for all devices

## 🔐 Security Features

- Advanced CSRF Protection
- Secure Authentication System
- Role-based Authorization
- Data Validation
- Encrypted Password Management

## 🎨 UI Features

- Modern, Clean Design
- Intuitive Navigation
- Consistent Visual Language
- Accessibility-First Approach
- Interactive Elements
- Mobile-Optimized Interface

## 👥 Community Roles

1. **Change-Makers (Volunteers)**
   - Discover Opportunities
   - Contribute to Causes
   - Track Impact

2. **Impact Leaders (Recruiters)**
   - Create Initiatives
   - Manage Volunteers
   - Measure Success

3. **Community Guardians (Administrators)**
   - Oversee Platform
   - Ensure Quality
   - Support Users

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👩‍💻 Author

**Shalvi Rajpura**
- GitHub: [@shalvirajpura2](https://github.com/shalvirajpura2)

## 🙏 Acknowledgments

- Django Community
- Bootstrap Team
- Font Awesome
- Open Source Community

---
© 2025 Sahyogi - Connecting Hearts, Creating Impact ❤️ by Shalvi Rajpura