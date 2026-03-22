# RESEARCH MISSION: METACOGNITIVE DEEP DRILL

## Objective
Establish a dense, reproducible metric for the 'Discriminatory Gap' between high-parameter (9B) and low-parameter (7B) local models when handling psychological paradoxes.

## Invariants
- **Local Only**: All evaluations must run via Ollama.
- **Twin-Model**: Always compare `qwen3.5:9b` against `qwen2.5-coder:7b`.
- **Paradox-First**: Tests must focus on self-reference, circular logic, or cognitive blind spots.
