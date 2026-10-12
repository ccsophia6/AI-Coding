"""房贷计算器

用法:
    python mortgage_calculator.py <贷款总额(万元)> <贷款年限(年)> <年利率(%)> <还款方式 1/2>

示例:
    python mortgage_calculator.py 100 30 3.1 1   # 100万、30年、年利率3.1%、等额本息
    python mortgage_calculator.py 100 30 3.1 2   # 同上，等额本金
"""
import sys


def calc_equal_payment(principal: float, annual_rate: float, months: int) -> None:
    """等额本息：每月还款额固定"""
    monthly_rate = annual_rate / 12
    # 等额本息月供公式：P * r * (1+r)^n / ((1+r)^n - 1)
    payment = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    total = payment * months
    print("【等额本息】")
    print(f"  每月还款: {payment:,.2f} 元")
    print(f"  还款总额: {total:,.2f} 元")
    print(f"  支付利息: {total - principal:,.2f} 元")


def calc_equal_principal(principal: float, annual_rate: float, months: int) -> None:
    """等额本金：每月还款额逐月递减"""
    monthly_principal = principal / months
    monthly_rate = annual_rate / 12
    first = monthly_principal + principal * monthly_rate
    last = monthly_principal + monthly_principal * monthly_rate
    # 总利息 = r * 本金 * (期数+1) / 2
    total_interest = (months + 1) * principal * monthly_rate / 2
    print("【等额本金】")
    print(f"  首月还款: {first:,.2f} 元")
    print(f"  末月还款: {last:,.2f} 元")
    print(f"  还款总额: {principal + total_interest:,.2f} 元")
    print(f"  支付利息: {total_interest:,.2f} 元")


def main() -> None:
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    principal = float(sys.argv[1]) * 10000
    months = int(float(sys.argv[2])) * 12
    annual_rate = float(sys.argv[3]) / 100
    method = sys.argv[4]
    if method == "1":
        calc_equal_payment(principal, annual_rate, months)
    elif method == "2":
        calc_equal_principal(principal, annual_rate, months)
    else:
        print("还款方式只能是 1（等额本息）或 2（等额本金）")
        sys.exit(1)


if __name__ == "__main__":
    main()
