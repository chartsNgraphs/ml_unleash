import  os

def build_image():
    commands = ['FROM ubuntu:16.04', 
    "RUN apt-get update -y && apt-get install -y python-pip python-dev python-jinja2 python-flask", 
    "WORKDIR /app",
    "RUN pip install -r requirements.txt",
    "COPY . /app",
    'ENTRYPOINT [ "python" ]',
    'CMD [ "app.py" ]']

    with open("dockerfile", 'w') as f:
        f.writelines(commands)
    
    print(os.system("docker build -t flask-tutorial:latest ."))
