#### Overview
This project implements a microservices architecture for a tax payment system using Flask and Docker. The system is divided into the following services:
- **Tax Calculation Service**: Handles all tax calculation logic.
- **Payment Record Service**: Manages payment transactions and records.
- **Reporting Service**: Generates reports based on user and transaction data.
- **Nginx**: Used as a reverse proxy and load balancer to route requests to the appropriate services.

Each service is containerized with its own Dockerfile, making the system easy to deploy and scale.

#### Prerequisites
- Docker
- Docker Compose

#### Installation & Running Instructions
1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd repository-name
   ```

2. **Build the services:**
   ```bash
   docker-compose build
   ```

3. **Run the services:**
   ```bash
   docker-compose up -d
   ```

4. **Access the application:**
    - Access the main gateway via `http://localhost:8000`
    - Access individual services via their respective ports as configured in `docker-compose.yml`.
    - For example To access Reporting service try `http://localhost:8002/reporting/`

5. **Shut down the services:**
   ```bash
   docker-compose down
   ```

#### Configuration
- Environment variables and other configurations specific to each service can be found and modified in the respective `Dockerfile` and service directory.
