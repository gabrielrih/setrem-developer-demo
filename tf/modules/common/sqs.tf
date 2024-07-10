resource "aws_sqs_queue" "sqs_queue" {
    name = var.aws_sqs_queue_name
}
