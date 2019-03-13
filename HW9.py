"""Homework 9. Knapsack problem"""


def get_data():
    data = []

    with open("./data") as f:
        for line in f.readlines():
            ref_line = line.strip().split(',')
            data.append([ref_line[0], int(ref_line[1]), int(ref_line[2])])

    return data


def chose_greedy(weight: float, data: list):
    result = []
    for item in sorted(data, key=lambda x: x[1] / x[2]):
        if weight - item[1] > 0:
            result.append(item)
            weight -= item[1]

    return result


if __name__ == '__main__':
    final_list = chose_greedy(400, get_data())

    print(final_list)
    print("Weight: " + str(sum([x[1] for x in final_list])))
    print("Value: " + str(sum([x[2] for x in final_list])))
