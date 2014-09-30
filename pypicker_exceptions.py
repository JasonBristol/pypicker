import sys

''' Custom PyPicker Exception Classes '''

class PyPickerException(Exception):
  ''' This is the base PyPicker error class '''
  pass

class BoundsException(PyPickerException):
  ''' This error occurs when the n argument is out of bounds '''
  def __init__(self, msg):
    self.msg = str(msg)

class OutputException(PyPickerException):
  ''' This error occurs when the output file cannot be written to '''
  def __init__(self, msg):
    self.msg = str(msg)

class ResultSetException(PyPickerException):
  ''' This error occurs when the requested result set is greater than the sample size '''
  def __init__(self, msg):
    self.msg = str(msg)
