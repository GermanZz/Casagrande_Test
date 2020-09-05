import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import ScalarFormatter
from scipy import stats
import numpy as np
import PIL
from UI import *


def get_graph():
    try:
        borehole_no = ui.borehole.text()
        sample_no = ui.sample.text()

        y = [float(ui.m1.text()), float(ui.m2.text()), float(ui.m3.text()), float(ui.m4.text())]
        X = [float(ui.b1.text()), float(ui.b2.text()), float(ui.b3.text()), float(ui.b4.text())]

        # Regression func
        def regress(x):
            return slope * x + intercept

        # Create Regression array
        slope, intercept, r, p, std_err = stats.linregress(X, y)
        mymodel = list(map(regress, X))
        rounded_model = [round(num, 1) for num in mymodel]

        # LIQUID_LIMIT: Value of Y-axis corresponding to 25 of X
        liquid_limit = round(np.interp(25, X, rounded_model), 1)

        # Coordinates to make line parralel to the X-axis that goes to the value of LIQUID_LIMIT
        x_coord = [0, 25]
        y_coord = [liquid_limit, liquid_limit]

        # Create graph
        fig = plt.figure(figsize=(9.5, 6))
        ax = plt.subplot(1, 1, 1)
        plt.yscale('log')  # Make it with log scale
        plt.scatter(X, y, s=10, color='black')  # Make scatter plot of initial data
        plt.plot(X, rounded_model, linewidth=1, color='black')  # Plot regression model
        plt.plot(x_coord, y_coord, linestyle='--', linewidth=1, color='black')  # Plot line correspondong 25 bumps
        plt.minorticks_off()  # Remove minor ticks
        # Graph customization
        plt.subplots_adjust(left=0.08, right=0.96, bottom=0.08, top=0.88)  # Adjustment
        plt.xlim(12, 50)
        ax.set_xticks([13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40, 45, 50])  # Set x - ticks
        ax.set_yticks(
            list(range(int(round(float(ui.m4.text()), 0) - 1), int(round(float(ui.m1.text()), 0) + 3), 2)))
        # Plot customization
        plt.title(f'Borehole: {borehole_no}, Sample: {sample_no}\nLiquid limit {liquid_limit}')
        plt.ylabel('MOISTURE CONTENT [%]', weight='bold')
        plt.xlabel('NUMBER OF BUMPS', weight='bold')
        plt.grid(axis='both', linestyle='-', color='black', linewidth=0.5)

        # Change format of x and y axis
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_formatter(ScalarFormatter())

        plt.show()
    except:
        def showwarn():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Something went wrong")
            msg.setWindowTitle("WARNING")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        showwarn()


def reset():
    ui.sample.clear()
    ui.borehole.clear()
    ui.m1.clear()
    ui.m2.clear()
    ui.m3.clear()
    ui.m4.clear()
    ui.b1.clear()
    ui.b2.clear()
    ui.b3.clear()
    ui.b4.clear()


if __name__ == "__main__":
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('D:\qt\i.png'))
    # Create UI
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Hook logic
    ui.plot.clicked.connect(get_graph)
    ui.reset.clicked.connect(reset)
    # Main loop
    sys.exit(app.exec_())
