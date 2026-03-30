import first_module

first_module.main()

print("This is the second module {} {}".format(__name__, first_module.__name__))