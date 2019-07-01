def koushui_create_people(arg):
    def inner():
        print('加口唾沫')
        arg()

    return inner


@koushui_create_people
def create_people():
    print('抓泥巴，捏个人，吹口气，活了！')


create_people()
