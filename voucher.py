def apply_voucher(total, discount):
    final_price = total - discount
    return max(0, final_price)
