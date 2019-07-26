#!/usr/bin/env python3

# System imports
import argparse

# 3rd party imports
import pandas
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Rather than including the data in the repo, take a CSV file to parse
parser = argparse.ArgumentParser(description='Take a file and plot the data')
parser.add_argument('-f', '--filename', type=str, required=True)
parser.add_argument('-o', '--outfile', type=str, required=False)
args = parser.parse_args()

groups = dict(
    A=('b','o'),
    B=('g','^'),
    C=('r','D'),
    D=('k','s'),
)

dataset = pandas.read_csv(args.filename)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

for k, v in groups.items():
    current_group = dataset.loc[dataset['Groups'] == k]
    ax.scatter(current_group['DiscFunc1'], current_group['DiscFunc2'],
               current_group['DiscFunc3'], c=groups[k][0], marker=groups[k][1],
               label=f'Group {k}')

ax.legend()
ax.set_xlabel('Discriminant Function 1')
ax.set_ylabel('Discriminant Function 2')
ax.set_zlabel('Discriminant Function 3')

if args.outfile:
    pyplot.savefig(args.outfile, format='eps', dpi=300)
else:
    pyplot.show()
