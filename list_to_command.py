#!/usr/bin/env python3

if __name__ == '__main__':
    with open('apt_manual.txt', 'r') as f:
        lines = f.read().strip().splitlines()
    with open('commands.txt', 'w') as f:
        for package in lines:
            f.write(f'apt-get install -y --no-install-recommends {package}\n')
