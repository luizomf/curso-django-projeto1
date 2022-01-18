# Deploy

Aqui estão os dados de referência para deploy de uma aplicação Django, de acordo
com as aulas do meu curso de Django na Udemy.

## Criando um servidor

Como vamos usar um servidor na nuvem (cloud server), é interessante que você
utilize algum serviço gratuito para isso. Recomendo a Google Cloud Platform.

Caso não tenha como usar a Google Cloud Platform, um servidor em máquina virtual
também funciona perfeitamente. Porém, não será possível disponibilizar a
aplicação online na Internet. VirtualBox (Windows, Linux e macOS intel),
Parallels (macOS M1), UTM (macOS M1), são alguns dos softwares mencionados
indicados para isso.

Siga as instruções da aula para criar um servidor na Google Cloud Platform.

### Chaves SSH

Para criar chaves ssh no seu computador, utilize o comando ssh-keygen. Se você
já tem chaves SSH no computador e por algum motivo queira usar outra, use o
comando:

```
ssh-keygen -t rsa -b 4096 -f CAMINHO+NOME_DA_CHAVE
```

Lembre-se que a pasta .ssh deve existir dentro da pasta do seu usuário para que
seja possível criar a chave SSH. Muito comum ocorrer erros no Windows por falta
dessa pasta.

Para conectar-se ao servidor usando uma chave SSH com caminho personalizado,
utilize:

```
ssh IP_OU_HOST -i CAMINHO+NOME_DA_CHAVE
```

### Ao entrar no servidor

A primeira coisa será atualizar tudo:

```
sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y
sudo apt install python3.9 python3.9-venv python3.9-dev -y
sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git
```

## Instalando o PostgreSQL

```
# Nós fizemos isso acima
sudo apt install postgresql postgresql-contrib -y
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

### Configurações

```
sudo -u postgres psql

# Criando um super usuário
CREATE ROLE usuario WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'senha';

# Criando a base de dados
CREATE DATABASE basededados WITH OWNER usuario;

# Dando permissões
GRANT ALL PRIVILEGES ON DATABASE basededados TO usuario;

# Saindo
\q

sudo systemctl restart postgresql
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

## Configurando o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
```
