def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_for_adult=float(37550.0)*no_of_adults
    rate_for_child=(37550/3)*no_of_children
    
    (total_ticket_cost1)=rate_for_child+rate_for_adult
    service_tax=(total_ticket_cost1)*(7/100)
    total_cost=total_ticket_cost1+service_tax
    discount=(total_cost)*(10/100)
    total_ticket_cost=total_cost-discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
