resource "aws_cloudwatch_log_group" "github_clone" {
  name = "/ecs/service/github-clone"
}

resource "aws_ecs_task_definition" "github_clone" {
  family                   = "github-clone-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.task_execution_role.arn
  task_role_arn            = aws_iam_role.task_execution_role.arn
  container_definitions    = <<DEFINITION
  [
    {
      "name": "github-clone-task",
      "image": "${aws_ecr_repository.github_clone.repository_url}:${var.github_clone_version}",
      "essential": true,
      "memory": 512,
      "cpu": 256,
      "networkMode": "awsvpc",
      "taskRoleArn": "${aws_iam_role.task_execution_role.arn}",
      "executionRoleArn": "${aws_iam_role.task_execution_role.arn}",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "${aws_cloudwatch_log_group.github_clone.name}",
          "awslogs-region": "${var.aws_region}",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "environment": [
        {
          "name": "FORK_REPO_QUEUE_URL",
          "value": "${var.aws_sqs_queue_id}"
        },
        {
          "name": "S3_BUCKET_NAME",
          "value": "${var.aws_s3_bucket_name}"
        },
        {
          "name": "AWS_REGION",
          "value": "${var.aws_region}"
        }
      ],
      "portMappings": []
    }
  ]
  DEFINITION
}

resource "aws_security_group" "github_clone" {
    name = "ecs-github-clone-sg"
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_ecs_service" "github_clone" {
  name            = "github-clone-service"
  cluster         = var.aws_ecs_cluster_id
  task_definition = aws_ecs_task_definition.github_clone.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [var.aws_default_subnet_a_id]
    security_groups  = [aws_security_group.github_clone.id]
    assign_public_ip = true
  }
}
