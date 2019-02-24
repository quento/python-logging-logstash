import logging
import logstash
import sys
import time


class MultipleChecker:
    """ A simple game that checks to interger values """

    def __init__(self): 
        # Show that game was initialized
        game_header()    
        game_instructions() 
        # Initialize logger class
        self.game_logger = Logger()
        # TODO - Log that game has started.  
        self.game_logger.doLog("info","python-logstash: new multiplier game initialized.")

    @property    
    def game_logger(self):
        return self._game_logger    

    @game_logger.setter
    def game_logger(self, value):
        self._game_logger = value
    

    def is_multiple(self, n, m):
        "Function takes 2 integers, checks if first is a multiple of second"
        
        # Use modulo to check if there is a remainder (i.e. if it's a multiple)    
        if n % m == 0:
            return True
        else:
            return False
        

    def play_game(self):
        """ Play the 'is multiple' game """
        status = "incomplete"
        
        while status == "incomplete":
            try:
                # Get two integers from user
                first_num = int(input("Type in first integer value: "))
                second_num = int(input("Type in second integer value: "))
                # TODO: WARNING  - Log that possible "vaue error may occurr?"
                self.game_logger.doLog("warn","python-logstash: Got user input may be null values.")
                
                print("++++++++++++++++++++++++++ RESULT +++++++++++++++++++++++++++++++")            
                
                # Check if second number is multiple of first 
                # TODO: INFO log game result           
                if self.is_multiple(first_num, second_num):
                    print("{0} is a multiple of {1}.".format(second_num, first_num))
                else:            
                    print("{0} is not a multiple of {1}.".format(second_num, first_num))
                
                print("*****************************************************************")
                self.game_logger.doLog("info","python-logstash: game success.")
                status = "complete"
                
            except ValueError:
                # If non-numeric value is typed, show error message
                error_display("ERROR: Please type in numeric input(s).")
                # TODO: ERROR Log Value Error
                self.game_logger.doLog("exception","python-logstash: ValueError occurred")


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

    def doLog(self,alert_type,msg):
        """ Write log message based on alert_type param """
        if alert_type == "info":
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

# Utility Functions to help with the display in the game.
def game_header():
    """ Display game msg or error """
    print("*****************************************************************")
    print("********************** Is a Multiple Of *************************")
    print("*****************************************************************")

def game_instructions():
    """ Display the game instructions """
    print("INSTRUCTIONS")
    print("Get two integers from user, check if 1st is a multiple of the 2nd.")

def error_display(error_msg):
    """ Display error messages """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+            ", error_msg, "          +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


def main():
    "Get two integers from user, check if 1st is multiple of 2nd"
    
    # Initialize the multiplier game class    
    multiplier_game = MultipleChecker()
    # play the game
    multiplier_game.play_game()
  
                
if __name__ == '__main__': main()            