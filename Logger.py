import logging
import logstash
import sys
import time

class Logger:
    """ Logger class uses logstash and sends data to ELK stack as well. """
    def __init__(self):
        # Create logger and levels
        self._app_logger = logging.getLogger('python-logstash-logger')
        self.app_logger.setLevel(logging.INFO)
        # Create a stream and logstash handler to show logs to output and send to ELK stack.
        self._stream_handler = logging.StreamHandler()
        self.app_logger.addHandler(logstash.LogstashHandler('34.227.222.14', 5959, version=1))  
        self.app_logger.addHandler(self.stream_handler)
    
    @property
    def app_logger(self):
        return self._app_logger

    @app_logger.setter
    def app_logger(self, value):
        self._app_logger = value

    @property
    def stream_handler(self):
        return self._stream_handler

    @stream_handler.setter
    def stream_handler(self, value):
        self._stream_handler = value

    def doLog(self,alert_type,msg,extra=None):
        """ Write log message based on alert_type param """
        if alert_type == "info":
            if extra != None:
                self.app_logger.info(msg,extra=extra)
            else:
                self.app_logger.info(msg)
        elif alert_type == "debug":
            self.app_logger.debug(msg)
        elif alert_type == "warn":
            self.app_logger.warning(msg)
        elif alert_type == "error":
            self.app_logger.error(msg)
        elif alert_type == "exception":
            self.app_logger.exception(msg)
        elif alert_type == "critical":
            self.app_logger.critical(msg)

if __name__ == '__main__' : main()             