#Assignment 4
#Author Brid Kennedy
#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository.
'''import requests
from git import Repo
from config import config as cfg 

def read_file_from_github(repo_owner, repo_name, branch, file_path):
    # Reads a file from a GitHub repository.
    # Returns the contents of the file, as a string.

    headers = {
        "Authorization": f"token {cfg['github_api_token']}"
    }
    response = requests.get(
        f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{file_path}",
        headers=headers
    )
    return response.content.decode()

def replace_text_in_file(file_contents, old_text, new_text):
    # Replaces all instances of a given text string in a file.
    # Returns the updated contents of the file, as a string.

    return file_contents.replace(old_text, new_text)

def commit_and_push_changes(repo, file_path, commit_message):
    # Commits and pushes changes to a Git repository.

    repo.git.add(file_path)
    repo.git.commit(m=commit_message)
    repo.git.push()

def main():
    # Get the repository owner, repository name, branch, and file path from the user.
    repo_owner = input("Enter the repository owner (e.g., BridK02): ")
    repo_name = input("Enter the repository name (e.g., data-representation-coursework): ")
    branch = input("Enter the branch name (e.g., main): ")
    file_path = input("Enter the path to the file to modify (e.g., Assignments/Assignment 4.0/test.txt): ")

    # Read the file from the repository.
    file_contents = read_file_from_github(repo_owner, repo_name, branch, file_path)

    # Replace all instances of the text "Andrew" with the user's name.
    new_file_contents = replace_text_in_file(file_contents, "Andrew", "Brid")

    # Debug: print the new content
    print("New File Contents:")
    print(new_file_contents)

    # Commit and push the changes to the repository.
    # Construct the GitHub repository URL
    repo_url = f"https://github.com/{repo_owner}/{repo_name}.git"
    repo = Repo(r"C:\Users\bridc\repo\data-representation-coursework")
    commit_message = "Replaced all instances of the text 'Andrew' with 'Brid'."
    commit_and_push_changes(repo, file_path, commit_message)

if __name__ == "__main__":
    main()'''
def read_file_from_github(repo, file_path):
    # Reads a file from a GitHub repository.
    # Returns the contents of the file, as a string.

    headers = {
        "Authorization": f"token {cfg['github_api_token']}"
    }
    response = requests.get(
        f"https://raw.githubusercontent.com/{repo.owner.name}/{repo.name}/{repo.active_branch.name}/{file_path}",
        headers=headers
    )
    return response.content.decode()

def replace_text_in_file(file_contents, old_text, new_text):
    # Replaces all instances of a given text string in a file.
    # Returns the updated contents of the file, as a string.

    return file_contents.replace(old_text, new_text)

def commit_and_push_changes(repo, file_path, commit_message):
    # Commits and pushes changes to a Git repository.

    # Stage the changes to the file.
    repo.git.add(file_path)

    # Commit the changes.
    repo.git.commit(m=commit_message)

    # Push the changes to the remote repository.
    repo.git.push()

def main():
    # Get the repository path from the user.
    repo_path = input("Enter the path to the repository: ")

    # Open the repository.
    repo = Repo(repo_path)

    # Get the file path from the user.
    file_path = input("Enter the path to the file to modify: ")

    # Read the file from the repository.
    file_contents = read_file_from_github(repo, file_path)

    # Replace all instances of the text "Andrew" with the user's name.
    new_file_contents = replace_text_in_file(file_contents, "Andrew", "Brid")

    # Debug: print the new content
    print("New File Contents:")
    print(new_file_contents)

    # Stage and commit the changes.
    commit_and_push_changes(repo, file_path, "Replaced all instances of the text 'Andrew' with 'Brid'.")

if __name__ == "__main__":
    main()


