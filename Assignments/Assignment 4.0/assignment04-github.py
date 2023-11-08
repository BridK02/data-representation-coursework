#Assignment 4
#Author Brid Kennedy
#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository.

import requests
import git
import os
import base64
from config import config as cfg


def read_file_from_github(repo_url, branch, file_path):
    # Reads a file from a GitHub repository.
    # Returns the contents of the file, as a string.

    headers = {
        "Authorization": f"token {cfg['github_api_token']}"
    }
    url = f"https://api.github.com/repos/{repo_url}/contents/{file_path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_content = response.json()["content"]
        return base64.b64decode(file_content).decode("utf-8")
    else:
        print("Error accessing the file via the GitHub API")
        return None


def replace_text_in_file(file_contents, old_text, new_text):
    # Replaces all instances of a given text string in a file.
    # Returns the updated contents of the file, as a string.

    return file_contents.replace(old_text, new_text)


def commit_and_push_changes(repo, relative_file_path, commit_message, new_file_contents):
    # Stage the changes to the file.
    repo.index.add(relative_file_path)

    # Write the updated content back to the local file.
    with open(relative_file_path, 'w') as file:
        file.write(new_file_contents)

    # Commit the changes.
    repo.index.commit(commit_message)

    # Push the changes to the remote repository.
    origin = repo.remote(name='origin')
    origin.push()


def main():
    # Get the repository owner, repository name, branch, and file path.
    repo_owner = input("Enter the repository owner (e.g., BridK02): ")
    repo_name = input("Enter the repository name (e.g., data-representation-coursework): ")
    branch = input("Enter the branch name (e.g., main): ")

    # Make sure the file exists before proceeding.
    file_path = input("Enter the path to the file to modify (e.g., Assignments/Assignment 4.0/test.txt): ")
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Clone the repository or open an existing repository.
    repo_url = f"{repo_owner}/{repo_name}"
    repo = git.Repo(f"C:/Users/bridc/repo/{repo_name}")

    # Construct the absolute file path and relative file path.
    absolute_file_path = os.path.abspath(file_path).replace("\\", "/")
    relative_file_path = absolute_file_path.replace(repo.working_tree_dir + "\\", "")

    # Read the file from the repository.
    file_contents = read_file_from_github(repo_url, branch, file_path)

    # Replace all instances of the text "Andrew" with your name.
    new_file_contents = replace_text_in_file(file_contents, "Andrew", "Brid")

    # Stage and commit the changes using the relative file path.
    commit_and_push_changes(repo, relative_file_path, "Replaced all instances of the text 'Andrew' with 'Brid'.", new_file_contents)


if __name__ == "__main__":
    main()