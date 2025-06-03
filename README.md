## Local development
This project is set up for local development with Docker. You can run the application in a containerized dev environment.

### Prerequisites
- Docker installed on your machine.
- Docker Compose installed.

### Running the Application
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Build and start the Docker container:
   ```bash
   docker-compose up --builddocker compose 
   ```
3. Access the application at `http://localhost:8000`.

## Adding dependencies
This project uses the `uv` package manager. To add new dependencies to the project, follow these steps:

1. Open a terminal in the project directory.
2. Add the dependency by executing:
    ```bash
    docker compose exec api uv add <package-name>
    ```