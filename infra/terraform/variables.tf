variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "aws_profile" {
  description = "AWS CLI profile name (optional)"
  type        = string
  default     = ""
}

variable "project_name" {
  description = "Base name for all resources"
  type        = string
  default     = "database-lab"
}

variable "db_host" {
  description = "RDS endpoint host"
  type        = string
}

variable "db_name" {
  description = "Database name"
  type        = string
}

variable "mysql_root_user" {
  description = "MySQL user"
  type        = string
}

variable "mysql_root_password" {
  description = "MySQL password"
  type        = string
  sensitive   = true
}

variable "jwt_secret" {
  description = "JWT secret"
  type        = string
  sensitive   = true
}
