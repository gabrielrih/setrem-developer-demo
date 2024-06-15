Steps:
- Criar uma conta na AWS

- Criar um usuário e uma access key no usuário com acesso administrativo à AWS

- Criar arquivo de configuração da AWS para usar no TerraForm.
Também podemos usar ele para usar o aws cli.

mkdir /Users/usuario/.aws
cp credentials /Users/usuario/.aws/

```conf
[default]
aws_access_key_id=put my access key here
aws_secret_access_key=put my secret access key here
```

CÓDIGO
O código de exemplo é Flask e tem algumas APIS simples.
Para testar você pode executar:

- http://localhost:3000/github-user?username=gabrielrih
- http://localhost:3000/github-user-repos?username=gabrielrih


TERRAFORM
```sh
cd tf/dev
terraform init
terraform plan
terraform apply
```

> Utilizar o Registry público da AWS (evita o erro de pulling que dá no DockerHub)


TAREFA
- Novo endpoint que recebe um repositório no GitHub e salva uma mensagem no SQS
- Criar um novo microservico que escuta essa fila. Toda vez que encontra uma mensagem, ele clona o repositório e salva em um S3.
