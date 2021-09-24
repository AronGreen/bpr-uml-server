# bpr-uml-server



## Onboarding notes

In this section notes about tools and packages should be added. Please add an appropriate heading along with a description of the subject.

### Python Virtual Environments (venv)

In order to make sure the project has the exact Python and package versions needed, we use venv. This creates a virtual environment for the project with its own installation of Python an packages - totally separate from other projects you may use.

**Setting up the environment:**

In the root project folder, run: `py -m venv .venv`

This should only be done once after cloning the project.

**Activating the environment:**

From powershell run: `.\.venv\Scripts\Activate.ps1` from the project root folder.

Your terminal should now be prefixed with `(.venv)`

With the environment active, all pip commands run locally to the project.

**Installed packages and source control:**

If you install a package in the project, you must check in the change in git, we do that by generating a `requirements.txt` file and checking that in. Here is how in powershell:

`pip freeze | Out-File -FilePath .\requirements.txt`

on the other end, restoring packages is done with pip:

`pip install -r requirements.txt`

**Further reading:**

[Python docs: Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

[Pythin docs: pip](https://docs.python.org/3/installing/index.html#installing-index)