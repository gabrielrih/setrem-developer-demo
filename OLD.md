## Passos para configuração inicial:
- Criar uma conta na AWS

- Criar um usuário e uma access key no usuário com acesso administrativo à AWS

- Criar arquivo de configuração da AWS para usar no TerraForm.
Também podemos usar ele para usar o aws cli.

```sh
mkdir /Users/usuario/.aws
cp credentials /Users/usuario/.aws/
```

O arquivo de configuração será algo parecido com isso:
```conf
[default]
aws_access_key_id=put my access key here
aws_secret_access_key=put my secret access key here
```

## Código
O código de exemplo é Flask e tem algumas APIS simples.
Para testar você pode executar:

- http://localhost:3000/github-user?username=gabrielrih
- http://localhost:3000/github-user-repos?username=gabrielrih
- http://localhost:3000/clone-repo?repo_url=https://github.com/gabrielrih/MSSQL_Management_Queries.git


## Terraform

Dependências pra rodar o TF: ter o docker na máquina
```sh
cd tf/dev
terraform init
terraform plan
terraform apply
```

> Utilizar o Registry público da AWS (evita o erro de pulling que dá no DockerHub)
