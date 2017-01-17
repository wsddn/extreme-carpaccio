
# >= 50 000 EUR	15 %
# >= 10 000 EUR	10 %
# >= 7 000 EUR	7 %
# >= 5 000 EUR	5 %
# >= 1 000 EUR	3 %

standard_reductions = {
    50000 : 0.15,
    10000 : 0.1,
    7000 : 0.07,
    5000 : 0.05,
    1000 : 0.03,
}

def reduce_total(after_tax, reduction_type):
    print("REDUCTION TYPE " + reduction_type)

    if reduction_type == "STANDARD":
        for key in sorted(standard_reductions.keys(), reverse=True):
            if after_tax >= key:
                return (1 - standard_reductions[key]) * after_tax


    return after_tax

