# Отримуємо дефолтний VPC (той, в якому в тебе вже RDS/EC2)
data "aws_vpc" "default" {
  default = true
}

# Отримуємо всі сабнети в цьому VPC
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# Security Group для ECS сервісу
resource "aws_security_group" "app" {
  name        = "${var.project_name}-ecs-sg"
  description = "Security group for ECS Fargate service"
  vpc_id      = data.aws_vpc.default.id

  # HTTP 8080 (прямий доступ до контейнера, якщо треба)
  ingress {
    description = "HTTP app port"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP 80 (для ALB)
  ingress {
    description = "HTTP via ALB"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# ECS кластер
resource "aws_ecs_cluster" "app" {
  name = "${var.project_name}-cluster"
}

# CloudWatch лог група для контейнера
resource "aws_cloudwatch_log_group" "app" {
  name              = "/ecs/${var.project_name}-app"
  retention_in_days = 7
}

# Трохи виводу, щоб було зручно дивитись
output "vpc_id" {
  description = "Default VPC id"
  value       = data.aws_vpc.default.id
}

output "subnet_ids" {
  description = "Subnet IDs for ECS service"
  value       = data.aws_subnets.default.ids
}

output "ecs_cluster_name" {
  description = "ECS cluster name"
  value       = aws_ecs_cluster.app.name
}

output "ecs_security_group_id" {
  description = "Security group ID for ECS service"
  value       = aws_security_group.app.id
}

