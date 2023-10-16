import os
import datetime
import glob
import subprocess
import uuid


TAG_CENTER_PATH = r'C:\Users\ps\Desktop\TagCenter'


def add_info(file_name='README', info = ''):

    if not '.md' in file_name:
        file_name = file_name+'.md'

    # Create new readme file
    if not os.path.exists(f'./{file_name}'):
        file_name = f'./{file_name}'
    else:
        file_name = os.path.splitext(file_name)[0]
        file_name = f'./{file_name}_NEW.md'

    with open(file_name, 'w') as f:
        f.write('## Note\n')
        f.write(info+'\n')


def open_program(application, file_path):
    # Open the file using the specified application
    subprocess.run([application, file_path])


def run_command(command):
    # Run the command in the shell
    subprocess.run(command)


def main():
    date_str_minutes = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    # print(date_str_minutes)
    # date_str_seconds = datetime.datetime.now().strftime('%Y%m%d%H%M_%S')
    # print(date_str_seconds)
    batch_tag = f'{date_str_minutes}_{uuid.uuid1()}'


    batch_name = f'BATCH_TAG_{batch_tag}'
    batch_folder_name = f'Batch_{batch_tag}'
    # if os.path.exists(f'./{batch_name}'):
        # file_list = glob.glob(f'./Batch_{date_str_minutes}*')
        # num = len(file_list)
        # batch_name = batch_name+ f'_{num}'

    print(batch_name)

    run_command(f'touch {TAG_CENTER_PATH}\{batch_name}')


    os.mkdir(f'./{batch_folder_name}')

    if not os.path.exists(f'./{batch_folder_name}/info.md'):
        add_info(f'./{batch_folder_name}/info.md')

    try:
        open_program(r'C:\Program Files\Typora\Typora.exe', f'./{batch_folder_name}/info.md')
    except:
        print('Typora not found..')


    with open(f'./{batch_folder_name}/{batch_name}', 'w') as f:
        pass





if __name__=='__main__':
    main()