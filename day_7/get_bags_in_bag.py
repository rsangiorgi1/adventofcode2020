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
    remaining_bags_to_check = [{
        "color": color,
        "count": 1
    }]
    total_bags_found = 0
    count = 0

    for rule in rules:
        print(is_end_bag(rule["outer_bag_color"], rules))

    while len(remaining_bags_to_check) != 0:
        print("\n")
        count += 1
        print(f"""bags left to check: {remaining_bags_to_check},
XXXX now checking bag {remaining_bags_to_check[0]}...""")
        new_end_bags_found, remaining_bags_to_check = count_bags_in_bag(remaining_bags_to_check[0], rules, remaining_bags_to_check)
        total_bags_found += new_end_bags_found
        print(f"--new end bags found: {new_end_bags_found}, total bags found so far: {total_bags_found} and need to check bags: {remaining_bags_to_check}")

    # remove most outer bag   
    return total_bags_found - 1
    # return "ok!"

def get_rule(rules, outer_color):
    # todo: break if rule found
    return [rule for rule in rules if rule["outer_bag_color"] == outer_color][0]

def count_bags_in_bag(bag, rules, remaining_bags_to_check):
    print("#######")
    print(rules[1])
    # returns number of outer bags (current bag) and which remaining bags left to check 
    number_of_bags = 0
    rule = get_rule(rules, bag["color"])
    print(f"rule for {bag['color']}: {rule}")
    print(f"is end bag? {is_end_bag(bag['color'], rules)} ")
    number_of_bags = bag["count"]
    if is_end_bag(bag["color"], rules):
        print(f"""no inner bags for for {bag['color']}""")
    for inner_bag in rule["inner_bags"]:
        print(f"""found inner bags for for {bag['color']}""")
        print(inner_bag)
        new_bag = dict(inner_bag)
        new_bag["count"] = inner_bag["count"] * number_of_bags
        remaining_bags_to_check.append(new_bag)

    # print(len(remaining_bags_to_check))
    remaining_bags_to_check.remove(bag)
    # print(len(remaining_bags_to_check))
    print(f"should add {number_of_bags}")
    return number_of_bags, remaining_bags_to_check

def is_end_bag(outer_color, rules):
    rule = get_rule(rules, outer_color)
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
    print(count_bags(data_to_list("./data"), "shiny gold"))