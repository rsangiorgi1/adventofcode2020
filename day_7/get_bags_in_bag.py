# parse rules
# for example, rule:
# dim black bags contain 1 posh magenta bag, 3 mirrored turquoise bags, 2 faded tomato bags, 4 dim turquoise bags.
# becomes:
# rule = {
#     "outer_bag_color": "dim black",
#     "inner_bags": [
#         {
#             "color": "posh magenta",
#             "count": 1
#         },
#         {
#             "color": "mirrored turqoise",
#             "count": 3
#         },
#         {
#             "color": "faded tomato",
#             "count": 2
#         },
#         {
#             "color": "dim turqoise",
#             "count": 4
#         }
#     ]
# }



def count_bags(data, color):
    rules = parse_rules(data)

    # first_rule = get_rule(rules, color)
    first_rule = get_rule(rules, "vibrant plum") # should return 11 per bag
    # first_rule = get_rule(rules, "muted yellow")
    print(f"first rule: {first_rule}")
    end_bag_count, remaining_bags_to_check = count_bags_by_rule(first_rule, rules, 2)
    print(f"bags found after first rule: {end_bag_count} and need to check bags: {remaining_bags_to_check}")

    return first_rule

def get_rule(rules, outer_color):
    # todo: break if rule found
    return [rule for rule in rules if rule["outer_bag_color"] == outer_color][0]

def count_bags_by_rule(rule, rules, number_of_bags):
    # returns # of end bags and which remainging bags to check
    end_bags_found = 0
    remaining_bags_to_check = []
    print(f"rule is {rule}")
    for inner_bag in rule["inner_bags"]:
        if is_end_bag(inner_bag["color"], rules):
            print(f"end of line for {rule['outer_bag_color']}")
            end_bags_found += inner_bag["count"] * number_of_bags
        else:
            inner_bag["count"] = inner_bag["count"] * number_of_bags
            remaining_bags_to_check.append(inner_bag)

    return end_bags_found, remaining_bags_to_check

def count_end_bags():
    number_of_end_bags = 0
    for bag in bags:
        if is_end_bag(bag[""])
    return number_of_end_bags


def is_end_bag(outer_color, rules):
    rule = get_rule(rules, outer_color)
    print(rule)
    print(rule["inner_bags"])

    return len(rule["inner_bags"]) == 0

def parse_rules(data):
    parsed_rules = []
    for rule in data:
        parsed_rule_template = {
            "outer_bag_color": "",
            "inner_bags": []
        }
        # set outer bag color
        parsed_rule_template["outer_bag_color"] = rule.split(" contain")[0].replace(" bags", "")
        # set inner bag rules
        inner_bags = rule.split("contain ")[1].replace(".", "")
        if inner_bags == 'no other bags':
            parsed_rule_template["inner_bags"] = []
        else:
            bags = inner_bags.split(",")
            for bag in bags:
                some_bag = bag.strip()
                parsed_rule_template["inner_bags"].append(
                    {
                    "color": " ".join(some_bag.split(" ")[1:3]),
                    "count": int(some_bag.split(" ")[0])
                    }
                )
        parsed_rules.append(parsed_rule_template)
    # print(parsed_rules)
    return parsed_rules

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    # print(count_bag_color_options(data_to_list("./data"), "shiny gold"))
    
    print(count_bags(data_to_list("./tdata"), "shiny gold"))
