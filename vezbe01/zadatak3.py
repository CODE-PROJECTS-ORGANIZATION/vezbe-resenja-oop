def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def main():
    assert True == leap_year(1600)
    assert False == leap_year(1800)
    assert False == leap_year(1900)
    assert False == leap_year(1983)
    assert True == leap_year(1984)
    assert True == leap_year(2000)
    assert True == leap_year(2004)
    assert False == leap_year(2001)


if __name__ == "__main__":
    main()
