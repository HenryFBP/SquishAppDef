import os
from pprint import pprint
from typing import Dict

import yaml
from git import Repo

SQUISH_APP_REPOS_FOLDER_NAME = '.SquishAppRepos'
SQUISH_APP_DIRECTORY_FILE_NAME = 'SquishAppDirectory.yaml'
SQUISH_APP_FORMAT_FILE_NAME = 'SquishAppFormat.yaml'


class SquishAppManager(object):
    """
    A helper class meant to manage SquishAppDirectories.
    """

    def __init__(self, root_directory: str):
        self.root_directory = os.path.abspath(root_directory)

        if not os.path.exists(self.root_directory):
            os.makedirs(self.root_directory)

        self.squish_applications = None

    def load_squish_app_directory(self, uri: str):

        repo_name = parse_git_uri_to_repository_name(uri)

        squishAppDirPath = '{}/{}/{}'.format(self.root_directory, SQUISH_APP_REPOS_FOLDER_NAME, repo_name)

        directoryRepo = clone_full_git_repo(
            uri,
            squishAppDirPath
        )

        appDir = read_squishAppDirectory_from_path(squishAppDirPath)

        pprint(appDir)

        directoryURIs = appDir['directory-uris']

        print("Found {} directory URIs:".format(len(directoryURIs)))

        for repoURI in directoryURIs:
            print("- {}".format(repoURI))

        # go through all of our SquishAppDirectory URIs
        squish_apps = SquishApplicationList()
        for repoURI in directoryURIs:
            # merge our application definitions into one object, so we can query it
            squishAppDef = fetch_directory_uri(self.root_directory, repoURI)
            squish_apps += squishAppDef

        self.squish_applications = squish_apps


class SquishApplicationList(object):
    """This class stores SquishAppDefs."""

    def __init__(self) -> None:
        self.applications = []

    def __add__(self, squishAppDef: Dict):
        pprint("__add__ MergedSquishApplicationDefs")
        pprint(squishAppDef)
        assert (squishAppDef['type'] == 'SquishAppDef')
        self.applications.append(squishAppDef['application'])
        return self

    def get_all_team_members(self):
        """TODO use itertools"""
        team_members = []
        app: Dict
        for app in self.applications:
            if 'team' in app.keys():
                if 'members' in app['team'].keys():
                    team_members.extend(app['team']['members'])
        return team_members


def clone_full_git_repo(uri: str, path: str) -> Repo:
    path = os.path.abspath(path)
    if not os.path.exists(path):
        repo = Repo.clone_from(uri, path)
        print("Cloned {} to {}".format(uri, path))
        return repo
    else:
        print("{} already exists.".format(path))
        return Repo(path)


def read_squishAppDirectory_from_path(path: str) -> Dict:
    with open(path + '/' + SQUISH_APP_DIRECTORY_FILE_NAME, 'r') as f:
        return yaml.safe_load(f)


def read_squishAppFormat_from_path(path: str) -> Dict:
    with open(path + '/' + SQUISH_APP_FORMAT_FILE_NAME, 'r') as f:
        return yaml.safe_load(f)


def fetch_directory_uri(path: str, squishAppDirectoryURI: Dict) -> Dict:
    """Given a SquishAppDirectory URI, clone it, and then return the contents of the YAML file as a Dict."""
    print()
    print("Loading {} ...".format(squishAppDirectoryURI))

    repoURI = squishAppDirectoryURI['uri']
    repoType = squishAppDirectoryURI['type']

    if repoType != 'git':
        raise NotImplemented(
            "Cloning non-git repositories is not currently supported!")

    repoName = parse_git_uri_to_repository_name(repoURI)

    repoPath = "{}/{}/{}".format(path, SQUISH_APP_REPOS_FOLDER_NAME, repoName)

    # 1. clone repo
    repo = clone_full_git_repo(repoURI, repoPath)

    # 2. read yaml file
    squishAppDefPath = os.path.join(repoPath, 'SquishAppDef.yaml')
    with open(squishAppDefPath, 'r') as f:
        squishAppDef = yaml.safe_load(f)

        pprint("SquishAppDef for {} - {}".format(
            repoName, squishAppDirectoryURI
        ))
        pprint(squishAppDef)

        # 3. return object
        return squishAppDef


def parse_git_uri_to_repository_name(git_uri: str) -> str:
    """Given a Git URI, return the name of the repository."""
    rightmost = git_uri.split('/')[-1]
    if rightmost.endswith('.git'):
        rightmost = rightmost[0:(-1 * len('.git'))]
    return rightmost


if __name__ == '__main__':
    manager = SquishAppManager('./teamAlphaDemo')
    manager.load_squish_app_directory('git@github.com:HenryFBP/TeamAlpha-SquishAppDirectory.git')

    print("All team members: ")
    pprint(manager.squish_applications.get_all_team_members())
