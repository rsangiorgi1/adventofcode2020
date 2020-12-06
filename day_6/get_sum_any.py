from functools import reduce

def get_sum(answers):
    counted_answers = list(map(lambda x: len(set(x)), answers))
    return reduce(lambda x, y: x + y, counted_answers)

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    grouped_content = list(map(str, content.split("\n\n")))
    return list(map(lambda x: x.replace("\n", ""), grouped_content))

if __name__ == "__main__":
    print(get_sum(data_to_list("./data")))