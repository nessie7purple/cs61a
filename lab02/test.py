def cake():
    print('beefs')

    def pie():
        print('sweets')
        return 'cake'

    return pie


chocolate = cake()
print(chocolate)
chocolate()
print("-----")
more_chocolate, more_cake = chocolate(), cake
print("-----")
more_chocolate
