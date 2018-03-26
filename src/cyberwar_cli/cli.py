import json
import os
import shutil
import sys

MY_PATH = os.path.abspath(__file__)[:-6]

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class CyWECLI():
    def __init__(self):
        super().__init__()
        self._arg_dict = {}
    
    def start(self):
        print(BColors.HEADER +  '\n This CLI helps your rapidly create your own game. \n' + BColors.ENDC)
        self.get_input('name', BColors.OKBLUE + 'Your cyberwar folder name:\n' + BColors.ENDC)
        self.get_input('cywe_path', BColors.OKBLUE + 'Your local CyWE path: (Don\'t use "~")\n' + BColors.ENDC)
        self.get_input('pypy_path', BColors.OKBLUE + 'Your local pypy path: (Don\'t use "~")\n' + BColors.ENDC)
        self.get_input('cc', BColors.OKBLUE + 'Your C&C folder name: (leave blank for not creating C&C)\n' + BColors.ENDC)
        self.write_config()
        self.processing()

    def processing(self):
        os.mkdir(self._arg_dict['name'])

        self.copy_files_from_cywe(self._arg_dict['cywe_path'], self._arg_dict['name'])
        
        os.system('cp {}/pypy/sandbox/libpypy3-c.so {}/'.format(self._arg_dict['pypy_path'], self._arg_dict['name']))
        os.system('cp {}/pypy/sandbox/pypy3-c-sandbox {}/'.format(self._arg_dict['pypy_path'], self._arg_dict['name']))

        os.system('cp {}cw.py {}/'.format(MY_PATH, self._arg_dict['name']))
        os.system('cp {}cwconfig.json {}/'.format(MY_PATH, self._arg_dict['name']))

        if len(self._arg_dict['cc']) > 0:
            os.mkdir('{}'.format(self._arg_dict['cc']))
            os.system('cp {}/python/bot/samples/command_and_control.py {}'.format(self._arg_dict['cywe_path'], self._arg_dict['cc']))
            os.system('cp {}/python/game/src/cyberwar/braininterface/translations.py {}'.format(self._arg_dict['cywe_path'], self._arg_dict['cc']))

        print(BColors.OKGREEN + 'Finished!' + BColors.ENDC)
    
    def update_game(self):
        cyberwar_path = input(BColors.OKBLUE + 'Your cyberwar path:\n' + BColors.ENDC)
        cywe_path = self.read_path_from_config()
        self.copy_files_from_cywe(cywe_path, cyberwar_path)
        print(BColors.OKGREEN + 'Updated!' + BColors.ENDC)

    def copy_files_from_cywe(self, cyberwar_path, cywe_path):
        os.system('cp {}/python/game/samples/simple_player_object_types.ini {}/'.format(cywe_path, cyberwar_path))
        os.system('cp {}/python/game/src/cyberwar/braininterface/translations.py {}/'.format(cywe_path, cyberwar_path))
        os.system('cp {}/python/game/pypy-sandbox/src/*.py {}/'.format(cywe_path, cyberwar_path))
        os.system('cp {}/python/bot/samples/*.py {}/'.format(cywe_path, cyberwar_path))
        os.system('mv {}/simple_player_object_types.ini {}/object_types.ini'.format(cyberwar_path, cyberwar_path))

    def write_config(self):
        config = None
        with open(MY_PATH + 'cwconfig.json', 'r') as f:
            config = json.load(f)

        config['cywe_path'] = os.path.abspath(self._arg_dict['cywe_path'])
        config['pypy_path'] = os.path.abspath(self._arg_dict['pypy_path'])
        with open(MY_PATH + 'cwconfig.json', 'w') as f:
            json.dump(config, f, indent='\t')

    def read_path_from_config(self):
        config = None
        with open(MY_PATH + 'cwconfig.json', 'r') as f:
            config = json.load(f)
        return config['cywe_path']

    def get_input(self, key, prompt):
        tmp = ''
        while True:
            tmp = input(prompt).strip()
            if key == 'name':
                if len(tmp) > 0:
                    break
                else:
                    prompt = BColors.WARNING + 'Please specify your folder name:\n' + BColors.ENDC
            elif key == 'cywe_path' or key == 'pypy_path':
                if os.path.exists(tmp):
                    break
                else:
                    prompt = BColors.FAIL + 'Path does not exist, input again:\n' + BColors.ENDC
            else:
                break
        self._arg_dict[key] = tmp

def main():
    cli = CyWECLI()
    if len(sys.argv) == 1 or sys.argv[1] == 'init':
        cli.start()
    elif sys.argv[1] == 'update':
        cli.update_game()
    else:
        print('Unknown command')

if __name__ == '__main__':
    main()
