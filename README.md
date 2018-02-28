# cyberwar-cli
CLI for rapid cyberwar building.

## Status: beta
Only basic features are in place and up to now the tool cannot do much help. There may still be many bugs.

## Installation
Very simple and no dependencies.
```sh
pip install git+https://github.com/princessV/cyberwar-cli.git
```
(Strongly recommend to use a virtual environment.)

## Quickstart
Strongly recommend to start from a clean directory within which are only Cyberwar-EDU and pypy sandbox, it will help you easily type the path when using this tool.

Just open terminal in this directory and type *cyberwar*.
```sh
cyberwar
# Follow the prompts!
```


## Notice
The tool will create a 'cyberwar' (you named it!) directory for your local game with all the necessary things. It will also create a directory for command & control system if you specify.

I also provide a quick-start script to init and launch the game. Config your *cwconfig.json* file and you can easily start the game.
```sh
python cw.py -m init # init the game
python cw.py -m launch # launch the game
```

The two files can be customized on your own interest.
## License
MIT