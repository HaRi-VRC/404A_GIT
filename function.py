def add_tax(price,taxrate=0.1):
    if price < 1:
        raise ValueError("金額は1円以上で指定してください")
    if taxrate < 0:
        raise ValueError("税率に負の数は設定できません")
    return int(price + price * taxrate)





if __name__ == "__main__":
    assert add_tax(1000) == 1100
    assert add_tax(1000,0.08) == 1080
    assert add_tax(1000, -0.5)
    assert add_tax(0)
    print("test")
