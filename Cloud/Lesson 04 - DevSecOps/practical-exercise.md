# DevSecOps - Practical

## Step 1:

- Login to [GitHub](https://github.com/) and [create a new repositry](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) 
- Set yourself as the owner
- Set the visibility to public
- Add a README
- Add a Python-based `.gitignore`
- Add an MIT license

## Step 2:

- [Create a new branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) using Github's UI
- Set the name of your branch as your intitials followed by `/prototype` (for example, if your name is Vic Fernandez, your branch should be `vf/prototype`)
- Set the source branch to `main`

## Step 3:

- Within a Linux-based environment (e.g., Windows Subsystem for Linux), open a CLI-based shell
- [Clone your repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=cli) using `git`, change directories to it using `cd`, and then, [checkout the branch](https://git-scm.com/docs/git-checkout) you created using `git`

Before moving on, verify you're on the correct branch by running the command below:

```bash
git branch
```

## Step 4:

- Create a directory called `.github` that contains another directory called `workflows`
- Create a file called `ci-pipeline.yml` under .github/workflows
- Add the content below to the `ci-pipeline.yml`
- Complete all TODOs

```yaml
# Set the pipeline name.
name: Continuous Integration

# Set pipeline execution criteria.
on:
  push

# Define all jobs within the pipeline.
# https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs
jobs:

  # Define the test job.
  # TODO: Set the `runs-on` parameter to ubuntu-latest.
  test:
    name: test
    runs-on: <to-do>
    steps:

      # Install Python.
      # TODO: Reference the following documentation to complete the missing `uses` parameter and set the `python-version` parameter to 3.12.
      # https://github.com/actions/setup-python
      - name: python
        uses: <to-do>
        with:
          python-version: <to-do>

      # Install Python dependencies.
      # TODO: Using pip install black.
      # https://github.com/psf/black
      - name: pip
        run: <to-do>

      # Download the source code.
      # TODO: Use the github checkout action to download the repo.
      # Ensure the version you use is set to **4**.
      # https://github.com/actions/checkout
      - name: clone
        uses: <to-do>

      # Conduct a QA test.
      # Remember you can reference black and all of its command flags using the official documentation.
      # https://github.com/psf/black
      - name: black
        run: black --diff --color --check .

  # Define the pre-build-scan job.
  # TODO: Set the needs parameter to the job.id of the test job. https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idneeds
  # TODO: Read somethings about semgrep at its official documentation https://semgrep.dev/docs/semgrep-ci/sample-ci-configs#github-actions
  pre-build-scan:
    name: pre-build-scan
    needs: <to-do>
    runs-on: ubuntu-latest
    container:
      image: semgrep/semgrep

    steps:
      # Download the source code.
      # TODO: Name this step clone and use github actions to checkout the repo
      # Hint: Remember that we did this earlier.
      # https://github.com/actions/checkout
      
      # Conduct a SAST scan.
      - name: semgrep
        run: semgrep scan --config auto

  # Define the build job.
  # TODO: Set the job.id of the build job to `build`, change the <needs> param to the job.id 
  # used by the pre-build-scan job, set the job to run on the latest version of ubuntu
  build:
    name: <to-do>
    needs: <to-do>
    runs-on: <to-do>
    steps:

      # Download the source code.
      # TODO

      # Build the container image.
      - name: docker
        run: docker build .
```

## Step 5:

- Commit the changes made to your local branch to the remote branch of your repository.

## Step 6:

- Open your code editor from within the root directory of your repository (this should be the same folder as the repository you created and downloaded)
- Write a simple Python script called `backend.py` that listens for HTTP requests.

## Step 7:

- Create an HTML file called `index.html` in the root of your repository.

## Step 8:

- Start you HTTP server by running the `backend.py` program you created.
- Verify it works by opening a  browser to `http://localhost:8000`. You should see your HTML page.

## Step 9:

- Stop your HTTP server
- Commit the changes you've made and [review the pipeline results](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-the-visualization-graph) in the GitHub UI.
- At this stage you workflow should still be failing the build job

## 