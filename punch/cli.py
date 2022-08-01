#!/bin/python3

import argparse
from punch.punch import get_driver, login, punch, go_to_timewatch_website


def load_args():
    parser = argparse.ArgumentParser(description='Punch CLI')
    parser.add_argument ('--company_id', help='Company ID', type=str, required=True)
    parser.add_argument('--employee_id', help='Employee ID', type=str, required=True)
    parser.add_argument('--employee_pass', help='Employee Password', type=str, required=True)
    return parser.parse_args()


def main():
    args = load_args()
    company_id, employee_id, employee_pass = args.company_id, args.employee_id, args.employee_pass
    driver = get_driver()
    go_to_timewatch_website(driver)
    login(driver,company_id, employee_id, employee_pass)
    punch(driver)


if __name__ == '__main__':
    main()