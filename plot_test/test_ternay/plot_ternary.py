import ternary

## Sample trajectory plot
figure, tax = ternary.figure(scale=1.0)
tax.boundary()
tax.gridlines(multiple=0.2, color="black")
tax.set_title("Plotting of sample trajectory data", fontsize=20)
points = []
# Load some data, tuples (x,y,z)
with open("sample_data/curve.txt") as handle:
    for line in handle:
        points.append(list(map(float, line.split(' '))))
# Plot the data
tax.plot(points, linewidth=2.0, label="Curve")
tax.ticks(axis='lbr', multiple=0.2, linewidth=1, tick_formats="%.1f")
tax.legend()
tax.show()