from voucher import apply_voucher

def test_negative_price():
    assert apply_voucher(100,150) == 0
