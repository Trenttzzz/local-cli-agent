# AI Terminal Interpreter

This project creates a daemon-based AI interpreter that allows you to ask questions directly in your terminal using Ollama.

## Features

- Ask AI questions directly in your terminal with `#ask your question`
- Daemon runs in the background for quick responses
- Works with Ollama for local LLM inference
- Compatible with both Bash and Zsh shells

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Make sure Ollama is installed and running on your system. If not, install it from [ollama.com](https://ollama.com/).

3. Pull the model you want to use (default is qwen3:1.7b):

```bash
ollama pull qwen3:1.7b
```

4. Source the shell script in your shell configuration file (e.g., .bashrc, .zshrc):

```bash
echo "source $(pwd)/askrc.sh" >> ~/.bashrc
# OR for Zsh
echo "source $(pwd)/askrc.sh" >> ~/.zshrc
```

5. Reload your shell configuration:

```bash
source ~/.bashrc
# OR for Zsh
source ~/.zshrc
```

## Usage

Once set up, you can use the AI interpreter directly in your terminal:

```bash
#ask what is the capital of France?
```

The AI will process your question and display the answer directly in the terminal.

### Managing the Daemon

You can manage the AI interpreter daemon with these commands:

- `askd start` - Start the daemon
- `askd stop` - Stop the daemon
- `askd restart` - Restart the daemon
- `askd status` - Check if the daemon is running

## Advanced Configuration

You can use a different Ollama model by specifying it when starting the daemon:

```bash
python ask_interpreter.py --start --model llama3
```

## Troubleshooting

If you encounter any issues:

- Check the logs at `/tmp/ai_interpreter.log`
- Make sure Ollama is running with `ollama list`
- Restart the daemon with `askd restart`