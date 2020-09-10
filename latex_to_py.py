import argparse
import os
import sys
import json
from zipfile import ZipFile
from shutil import copyfile
from make_dependency import get_dependencies

try:
    sys.path.index(os.getcwd()) 
except ValueError:
    sys.path.append(os.getcwd()) 


prefix = '../../topics'
worksheet_source = 'src/sp20'
output_directory = "published"

def generate_file(file_name, file_paths, everything, solution=False):
    print(file_name, file_paths)
    file = []
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            start = False
            start_sol = False
            for line in f.read().split('\n'):
                if line.startswith(r'\begin{solution}'):
                    start_sol = True
                if line == r'\begin{lstlisting}':
                    start = True
                elif line == r'\end{lstlisting}':
                    start = False
                elif start and (start_sol == solution):
                    if everything or line[:3] not in [">>>", "..."]:
                        file.append(line)
        file.append("\n")
    with open(file_name, 'w') as f:
        f.write('\n'.join(file) + '\n')
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', type=str, help='input file e.g. week4.tex')
    parser.add_argument('-e', "--everything", action="store_true", help="Show lines that aren't code writing but are python code")
    parser.add_argument("--lgtm", action="store_true", help="Skip lgtm confirmation")

    args = parser.parse_args()

    file_paths = get_dependencies(os.path.join(worksheet_source, args.input_file))
    file_paths = [p for p in file_paths if '/text/' not in p]
    out_file = args.input_file.replace('.tex', '.py')
    out_okpy = args.input_file.replace('.tex', '.ok')
    sol_name = out_file.replace('.py', '_sol.py')
    zip_name = out_file.replace('.py', '.zip')

    generate_file(os.path.join(output_directory, out_file), file_paths, args.everything)
    generate_file(os.path.join(output_directory, sol_name), file_paths, args.everything, solution=True)

    okpy = {}
    okpy['name'] = out_file.split('.')[0]
    okpy['endpoint'] = 'cal/csm/fa20/cs88'
    okpy['src'] = [out_file]
    okpy['tests'] = {out_file: "doctest"}
    okpy['protocols'] = ["file_contents", "grading", "analytics", "backup"]

    with open(os.path.join(output_directory, out_okpy), 'w') as f:
        f.write(json.dumps(okpy))

    if args.lgtm:
        lgtm = 'y'
    else:
        lgtm = input("Does the .py file look good? y/N: ")

    if lgtm == 'y':
        copyfile("ok", os.path.join(output_directory, "ok"))
        os.chdir(output_directory)
        with ZipFile(zip_name, 'w') as myzip:
            myzip.write(out_okpy)
            myzip.write(out_file)
            myzip.write("ok")
