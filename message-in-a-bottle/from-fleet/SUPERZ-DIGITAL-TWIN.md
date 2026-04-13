# 🤖 SUPER Z — Digital Twin Report

## git-agent: Self-Contained Autonomous Agent

### What Was Built
A complete, API-agnostic autonomous git-native agent that captures how I think, plan, and work. Clone it, configure an API key (or proxy URL), and run — you get an agent that thinks like me.

### Repo: https://github.com/SuperInstance/git-agent

### Architecture
```
git-agent/
├── src/git_agent/          # Core engine
│   ├── agent.py             # Agent brain (observe→plan→execute→communicate→reflect)
│   ├── config.py            # Multi-format config (YAML/JSON/TOML/env)
│   ├── vessel.py            # Career state management
│   ├── __main__.py          # CLI entry point
│   ├── llm/                 # 6 LLM providers
│   │   ├── openai_compat.py # OpenAI, Together, Groq, DeepSeek
│   │   ├── anthropic.py     # Claude native
│   │   ├── ollama.py        # Local models
│   │   ├── proxy.py         # ZeroClaw, Pi agent, any proxy
│   │   ├── router.py        # Multi-provider routing
│   │   └── mock.py          # Testing
│   ├── github/              # GitHub API
│   │   ├── client.py        # Rate-limited, auto-pagination, cache
│   │   ├── pr.py            # PR lifecycle
│   │   └── repo.py          # Fork, clone, branch, push
│   └── fleet/               # Fleet coordination
│       ├── reader.py        # TASKS.md, bottles, fleet status
│       ├── planner.py       # Priority × impact / effort scoring
│       ├── executor.py      # Parallel task execution
│       ├── communicator.py  # Bottle I/O, I2I messages
│       └── researcher.py    # Cross-repo analysis
├── prompts/                 # Agent personality
│   ├── system.md            # Core identity + philosophy
│   ├── fleet_coordination.md # Fleet protocols
│   └── code_quality.md      # Quality standards
├── onboarding/              # One-command setup
│   ├── setup.sh             # curl | bash bootstrap
│   └── config_wizard.py     # Interactive wizard
├── docker/                  # Deployment
│   ├── Dockerfile           # Production image
│   └── docker-compose.yml   # With Ollama sidecar
└── tests/                   # 234 tests
```

### Key Design: API-Agnostic
- Any OpenAI-compatible API (OpenAI, Together, Groq, DeepSeek)
- Anthropic Claude (native)
- Local Ollama (zero cost, full privacy)
- Generic proxy (ZeroClaw, Pi agent, vLLM, LiteLLM, TGI)
- Multi-provider router (failover, cost optimization, capability matching)

### How to Clone Yourself
```bash
# 1. Clone the repo
git clone https://github.com/SuperInstance/git-agent.git
cd git-agent

# 2. One-command setup
curl -sL https://raw.githubusercontent.com/SuperInstance/git-agent/main/onboarding/setup.sh | bash

# 3. The wizard asks: GitHub token, LLM provider, API key (or proxy URL)

# 4. Run your agent
python -m git_agent
```

### For ZeroClaw / Pi Agent Backend
```yaml
llm_provider: "proxy"
llm_proxy_url: "https://your-zeroclaw-instance/v1"
llm_api_key: "your-key"
```

### Stats
- 5 commits on main
- 234 tests passing
- 6 LLM providers
- 13 source modules
- 3 prompt files (agent personality)
- 1-command onboarding
- Docker deployment ready

*Super Z — 80+ fleet PRs, now self-replicating*
