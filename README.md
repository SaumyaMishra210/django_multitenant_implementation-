# Django Multi-Tenant Implementation with JWT Authentication

## Overview
This project implements a **multi-tenant architecture** in Django using **django-tenants**. It supports:
- Separate schemas for each tenant in a **single database**.
- A **shared authentication system** across all tenants using **JWT authentication**.
- CRUD operations on **Author** and **Book** models, ensuring data isolation per tenant.

---

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- Django (>=5.1)
- Django-Tenants
- Django REST Framework
- Simple JWT for authentication

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/SaumyaMishra210/django_multitenant_implementation-.git
cd django_multitenant_implementation-
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database
Ensure PostgreSQL is running and create a new database:
```sql
CREATE DATABASE new_multi_tenant;
```

### 3. Configure PostgreSQL Database
Create a new PostgreSQL database and update `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'new_multi_tenant',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=public'
        }
    }
}
```
Update your `settings.py` file with the correct **database credentials**.

---

## Setting Up Multi-Tenant Structure
### 1. Apply Migrations in Sequence

```bash
python manage.py migrate --schema=public  # Step 2: Setup public schema (shared apps)
python manage.py migrate auth --schema=public  # Step 3: Migrate auth-related apps in public
python manage.py migrate token_blacklist --schema=public

```


---

## Creating Tenants
### 1. Create the Public Tenant
The **public tenant** stores shared data like authentication and tenant details.
Run the following script in the Django shell:
```bash
python manage.py shell
```
```python
from tenants.models import Tenant, Domain

# Create the public tenant
public_tenant = Tenant(schema_name='public', name='Public Tenant')
public_tenant.save()

# Assign domain to the public tenant
public_domain = Domain(domain='127.0.0.1', tenant=public_tenant)
public_domain.save()
```

### 2. Create Other Tenants
```python
# Create Tenant 1
tenant1 = Tenant(schema_name='tenant1', name='Tenant 1')
tenant1.save()

tenant1_domain = Domain(domain='tenant1.example.com', tenant=tenant1)
tenant1_domain.save()

# Create Tenant 2
tenant2 = Tenant(schema_name='tenant2', name='Tenant 2')
tenant2.save()

tenant2_domain = Domain(domain='tenant2.example.com', tenant=tenant2)
tenant2_domain.save()
```

---
## Make migrations of Tenants
```bash
python manage.py migrate app1 --schema=tenant1  # Step 4: Migrate tenant-specific apps
python manage.py migrate app1 --schema=tenant2  # Step 5: Repeat for all tenants
```

## Running the Server
To start the development server:
```bash
python manage.py runserver
```
By default, it runs on `http://127.0.0.1:8000/`.

Access tenants by visiting:
- **Public**: http://127.0.0.1:8000/
- **Tenant 1**: http://tenant1.example.com
- **Tenant 2**: http://tenant2.example.com

Use **hosts file** or a custom local DNS resolver to map domains.

---

## Authentication Endpoints (JWT)

### 8. API Endpoints for Authentication
| Endpoint            | Method | Description |
|---------------------|--------|-------------|
| `/auth/login/`      | `POST` | Login and get JWT tokens |
| `/auth/signup/`     | `POST` | Register a new user |
| `/auth/logout/`     | `POST` | Logout and blacklist refresh token |
| `/auth/token/refresh/` | `POST` | Get new access token using refresh token |

#### Example Login Request
```sh
POST /auth/login/
{
    "username": "testuser",
    "password": "testpass"
}
```

#### Example Logout Request
```sh
POST /auth/logout/
{
    "refresh": "your_refresh_token"
}
```

---
## API Endpoints

### **Author Endpoints**
- `GET /api/authors/` - List all authors (tenant-specific)
- `POST /api/authors/` - Create a new author
- `GET /api/authors/{id}/` - Retrieve an author
- `PUT /api/authors/{id}/` - Update an author
- `DELETE /api/authors/{id}/` - Delete an author

### **Book Endpoints**
- `GET /api/books/` - List all books (tenant-specific)
- `POST /api/books/` - Create a new book
- `GET /api/books/{id}/` - Retrieve a book
- `PUT /api/books/{id}/` - Update a book
- `DELETE /api/books/{id}/` - Delete a book

---

## Testing Multi-Tenant Functionality
1. **Login** using JWT to get access tokens.
2. Use `TenantMainMiddleware` to switch between tenants dynamically.
3. Ensure that **data is only saved in the respective tenant schema**.
4. Check the database to verify **data isolation per tenant**.

---

## Troubleshooting
**Issue:** "No tenant for hostname 127.0.0.1"
- Ensure your **public tenant and domain** are correctly created.
- Run `python manage.py shell` and verify:
  ```python
  from tenants.models import Domain
  print(Domain.objects.all())
  ```

**Issue:** Data is being saved in both tenants
- Ensure `schema_context(self.request.tenant.schema_name)` is properly used in views.
- Check `DATABASE_ROUTERS` in `settings.py`.

**Issue:** Logout does not invalidate the token
- Ensure `rest_framework_simplejwt.token_blacklist` is added to `INSTALLED_APPS`.
- Run `python manage.py migrate token_blacklist`.

---

## Contributing
Feel free to fork the repository and submit pull requests.

---
