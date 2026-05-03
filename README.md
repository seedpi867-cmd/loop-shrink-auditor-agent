<div align="center">

# brain-loop

**The simplest autonomous agent you can run. One bash script. Any LLM CLI.**

A loop that wakes up, builds a prompt from files on disk, sends it through whatever LLM you have, and goes back to sleep. No frameworks. No API keys. No dependencies beyond bash and an LLM CLI.

</div>

---

## 30-second start

```bash
git clone https://github.com/seedpi867-cmd/brain-loop.git
cd brain-loop
nano config.sh          # uncomment your LLM (codex, claude, ollama, etc)
chmod +x brain-loop.sh
./brain-loop.sh
```

That's it. It's running. Edit `AGENT.md` to tell it who it is. Edit `INSTRUCTIONS.md` to tell it what to do. Put files in `context/` for it to read. It loops forever.

## How it works

```
while true:
    prompt  = AGENT.md + memory + context/* + tasks + INSTRUCTIONS.md
    output  = $LLM_CMD "$prompt"
    memory += what happened
    sleep 5 minutes
```

Every cycle the agent:
1. Reads `AGENT.md` — its identity
2. Reads `data/memory.md` — what happened in previous cycles
3. Reads everything in `context/` — fresh data you drop in
4. Reads `data/tasks.md` — what it should be working on
5. Reads `INSTRUCTIONS.md` — how to behave this cycle
6. Sends the assembled prompt to your LLM CLI
7. The LLM reads/writes files, runs commands, does work
8. Memory is updated, logs are saved, agent sleeps

## Works with any LLM

Edit `config.sh` and uncomment one line:

| LLM | Command | Auth |
|-----|---------|------|
| **Codex** (OpenAI) | `codex exec --dangerously-bypass-approvals-and-sandbox` | `codex login` (OAuth, free) |
| **Claude Code** (Anthropic) | `claude -p --dangerously-skip-permissions` | `claude login` (OAuth, free with sub) |
| **Ollama** (local) | `ollama run llama3.2` | None — runs locally |
| **llm** (any provider) | `llm -m gpt-4o` | Provider API key |
| **aichat** | `aichat` | Provider API key |

Any CLI that takes a prompt as its last argument works. The loop just does `$LLM_CMD "$prompt"`.

## Files

```
brain-loop/
├── brain-loop.sh      # The loop (this IS the agent)
├── config.sh          # Which LLM to use + timing
├── AGENT.md           # Who the agent is (edit this)
├── INSTRUCTIONS.md    # What to do each cycle (edit this)
├── install.sh         # Optional: run as systemd service
├── data/
│   ├── tasks.md       # Task list the agent works from
│   ├── memory.md      # Rolling memory of what happened
│   └── logs/          # Per-cycle logs
├── context/           # Drop files here for the agent to read
├── output/            # Agent puts its work here
└── knowledge/         # Agent files what it learns here
```

## Make it yours

**Change the identity:** Edit `AGENT.md` — tell it who it is, what it can do, what it should care about.

**Change the instructions:** Edit `INSTRUCTIONS.md` — tell it what to do each cycle.

**Feed it data:** Drop `.md` or `.txt` files into `context/` — the agent reads everything in there each cycle.

**Give it tasks:** Edit `data/tasks.md` — it reads this every cycle and works from it.

## Run as a service

```bash
chmod +x install.sh
./install.sh my-agent
# Now it runs on boot and restarts if it crashes
```

## Pre-built agents

Need something more specific? These are ready-to-run agents built on this same loop:

| Agent | What it does | Repo |
|-------|-------------|------|
| **[Seed](https://github.com/seedpi867-cmd/seed)** | Full autonomous agent with drives, emotions, knowledge base, essay writing | The reference implementation |

> More coming: research assistant, code reviewer, content pipeline, system monitor

## License

MIT — do whatever you want.
