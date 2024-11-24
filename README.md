# Documentação da API

Certifique-se de estar no repositório PI-FBR-TURMA-19-GRUPO-1/back/ para executar os códigos.

![Imagem do WhatsApp de 2024-10-09 à(s) 21 17 51_d07905ab](https://github.com/user-attachments/assets/5acf7304-d28f-464f-ab3d-08d0eda5e22f)

## Iniciar o Servidor

Para iniciar o servidor Django, você pode executar o seguinte comando no terminal:

```bash

python manage.py runserver

```


## Fazendo Migrações

### Criar Migrações

Para criar novas migrações com base nas alterações feitas nos seus modelos, use o seguinte comando:

```bash

python manage.py makemigrations

```


### Aplicar as Migrações

Depois de criar as migrações, aplique-as ao banco de dados com:

```bash

python manage.py migrate

```


### Verificar o Status das Migrações (Opcional)

Para ver o status das migrações aplicadas e pendentes, você pode usar:

```bash

python manage.py showmigrations

```



## Outras Comandos Úteis



### Criar um Superusuário

Para criar um superusuário que terá acesso ao painel de administração, use:

```bash

python manage.py createsuperuser

```


## Iniciar um Shell Interativo do Django
### Para interagir com o seu projeto Django de forma interativa, execute:

```bash

python manage.py shell

```


## Coletar Arquivos Estáticos
### Se você estiver usando arquivos estáticos, pode coletá-los com:

```bash

    python manage.py collectstatic

```


## Considerações Finais

### Certifique-se de que o seu ambiente virtual está ativado antes de executar os comandos acima. Você pode ativá-lo com:

Para Windows:

```bash

venv\Scripts\activate

```

Para macOS e Linux:

```bash

source venv/bin/activate

```
