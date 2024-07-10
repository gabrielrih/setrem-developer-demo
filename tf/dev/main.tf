provider "aws" {
    region = var.aws_region
}

module "common" {
    source = "../modules/common"
    aws_sqs_queue_name = var.common_aws_sqs_queue_name
}

# module "github-api" {
#     source = "../modules/github-api"
#     depends_on = [ module.common ]
#     github_api_version = var.github_api_version
#     aws_region = var.aws_region
#     aws_default_vpc_id = module.common.default_vpc_id
#     aws_default_subnet_a_id = module.common.default_subnet_a_id
#     aws_default_subnet_b_id = module.common.default_subnet_b_id
#     aws_sqs_queue_id = module.common.sqs_queue_id
#     aws_sqs_queue_arn = module.common.sqs_queue_arn
# }

module "github-clone" {
    source = "../modules/github-clone"
    depends_on = [ module.common ]
}
