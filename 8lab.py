def file_reader_one(file):
    for line in file:
        yield print(line.strip())

def file_reader_two(file):
    while True: 
        line = file.readline()
        if not line:
            break
        yield print(line.strip())

with open('chakhokhbili_recipe.txt', 'r') as file:
    gen_one = file_reader_one(file)
    next(gen_one)
    next(gen_one)
    gen_two = file_reader_two(file)
    next(gen_two)
    next(gen_two)
    
    #demo on 20 lines
    for i in range(20):  
        next(gen_two)
    