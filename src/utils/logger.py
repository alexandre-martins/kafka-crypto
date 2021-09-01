import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

class CryptoLogger:
    """Custom loggin configuration."""

    def __init__(self):
        self.logger = logging.getLogger("CryptoLogger")
    
    def info(self, msg):
        return self.logger.info(msg)
    
    def warn(self, msg):
        return self.logger.warn(msg)
    
    def error(self, msg):
        return self.logger.error(msg)
