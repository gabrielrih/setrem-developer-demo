resource "aws_sqs_queue" "common" {
    name = var.aws_sqs_queue_name
    visibility_timeout_seconds = 120
}
