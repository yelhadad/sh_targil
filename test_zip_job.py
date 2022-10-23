import sys, zipfile, os, fnmatch

VERSION = '1.2.0'
#VERSION = os.environ["VERSION"]


"""return true if there are 4 files in the provided directory and format
    else return false"""
def check_if_4_files(directory_path, file_format):
    count = len(fnmatch.filter(os.listdir(directory_path), f'*.{file_format}'))
    return count == 4

def main():

    arr = ['a', 'b', 'c', 'd']
    text_files_path = 'text_files'
    zip_files_path = 'ziped_files'

    # make sure the script fails if this function doesnt work
    for x in arr:
        f = open(f'{text_files_path}/{x}.txt', 'w')
        f.write(x)
        f.close()
    if check_if_4_files(text_files_path,'txt') is False:
        sys.exit('not all txt files created')

    # fail the script if this step doesnt work
    for x in arr:
        zipfile_name = f'{zip_files_path}/{x}_{VERSION}.zip'
        zipfile.ZipFile(zipfile_name, mode='w', compression=zipfile.ZIP_DEFLATED).write(f'{text_files_path}/{x}.txt', f'{x}.txt')
    if check_if_4_files(zip_files_path, 'zip') is False:
        sys.exit('not all zip files created')


if __name__ == '__main__':
    main()
