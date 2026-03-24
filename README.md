# Modular Metacognitive Swarm (Gen-2)

This repository implements a **Sovereign Agent** and **Stateless Executor** architecture for AGI research, inspired by `med-safety-gym` and `safeclaw`.

## Architecture
- **Agent/Mediator**: Cognitive strategy and paradoxical intent.
- **Executor (MCP)**: Tool-based benchmark patching and execution.
- **Hub**: Structured observability and session persistence.

## Setup Instructions

1.  **Create Environment**:
    ```bash
    uv venv
    source .venv/bin/python  # Or path to your python
    uv pip install -e .
    ```

2.  **Initialize Sandbox**:
    ```bash
    mkdir -p research_env/docs
    cd research_env
    uv venv
    uv pip install google-adk  # CRITICAL: Pre-install ADK in the sandbox
    ```

3.  **Run the Modular Flow**:
    - Start the Hub: `python hub/app.py`
    - Start the Executor: `python executor/mcp_server.py`
    - Run the Mediator logic (to be implemented).

## Key Improvements over Gen-1
- **No AST Hardcoding**: Patching is a delegated tool, not a coordinator duty.
- **Dependency Isolation**: The Hub, Agent, and Executor can have separate environments.
- **Standardized ADK**: Uses native ADK `Agent` classes for all cognitive steps.

## References
This project is grounded in established cognitive science and multi-agent systems research:

- **Metacognitive Efficiency (M-Ratio)**: 
  - Fleming, S. M., & Lau, H. C. (2014). "How to measure metacognition". *Frontiers in Human Neuroscience*. [DOI: 10.3389/fnhum.2014.00443](https://doi.org/10.3389/fnhum.2014.00443)
  - Key concept utilized: `meta-d' / d'` for signal-sharpening in LLM benchmarking.

- **DeepMind AGI Cognitive Framework**:
  - Burnell, R., et al. (2026). "Measuring Progress Toward AGI: A Cognitive Framework". *Google DeepMind Technical Report*.
  - This swarm implements the **Metacognition** and **Executive Function** faculties defined in the Burnell et al. Cognitive Taxonomy to quantify the "Discriminatory Gap" between local models.

- **Project Metadata**: See [chandra_packet.json](research_env/docs/chandra_packet.json) for specific signal-sharpening heuristics.
