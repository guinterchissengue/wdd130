'''
Author: Guinter Chissengue

Program: Service Queue Simulator for Customer Attendance

Enhancements: Several possible improvements to this program exist in the future, and some possible improvements 
could involve the addition of two or more service counters so that customers will be able to receive service faster 
than they would currently receive service at an existing single service counter. Another possibility could develop a 
way to rank customers when they arrive at service counters (i.e., find a way to effectively identify a priority customer, 
or an emergency incident) in order to provide them with prompt service compared to non-priority customers. Another potential 
way to improve this program would be by building a user-friendly and visual interface through which customers would communicate 
directly with customer service representatives or by pulling up electronic files for a customer’s data from a stored database 
instead of generating random numbers for display purposes.
'''

import random
from datetime import datetime
import math

# -----------------------------
# Queue Simulation Functions
# -----------------------------

def generate_customers(num_customers):

    # List of customers with arrival times.
    customers = []
    for i in range(num_customers):
        customers.append({
            'id': i + 1,
            'arrival_time': random.randint(0, 30)
        })
    return customers


def add_to_queue(queue, customer):

    # Add a customer to the queue.
    queue.append(customer)
    return queue


def calculate_wait_time(arrival_time, service_time):
    
    # Calculate waiting time.
    wait = service_time - arrival_time
    return max(wait, 0)


def serve_customer(queue, current_time):

    # Serve the first customer in the queue.
    if not queue:
        return None, current_time

    customer = queue.pop(0)
    service_duration = random.randint(2, 6)
    start_time = max(customer['arrival_time'], current_time)
    finish_time = start_time + service_duration

    wait_time = calculate_wait_time(customer['arrival_time'], start_time)

    return {
        'id': customer['id'],
        'wait_time': wait_time,
        'service_duration': service_duration
    }, finish_time


def simulate_service(customers):

    # Simulate the service queue.
    queue = []
    served_customers = []
    current_time = 0

    for customer in customers:
        add_to_queue(queue, customer)

        served, current_time = serve_customer(queue, current_time)
        if served:
            served_customers.append(served)

    return served_customers


def get_statistics(served_customers):

    #Return statistics from the simulation.
    if not served_customers:
        return 0, 0

    total_wait = sum(c['wait_time'] for c in served_customers)
    avg_wait = math.ceil(total_wait / len(served_customers))

    return total_wait, avg_wait


def display_results(stats):

    # Display simulation results.
    total_wait, avg_wait = stats
    print('Simulation Results')
    print('------------------')
    print(f'Total wait time: {total_wait} minutes')
    print(f'Average wait time: {avg_wait} minutes')


def main():
    customers = generate_customers(10)
    served_customers = simulate_service(customers)
    stats = get_statistics(served_customers)
    display_results(stats)


if __name__ == '__main__':
    main()
