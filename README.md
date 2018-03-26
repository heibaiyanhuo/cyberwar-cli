# cyberwar-cli
CLI for rapid cyberwar building.

## Changelog

### 0.2.0 (Mar. 26, 2018)
- Feature add: the tool now can update the game when the Cyberwar-EDU updates.

### 0.1.0 (Feb. 28, 2018)
- Implementing quick installation for cyberwar.

## Environment
This CLI is based on Python 3. You should use a Python 3 virtual environment if the Python 2 is also installed on your system.

## Status: beta
Only basic features are in place and up to now the tool cannot do much help. There may still be many bugs.

## Installation
Very simple and no dependencies.
```sh
pip install git+https://github.com/princessV/cyberwar-cli.git
```
(Strongly recommend to use a virtual environment.)

## Instructions
Strongly recommend to start from a clean directory within which are only Cyberwar-EDU and pypy sandbox, it will help you easily type the path when using this tool.

Just open terminal in this directory and type *cyberwar* or *cyberwar init*:
```sh
cyberwar # or cyberwar init
# Follow the prompts!
```
If you've already created the game and want to update the game (e.g., the Cyberwar-EDU is updated). Type *cyberwar update*:
```sh
cyberwar update
# Follow the prompts!
```
You can use the relative path when you input the path. That's why staring from a clean directory within which are only Cyberwar-EDU and pypy sandbox is strongly recommended. Since the file path tab completion feature is not enabled, using relative path will be less painful.

## Notice
The tool will create a 'cyberwar' (you named it!) directory for your local game with all the necessary things. It will also create a directory for command & control system if you specify.

There is also a quick-start script to init and launch the game. Config your *cwconfig.json* file in your *cyberwar/* and you can easily start the game. The *cwconfig.json* is like 
```json
{
	"cywe_path": "/path/to/Cyberwar-EDU",
	"pypy_path": "/path/to/sandbox",
	"network": {
		"switch": {
			"host": "127.0.0.1",
			"port": ""
		},
		"vnic": {
			"playground_address": ""
		}
	}
}
```
The *cywe_path* and *pypy_path* will be automatically created when your create the game. Once you specify the TCP port of your switch and the playground address of your CC. You can easily use:
```sh
python cw.py -m init # init the game
python cw.py -m launch # launch the game
```
The two files can be customized on your own interest.

## License
MIT