# Swarm of Agents

A configuration experiment for role-based coding workflows using the Roo Code extension and local models through Ollama.

[swarm_deploy.py](swarm_deploy.py) contains the generator for the role prompts and workspace files. The roles describe work such as planning, implementation and review. Roo Code and the selected local model handle inference and interaction.

The project is a snapshot of an earlier local setup. Review the paths and file-writing behavior in the generator before running it in a disposable workspace. Compatibility with current Roo Code and Ollama versions has not been verified.

**Upstream tools** · [Roo Code](https://github.com/RooCodeInc/Roo-Code) · [Ollama](https://github.com/ollama/ollama).
