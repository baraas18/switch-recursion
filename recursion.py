# ex .1 :
def fibonacci(num):
    if num <= 1 : 
        return num 
    return fibonacci(num - 1) + fibonacci(num - 2)


#ex 2 : 
def find_subsets(lst):
    if len(lst)==0:
        return [[]]
    first_element = lst[0]
    all_subsets_without_first = find_subsets(lst[1:])
    result = []
    for sub in all_subsets_without_first:
        result.append(sub)
        result.append([first_element] + sub) 
    return result  


if __name__ == "__main__":
#Example

   print(fibonacci(6)) 
   print(find_subsets([1,2,3]))






