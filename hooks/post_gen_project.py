import os
import shutil
import subprocess

def print_current_directory():
    print(os.getcwd())

def rename_copy_remove():
    source_directory = "../{{ cookiecutter.name | lower }}"
    temp_directory = "../temp"

    try:
        os.rename(source_directory, temp_directory)
        os.chdir('..')
        shutil.copytree(os.path.join(os.getcwd(), "temp"), os.getcwd(), dirs_exist_ok=True)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        shutil.rmtree(os.path.join(os.getcwd(), "temp"))

def remove_file_or_directory(filepath):
    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)

def remove_deploy_docc():
    filepath = os.path.join(os.getcwd(), '.github/workflows/deploy_docc.yml')
    remove_file_or_directory(filepath)

def initialize_swift_library():
    project_name = "{{ cookiecutter.name }}"
    subprocess.run(["swift", "package", "init", "--name", project_name, "--type", "library"])

def run_make_commands():
    subprocess.run(["make", "bootstrap"])
    subprocess.run(["make", "fmt"])

def initialize_git_repository():
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

def main():
    print_current_directory()

    create_docc = '{{ cookiecutter.deploy_docc.lower() }}' == 'yes'

    if not create_docc:
        remove_deploy_docc()

    rename_copy_remove()

    initialize_swift_library()

    run_make_commands()

    initialize_git_repository()

if __name__ == "__main__":
    main()
