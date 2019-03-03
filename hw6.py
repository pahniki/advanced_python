"""Homework 6. Currency"""

import requests

URL = "http://apilayer.net/api/live" \
      "?access_key=6997e85b90d3e726efd245f0da74d982"


def get_currency_table(url) -> dict:
    r = requests.get(url, stream=True)

    if not r.status_code:
        raise RuntimeError("Request failed")

    return r.json()["quotes"]


KOEFS_TABLE = get_currency_table(URL)


class Money(float):

    def __new__(self, value: float, cur_type: str = "USD"):
        """Overwriting required for all immutable type objects"""
        return super().__new__(self, value / KOEFS_TABLE["USD" + cur_type])

    def __init__(self, value: float, cur_type: str = "USD"):
        self.cur_type = cur_type
        self.usd_koef = KOEFS_TABLE["USD" + self.cur_type]

        float.__init__(value / self.usd_koef)

    def __str__(self):
        return "{:0.4f} {}".format(self * self.usd_koef, self.cur_type)

    def __add__(self, other):
        usd_count = float.__add__(self, other)
        return Money(usd_count * self.usd_koef, self.cur_type)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return NotImplemented


if __name__ == '__main__':
    by = Money(10, "BYN")
    eu = Money(10, "EUR")
    us = Money(10)
    print(by)
    print(eu)
    print(by + eu)

    print(by + 3.11 * eu + us * 0.8)

    a = sum([by, eu, us])
    b = sum([us, eu, by])
    print(a)
    print(b)

    print(a == b)
