import pygal
from mInitial_Data import data

bar_chart = pygal.Bar()
bar_chart.add('readings', data.prev_readings.values())
print(data.prev_readings.values())
bar_chart.render_to_file(data.file_gistogram_svg)
