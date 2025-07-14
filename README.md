# assignment
Design Decisions
Language & Framework: Built using Python + FastAPI for fast development, automatic docs, and easy Dockerization.

External API: Uses exchangerate.host for free, reliable real-time exchange rates.

Architecture:

REST endpoint: /convert?from=USD&to=EUR&amount=100

Frontend: Lightweight HTML+JS served by FastAPI to keep UI minimal.

Containerization: Alpine-based Docker image with non-root user for security.

Infrastructure: Helm for Kubernetes deployment; Terraform provisions EKS cluster and supports GitOps deployment.

CI/CD: GitHub Actions builds and pushes Docker image to Docker Hub, then deploys via Helm on EKS.

Run Locally (Docker)
bash
Copy
Edit
# Build Docker image
docker build -t currency-converter:latest .

# Run container
docker run -d \
  --name currency-converter \
  -p 8000:8000 \
  currency-converter:latest

# Access the UI
# Visit http://localhost:8000 in your browser

**Provision Infrastructure (Terraform)**

Fork this repo under the repo secrets Add values to the secrets AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY
cd terraform

# Initialize working directory
terraform init

# Preview changes
terraform plan 

# Create infrastructure and deploy chart
terraform apply 

Creates EKS cluster, IAM roles, and executes Helm deployment post-cluster creation.

**CI/CD Pipeline (GitHub Actions)**
The workflow ./github/workflows/pipeline.yml performs:

Checkout code

Build Docker image

Push to Docker Hub (requires DOCKERHUB_USERNAME, DOCKERHUB_TOKEN i have added my docker credentials as secret)

****Triggering Pipeline:
****
Push to main branch

OR create a pull request against main

You can monitor progress via the Actions tab in GitHub.


├── dockerfile                  # Container setup (alpine, non-root)
├── app/                        # FastAPI service + frontend
│   └── main.py
├── helm/
│   └── currency-converter/    
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/
│   └── workflows/
│       └── pipeline.yml       # CI/CD pipeline file
└── README.md                 
