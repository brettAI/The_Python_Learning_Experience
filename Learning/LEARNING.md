# Learning Python



This Learning sections provides links to resources by type as well as links to specific types of information:

- [Books](BOOKS.md)
- [Videos](VIDEOS.md)
- [Tutorials](TUTORIALS.md)

## Language

## Development Environment

- [Microsoft Visual Studio Code](https://code.visualstudio.com/)
- [MS Visual Studio Code - Virtual Environment]

### VS Code User Settings

Update VS Code User settings to include the following:
```json
{
    "editor.fontSize": 16,
    "guides.enabled": false,
    "editor.formatOnType": true,
    "editor.formatOnPaste": true,
    "editor.formatOnSave": true,
}
```

### Creating a Python Virtual Environment within MS Visual Code

Virtual Environment - Links

#### Virtual Environment Overview

A Virtual Environment allows you to keep downloaded packages outside of the global package space, this allows you to run different versions of the same package for different projects, each to match their own needs.

#### Configuring the Virtual Environment

The following outlines how to add a Python Virtual Environment.

1. Within the Project folder open a Terminal window.
2. By Default this will open to the root folder of this 'project'.
3. Type `python -m venv {virtual environment name}`
   1. May need to change Powershell execution policy through a Powershell Command Prompt run as Administrator
   2. then run `Set-ExecutionPolicy RemoteSigned1
4. A sub folder will be create with the name supplied and 'local' copies of the python compiler and other files will be copied there.
5. Close the Terminal window.
6. On the status bar, click the Python interpreter and change it to the one in the Virtual Environment just created.

This project now has a separate environment for installed modules than the global space.

#### TODO

1.Create a project specific the describing strings.
    1. Include a file with examples and explanations of built in string functions
    2. Include modules which perform specific string manipulations
       1. Reverse a string and remove unwanted characters
