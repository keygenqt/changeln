# Install Changeln *.pyz

This method is as simple as possible - the entire application is in a pyz file.

### Create folder

```shell
mkdir ~/.local/opt
```

### Download

```shell
wget -x https://github.com/keygenqt/changeln/raw/main/builds/changeln-2.0.1.pyz \
  -O ~/.local/opt/changeln.pyz
```

### Add alias to `~/.bashrc`

```shell
alias changeln='python3 ~/.local/opt/changeln.pyz'
```

### Update environment

```shell
source ~/.bashrc
```
