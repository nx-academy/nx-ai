# NX Academy - AI Source Code  
Collection of Python scripts using the OpenAI API to generate content (quizzes, summaries, …) and run automated jobs.

## Welcome to NX Academy 👋

Thanks for taking the time to read this documentation!  
This repository is dedicated **only** to the AI jobs and workflows powering NX Academy.  

At the moment, it mainly relies on the OpenAI API to:  
- create quizzes  
- generate article drafts  
- extract summaries  
- (soon) run Discord bots acting as small back-office tools for the project  

You’re free to clone this repo and explore the source code. Keep in mind that it’s tightly coupled to NX Academy: you’ll need your own environment variables to make it fully work. That being said, feel free to look around and reach out if you have questions — my Discord username is **tdimnet** and I’m usually available to answer.

---

### Key Points

- NX Academy uses **Python** for much of its backend logic.  
- The project is built around a **CLI** using [Click](https://click.palletsprojects.com/en/stable/) (far more readable than argparse).  
- Everything runs inside a **Docker container**.  
- For local development, I strongly recommend using the [DevContainer VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). It works almost out-of-the-box with a single command.  
- I’ve tried to keep the code **modular but simple** — _Simple is better than complex_.  

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) — tested on both Windows and Linux  
- [VSCode DevContainer extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) — really, just use it 😉  
- A `.env` file containing your tokens:  
  - **OPENAI_API_KEY**  
  - **GITHUB_TOKEN**  
  - **DISCORD_TOKEN**  
  (_and no, I won’t share mine!_)  

```bash
cp .example.env .env
```

### Install dependencies

Once the repo is cloned and running inside a container:

```bash
pip install -r requirements.txt
```

### Run the CLI

Most of this project is designed for CLI usage. To get available commands:

```bash
python app.py --help
```

---

## Project Structure

Here’s a quick overview of the structure:

```text
/
├── mock/                  # Mock files to simulate GPT calls
├── nx_ai/
│   ├── discord_service/   # All services follow the same structure
│   │   ├── discord_api.py # Interface with the Discord API
│   │   └── discord_cli.py # CLI commands for testing purposes
│   ├── github_service/
│   ├── openai_service/
│   ├── utils/             # Utilities not tied to business logic
│   └── workflows/
│       ├── generate_quiz.py
│       ├── generate_recap.py
│       └── workflows_cli.py # Main CLI entry point (daily usage)
└── tests/                 # Yep, it’s tested!
```

---

## Contributing

At the moment, external contributions are not accepted. We’re a small team working to strike the right balance. Once the project stabilizes, we’ll gladly open it up.  
