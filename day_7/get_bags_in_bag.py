def count_bags(data, color):
    rules = parse_rules(data)
    remaining_bags_to_check = [{
        "color": color,
        "count": 1
    }]
    total_bags_found = 0

    while len(remaining_bags_to_check) != 0:
        outer_bags_found, remaining_bags_to_check = count_bags_in_bag(remaining_bags_to_check[0], rules, remaining_bags_to_check)
        total_bags_found += outer_bags_found

    # remove most outer bag   
    return total_bags_found - 1

def count_bags_in_bag(bag, rules, remaining_bags_to_check):
    # returns number of outer bags (current bag) and which remaining bags left to check 
    number_of_bags = 0
    rule = get_rule(rules, bag["color"])
    number_of_bags = bag["count"]
    for inner_bag in rule["inner_bags"]:
        # why is this cloning a dict so important!
        bag_to_check = dict(inner_bag)
        bag_to_check["count"] = inner_bag["count"] * number_of_bags
        remaining_bags_to_check.append(bag_to_check)
    remaining_bags_to_check.remove(bag)
    return number_of_bags, remaining_bags_to_check

def get_rule(rules, outer_color):
    # todo: break if rule found
    return [rule for rule in rules if rule["outer_bag_color"] == outer_color][0]

def parse_rules(data):
    parsed_rules = []
    for rule in data:
        parsed_rule_template = {
            "outer_bag_color": "",
            "inner_bags": []
        }
        # set outer bag color
        parsed_rule_template["outer_bag_color"] = rule.split(" contain")[0].replace(" bags", "")
        # set inner bags
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
    return parsed_rules

def data_to_list(file_path):
    datafile = open(file_path)
    content = datafile.read()
    return list(map(str, content.split("\n")))

if __name__ == "__main__":
    print(count_bags(data_to_list("./data"), "shiny gold"))