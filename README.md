# Electrolux SDET Python Tech Challenge

## Overview

This project is a lightweight and maintainable API automation framework built using Python, pytest, and the requests library.

It automates the testing of the public JSONPlaceholder Posts API by validating important API functionality, including positive and negative scenarios.

---

## Tech Stack

- Python 3.13
- pytest
- requests

---

## Project Structure

```
.
├── api/
│   └── posts_api.py
├── config/
│   └── settings.py
├── tests/
│   └── test_posts_api.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Structure Explanation

- **api/** – Contains API interaction logic.
- **config/** – Stores project configuration such as the base URL.
- **tests/** – Contains all API test cases.
- **conftest.py** – Provides reusable pytest fixtures.
- **pytest.ini** – Pytest configuration.

---

## Test Coverage

Implemented scenarios include:

- Retrieve all posts
- Retrieve a post by ID
- Create a new post
- Verify behaviour for a non-existing post (negative test)

---

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd electrolux-sdet-python-challenge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Verbose execution:

```bash
pytest -v
```

---

## Design Decisions

- pytest was selected because of its concise syntax and powerful fixture mechanism.
- API communication is separated from test logic using a dedicated API client.
- Configuration is centralized in a separate settings module.
- A requests Session is used for connection reuse.
- The framework intentionally avoids unnecessary abstractions to keep the solution simple and maintainable.

---

## Future Improvements

- Logging
- Test reporting
- Environment-specific configuration
- Request/response logging
- Schema validation
- CI/CD integration