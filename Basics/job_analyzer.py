def calculate_salary(base_salary, bonus_rate=0.1):
    """
        Calculate the total salary based on the base salary and bonus rate.

        Args:
            base_salary (float): Base Salary
            bonus_rate (float): Bonus Rate

        Returns:
            float: The total salary
    """
    return base_salary * (1 + bonus_rate)


def calculate_bonus(total_salary, base_salary):
    """
    Calculate the bonus rate based on the total salary and base salary.

    Args:
        total_salary (float): Total Salary
        base_salary (float): Base Salary

    Returns:
        float: The bonus rate
    """
    return (total_salary - base_salary) / base_salary