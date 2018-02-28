import json
import os
import shutil

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
        os.system('cp {}/python/game/samples/simple_player_object_types.ini {}/'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}/python/game/src/cyberwar/braininterface/translations.py {}/'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}/python/game/pypy-sandbox/src/*.py {}/'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}/python/bot/samples/*.py {}/'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))

        os.system('cp {}/pypy/sandbox/libpypy3-c.so {}/'.format(self._arg_dict['pypy_path'], self._arg_dict['name']))
        os.system('cp {}/pypy/sandbox/pypy3-c-sandbox {}/'.format(self._arg_dict['pypy_path'], self._arg_dict['name']))

        os.system('mv {}/simple_player_object_types.ini {}/object_types.ini'.format(self._arg_dict['name'], self._arg_dict['name']))

        os.system('cp {}cw.py {}/'.format(MY_PATH, self._arg_dict['name']))
        os.system('cp {}cwconfig.json {}/'.format(MY_PATH, self._arg_dict['name']))

        if len(self._arg_dict['cc']) > 0:
            os.mkdir('{}/{}'.format(self._arg_dict['name'], self._arg_dict['cc']))
            os.system('cp {}/python/bot/samples/command_and_control.py {}/{}'.format(self._arg_dict['cywe_path'], self._arg_dict['name'], self._arg_dict['cc']))
            os.system('cp {}/python/game/src/cyberwar/braininterface/translations.py {}/{}'.format(self._arg_dict['cywe_path'], self._arg_dict['name'], self._arg_dict['cc']))

        print(BColors.OKGREEN + 'Finished!' + BColors.ENDC)
    
    def write_config(self):
        config = None
        with open(MY_PATH + 'cwconfig.json', 'r') as f:
            config = json.load(f)

        config['cywe_path'] = os.path.abspath(self._arg_dict['cywe_path'])
        config['pypy_path'] = os.path.abspath(self._arg_dict['pypy_path'])
        with open(MY_PATH + 'cwconfig.json', 'w') as f:
            json.dump(config, f, indent='\t')

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
    cli.start()

if __name__ == '__main__':
    main()
