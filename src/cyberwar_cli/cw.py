import argparse
import json
import os

CONFIG = None
MY_PATH = os.path.abspath(__file__)[:-5]

def processing():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mode', choices=['init', 'launch'], required=True)
    parser.add_argument('--host', default=CONFIG['network']['switch']['host'])
    parser.add_argument('-p', '--port', default=CONFIG['network']['switch']['port'])
    parser.add_argument('-a', '--playground-address', default=CONFIG['network']['vnic']['playground_address'])
    args = parser.parse_args()
    run(args)

def run(args):
    if args.mode == 'init':
        command = 'PYTHONPATH={}/python/game/src/ python -m cyberwar.game --init={},{},{}'.format(CONFIG['cywe_path'], args.host, args.port, args.playground_address)
        os.system(command)
    elif args.mode == 'launch':
        command = 'PYTHONPATH={}/python/game/src/ python -m cyberwar.game --pypy={}'.format(CONFIG['cywe_path'], CONFIG['pypy_path'])
        os.system(command)
        pass

if __name__ == '__main__':
    with open(MY_PATH + 'cwconfig.json', 'r') as f:
        CONFIG = json.load(f)
    processing()
