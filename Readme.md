# User CRUD Service

This is a simple CRUD service for managing users built with Flask. It allows you to create, read, update, and delete users via a REST API. The service also includes a single-page UI for performing CRUD operations.

## Project Structure

- `app.py` - Main Flask application with routes for CRUD operations.
- `user/`
  - Initialization file for the `user` module.
  - `data.py` - Contains the in-memory user data store.
  - `services.py` - Contains CRUD operations logic.
- `templates/`
  - `index.html` - HTML template for the single-page UI.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ibrahim-Akram/CrudPy.git
   cd CrudPy
