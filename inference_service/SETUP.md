# Inference Environment Setup

This guide provides instructions for setting up a containerized environment to run inference for both **Approach 1** (Multi-modal) and **Approach 2** (Temporal Sequence). We use Docker to ensure consistent dependency management across different Operating Systems and hardware configurations.

---

## 📋 Prerequisites

Before starting, ensure you have the following installed on your host machine:

1.  **Docker Desktop:** [Download for Windows/Mac/Linux](https://www.docker.com/products/docker-desktop/)
2.  **Visual Studio Code** (Recommended): For an integrated development experience [Download for Windows/Mac/Linux](https://code.visualstudio.com/download/).

---

## 1. Building the Container

You can spin up the inference environment using one of the two methods below:

### Method A: Visual Studio Code (Recommended)
1. Install the **Docker Extension** in VS Code.
2. Navigate to the `inference_service/` directory.
3. Right-click on `docker-compose.yaml` and select **Compose Up**.

### Method B: Command Line Interface (CLI)
Navigate to the root of the `inference_service` folder and execute:
```bash
docker-compose up -d --build
```

The -d flag runs the container in detached mode (background), and --build ensures the latest dependencies are compiled.

## 2. Running Inference

Once the service is active, you can execute the inference scripts for your chosen approach.

#### Step 1: Navigate to the approach folder

Depending on your research needs, enter one of the following directories:
- **Approach 1** :  [/single-line-analysis/inference/](/single-line-analysis/inference/)
- **Approach 2** :  [/temporal-sequence-analysis/inference/](/temporal-sequence-analysis/inference/)

#### Step 2: Execution
Once the environment is ready, you can run the inference pipeline.

**2.1**: Navigate to the specific approach's inference directory:
```bash
cd [approach-direcotry]/inference
```
**2.2**: Grant execution permissions to the shell script (required for Linux/macOS users):
```bash
chmod +x ./predict.sh
```

**2.3**: Run the inference script
```bash
bash predict.sh
```

## 3. Using Custom Data
To run predictions on your own OCT images:
- Prepare Data: Place your images/sequences into the respective data/ folder within the approach directory.
- Configure Script: Open predict.sh and update the input path variable to point to your new data location.
- Run: Re-execute the command in Step 2.

