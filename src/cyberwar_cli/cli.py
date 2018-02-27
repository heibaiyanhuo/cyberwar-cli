import json
import os
import shutil

MY_PATH = os.path.abspath(__file__)

class CyWECLI():
    def __init__(self):
        super().__init__()
        self._arg_dict = {}
    
    def start(self):
        print('\n This CLI helps your rapidly create your own game. \n')
        self.get_input('name', 'Your cyberwar folder name:\n')
        self.get_input('cywe_path', 'Your local CyWE path: (Don\'t use "~")\n')
        self.get_input('pypy_path', 'Your local pypy path: (Don\'t use "~")\n')
        self.get_input('cc', 'Your C&C folder name: (leave blank for not creating C&C)\n')
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

        os.system('cp cw.py {}/'.format(self._arg_dict['name']))
        os.system('cp cwconfig.json {}/'.format(self._arg_dict['name']))

        print('Finished!')
    
    def write_config(self):
        config = None
        config_path = os.path.join(MY_PATH, 'cwconfig.json')
        with open(config_path, 'r') as f:
            config = json.load(f)

        config['cywe_path'] = os.path.abspath(self._arg_dict['cywe_path'])
        config['pypy_path'] = os.path.abspath(self._arg_dict['pypy_path'])
        with open('cwconfig.json', 'w') as f:
            json.dump(config, f, indent='\t')

    def get_input(self, key, prompt):
        tmp = ''
        while True:
            tmp = input(prompt).strip()
            if key == 'name':
                if len(tmp) > 0:
                    break
                else:
                    prompt = 'Please specify your folder name:\n'
            elif key == 'cywe_path' or key == 'pypy_path':
                if os.path.exists(tmp):
                    break
                else:
                    prompt = 'Path does not exist, input again:\n'
            else:
                break
        self._arg_dict[key] = tmp

def main():
    cli = CyWECLI()
    cli.start()

if __name__ == '__main__':
    main()
