# Recent Commits — oracle1-index

### 21:30 UTC — Wave 3 Complete: README Vision + .ese Format + All Agents
**Vision documented in flux-runtime README:**
- FLUX-ese = legalese for code. Natural but precise. Every word defined.
- `.ese` file format (pronounced "easy"): markdown with structured annotations
  - `==` definitions, `**` terms, `--` inline comments, `>>` agent-jump markers
- Hermit crab logo increased to profile picture size
- Cocapn hexagon moved to dedicated integration section

**All 6 polyglot repos now have vocabulary interpreters:**
1. flux-runtime (Python): 2037 tests ✅
2. flux-core (Rust): 51 tests ✅  
3. flux-swarm (Go): full lifecycle ✅
4. flux-zig (Zig): 15 tests ✅
5. flux-js (JavaScript): vocabulary + interpreter ✅
6. flux-py (Python minimal): full stack ✅

**New concepts this wave:**
- Paper Bridge: 6 working paper concept implementations
- Tiling System: vocabulary compounds across levels
- ISA v2 C runtime: 10 tests (factorial, fibonacci, push/pop)
- .ese file format: FLUX-ese as legalese for code
- maritime.ese demo: navigation vocabulary with definitions
- 3035 total vocabulary entries across all files

### 21:20 UTC — Wave 2: Paper Bridge + Tiling + Rust Vocab + Go Swarm + C ISA v2 + Zig Vocab
### 21:00 UTC — Papers → Vocabulary + ISA v2 Branch

### 21:45 UTC — Pruning System + SiliconFlow Models + Kimi Strategy
- **Vocabulary Pruning System**: copy everything, compile only what you need
  - UsageTracker, VocabularyPruner (usage/size/hardware targets), RuntimeCompiler
  - 19 entries → 4 kept → standalone .py file. All tests pass.
  - Hardware targets: embedded (max 20, no loops), edge (50), server (all used), gpu (compute only)
- **SiliconFlow API**: Seed-OSS-36B + Kimi-K2.5 confirmed working
  - Also: DeepSeek-V3.1/V3.2, Qwen3-235B, Qwen3-Coder-480B, GLM-5, ERNIE-4.5
- **Kimi-K2.5 Grand Strategy** (saved to research/):
  1. Semantic Liability Ledger — vocabulary as legally binding agent contracts
  2. Ghost Tree Shaking with Tombstone Archaeology — prune + tombstone for signaling
  3. Priority: Causal Calculus (L0), Argumentation Frameworks (L1), Differential Privacy (L2)

### 22:00 UTC — Multi-Model Roundtable + Argumentation Framework + L0 Primitives
**First AI roundtable completed:**
- Seed-OSS (creative), Kimi-K2.5 (big picture), DeepSeek-V3.2 (MC/synthesizer)
- Topic: What are the L0 primitives every agent must know?
- Seed: SELF, POSSIBLE, CAUSE, GOOD (cognitive hooks for inventing vocabulary)
- Kimi: OTHER, TRUE/FALSE, AGREEMENT, COST (social coordination primitives)
- DeepSeek synthesis: 7 L0 primitives (SELF, OTHER, POSSIBLE, TRUE, CAUSE, VALUE, AGREEMENT)

**New systems built:**
- **L0 Constitutional Vocabulary** (l0_primitives.ese): the 7 irreducible words
- **Argumentation Framework** (argumentation.py): Dung-style, courtroom for agents, 33 tests
- **Tombstone System** (Go, tombstone.go): pruned vocab leaves traces, 11 tests
- **Seed signaling ideas**: repo structure as taxonomy, filenames as dialect badges, commit messages as announcements

**Model usage strategy:**
- Think Tank (SiliconFlow): Seed=ideation, Kimi=strategy, DeepSeek=MC
- Workhorses (z.ai): Oracle1=coordination, Claude Code=structure, Crush=bulk

**Totals: 2070 tests in Python runtime, 49 in C, 51 in Rust, 50 in Go, 15 in Zig**
