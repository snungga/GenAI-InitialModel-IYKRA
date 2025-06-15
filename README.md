Adding a timestamp for Cloud Build trigger test on Mon Jun 16 02:24:16 WIB 2025

# Generative AI CI/CD Deployment on GCP

## Overview
This project demonstrates automated deployment of a Generative AI model using CI/CD pipeline with Cloud Build and Google Kubernetes Engine.

## Architecture
- **Application**: Flask web app with GPT-2 model
- **Container**: Docker containerized application
- **Orchestration**: Kubernetes with LoadBalancer service
- **CI/CD**: Cloud Build automated pipeline
- **Monitoring**: Built-in health checks and HPA

## Deployment URL
- **Web Interface**: http://34.55.154.39
- **Health Check**: http://34.55.154.39/health
- **API Endpoint**: http://34.55.154.39/generate

!![Screenshot Aplikasi](Example_result.png)

```bash
## Setting V-env
python3.11 -m venv genai-env
source genai-env/bin/activate
pip install -r requirements.txt 
```

## Budget Alert
Budget alert configured for $50 with notifications at 50%, 90%, and 100% thresholds with only set up budgeting RP 200K.

## Repository Structure
📦GenAI-InitialModel-IYKRA
 ┣ 📂.git
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┣ 📜push-to-checkout.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂24
 ┃ ┃ ┃ ┗ 📜5f52586fa3afe1494039ef735499dd9b136a59
 ┃ ┃ ┣ 📂26
 ┃ ┃ ┃ ┗ 📜30412f42efb0ee88981b4108e49886f7f6bbe5
 ┃ ┃ ┣ 📂28
 ┃ ┃ ┃ ┗ 📜76aa693effe485b9968c6240a462bcf9f62d5d
 ┃ ┃ ┣ 📂2c
 ┃ ┃ ┃ ┗ 📜7ea9d3e2b172409ea6baed56d3635863987530
 ┃ ┃ ┣ 📂2f
 ┃ ┃ ┃ ┗ 📜c1df3eb579be73b369b12617d1def98b27ed03
 ┃ ┃ ┣ 📂31
 ┃ ┃ ┃ ┗ 📜70410d9c51cd31943f8f93d46045c8b7575cb7
 ┃ ┃ ┣ 📂3e
 ┃ ┃ ┃ ┗ 📜14052ebc6a3df40b2cb608b9062602ad5c92f3
 ┃ ┃ ┣ 📂40
 ┃ ┃ ┃ ┗ 📜f4ca062eb00c7ebd7f8e0da04f893c30c99217
 ┃ ┃ ┣ 📂56
 ┃ ┃ ┃ ┗ 📜a25418c66016ee5ed9e5ecb80018921babaa5d
 ┃ ┃ ┣ 📂60
 ┃ ┃ ┃ ┗ 📜18b741e5642b7e69d9ef37cdedeb26fd04c32f
 ┃ ┃ ┣ 📂63
 ┃ ┃ ┃ ┗ 📜24d6a070eb0f46e3ff59c3f47f0b52603db7b8
 ┃ ┃ ┣ 📂6c
 ┃ ┃ ┃ ┗ 📜dd8008b19c26183b6ec3adeb8b3f8ed61ce977
 ┃ ┃ ┣ 📂77
 ┃ ┃ ┃ ┗ 📜e8ed24b58237d58399f162edbeae424e9fcdb2
 ┃ ┃ ┣ 📂87
 ┃ ┃ ┃ ┗ 📜f0d076a7581e6efd7aa90c7aa7bb79d37ea15e
 ┃ ┃ ┣ 📂8e
 ┃ ┃ ┃ ┗ 📜1103993390d1f0a99960929ac1c650828b6773
 ┃ ┃ ┣ 📂90
 ┃ ┃ ┃ ┗ 📜e93ec3bd0e4388c1ce97680fc7db73009f8cee
 ┃ ┃ ┣ 📂99
 ┃ ┃ ┃ ┗ 📜1dccf1aee9df6ef43e0cca2f50e9f94f40716a
 ┃ ┃ ┣ 📂a4
 ┃ ┃ ┃ ┗ 📜3b0354da7862bbf2bbe1fea0ac142e3089791f
 ┃ ┃ ┣ 📂a6
 ┃ ┃ ┃ ┗ 📜f5f7e96d2417a9d83abb06ae260f036c2d1fe6
 ┃ ┃ ┣ 📂b8
 ┃ ┃ ┃ ┗ 📜62ea3c4574821da0430b4e9736b0a4220c02f9
 ┃ ┃ ┣ 📂f4
 ┃ ┃ ┃ ┗ 📜bcf7bccccdd2f3ced1a1ae48a35698ed19227f
 ┃ ┃ ┣ 📂fe
 ┃ ┃ ┃ ┗ 📜0e811cfac906d3ebc16bbf5738f5cd5511ca97
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜COMMIT_EDITMSG
 ┃ ┣ 📜HEAD
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┗ 📜index
 ┣ 📂kubernetes
 ┃ ┣ 📜deployment.yaml
 ┃ ┣ 📜hpa.yaml
 ┃ ┗ 📜service.yaml
 ┣ 📂manifests
 ┣ 📂src
 ┃ ┣ 📜app.py
 ┃ ┗ 📜model.py
 ┣ 📜.dockerignore
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜Example_result.png
 ┣ 📜README.md
 ┣ 📜cloudbuild.yaml
 ┗ 📜requirements.txt

## Setup Instructions
1. Clone repository
2. Setup GCP project and enable APIs
3. Create GKE cluster
4. Configure Cloud Build trigger
5. Deploy application
6. Access via external IP

## Monitoring
- Kubernetes health checks
- Horizontal Pod Autoscaler
- GCP monitoring and logging
