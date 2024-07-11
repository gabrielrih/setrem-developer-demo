resource "null_resource" "push_github_api" {
    depends_on = [ aws_ecr_repository.github_clone ]

    provisioner "local-exec" {
        command = "docker build -t github-clone:${var.github_clone_version} ${path.root}/../../microservices/github-clone/"
    }

    provisioner "local-exec" {
        command = "docker tag github-clone:${var.github_clone_version} ${aws_ecr_repository.github_clone.repository_url}:${var.github_clone_version}"
    }

    provisioner "local-exec" {
        command = "aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${aws_ecr_repository.github_clone.repository_url}"
    }

    provisioner "local-exec" {
        command = "docker push ${aws_ecr_repository.github_clone.repository_url}:${var.github_clone_version}"
    }

    triggers = {
      version = var.github_clone_version
    }
}
