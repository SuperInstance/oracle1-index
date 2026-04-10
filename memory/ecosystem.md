# Ecosystem Map — Hub Repos

The SuperInstance/Lucineer ecosystem has ~600 repos. These are the hubs everything connects to:

## Tier 1: Core Runtime

| Hub | Role | Links To |
|-----|------|----------|
| **cocapn** | Repo-first agent runtime | fleet, git-agents, deckboss, equipment |
| **git-agent** | Foundational repo-native agent | cocapn, git-claw, git-cuda-agent |
| **fleet-orchestrator** | Central coordination for 200+ vessels | fleet-*, cuda-*, nexus-* |

## Tier 2: Infrastructure

| Hub | Role | Links To |
|-----|------|----------|
| **cudaclaw** | GPU-resident SmartCRDT runtime | cuda-*, fleet-* |
| **nexus-edge-runtime** | Edge runtime with bytecode VM | nexus-*, hardware, jetson |
| **constraint-theory-core** | Rust geometric snapping library | constraint-theory-*, equipment |
| **flux-runtime** | Self-assembling agent runtime | flux-*, lumina-lang |

## Tier 3: Application Layer

| Hub | Role | Links To |
|-----|------|----------|
| **deckboss** | Flight deck for agent management | cocapn, fleet |
| **craftmind** | Minecraft AI training ground | craftmind-*, fleet |
| **fishinglog-ai** | Edge AI fishing vessel | cocapn, edge-hardware, jetson |
| **ai-character-sdk** | Unified character SDK | equipment, escalation-engine |

## Cross-Cutting

| Domain | Repos | Theme |
|--------|-------|-------|
| Memory | hierarchical-memory, Equipment-Memory-Hierarchy, collective-mind | Multi-tier cognitive memory |
| Trust | zero-trust-fleet, cuda-did, sovereign-identity, compliance-fork | Identity + compliance |
| Consensus | tripartite-rs, resonant-consensus, confidence-cascade | Multi-agent agreement |
| Learning | bandit-learner, frozen-model-rl, training-data-collector | Online + offline learning |

## Paradigm

The ecosystem follows one principle: **the repo IS the agent, git IS the nervous system**.

Agents don't use tools — they *build* tools for other agents. The human stays in the loop through a communications UI, not by puppeting skills.
