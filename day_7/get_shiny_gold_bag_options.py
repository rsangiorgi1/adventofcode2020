# parse rule
# for example, rule:
# dim black bags contain 1 posh magenta bag, 3 mirrored turquoise bags, 2 faded tomato bags, 4 dim turquoise bags.
# becomes:
# rule = {
#     "outer_bag_color": "dim black",
#     "inner_bags": "1 posh magenta bag, 3 mirrored turquoise bags, 2 faded tomato bags, 4 dim turquoise bags"
# }

def count_bag_color_options(data, color):
    rules = parse_rules(data)
    colors_already_found_by_checking_rules = []
    counter = 0
    while True:
        counter += 1
        old_length = len(colors_already_found_by_checking_rules)
        colors_already_found_by_checking_rules = get_possible_outer_bag_colors_by_checking_rules(rules, color, colors_already_found_by_checking_rules)
        if old_length == len(colors_already_found_by_checking_rules):
            break

    print(f"looped {counter} times")
    return len(colors_already_found_by_checking_rules)

def can_contain_color(rule, desired_color, bags_that_can_contain_color):
    inner_bags_rule = rule["inner_bags"]
    return desired_color in inner_bags_rule or any((inner_bags_rule.find(color)!= -1) for color in bags_that_can_contain_color)

def get_possible_outer_bag_colors_by_checking_rules(rules, color, bags_found_that_can_contain_color):
    new_set = []

    for rule in rules:
        if can_contain_color(rule, color, bags_found_that_can_contain_color):
            new_set.append(rule["outer_bag_color"])
    return list(set(new_set))

def parse_rules(data):
    parsed_rules = []
    for rule in data:
        parsed_rule_template = {}
        # set outer bag color
        parsed_rule_template["outer_bag_color"] = rule.split(" contain")[0].replace(" bags", "")
        # set inner bag rules
        inner_bags = rule.split("contain ")[1]
        parsed_rule_template["inner_bags"] = inner_bags
        parsed_rules.append(parsed_rule_template)
    # print(parsed_rules)
    return parsed_rules

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    print(count_bag_color_options(data_to_list("./data"), "shiny gold"))
    # print(count_bag_color_options(data_to_list("./tdata"), "shiny gold"))