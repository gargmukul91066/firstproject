import sys  # for system

class customexception(Exception):    # here 'Exception' is a parent class

    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        pass

    def __str__(self):
        pass

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        #print(e)
        raise customexception(e,sys)