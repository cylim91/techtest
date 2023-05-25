### Description

This folder contains the answer for the second question.

#### Contents
* [Setup](#setup)
* [Endpoints](#endpoints)
* [Running Tests](#running-tests)
* [Extra](#extra)
---
### Setup

1. Install Python (preferably Python 3.11)
2. Install required libraries using the following command
   ```
   pip install -r requirements.txt
   ```
3. Run the following command to start server
   ```
    python manage.py runserver
    ```

---

### Endpoints

- `/rhm/generate_hash/`
- `/rhm/check_hash/`

---

### Running Tests

1. Run the following command to run test
   ```
    python manage.py test modules
    ```

---

#### Extra:

If you are using postman, you can import the collections with the `Q2 endpoints.postman_collection.json` file.