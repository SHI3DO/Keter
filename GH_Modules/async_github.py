from github import Github
from git import Repo
import json
import asyncio

with open('botsetup.json', 'r', encoding="UTF-8") as f:
    bot_data = json.load(f)  # loads bot setups

g = Github(bot_data["github_token"])
loop = asyncio.get_event_loop()


async def get_gh_org(org_name: str):
    return await loop.run_in_executor(None, _get_gh_org, org_name)


def _get_gh_org(org_name: str):
    return g.get_organization(org_name)


async def get_gh_org_repo(org, repo_name: str):
    return await loop.run_in_executor(None, _get_gh_org_repo, org, repo_name)


def _get_gh_org_repo(org, repo_name: str):
    return org.get_repo(repo_name)


async def get_gh_repo(repo_name: str):
    return await loop.run_in_executor(None, _get_gh_repo, repo_name)


def _get_gh_repo(repo_name: str):
    return g.get_repo(repo_name)


async def clone_gh_repo(gh_repo, repo_folder: str):
    return await loop.run_in_executor(None, _clone_gh_repo, gh_repo, repo_folder)


def _clone_gh_repo(gh_repo, repo_folder: str):
    try:
        Repo.clone_from(gh_repo.clone_url, repo_folder)
    except:
        local_repo = Repo(repo_folder).remotes.origin
        local_repo.pull()


async def push_local_repo(repo_folder: str, msg: str):
    return await loop.run_in_executor(None, _push_local_repo, repo_folder, msg)


def _push_local_repo(repo_folder: str, msg: str):
    repo = Repo(repo_folder)
    repo.git.add(all=True)
    repo.index.commit(msg)
    web_o = repo.remotes.origin
    web_o.push()
