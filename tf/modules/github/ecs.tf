resource "aws_ecs_cluster" "github_api" {
  name = "github-api-cluster"
}

resource "aws_cloudwatch_log_group" "github_api" {
  name = "/ecs/service/github-api"
}

resource "aws_ecs_task_definition" "github_api" {
  family                   = "github-api-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.task_execution_role.arn
  task_role_arn            = aws_iam_role.task_execution_role.arn
  container_definitions    = <<DEFINITION
  [
    {
      "name": "github-api-task",
      "image": "${aws_ecr_repository.github_api.repository_url}:${var.github_api_version}",
      "essential": true,
      "memory": 512,
      "cpu": 256,
      "networkMode": "awsvpc",
      "taskRoleArn": "${aws_iam_role.task_execution_role.arn}",
      "executionRoleArn": "${aws_iam_role.task_execution_role.arn}",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "${aws_cloudwatch_log_group.github_api.name}",
          "awslogs-region": "${var.aws_region}",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "environment": [
        {
          "name": "GITHUB_API_VERSION",
          "value": "${var.github_api_version}"
        },
        {
          "name": "FLASK_PORT",
          "value": "${var.github_api_internal_port}"
        },
        {
          "name": "FORK_REPO_QUEUE_URL",
          "value": "${aws_sqs_queue.sqs_queue.id}"
        },
        {
          "name": "AWS_REGION",
          "value": "${var.aws_region}"
        }
      ],
      "portMappings": [
        {
          "containerPort": ${var.github_api_internal_port},
          "hostPort": ${var.github_api_internal_port}
        }
      ]
    }
  ]
  DEFINITION
}

resource "aws_security_group" "github_api_ecs_sg" {
    name = "ecs-sg"
    ingress {
        from_port = var.github_api_internal_port
        to_port = var.github_api_internal_port
        protocol = "tcp"
        security_groups = [ aws_security_group.load_balancer_sg.id ]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_ecs_service" "github_api" {
  name            = "github-api-service"
  cluster         = aws_ecs_cluster.github_api.id
  task_definition = aws_ecs_task_definition.github_api.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_default_subnet.default_a.id]
    security_groups  = [aws_security_group.github_api_ecs_sg.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.github_api_lb_tg.arn
    container_name   = aws_ecs_task_definition.github_api.family
    container_port   = var.github_api_internal_port
  }

  depends_on = [aws_lb_listener.github_api_lb_listener]
}
