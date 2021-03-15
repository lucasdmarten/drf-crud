<h1 align="center">Navedex Api</h1>
<p align="center"> Sistema desenvolvido para o teste proposto pela empresa <a href="https://github.com/naveteam">Nave</a>.</p>

<h3>💻 Sobre o projeto</h3>
<p>O sistema possui mecanismo de autenticação por email e senha que da acesso ao token individual de cada usuario cadastrado. Após o registro a api dará o acesso aos dados de Navers e Projetos onde é possível criar, listar, alterar e deletar cada objeto do banco de dados</p>

<h3>🔨 Tecnologias</h3>  
<p>As seguintes ferramentas foram usadas na construção do projeto:</p>
<ul>
  <li><a href="">Python</a></li>
  <li><a href="">Django</a></li>
  <li><a href="">MySQL</a></li>
  <li><a href="">Django Rest Framework</a></li>
</ul>

### Como configurar o banco de dados MySQL:
 ```bash
# Para instalar MySQL no Ubuntu
$ sudo apt install mysql-server
# Instalar MySQL Database Connector
$ sudo apt install python3-dev
$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
# Acessar terminal mysql
$ sudo mysql -u root
# Criar base de dados
mysql> CREATE DATABASE navedexAPI;
# Criar usuario
mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
# Garantir acesso ao usuario
mysql> GRANT ALL ON blog_data.* TO 'djangouser'@'%';
mysql> FLUSH PRIVILEGES;
 ```

### Conectar MySQL ao Django:
 ```bash
# Editar DATABASES no settings.py
$ nano ./root/settings.py

    ...
    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': './.env',
            },
        }
    }
    ...

# Criar arquivo no diretório base chamado .env
# Este arquivo irá conter as informações do banco de dados.
$ nano ./.env

    [client]
    database = navedexAPI
    user = djangouser
    password = password
    default-character-set = utf8    
```

 


### Como rodar este projeto:
 ```bash
 
 # Crie uma pasta
 $ mkdir navedexAPI
 # Entre na pasta
 $ cd navedexAPI
 # Crie um virtual environment
 $ python -m venv env
 # Para ativar
 $ source ./env/bin/activate
 # Clone o repositório 
 $ git clone git@github.com:lucasdmarten/navedexAPI.git
 # Instale todas as bibliotecas
 $ pip install -r requirements.txt
 # Entre na pasta do projeto
 $ cd navedexAPI
 # Migre o banco de dados
 $ python manage.py migrate
 # Runserver...
 $ python manage.py runserver
 ```
### Rota para cadastro:
<p>Registro de usuario:</p>

 ```bash
 http://localhost:8000/api/register/
 ```
### Rota para login:
<p>Aqui sera feito login com base no cadastro feito préviamente, e será liberado dois #tokens: refresh e access.</p>

 ```bash
 http://localhost:8000/api/login/
 ```


### Rota para criar, listar, alterar e deletar Navers
 ```bash
 http://localhost:8000/api/navers/
 ```

### Rota para filtrar um Naver pelo ID e criar, listar, alterar e deletar o Naver selecionado
 ```bash
 http://localhost:8000/api/navers/<int:id>
 ```

<br>

 <h2> Dificuldades </h2>
 <h3>Relação entre Naver e Projeto:</h3>
 <p>Neste projeto fiquei com muita dificuldade em fazer a relação correta entre Naver e Projeto. Usei o model User do próprio Django mas customizado com email obrigatório. A partir deste model foi criado o objeto Projeto que possui relação ManyToMany com o MyUser, ou seja, um usuario pode participar de N projetos e cada projeto possui relação com N usuarios. Posteriormente foi criado o objeto Naver que está relacionado com usuario a partir do campo OneToOneField e projetos a partir do campo ManyToManyField, assim um naver está ligado a apenas UM usuario e o naver pode estar ligado com varios projetos.</p>
 <p>Problema: Não consigo relacionar um Naver a um Projeto a partir do método POST, só na pagina de admin do Django.</p>
 