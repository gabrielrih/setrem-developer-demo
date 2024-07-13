resource "aws_lambda_function" "github_clone_lambda" {
    function_name = "clone_github_repo"
    filename = "${path.root}/../../microservices/tmp/github-clone-lambda.zip"
    handler = "lambda.handler"  # main file + main function
    runtime = "python3.11"
    memory_size = 512
    source_code_hash = filebase64sha256("${path.root}/../../microservices/tmp/github-clone-lambda.zip")
    ephemeral_storage {
      size = 512
    }
    environment {
      variables = {
        S3_BUCKET_NAME = aws_s3_bucket.github_clone_lambda.bucket
      }
    }
    role = aws_iam_role.github_clone_lambda.arn
    layers = [
        "arn:aws:lambda:${var.aws_region}:553035198032:layer:git-lambda2:8"
    ]
    timeout = 120
}

resource "aws_lambda_event_source_mapping" "github_clone_sqs_trigger" {
    event_source_arn = var.aws_sqs_queue_arn
    function_name = aws_lambda_function.github_clone_lambda.arn
    batch_size = 1
}

resource "aws_iam_role" "github_clone_lambda" {
    name = "github-clone-lambda-role"
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Principal = {
                    Service = "lambda.amazonaws.com"
                }
            }
        ]
    })
}

resource "aws_iam_role_policy" "github_clone_lambda" {
    name = "github-clone-lambda-policy"
    role = aws_iam_role.github_clone_lambda.id
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["s3:PutObject", "s3:GetObject"]
                Effect = "Allow"
                Resource = [
                    aws_s3_bucket.github_clone_lambda.arn,
                    "${aws_s3_bucket.github_clone_lambda.arn}/*"
                ]
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "github_clone_lambda_sqs" {
    role = aws_iam_role.github_clone_lambda.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole"
}

resource "aws_iam_role_policy_attachment" "github_clone_lambda_basic" {
    role = aws_iam_role.github_clone_lambda.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
