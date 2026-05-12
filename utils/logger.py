from loguru import logger

logger.add(
    "logs/ai_system.log",
    rotation="5 MB",
    level="INFO"
)

logger.info("AI System Started")