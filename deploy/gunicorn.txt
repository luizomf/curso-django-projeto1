###############################################################################
# Replace
# ___GUNICORN_FILE_NAME___ to the name of the gunicorn file you want
# __YOUR_USER__ to your user name
# __PROJECT_FOLDER__ to the folder name of your project
# __WSGI_FOLDER__ to the folder name where you find a file called wsgi.py
#
###############################################################################
# Criando o arquivo ___GUNICORN_FILE_NAME___.socket
sudo nano /etc/systemd/system/___GUNICORN_FILE_NAME___.socket

###############################################################################
# Conteúdo do arquivo
[Unit]
Description=gunicorn blog socket

[Socket]
ListenStream=/run/___GUNICORN_FILE_NAME___.socket

[Install]
WantedBy=sockets.target

###############################################################################
# Criando o arquivo ___GUNICORN_FILE_NAME___.service
sudo nano /etc/systemd/system/___GUNICORN_FILE_NAME___.service

###############################################################################
# Conteúdo do arquivo
[Unit]
Description=Gunicorn daemon (You can change if you want)
Requires=___GUNICORN_FILE_NAME___.socket
After=network.target

[Service]
User=__YOUR_USER__
Group=www-data
Restart=on-failure
EnvironmentFile=/home/__YOUR_USER__/__PROJECT_FOLDER__/.env
WorkingDirectory=/home/__YOUR_USER__/__PROJECT_FOLDER__
# --error-logfile --enable-stdio-inheritance --log-level and --capture-output
# are all for debugging purposes.
ExecStart=/home/__YOUR_USER__/__PROJECT_FOLDER__/venv/bin/gunicorn \
          --error-logfile /home/__YOUR_USER__/__PROJECT_FOLDER__/gunicorn-error-log \
          --enable-stdio-inheritance \
          --log-level "debug" \
          --capture-output \
          --access-logfile - \
          --workers 6 \
          --bind unix:/run/___GUNICORN_FILE_NAME___.socket \
          __WSGI_FOLDER__.wsgi:application

[Install]
WantedBy=multi-user.target

###############################################################################
# Ativando
sudo systemctl start ___GUNICORN_FILE_NAME___.socket
sudo systemctl enable ___GUNICORN_FILE_NAME___.socket

# Checando
sudo systemctl status ___GUNICORN_FILE_NAME___.socket
curl --unix-socket /run/___GUNICORN_FILE_NAME___.socket localhost
sudo systemctl status ___GUNICORN_FILE_NAME___

# Restarting
sudo systemctl restart ___GUNICORN_FILE_NAME___.service
sudo systemctl restart ___GUNICORN_FILE_NAME___.socket
sudo systemctl restart ___GUNICORN_FILE_NAME___

# After changing something
sudo systemctl daemon-reload

# Debugging
sudo journalctl -u ___GUNICORN_FILE_NAME___.service
sudo journalctl -u ___GUNICORN_FILE_NAME___.socket