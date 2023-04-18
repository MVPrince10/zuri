# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count = 0
    while True:
        try:
            print_hi('araksan')
        except KeyboardInterrupt as exc:
            print('exc')
            count += 1
            if count > 1:
                break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
