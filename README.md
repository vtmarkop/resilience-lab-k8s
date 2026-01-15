# 🛡️ Resilience Lab: Kubernetes Chaos Engineering

![Build Status](https://github.com/YOUR_USERNAME_HERE/resilience-lab-k8s/actions/workflows/build-check.yml/badge.svg)

## 📋 Project Overview
A specialized demonstration of **Chaos Engineering** principles applied to a microservices architecture. This project uses **Chaos Mesh** to inject network failures into a Kubernetes cluster to validate system behavior under stress.

## 🛠️ Technology Stack
| Category | Tool | Usage |
| :--- | :--- | :--- |
| **Orchestration** | Kubernetes (K8s) | Application hosting |
| **Chaos** | Chaos Mesh | Fault injection (Network Latency) |
| **App** | Python (Flask) | REST API simulation |
| **CI/CD** | GitHub Actions | Build verification |

## 🧪 The Experiment: Network Latency
**Goal:** Verify that the application API degrades gracefully when database latency spikes.

1. **Steady State:** API returns JSON in <50ms.
2. **Hypothesis:** If network latency increases by 250ms, the service should remain available (HTTP 200) but with increased response time.
3. **Injection:** Applied `experiments/network-delay.yaml`.
4. **Observation:** - Before Chaos: `42ms` average.
   - During Chaos: `295ms` average.
   - Errors: 0% (Success - Resilience Confirmed).

## 🚀 How to Run (Locally)
1. **Prerequisite:** Ensure `minikube` and `kubectl` are installed.
2. **Deploy App:**
   ```bash
   kubectl apply -f k8s/
   ```
3. **Inject Chaos:**
   ```bash
   kubectl apply -f experiments/network-delay.yaml
   ```

## 📂 Repository Structure
- `/app`: The target microservice code.
- `/k8s`: Manifests for Deployment and Service.
- `/experiments`: YAML configurations for Chaos Mesh.
- `.github`: CI/CD pipelines.
