"""Print out all the melons in our inventory."""

from melons import melons


def print_melon_inventory(melon_dict):
    """Print each melon in inventory and its corresponding attributes."""

    # loop thru melon_dict and print melon name + attributes
    for name, attributes in melon_dict.items():
        print(name.upper())
        for attribute_name, attribute_value in attributes.items():
            print(f"\t{attribute_name}: {attribute_value}")
        print("\n")

print_melon_inventory(melons)

