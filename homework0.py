class test:

  def __init__(self):

  def appendsums(lst):
      if len(lst) <=3:
          to_be_appended = 0
          for values in range(0,len(lst)):
              to_be_appended += values
          lst.append(to_be_appended)

      else:
          to_be_appended = 0
          index = 1
          while(index <= 3):
              to_be_appended += lst[-index]
              index+=1
          lst.append(to_be_appended)
