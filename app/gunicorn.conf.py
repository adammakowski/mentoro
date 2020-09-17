import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 3 + 1
worker_connections = 10240
limit_request_line = 8190
loglevel = "info"