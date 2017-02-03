import unittest


def dp_make_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def build_change_list(coins_used, change):
    change_list = []
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        change_list.append(this_coin)
        coin = coin - this_coin
    return change_list


def main():
    amnt = 27
    clist = [1, 5, 10, 21, 25]
    coins_used = [0]*(amnt+1)
    coin_count = [0]*(amnt+1)

    print("Making change for", amnt, "with", clist, "coins requires")
    print(dp_make_change(clist, amnt, coin_count, coins_used), "coins")
    print("They are:")
    print(build_change_list(coins_used, amnt))
    # print("The used list is as follows:")
    # print(coins_used)

if __name__ == '__main__':
    main()


class TestMakeChange(unittest.TestCase):

    def test_test2(self):
        amnt = 63
        clist = [1, 5, 10, 21, 25]
        coins_used = [0] * (amnt + 1)
        coin_count = [0] * (amnt + 1)
        expected_coins = [1]
        dp_make_change(clist, amnt, coin_count, coins_used)
        change_list = build_change_list(coins_used, amnt)
        self.assertEqual(change_list, [])
