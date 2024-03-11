# Install Changeln from GitHub

This method is suitable for development.

### Create folder

```shell
mkdir -p ~/.local/opt/changeln
```

### Clone project

```shell
git clone https://github.com/keygenqt/changeln.git ~/.local/opt/changeln
```

### Open folder project

```shell
cd ~/.local/opt/changeln
```

### Init environment

```shell
virtualenv .venv
```

### Open environment

```shell
source .venv/bin/activate
```

### Install requirements

```shell
pip install -r requirements.txt
```

### Run app

```shell
python -m changeln
```
