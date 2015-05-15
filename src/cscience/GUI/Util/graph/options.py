
class PlotCanvasOptions:
    def __init__(self):
        self.legend = False;
        self.invert_x_axis = False

        self._m_legend = None
        self._m_invert_x_axis = False
        self._m_invert_y_axis = False
        self._m_show_axes_labels = False
        self._m_show_grid = False

    def copy(self):
        ret = PlotCanvasOptions()
        ret.set_invert_y_axis(self.get_invert_y_axis())
        ret.set_invert_x_axis(self.get_invert_x_axis())
        ret.set_show_axis_labels(self.get_show_axis_lables())
        ret.set_show_legend(self.get_show_legend())
        ret.set_show_grid(self.get_show_grid())
        return ret

    def get_invert_x_axis(self):
        return self._m_invert_x_axis
        
    def get_invert_y_axis(self):
        return self._m_invert_y_axis

    def get_show_axis_lables(self):
        return self._m_show_axes_labels

    def get_show_legend(self):
        return self.legend

    def get_show_grid(self):
        return self._m_show_grid

    def set_show_axis_labels(self, yes):
        self._m_show_axes_labels = yes

    def set_show_grid(self, yes):
        self._m_show_grid = yes

    def set_show_legend(self, yes):
        self.legend = yes

    def set_invert_x_axis(self, yes):
        self._m_invert_x_axis = yes

    def set_invert_y_axis(self, yes):
        self._m_invert_y_axis = yes

    def plot_with(self, _, plot):
        if self._m_invert_y_axis ^ plot.yaxis_inverted():
            plot.invert_yaxis()
        if self._m_invert_x_axis ^ plot.xaxis_inverted():
            plot.invert_xaxis()

        if self._m_show_grid:
            plot.grid(self._m_show_grid)

        if self.legend:
            self._m_legend = plot.legend()
        elif self._m_legend:
            self._m_legend.remove()
            self._m_legend = None

    def enable_legend(self,yes):
        self.legend = yes

    def __str__(self):
        return "legend: %s; invert_x: %s;" \
               "invert y: %s; show_labels: %s; " \
               "show_grid: %s;" % \
               (self._m_legend, self._m_invert_x_axis,
                self._m_invert_y_axis, self._m_show_axes_labels, self._m_show_grid)



# Options for a single xvy plot. Not the case for the
# more global options about plotting.
class PlotOptions:
    def __init__(self):
        self.color = (0,0,0)
        self.fmt = "o"
        self.interpolation_strategy = None
        self.computation_plan = None

    # plot points on plot under the context
    # represented by this object
    #
    # points :: [PlotPoint]
    # plot :: Matplotlib plot thing
    def plot_with(self, points, plot):
        (xs, ys, _, _) = points.unzip_points()
        l_color_tup = (self.color[0], self.color[1], self.color[2]) # ghetto hack to make 3.0.0 work with 3.0.2
        l_color_str = "#%02x%02x%02x"%l_color_tup

        if self.interpolation_strategy:
            (xs_p, ys_p) = self.interpolation_strategy.interpolate(xs, ys)
            if not self.fmt:
                # this is the main plot then.
                plot.plot(xs_p, ys_p, '-', color=l_color_str, label=points.get_variable_name())
            else:
                plot.plot(xs_p, ys_p, '-', color=l_color_str)

        if self.fmt:
            plot.plot(xs, ys, self.fmt, color=l_color_str, label=points.get_variable_name(), picker=5)
