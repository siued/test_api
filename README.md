## Local development
This project is set up for local development with Docker. You can run the application in a containerized dev environment.

### Prerequisites
- Docker installed on your machine.
- Docker Compose installed.

### Initial setup
1. Create a `.env` file in the root directory of the project and fill in the required environment variables. You can use the provided `.env.example` as a template:
   ```bash
   cp .env.example .env
   ```
2. Run Docker compose 

### Running the Application
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Build and start the Docker containers:
   ```bash
   docker compose up -d
   ```
3. Run the FastAPI applcation:
   ```bash
   uv run fastapi dev
   ```
4. Access the application at `http://localhost:8000`.

## Adding dependencies
This project uses the `uv` package manager. To add new dependencies to the project, follow these steps:

1. Open a terminal in the project directory.
2. Add the dependency by executing:
    ```bash
    docker compose exec api uv add <package-name>
    ```