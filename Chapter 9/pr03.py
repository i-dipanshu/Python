for i in range(2, 21):
    with open(f"Chapter 9\Tables\Multiplication Table of {i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}")
            if j != 10:
                f.write("\n")
    