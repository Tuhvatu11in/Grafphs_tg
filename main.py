from time import time

import HTML_to_CSV
import CSV_to_grouped_DF
import MakingPlot

t0 = time()
output_file = HTML_to_CSV.start()
result_dict = CSV_to_grouped_DF.start(output_file)
MakingPlot.start(result_dict, 50)
print(f'{(time() - t0):.2f}')
MakingPlot.show_plot()