# Rating System Microservice

This is a Flask microservice for managing a simple rating system through a REST API.

## Getting Started

To get started with the project, follow these instructions:

1. **Clone the repository:**

    ```bash
    git clone [<repository_url>](https://github.com/3ashryy2/Rating-Microservice/)
    cd rating_system
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app:**

    ```bash
    python run.py
    ```

    The app will start running on `http://127.0.0.1:5000/`.

## Usage

The following endpoints are available:

- `GET /ratings`: Get all ratings.
- `POST /ratings`: Add a new rating. Requires a JSON payload with `user_id` and `rating` fields.
- `GET /ratings/average`: Get the average rating.

