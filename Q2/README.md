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
- `/rhm/get_odd_hash/`
- `/rhm/get_optimized_odd_hash/`

---

### Running Tests

1. Run the following command to run test
   ```
    python manage.py test modules
    ```

---

#### Extra:

If you are using postman, you can import the collections with the `Q2 endpoints.postman_collection.json` file.

#### Note: 

For question 4 `Optional: Please investigate if there is anyway to increase the performance of the RHM if possible.`

I've created a `get_optimized_odd_hash`, which uses multithreading to increase the performance of the RHM. To optimize it, i've created 4 workers and calling the endpoint 1 4 times in parallel, increasing the chances of getting an odd hash. By doing so, it would not need to wait for the previous call to finish before calling the next one.
