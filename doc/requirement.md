# ✅ Library Management System Checklist

## 1. Project Setup
- [*] Initialize Django project and app
- [*] Configure settings for PostgreSQL
- [ ] Create `.env` file for secrets and DB credentials
- [*] Set up Git repository

## 2. User Management
- [*] Extend Django `User` model with custom `User` model (e.g. role field: anonymous, registered, admin)
- [*] Enable user registration and login APIs
- [*] Implement JWT authentication (e.g. with `SimpleJWT`)
- [ ] Apply authentication/authorization on protected routes

## 3. Database Models
- [*] **User** model with roles
- [*] **Book** model:
  - [*] Title
  - [*] Author
  - [*] ISBN
  - [*] Page count
  - [*] Availability status
- [*] **Loan** model:
  - [ ] ForeignKey to User
  - [ ] ForeignKey to Book
  - [ ] Borrow date
  - [ ] Return date (nullable)
  - [ ] Is returned

## 4. API Endpoints

### General
- [*] Book list (available to everyone)

### Authenticated User
- [ ] Borrow book
- [ ] Return book

### Admin Only
- [ ] Add new book
- [ ] Remove book
- [ ] Manage users (optional)

## 5. Admin Panel
- [ ] Customize Django admin for:
  - [ ] Book model
  - [ ] Loan model
  - [ ] User model (with filters for role, etc.)

## 6. API Features
- [ ] Pagination (e.g. DRF's `PageNumberPagination`)
- [ ] Filtering (e.g. by title, author, availability)
- [ ] Permissions (IsAdminUser, IsAuthenticated, etc.)

## 7. Security
- [ ] CSRF protection (where needed)
- [ ] Input validation to prevent SQL Injection
- [ ] Escape output in templates to prevent XSS

## 8. Testing

### Unit Tests
- [ ] Models
- [ ] Serializers
- [ ] Views

### Integration Tests
- [ ] Register + Login flow
- [ ] Borrow/Return book flow
- [ ] Permissions check for various roles

### Coverage
- [ ] Ensure test coverage report using `coverage.py`

## 9. Documentation
- [ ] Swagger/OpenAPI via `drf-yasg`
- [ ] Auto-generated API documentation available at `/swagger/`
- [ ] README file including:
  - [ ] Project description
  - [ ] Setup instructions
  - [ ] How to run locally
  - [ ] Deployment steps

## 10. Deployment
- [ ] Dockerize the application
  - [ ] `Dockerfile`
  - [ ] `docker-compose.yml` for local setup (optional)
- [ ] Configure environment for production (e.g. `DEBUG=False`)
- [ ] Deploy to Heroku (or alternative)
  - [ ] Add `Procfile`
  - [ ] Set up Heroku PostgreSQL
  - [ ] Configure allowed hosts and static files

## 11. Bonus (Optional but Valuable)
- [ ] Implement Book reservation feature (queue system)
- [ ] Add email notifications for due dates
- [ ] Role-based dashboard for users vs admins
- [ ] Audit log for book borrow/return actions
