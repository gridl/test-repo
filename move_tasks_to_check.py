# -*- coding: utf-8 -*-

import os
import subprocess

default_path = 'exercises/'

chapter_to_folder_map = {
 1: '01_intro',
 2: '02_git_github',
 3: '03_start',
 4: '04_data_structures',
 5: '05_basic_scripts',
 6: '06_control_structures',
 7: '07_files',
 9: '09_functions',
 11: '11_modules',
 12: '12_useful_modules',
 15: '15_module_re',
 17: '17_serialization',
 18: '18_db',
 19: '19_ssh_telnet',
 20: '20_concurrent_connections',
 21: '21_jinja2',
 22: '22_textfsm',
 24: '24_ansible_for_network'}


def SyncError(Exception):
    pass


def call_command(command):
    result = subprocess.run(command, shell=True, encoding='utf-8',
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    return result


def get_chapter_to_folder_map(path):
    all_dirs = os.listdir(path)
    return {int(d.split('_')[0]): d for d in all_dirs if d[0].isdigit()}


def git_checkout(branch='master'):
    call_command('git checkout {}'.format(branch))


def git_pull():
    for i in range(2):
        result = call_command('git pull')
        if i==0:
            if 'Already up-to-date.' in result.stdout:
                return True
        else:
            if 'Already up-to-date.' not in result.stdout:
                raise SyncError
    return True


def copy_tasks_to_task_check(folder):
    call_command('git checkout master {}{}/'.format(default_path, folder))
    git_commands = ['git add .',
                    'git commit -m "Загрузила решения в ветку task_check"',]
                    #'git push origin task_check']

    for command in git_commands:
        result = call_command(command)
        #print(result.stdout)


def do_magic(folder):
    git_checkout('master')
    git_pull()
    git_checkout('task_check')
    copy_tasks_to_task_check(folder)



if __name__ == '__main__':
    do_magic(chapter_to_folder_map[17])
