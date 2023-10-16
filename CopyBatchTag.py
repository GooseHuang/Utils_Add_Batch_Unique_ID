import os
import datetime
import glob
import subprocess
import time


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


def get_latest_tag():
    tag_list = os.listdir(TAG_CENTER_PATH)
    tag_list = [x for x in tag_list if 'BATCH_TAG_' in x]
    tag_list = sorted(tag_list)
    if tag_list:
        res = tag_list[-1]
    else:
        res = ''
        
    res = res.replace('BATCH_TAG_', '')
        
    return res

def main():
    date_str_minutes = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    # print(date_str_minutes)
    # date_str_seconds = datetime.datetime.now().strftime('%Y%m%d%H%M_%S')
    # print(date_str_seconds)
    batch_tag = get_latest_tag()
    batch_name = "BATCH_TAG_" + batch_tag
    batch_folder_name = 'Batch_'+batch_tag

    
    if not batch_tag:
        print('\nStop: No batch tag found...\n')
        return

    if not os.path.exists(batch_folder_name):
        os.mkdir(batch_folder_name)

    if not os.path.exists(f'./{batch_folder_name}/info.md'):
        add_info(f'./{batch_folder_name}/info.md')

    
    
    with open(f'./{batch_folder_name}/{batch_name}', 'w') as f:
        pass

    print(f"\n{batch_name} created...\n")






if __name__=='__main__':
    main()
    print('\nDone.\n')

    time.sleep(10)