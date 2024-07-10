resource "aws_s3_bucket" "github_clone" {
  bucket = var.aws_s3_bucket_name
}