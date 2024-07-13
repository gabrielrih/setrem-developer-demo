resource "aws_s3_bucket" "github_clone_lambda" {
  bucket = var.aws_s3_bucket_name
}