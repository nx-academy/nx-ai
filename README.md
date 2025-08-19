# NX Academy - AI Source code
Collection of scripts built with Python that use OpenAI API to generate content (quiz, summary, ...), and to run jobs.

## Welcome to NX Academy 👋!

As always, thank you for taking the time to read this documentation. Please note that this repository is only related to the AI jobs and workflows that run on NX Academy. At the moment, I'm only using OpenAI API for creating content such as quizzes, write articles on the web and extract summary, and soon run Discord bots that act as small back offices for the project.

You are free to clone this repo and to take a look at the source code. However, you should know that this repo is really coupled to NX Academy and you'll need your own environment variables to make it fully work. That being said, feel free to look aroud and to ask questions. My Discord username is tdimnet and I'm always avaiable to answers your questions.


Here are the key points you need to remember:

- NX Academy uses Python for many of its backend logic.
- This project is usable in CLI [with Click](https://click.palletsprojects.com/en/stable/), which tends to be far more readable than argparse.
- All the project has been written inside a Docker container.
- If you want to run it locally, I strongly recommend that you install [the DevContainer VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) as it almost works out of the box - it's a one-command installation.
- When working on the project, I tried to find the right balance between modularity and simplicity - **Simple is better than complex**.


## How to Run this Project on your Computer?

### Prerequisites

- [Docker](https://www.docker.com/) - Please note that this project has been tested on Windows and Linux machines.
- [the DevContainer VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - Honestly, use this extension, don't be a fool.
- Create a `.env` file (`cp .example.env .env`) and add your **OPENAI_API_KEY**, **GITHUB_TOKEN**, and **DISCORD_TOKEN** tokens. _Sorry hacker guys, I'll not share mine_.


### Installing the modules

Once you cloned the repo and launched it inside a container, you can now install the modules with pip.

```bash
pip install -r requirements.txt
```


### Launch the CLI

The vast majority of this project is usable (and used!) in CLI. To run it and get informations on the avaiable commands, run:

```bash
python app.py --help
```


### Project Structure

Because project structure is important (and that I like having a nice project structure), here are some information:

```text
/
├── mock/ # Some mock files that I use to fake calls to GPT
├── nx_ai/
│   └── discord_service/ # All the services have the same structure
│       └── discord_api.py # Interfaces with the Discord API
│       └── discord_cli.py # Commands that are useful for testing purpose
│   └── github_service/
│       └── ...
│   └── openai_service/
│       └── ...
│   └── utils/ # Some basic utils that are not related to business logics
│   └── workflows/
│       └── generate_quiz.py
│       └── generate_recap.py
│       └── workflows_cli.py # The main entry point for the app - all the commands that I use on a daily basis
└── tests/ # Yep, this project is tested
```


## Contributing?

Currently, we do not accept external contributors. We are a small team working to find the right balance. Once we achieve this balance, we will open up for external contributions.
