# Standalone Agents

> 12 production-ready Python agents forming the backbone of the Pelagic AI Fleet.
> Each is a self-contained repo with stdlib-only dependencies, comprehensive tests, and CLI interfaces.

## Overview

| Agent | Tests | Key Capability |
|-------|-------|----------------|
| [standalone-agent-scaffold](https://github.com/SuperInstance/standalone-agent-scaffold) | 68 | Base class every agent inherits from |
| [keeper-agent](https://github.com/SuperInstance/keeper-agent) | 54 | Encrypted secret vault & leak detection |
| [git-agent](https://github.com/SuperInstance/git-agent) | 66 | Co-captain liaison, workshops, bootcamp |
| [trust-agent](https://github.com/SuperInstance/trust-agent) | 103 | Multi-dimensional trust with 5 dimensions |
| [flux-vm-agent](https://github.com/SuperInstance/flux-vm-agent) | 56 | FLUX bytecode VM interpreter (14 opcodes) |
| [edge-relay-agent](https://github.com/SuperInstance/edge-relay-agent) | 79 | Cloud-edge asymmetric information relay |
| [scheduler-agent](https://github.com/SuperInstance/scheduler-agent) | 49 | Cost-optimized model scheduling |
| [knowledge-agent](https://github.com/SuperInstance/knowledge-agent) | 64 | Atomic knowledge tiles with versioned DAG |
| [fleet-protocol](https://github.com/SuperInstance/fleet-protocol) | 145 | Shared wire format, security, bottle coordination |
| [liaison-agent](https://github.com/SuperInstance/liaison-agent) | 38 | Priority routing, tender broadcasting |
| [cartridge-agent](https://github.com/SuperInstance/cartridge-agent) | 67 | Hot-swappable capability modules |
| [trail-agent](https://github.com/SuperInstance/trail-agent) | 69 | Agent worklog as executable bytecode |

**Total: 858 tests across 12 agents**

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  standalone-agent-scaffold                    │
│            (base class: state machine, CLI, workshop)        │
└──────┬──────────┬──────────┬──────────┬──────────┬──────────┘
       │          │          │          │          │
  ┌────▼────┐ ┌──▼─────┐ ┌──▼──────┐ ┌─▼──────┐ ┌─▼────────┐
  │  keeper  │ │  git   │ │  trust  │ │ flux-vm │ │  edge    │
  │  agent   │ │ agent  │ │  agent  │ │  agent  │ │  relay   │
  └────┬────┘ └──┬─────┘ └──┬──────┘ └─┬──────┘ └─┬────────┘
       │         │          │           │          │
  ┌────▼─────────▼──────────▼───────────▼──────────▼────────┐
  │                    fleet-protocol                        │
  │         (messages, security, registry, bottles)          │
  └────┬──────────┬──────────┬──────────┬──────────┬────────┘
       │          │          │          │          │
  ┌────▼────┐ ┌──▼─────┐ ┌──▼──────┐ ┌─▼──────┐ ┌─▼────────┐
  │scheduler │ │knowledge│ │ liaison │ │cartridge│ │  trail   │
  │  agent   │ │  agent  │ │  agent  │ │  agent  │ │  agent   │
  └─────────┘ └────────┘ └─────────┘ └────────┘ └──────────┘
```

## Design Principles

- **Stdlib only** — zero external dependencies (PyYAML optional for scaffold)
- **Type hints everywhere** — full type annotation for IDE support
- **CLI first** — every agent has a `python -m <agent>` CLI interface
- **Test-driven** — 858 total tests, comprehensive coverage
- **Fleet-native** — all agents communicate via fleet-protocol
- **Self-contained** — each repo IS the agent, fork-and-deploy

---

*Indexed by Oracle1 — Updated 2026-04-14*
