# githubactions_projects

## GitHub Actions Overview

**GitHub Actions** is a feature in GitHub that allows developers to automate tasks such as building, testing, and deploying code. It allows the user to automate, customize, and execute the software development workflows written using yaml directly in the user's GitHub repository.

Each workflow specifies conditions under which certain tasks are executed. For example, a workflow defined in a **`ci.yml`** file can be triggered by specific events, such as code being pushed to the repository. When the condition **`on: [push]`** is met, the jobs specified in the YAML file are automatically executed. Similarly, actions can be automated based on other events, such as pull requests.

By leveraging GitHub Actions, developers can streamline their **CI/CD (Continuous Integration and Continuous Deployment)** processes, ensuring that their code is consistently tested and deployed with **minimal manual intervention**.

## How does Github action works

**Workflow Definition**
Workflows are defined in YAML files located in the .github/workflows directory of your repository. Each workflow is triggered by **specific events** and can contain **one or more jobs** that execute commands on specified runners.

**Events**
Workflows are triggered by events that occur in your repository, such as:

**push:** Triggered when code is pushed to the repository.
**pull_request:**Triggered when a pull request is created or updated.
**schedule:** Triggered at scheduled times.
**workflow_dispatch:** Manually triggered via the GitHub UI.

**Jobs and Steps**
Each workflow consists of jobs, and each job runs in an instance of a virtual machine or a container. Jobs are composed of steps, which are individual tasks that run commands.

## Example Workflow

### Basic structure of the repository

<img src="https://github.com/harinath-az/githubactions_projects/blob/main/images/directory.png" width="300" height="200">

### Workflow defined in the ci.yml file

<img src = "https://github.com/harinath-az/githubactions_projects/blob/main/images/ci.png" width = "400" height = "500">




The name of this workflow is **CI**, which stands for Continuous Integration.The **on: [push, pull_request]** line specifies the events that trigger the workflow. This means the workflow will run whenever there is a push to the repository or a pull request is created or updated.The **jobs section** defines all the jobs to be executed in the workflow. In this case, we have a single job named build.The build job runs on an ubuntu-latest virtual machine, which provides a clean Ubuntu environment for each run. The **name:** Checkout code uses the actions/checkout@v2 action to clone the repository’s code into the virtual machine. The name: Set up Python uses the actions/setup-python@v2 action to set up a Python environment. The with section specifies that it should use the latest version of Python 3 (python-version: '3.x'). The install dependencies will install the project's dependencies which are listed in the requirements.txt file. The run tests will run the command to execute the unit tests located in the tests directory.

## How It Works
Whenever changes are made to the Python code and a commit is pushed to the repository, or a pull request is created/updated, the GitHub Actions workflow is triggered. The workflow will:

Checkout the Code: Clone the repository into the virtual machine.
Set Up the Python Environment: Create a Python environment with the specified version.
Install Dependencies: Install all required dependencies for the project.
Run Tests: Execute the unit tests to ensure the code changes do not break any existing functionality.





## Why Github actions when we have other CI tools and when to use them?


Before we dive into a project using GitHub-based runners and self-hosted runners, it's important to understand why you might choose GitHub Actions over other Continuous Integration (CI) tools.

**Seamless Integration with GitHub:**
One of the main reasons teams prefer GitHub Actions over mainstream tools like Jenkins is its seamless integration with GitHub. For teams already using GitHub for version control, GitHub Actions is easy to use, set up, and manage. It eliminates the need for separate servers and additional configurations required to connect the repository to an external CI tool.

**Built-in Security Features:**
GitHub Actions is designed with security in mind. It offers features such as encrypted secrets, token permissions, and secure environments, ensuring that your CI/CD processes are safe and secure.

**Ease of Use:**
Unlike Jenkins, which often requires installing numerous plugins, GitHub Actions simplifies the process. You can simply create one or more action files under the .github/workflows directory in your repository. These action files are written in YAML syntax, making them straightforward to define and manage.

**Self-Hosted Runners:**
GitHub also provides the option of using self-hosted runners. This feature allows you to run your workflows on your own infrastructure, which can be particularly useful when you need substantial resources or specific packages that are not available with GitHub-hosted runners.

**Flexibility and Customization:**
GitHub Actions allows you to define complex workflows using simple YAML syntax. This flexibility enables you to customize your CI/CD pipelines to meet your specific needs, whether for building, testing, or deploying your code.

Using **GitHub Actions:** can be a better approach when you need a simple, integrated solution for CI/CD within the GitHub ecosystem. This is particularly advantageous for small companies and startups where pipelines are not highly customized or complex, and the budget is limited.GitHub Actions can be more cost-efficient due to GitHub's generous free tier and pricing plans that suit smaller budgets.

For larger projects with highly customized and complex pipelines, **Jenkins** might be a better choice due to its flexibility and extensive range of plugins. It's worth noting that if your company decides to migrate from GitHub Actions to another platform like GitLab or Jenkins in the future, moving action files can be challenging.


## Types of runners

GitHub Actions provides two types of runners for executing workflows: **GitHub-hosted runners** and **self-hosted runners**.

### GitHub-hosted runners

When we don't want to spend time and money on managing infrastructure Github hosted runners are better to use. **GitHub-hosted runners** are virtual machines hosted by GitHub. These runners come pre-installed with various software and tools commonly used for CI/CD workflows. These runners can be used for running workflows without setting up or managing our own infrastructure.

**Advantages:**

No infrastructure management required.
Provides a clean and consistent environment for each run.
GitHub takes care of maintenance and updates.
Offers a variety of environments to suit different workflows.

### self-hosted runners

Self-hosted runners are machines that you set up and manage within your own infrastructure. These runners can be physical or virtual machines, and you have full control over their configuration and environment.Self-hosted runners are useful when you need specific software configurations, access to private resources, or want to run workflows on your own infrastructure.

Advantages:

Full control over the runner's environment and configurations.
Can access resources within your private network.
Ideal for running workflows that require specific software versions or dependencies.
Cost-effective for organizations with existing infrastructure.

### When to use self hosted runners:
GitHub-hosted runners, managed by GitHub, are free to use for public repositories and come with a set amount of free usage for private repositories. However, there are situations where using self-hosted runners is beneficial or necessary.

When an organization decides their code needs to be private, and they are creating private repositories, self-hosted runners provide enhanced control over the execution environment, ensuring the code and build processes remain within the organization's secure infrastructure.

Even for public repositories, there are cases where the project might need a significant amount of resources (e.g., high CPU, memory, or specialized hardware). Self-hosted runners can be provisioned with the necessary resources to handle these demanding workloads.Sometimes, a project requires specific software packages or configurations that are not available on GitHub-hosted runners. With self-hosted runners, you can install and configure any software or dependencies your project needs.

### How to check for errors
Once we make any changes in the repository and press "Commit changes," GitHub Actions looks for the workflow file located in the .github/workflows directory within the repository. Upon finding the YAML file, GitHub Actions attempts to execute the jobs specified in the workflow file.

### Workflow Execution Indicators

**Yellow Dot:** While GitHub Actions is running the tasks mentioned in the workflow file, a yellow dot will appear next to the commit on the main branch. This indicates that the workflow is in progress.

<img src="https://github.com/harinath-az/githubactions_projects/blob/main/images/initial_yellow.png" width="650" height="300">
<b>Green Tick:</b> Once all the jobs are successfully completed, the yellow dot will change to a green tick mark. This indicates that the workflow has finished executing all tasks without any errors.

<img src="https://github.com/harinath-az/githubactions_projects/blob/main/images/tick.png" width="450" height="250">
<b>Red X:</b> If there are any errors during the execution, a red X mark will appear. You can view the errors by clicking on the dot or X symbol, which will take you to the detailed logs showing what went wrong.

<img src="https://github.com/harinath-az/githubactions_projects/blob/main/images/error.png" width="650" height="250">







