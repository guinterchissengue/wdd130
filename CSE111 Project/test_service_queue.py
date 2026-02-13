'''
Author: Guinter Chissengue

Program:Service Queue Simulator for Customer Attendance

Enhancements: To increase the quality of the testing, additional tests need to be added 
to the test file that will include testing for an empty and very large customer queue. 
To also test the performance of the system in various operation environments, tests will need to be created.
'''


from service_queue import (
    generate_customers,
    add_to_queue,
    calculate_wait_time,
    serve_customer
)

def test_generate_customers():
    customers = generate_customers(3)
    customers_again = generate_customers(3)

    assert len(customers) == 3
    assert len(customers_again) == 3


def test_add_to_queue():
    queue = []
    customer = {'id': 1, 'arrival_time': 5}

    add_to_queue(queue, customer)
    add_to_queue(queue, customer)

    assert len(queue) == 2
    assert queue[0]['id'] == 1


def test_calculate_wait_time():
    wait1 = calculate_wait_time(5, 10)
    wait2 = calculate_wait_time(10, 5)

    assert wait1 == 5
    assert wait2 == 0


def test_serve_customer():
    queue = [{'id': 1, 'arrival_time': 3}]
    served, time = serve_customer(queue, 5)

    assert served is not None
    assert served['wait_time'] >= 0
