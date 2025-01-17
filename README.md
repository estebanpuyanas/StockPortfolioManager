# Stock Portfolio Manager

<u>Running this project:</u>

1. Clone this repository by running the following command in the terminal:
   `git clone https://github.com/estebanpuyanas/StockPortFolioManager.git` <br>

Alternatively, you can clone the repository by inserting the repository's `.git` url in your IDE's repository cloning option.

2. Open the project in VS Code <br>

Create the virtual enviornment by executing the following command in the root folder of the project: <br>
`python3 -m venv .venv` <br>

After this, look for the `.code-workspace` file. This file configures the virtual environment to activate automatically when you open a terminal in VSCode. If you are working from a Mac/Linux machine make sure the following line in the `.code-workspace` file is uncommented: <br>
`"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python", `. <br>

Otherwise, if working from a Windows make sure the following line is uncommented and comment out the Mac/Linux line:<br>
`"python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe"` <br>

Afterwards, save the file, and click on the `open workspace` button to allow the automatic venv activation configuration.

If for any reason the virtual environment is not activated automatically, you can activate it manually:

- Windows: `\.venv\Scripts\activate`
- Mac/Linux: `source .venv/bin/activate`

**Note: If the project will not be ran from VS Code the venv will have to be manually activated every single time the project is opened/ran**

Once activated, the terminal should show: `(.venv) username$`

3. To install all the required dependecies needed to run the project, execute the following command: `$ pip install -r requirements.txt`

<u>Commiting to this project:</u>

1. Go to develop branch: `git checkout develop`
2. Fetch & pull: `git fetch` & `git pull origin develop`
3. Make a new branch from develop: `git checkout -b <feature-name>`

Once you have finished working on your feature and you have successfully tested it, commit and push it to be able to create a pull request (PR) to merge into develop branch once approved:

1. Fetch & pull: `git fetch` & `git pull origin develop`
2. Stage files to commit: `git add .`
3. Commit files: `git commit -m "commit message"`. In commit messages please give a brief general overview of the commit.
4. Push the commit: `git push -u origin <branch-name>`

Now, in GitHub, create a PR to merge the branch into develop. Make sure you title the PR appropriately and be as detailed as possible in the description box of the PR. Once the PR has been approved and merged, the branch will be automatically deleted remotely, so ensure it is deleted locally as well. That can be done manually or by doing the following:

1. Fetch: `git fetch`
2. Pull: `git pull origin develop`

When creating branches from `develop` to edit/fix/add features, please ensure that the branch name follows this convention:
`<project-folder-name branch-work>`. <br>
For example, If you were to create a branch to create tests for backend API calls, the branch should be called: `backend-API-Calls-Tests` <br>
Similarly, if you were creating the frotend UI for user login, the branch should be called: `frontend-User-login-UI` <br>

Not all PR branches will have a clear cut name that follows this format, but follow this convetion whenever possible. It helps mantain a neat commit history and understanding of the project's progress/state.

Created by Qin Davis & Esteban Puyana.
