# 📝 BlogSphere — Full-Stack Blog Platform

A feature-rich blogging platform built with **Django**, supporting multi-user authentication, a full admin dashboard, blog post management, category filtering, commenting, and dynamic social links — all backed by a clean MVT (Model-View-Template) architecture.

---

## 🚀 Features

### Public-Facing Site

- 🏠 **Homepage** — Showcases featured and latest published blog posts
- 📖 **Blog Detail Page** — Full post view with a comment section (authenticated users)
- 🗂️ **Category Filtering** — Browse posts by category
- 🔍 **Search** — Full-text search across title, description, and body
- 👤 **About Section** — Dynamically managed "About Us" content
- 🔗 **Social Links** — Dynamic social media links rendered site-wide via context processors

### User Authentication

- 📝 **Register** — New user sign-up with Django form validation
- 🔐 **Login / Logout** — Session-based authentication using Django's `AuthenticationForm`
- 🛡️ **Protected Routes** — Dashboard requires login (`@login_required` decorator)

### Admin Dashboard

- 📊 **Dashboard Overview** — At-a-glance count of categories and total blog posts
- ✍️ **Post Management** — Create, Read, Update, Delete (CRUD) for blog posts
  - Auto-generates SEO-friendly slugs on save
  - Draft / Published status control
  - Featured post toggle
  - Image upload with date-based directory organization
- 🗃️ **Category Management** — Full CRUD for blog categories
- 👥 **User Management** — Add, edit, and delete users directly from the dashboard

---

## 🛠️ Tech Stack

| Layer       | Technology                          |
| ----------- | ----------------------------------- |
| Backend     | Python, Django 6.x                  |
| Database    | SQLite3 (development)               |
| Frontend    | HTML5, Bootstrap 4, Crispy Forms    |
| Auth        | Django built-in authentication      |
| Media Files | Django `ImageField` + Media storage |
| Forms       | Django Forms + `crispy-forms`       |

---

## 📁 Project Structure

```
blog_main/           # Core Django project (settings, URLs, auth views)
│
blogs/               # Blog app
│   ├── models.py    # Category, Blog, Comment models
│   ├── views.py     # Blog detail, category filter, search
│   └── context_processors.py  # Global categories & social links
│
dashboards/          # Admin dashboard app
│   ├── views.py     # Full CRUD for posts, categories, users
│   └── forms.py     # BlogPostForm, CategoryForm, AddUserForm, EditUserForm
│
assignments/         # Site content app
│   └── models.py    # About & SocialLink models
│
templates/           # All HTML templates
│   ├── base.html
│   ├── home.html
│   ├── blogs.html
│   ├── search.html
│   └── dashboard/   # All dashboard templates
│
media/               # Uploaded blog images (auto-organized by date)
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sakshamiishra/BlogSphere.git
cd BlogSphere

# 2. Create and activate a virtual environment
python -m venv env
env\Scripts\activate        # Windows
# source env/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for the dashboard)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Open your browser and navigate to **http://127.0.0.1:8000/**

---

## 🌐 Key Pages

| Page              | URL                       |
| ----------------- | ------------------------- |
| Home              | `/`                       |
| Blog Detail       | `/blogs/<slug>/`          |
| Category Posts    | `/post-by-category/<id>/` |
| Search            | `/search/?keyword=...`    |
| Dashboard         | `/dashboard/`             |
| Manage Posts      | `/dashboard/posts/`       |
| Manage Categories | `/dashboard/categories/`  |
| Manage Users      | `/dashboard/users/`       |
| Register          | `/register/`              |
| Login             | `/login/`                 |

---

## 🧠 Key Concepts Demonstrated

- ✅ Django **MVT (Model-View-Template)** architecture
- ✅ **ORM queries** — filtering, foreign keys, Q objects for OR-based search
- ✅ **Function-based views** for all app logic
- ✅ **Django Forms** with validation and `commit=False` pattern
- ✅ Auto **slug generation** using `slugify`
- ✅ **Context processors** for site-wide data injection
- ✅ **`@login_required`** decorator for route protection
- ✅ **Media file uploads** with organized directory structure
- ✅ **Django Admin** customization
