

def arithmetic_arranger(problems, show_answers=False):
  #initialize list for first operand, operator with second operand, dash lines, and results 
  first_line = []
  second_line = []
  dashes = []
  results = []

  if len(problems) > 5:
    return "Error: Too many problems."
  
  #loop through all problems 
  for problem in problems:
    pieces = problem.split()

    #situations that cause error messages
    if pieces[1] not in ('+','-'):
      return "Error: Operator must be '+' or '-'."
    if pieces[0].isnumeric() == False or pieces[2].isnumeric() == False:
      return "Error: Numbers must only contain digits."
    if len(pieces[0]) > 4 or len(pieces[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    #calculate result
    total = 0 
    if pieces[1] == '+':
      total = int(pieces[0]) + int(pieces[2])      
    else:
      total = int(pieces[0]) - int(pieces[2])

    #set width of problem
    width = 0
    if len(pieces[2]) > len(pieces[0]):
      width = len(pieces[2]) + 2
    else:
      width = len(pieces[0]) + 2

    #insert strings, right adjusted by width, into separate lists to print out later 
    first_line.append(pieces[0].rjust(width))
    second_line.append(pieces[1] + pieces[2].rjust(width-1))
    dashes.append(''.rjust(width,'-'))
    results.append(str(total).rjust(width))

  #create string for each line 
  first_line_str = '    '.join(first_line)
  second_line_str = '    '.join(second_line) 
  third_line_str = '    '.join(dashes) 
  fourth_line_str = '    '.join(results)

  #create arranged_problems string depending on optional argument
  if show_answers:
    arranged_problems = first_line_str + '\n' + second_line_str + '\n' + third_line_str + '\n' + fourth_line_str
    return arranged_problems
  else:
    arranged_problems = first_line_str + '\n' + second_line_str + '\n' + third_line_str
    return arranged_problems

  