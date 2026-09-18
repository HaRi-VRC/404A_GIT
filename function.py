def add_tax(price,taxrate=0.1):
    return int(price + price * taxrate)






if __name__ == "__main__":
    assert add_tax(1000) == 1100
    assert add_tax(1000,0.08) == 1080
    print("test")
