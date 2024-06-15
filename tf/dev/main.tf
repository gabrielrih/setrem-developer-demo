provider "aws" {
    region = var.aws_region
}

module "github" {
    source = "../modules/github"
    github_api_version = var.github_api_version
    aws_region = var.aws_region
}
