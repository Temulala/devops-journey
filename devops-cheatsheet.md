# Temu's DevOps Cheat Sheet 🚀

## Linux
```bash
pwd                          # where am I?
ls -la                       # list files with details
cd ~                         # go home
mkdir -p folder/subfolder    # create nested folders
cat file.txt                 # read file
head -5 file.txt             # first 5 lines
tail -5 file.txt             # last 5 lines
grep "word" file.txt         # search in file
chmod 600 file               # permissions (owner read/write only)
chmod 755 file               # permissions (owner all, others read/execute)
ps aux                       # see all processes
ps aux --sort=-%cpu          # sort by CPU usage
kill PID                     # stop a process
kill -9 PID                  # force stop
df -h                        # disk space
free -h                      # memory usage
ss -tuln                     # open ports
ping google.com              # test connectivity
curl -I https://google.com   # check HTTP response
```

## SSH
```bash
ssh -i ~/.ssh/key.pem ec2-user@IP    # connect to Amazon Linux
ssh -i ~/.ssh/key.pem ubuntu@IP      # connect to Ubuntu
chmod 600 ~/.ssh/key.pem             # fix key permissions
```

## Docker
```bash
docker build -t myapp:v1 .           # build image
docker run -d -p 8080:80 --name myapp myapp:v1  # run container
docker run -d -p 8080:80 \
  -v ~/myfolder:/container/path \
  --name myapp myapp:v1              # run with volume
docker ps                            # running containers
docker ps -a                         # all containers
docker images                        # downloaded images
docker start myapp                   # start stopped container
docker stop myapp                    # stop container
docker rm myapp                      # delete container
docker rmi myapp:v1                  # delete image
docker exec -it myapp bash           # go inside container
docker logs myapp                    # see container logs
```

## Docker Compose
```bash
docker compose up -d                 # start all containers
docker compose down                  # stop all containers
docker compose ps                    # see running containers
docker compose logs                  # see all logs
docker compose logs web              # logs for specific service
docker compose up -d --build         # rebuild and start
```

## Git
```bash
git init                             # initialize repo
git add .                            # stage all changes
git commit -m "message"              # commit
git push                             # push to GitHub
git pull                             # pull latest changes
git status                           # see changes
git log                              # see commit history
```

## AWS CLI
```bash
aws configure                        # set up credentials
aws s3 ls                            # list S3 buckets
aws s3 cp file.txt s3://bucket/      # upload to S3
aws ec2 describe-instances           # list EC2 instances
```

## Terraform
```bash
terraform init                       # initialize project
terraform plan                       # preview changes
terraform apply                      # create infrastructure
terraform destroy                    # delete infrastructure
```

## Key Concepts
- Image = blueprint (like ISO file)
- Container = running instance (like mounted ISO)
- Volume = persistent storage (like C++ pointer to file)
- EC2 = cloud server
- S3 = cloud storage (never store files on EC2)
- IAM = users and permissions (least privilege)
- Security Group = firewall (control which ports are open)
- Terraform = infrastructure as code (never click, always code)
- CI/CD = automated test, build, deploy on every push