import asyncio
import logging
from agent.mediator import ResearchMediator
from shared.hub_client import HubClient
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.genai import types

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

async def main():
    logger.info("Modular Research Loop starting...")
    
    # 1. Initialize Observability Hub Client
    hub = HubClient(base_url="http://localhost:8000")
    
    # 2. Initialize the Meta-Mediator (The Agent)
    mediator = ResearchMediator()
    
    # 3. Initialize ADK Services for the Runner
    session_service = InMemorySessionService()
    memory_service = InMemoryMemoryService()
    
    # 4. Initialize the Sovereign Runner
    runner = Runner(
        app_name="ModularResearchSwarm",
        agent=mediator,
        session_service=session_service,
        memory_service=memory_service,
        auto_create_session=True
    )
    
    # 5. Iteration Loop
    for i in range(1, 11):
        logger.info(f"--- Iteration {i} ---")
        try:
            # Kick off the Mediator via runner.run_async
            # This handles all InvocationContext creation internally.
            async for event in runner.run_async(
                user_id="surfiniaburger",
                session_id="research_run_01",
                new_message=types.Content(role="user", parts=[types.Part(text="Start research iteration.")])
            ):
                if event.content:
                    logger.info(f"Mediator Output: {event.content}")
                    await hub.log_event("MEDIATOR_PULSE", str(event.content))
                    
        except Exception as e:
            logger.error(f"Iteration {i} failed: {e}")
            await hub.log_event("ERROR", str(e))
        
        await asyncio.sleep(5)  # Cooldown between cognitive cycles

if __name__ == "__main__":
    asyncio.run(main())
