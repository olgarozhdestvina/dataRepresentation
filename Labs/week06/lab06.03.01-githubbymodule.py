import requests
from github import Github

g = Github("apikey")
#for repo in g.get_user().get_repos():
#    print(repo.name)

repo = g.get_repo("olgarozhdestvina/datarepresentationstudent")
#print(repo.clone_url)

fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
# print(contentOfFile)

newContent = contentOfFile + "\n## Another header added \n"
#print(newContent)

gitHubResponse = repo.update_file(fileInfo.path, "update by prog", newContent, fileInfo.sha)
print(gitHubResponse)