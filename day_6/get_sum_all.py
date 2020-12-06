from functools import reduce

def get_sum_all(answers):
    counted_answers = list(map(get_unanimous_answers, answers))
    return reduce(lambda x, y: x + y, counted_answers)

def get_unanimous_answers(answers_from_group):
    individual_answers = answers_from_group.split("\n")
    return len(reduce((lambda x, y: set(x).intersection(set(y))), individual_answers))

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n\n")))

if __name__ == "__main__":
    print(get_sum_all(data_to_list("./data")))