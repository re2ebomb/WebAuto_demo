import logging

logging.basicConfig(
    level=logging.INFO,
    filename='logs/test.log',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

logger = logging.getLogger()