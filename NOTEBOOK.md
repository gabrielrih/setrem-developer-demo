Repo to use as data:
```
https://github.com/golang/go.git
https://github.com/python/cpython.git
https://github.com/strapi/strapi.git
```

Popular o S3 com estes repositórios.

```json
{
    "repo_url": "https://github.com/golang/go.git",
    "extension": ".go"
}
```

```json
{
    "repo_url": "https://github.com/python/cpython.git",
    "extension": ".py"
}
```

```json
{
    "repo_url": "https://github.com/strapi/strapi.git",
    "extension": ".ts"
}
```


## References
- https://tree-sitter.github.io/tree-sitter/
- https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#kmeans



## Ideia de projeto
Posso treinar o modelo na máquina local, usar a biblioteca pickle para enviar o modelo treinado para o S3. E aí no lambda eu posso pegar esse modelo e usar.

Outra opção é já passar esse cara no ZIP, junto com o código da Lambda function. Assim não precisa nem do overhead de baixar no S3.
