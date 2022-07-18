import asyncio
import shlex
from typing import Tuple
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from AdityaHalder import config
from ...logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(
        install_requirements()
    )


def git():
    REPO_LINK = config.GIT_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        GIT_REPO = (
            f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
        )
    else:
        GIT_REPO = config.GIT_REPO
    try:
        repo = Repo()
        LOGGER(__name__).info(f"Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", GIT_REPO)
        origin.fetch()
        repo.create_head(
            config.GIT_BRANCH,
            origin.refs[config.GIT_BRANCH],
        )
        repo.heads[config.GIT_BRANCH].set_tracking_branch(
            origin.refs[config.GIT_BRANCH]
        )
        repo.heads[config.GIT_BRANCH].checkout(True)
        try:
            repo.create_remote("origin", config.GIT_REPO)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(config.GIT_BRANCH)
        try:
            nrs.pull(config.GIT_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -r Installer")
        LOGGER(__name__).info(f"Fetched Updates from: {REPO_LINK}")
