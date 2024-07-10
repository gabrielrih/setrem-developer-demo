resource "aws_security_group" "load_balancer_sg" {
    name = "load-balancer-sg"
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_lb" "github_api_lb" {
    name = "github-api-lb"
    load_balancer_type = "application"
    subnets = [var.aws_default_subnet_a_id, var.aws_default_subnet_b_id]
    security_groups = [aws_security_group.load_balancer_sg.id]
}

resource "aws_lb_target_group" "github_api_lb_tg" {
    port = var.github_api_internal_port
    protocol = "HTTP"
    target_type = "ip"
    vpc_id = var.aws_default_vpc_id
    health_check {
        enabled = true
        path = "/_health"
        matcher = 200
        interval = 5
        timeout = 2
        healthy_threshold = 2
        unhealthy_threshold = 2
    }
}

resource "aws_lb_listener" "github_api_lb_listener" {
    load_balancer_arn = aws_lb.github_api_lb.arn
    port = 80
    protocol = "HTTP"
    default_action {
      target_group_arn = aws_lb_target_group.github_api_lb_tg.arn
      type = "forward"
    }
}
