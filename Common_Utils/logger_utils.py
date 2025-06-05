import logging
import io

# Create in-memory log stream
log_stream = io.StringIO()

# Create and configure logger
logger = logging.getLogger()
logger.setLevel(logging.ERROR)  # You can change this to ERROR, DEBUG, etc.
logger.propagate = False  # Prevent duplicate logs

# Add stream handler if not already added
if not logger.handlers:
    stream_handler = logging.StreamHandler(log_stream)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# Make log_stream accessible
logger.stream = log_stream