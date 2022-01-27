import sys
import git
from git_contributions_importer import *

repos_path = [
    r'C:\Users\omarm\Desktop\DiegoWork\APPOLO\sireo',
    r'C:\Users\omarm\Desktop\DiegoWork\APPOLO\appolo-server',
]
repos = []
for repo_path in repos_path:
    repos.append(git.Repo(repo_path))

mock_repo_path = r'C:\Users\omarm\Desktop\DiegoWork\APPOLO\Contributions-Importer-For-Github'
mock_repo = git.Repo.init(mock_repo_path)

importer = Importer(repos, mock_repo)
importer.set_author(['Diegodguez@hotmail.com', 'diego.dominguez@hivisionled.red'])
importer.set_commit_max_amount_changes(15)
importer.set_changes_commits_max_time_backward(60*60*24*30)
importer.set_max_changes_per_file(60)
importer.set_collapse_multiple_changes_to_one(True)
importer.import_repository()
