class Dad:

    football = 1

    pass


class Son(Dad):
    dance=1
    def is_dance (self):
        print(f"yes i can dance proparly {self.dance}")   # it is an example of polymorphysm since a methode is morphed
    pass


class Grandson(Son):
    dance=6
    # def is_dance (self):
    #     print(f"yes i can dance {self.dance}")
    pass


darry = Dad()
larry = Son()
harry = Grandson()


harry.is_dance()
s=harry.football
print(s)