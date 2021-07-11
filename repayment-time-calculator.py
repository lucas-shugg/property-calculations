def repayment_time(loan_taken, interest_rate, rent_pa, personal_contributions, time=0):
    
    if(loan_taken <= 0):
        
        return time
    
    loan_taken = loan_taken + (loan_taken * interest_rate) - (rent_pa + personal_contributions)
    
    return repayment_time(loan_taken, interest_rate, rent_pa, personal_contributions, time + 1)

if __name__ == '__main__':  
    print(repayment_time(400000, 0.03, 28600, 12000))
    