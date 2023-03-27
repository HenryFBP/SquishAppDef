# SquishAppFormat

A file-based, distributed way of defining software applications and related infrastructure.

The files are fully linkable, in a way that allows for bidirectional discovery of applications and infrastructure, provided you have credentials to view the SCM repositories.

Application information is stored in a file, at the root of a VCS repo, called `SquishAppDef.yaml`.

Directories of applications are stored in a file, at the root of a VCS repo, called `SquishAppDirectory.yaml`.

## Demo

```sh
cd ./SquishAppFormat
poetry install
bash run_demo.sh
```

## Example

Pretend that "Team Alpha", is a team that maintains 2 applications - WebGoat and BWAPP.

WebGoat is a Java application, and BWAPP is a PHP application.

To get a list of characteristics for these 2 apps, we can recursively traverse the SquishAppDirectory file, and in turn, all of the SquishAppDev files.

Their directory of applications:

- https://github.com/HenryFBP/TeamAlpha-SquishAppDirectory

The 2 applications:

- https://github.com/HenryFBP/WebGoat-SquishAppDef
- https://github.com/HenryFBP/BWAPP-SquishAppDef

## SquishAppDef

A "SquishAppDef" file, short for "Squished Application
  Definition". It's meant to describe different characteristics about a software
  application in a simple, easy-to-edit, easy-to-read, and
  easy-for-a-machine-to-parse format. Please see
  https://github.com/henryfbp/SquishAppFormat for more information.
  
- Application
  - Build
  - Infrastructure
  - Programming Language
  - Team composition

## SquishAppDirectory

A "SquishAppDirectory" file, short for "Squished Application
  Directory". It's meant to describe a list of software applications in a
  simple, easy-to-edit, easy-to-read, and easy-for-a-machine-to-parse format.
  Please see https://github.com/henryfbp/SquishAppFormat for more information.
