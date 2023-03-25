# SquishAppDef

WIP :3c

A file-based, distributed way of defining in-house software applications and infrastructure.

Ideally, the files are fully linkable, in a way that allows for bidirectional discovery of applications and infrastructure, provided you have credentials to view the SCM repositories.

Application information is stored in files, at the root of a VCS repo, called `SquishAppDef.yaml`.

Directories of applications are stored in files, at the root of a VCS repo, called `SquishAppDirectory.yaml`.

## Example

Pretend that "Team Alpha", is a team that maintains 2 applications - WebGoat and BWAPP.

WebGoat is a Java application, and BWAPP is a PHP application.

Their directory of applications:

- https://github.com/HenryFBP/TeamAlpha-SquishAppDirectory

The 2 applications:

- https://github.com/HenryFBP/WebGoat-SquishAppDef
- https://github.com/HenryFBP/BWAPP-SquishAppDef
