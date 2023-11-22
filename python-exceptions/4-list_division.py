#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else None
            element_2 = my_list_2[i] if i < len(my_list_2) else None

            if element_1 is None or element_2 is None:
                raise IndexError("out of range")

            result = element_1 / element_2
            result_list.append(result)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)

        except (TypeError, ValueError):
            print("wrong type")
            result_list.append(0)

        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list
