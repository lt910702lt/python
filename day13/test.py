def func():
    name = "name"
    def inner():
        print(name)
    inner()
    print(inner.__closure__)
func()