"""TODO(ogolovatyi): DO NOT SUBMIT without one-line documentation for task1.
My task from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
TODO(ogolovatyi): DO NOT SUBMIT without a detailed description of task1.
"""

#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function

#from absl import app
#from absl import flags

#tLAGS = flags.FLAGS


#def main(argv):
#  if len(argv) > 1:
#    raise app.UsageError('Too many command-line arguments.')

#if __name__ == '__main__':
#  app.run(main)

name = raw_input("What is your Name: ")
print ("your name is:" +name)
age = int(raw_input("Enter your age: "))
if age <100:
 age100 = int(100-age)
 print ("you will reach 100 in " +str(age100)+" years.")
else:
 print ("Your age is already >100 years")

repeat=int(raw_input("repeats number: "))
for i in range(repeat):
    print ("this is repeat number"+str(i))


