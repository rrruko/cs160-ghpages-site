'''Robot treasure hunt'''

from math import factorial, sqrt

# pip install plotly and numpy
import plotly
import plotly.graph_objs as go
import numpy as np

def distance_to_reach(energy, algo):
    '''Distance to reach energy at a given position using a given algorithm'''
    if energy == 0: return 0
    i = 0
    dist = 0
    pos = 0
    while True:
        d = algo(i)
        if pos + d >= energy and energy > 0:
            dist += energy - pos
            break
        elif pos + d <= energy and energy < 0:
            dist += pos - energy
            break
        else:
            dist += abs(d)
        pos += d
        i += 1
    return dist

def naive(n):
    return (2*(n%2)-1) * n

def square(n):
    return (2*(n%2)-1) * (n**2)

def pow2(n):
    return (2*(n%2)-1) * (2**n)

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

def fib2(n):
    return (2*(n%2)-1) * fib(n)

def fact(n):
    return (2*(n%2)-1) * factorial(n)

def evaluate(algo):
    '''Print the performance of the algorithm at 50m, 100m, 500m, and 1000m'''
    for energy in [50, 100, 500, 1000]:
        ad = avg_dist(energy, algo)
        print('Took ' + str(ad) + ' to reach +/-' + str(energy) + ' on average.')

def avg_dist(energy, algo):
    return distance_to_reach(energy, algo) + distance_to_reach(-energy, algo)

def print_tests():
    print('Testing naive')
    evaluate(naive)

    print('Testing square')
    evaluate(square)

    print('Testing pow2')
    evaluate(pow2)

    print('Testing fact')
    evaluate(fact)

def make_graph():
    '''Write log plots of the algorithms to an HTML file'''

    # Plot the performance of the algorithm at intervals of 50 up to 10000
    N = 1000000
    graph_x = list(range(0, N, N//200))
    low_res = list(range(0, N, N//40))

    # Returns a named graph of the given algorithm
    def graph_algo(algo, name):
        y = list(map(lambda energy: avg_dist(energy, algo), graph_x))
        return go.Scatter(x=graph_x, y=y, name=name)

    naive_graph = go.Scatter(
        x=low_res,
        y=list(map(lambda energy: avg_dist(energy, naive), low_res)),
        name='linear'
    )
    square_graph = graph_algo(square, 'polynomial')
    pow2_graph = graph_algo(pow2, 'exponential')
    fib_graph = graph_algo(fib2, 'fibonacci')
    fact_graph = graph_algo(fact, 'factorial')

    # We want to plot all the functions on one chart
    data = [naive_graph, square_graph, pow2_graph, fib_graph, fact_graph]

    # The exponential and factorial algorithms are so much better that we need
    # to use a log plot to really see everything
    layout = go.Layout(
        xaxis=dict(
            type='linear',
            title='Distance to energy',
            autorange=True
        ),
        yaxis=dict(
            type='log',
            title='Distance traveled',
            autorange=True
        )
    )

    # Write the chart to a file
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='robot_graph.html', auto_open=False)

def main():
    print_tests()
    make_graph()

main()
