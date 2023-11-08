#Assignment 4
#Author Brid Kennedy
#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository.

import requests
import git
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

def commit_and_push_changes(repo, file_path, commit_message):
    # Commits and pushes changes to a Git repository. Stage only the target file for commit.
    repo.git.add(file_path)

    # Commit the changes.
    try:
        repo.git.commit(m=commit_message, a=True)
    except git.exc.GitCommandError as e:
        print(f"Commit failed: {e}")
        return

    # Push the changes to the remote repository.
    try:
        repo.git.push()
        print("Changes successfully pushed to the remote repository.")
    except git.exc.GitCommandError as e:
        print(f"Push failed: {e}")



def main():
    # Get the repository owner, repository name, branch, and file path.
    repo_owner = input("Enter the repository owner (e.g., BridK02): ")
    repo_name = input("Enter the repository name (e.g., data-representation-coursework): ")
    branch = input("Enter the branch name (e.g., main): ")
    file_path = input("Enter the path to the file to modify (e.g., Assignments/Assignment 4.0/test.txt): ")

    # Clone the repository or open an existing repository.
    repo_url = f"{repo_owner}/{repo_name}"
    repo = git.Repo(f"C:/Users/bridc/repo/{repo_name}")

    # Read the file from the repository.
    file_contents = read_file_from_github(repo_url, branch, file_path)

    # Replace all instances of the text "Andrew" with your name.
    new_file_contents = replace_text_in_file(file_contents, "Andrew", "Brid")

    # Debug: print the new content
    print("New File Contents:")
    print(new_file_contents)

    # Stage and commit the changes.
    commit_and_push_changes(repo, file_path, "Replaced all instances of the text 'Andrew' with 'Brid'.")

if __name__ == "__main__":
    main()