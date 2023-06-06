#!/usr/bin/python3
print(*(f"0{i}" if i < 10 else str(i) for i in range(100)), sep=", ", end= " ")
