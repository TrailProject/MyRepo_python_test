import argparse

def calculateSumOfLineWidth(line=[]):
    sum_Width=0 
    for word in line:
        sum_Width+=len(word)
    #print("calculating sum of width of passed line",sum_Width)
    return sum_Width

def justify_paragraph(paragraph, paragraph_width):
    words = paragraph.split()
    #print(words)
    lines = []
    current_line = []
    
    #count=0

    for word in words:
        #count+=1
        #print("for loop iteration count",count)
        if len(' '.join(current_line + [word])) <= paragraph_width:
            current_line.append(word)
            #print("if condition",current_line)
        else:
            #used to append the current_line to lines because it is already satisfied with width matching to paragraph_width 
            lines.append(current_line)
            #print("appended lines are",lines)
            current_line = [word]
            #print("else condition",current_line)
        #++count
        
    #for adding last current_line into lines if its not added
    if current_line:
        lines.append(current_line)
    
    #For Adding spaces in gap
    justified_lines = []
    for line in lines:
        #number of spaces_to_add in between words to match paragraph_width
        spaces_to_add = paragraph_width - calculateSumOfLineWidth(line)
        #spaces_to_add = paragraph_width - sum(len(word) for word in line)
        
        num_gaps = len(line) - 1
        #if line is having more than 1 word then if block code will trigger
        if num_gaps > 0:
            spaces_per_gap = spaces_to_add // num_gaps
            #print("spaces_per_gap",spaces_per_gap)
            extra_spaces = spaces_to_add % num_gaps
            #print("extra_spaces",extra_spaces)
            justified_line = ''
            for i, word in enumerate(line):
                justified_line += word
                if i < num_gaps:
                    justified_line += ' ' * spaces_per_gap
                    if extra_spaces > 0:
                        justified_line += ' '
                        extra_spaces -= 1

        #if line is having only one word then else block code will trigger
        else:
            justified_line = line[0] + ' ' * spaces_to_add
        justified_lines.append(justified_line)

    return justified_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Justify Paragraph to a specific width')
    parser.add_argument('paragraph', nargs='?', type=str, help='Enter paragraph to justify')
    parser.add_argument('paragraph_width', nargs='?', type=int, help='Width to justify the paragraph to')
    args = parser.parse_args()

    if not args.paragraph or not args.paragraph_width:
        paragraph = input("Enter paragraph data: ")
        paragraph_width = int(input("enter paragraph width: "))
    else:
        paragraph = args.paragraph
        paragraph_width = args.paragraph_width
    my_final_list=justify_paragraph(paragraph, paragraph_width)
    print(my_final_list)
    # Sample input
    # Output
    for i in range(len(my_final_list)):
        print("Array ["+str(i+1)+"] = \""+my_final_list[i]+"\"")
