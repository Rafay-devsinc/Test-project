# DevOps Assignment - CI + Kubernetes + Load Testing1111555

## Steps Implemented
1. **GitHub Actions Workflow** triggers on PR to `main`.
2. **KinD Multi-node Cluster** is provisioned inside the runner.
3. **NGINX Ingress Controller** deployed.
4. Two `http-echo` apps deployed (`foo`, `bar`).
5. Ingress routes `foo.localhost` → foo, `bar.localhost` → bar.
6. Load test executed with `hey`.
7. PR comment automatically posted with results.

## Requirements
- Go installed (`hey` tool used).
- Python 3 for posting PR comment.

## Time Taken
~4.5 hours (setup, debugging, docs).
