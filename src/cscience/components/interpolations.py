import cscience.components
import numpy as np
import scipy.interpolate
from scipy.interpolate import splprep
from scipy.interpolate import splev
from cscience.components import UncertainQuantity

class InterpolateModelLinear(cscience.components.BaseComponent):
    visible_name = 'Interpolate Age/Depth Model (Linear Spline)'
    inputs = {'required':('Calibrated 14C Age',)}
    #outputs = {} #TODO: add an output type that is an object, for great justice

    def run_component(self, core):
        #need to have x monotonically increasing...
        xyvals = zip(*sorted([(sample['depth'],
                               sample['Calibrated 14C Age'])
                              for sample in core]))
        interp = scipy.interpolate.InterpolatedUnivariateSpline(*xyvals, k=1)
        core['all']['age/depth model'] = interp

class InterpolateModelSpline(cscience.components.BaseComponent):
    visible_name = 'Interpolate Age/Depth Model (B-Spline)'
    inputs = {'required':('Calibrated 14C Age',)}

    def run_component(self, core):
        xyvals = zip(*sorted([(sample['depth'],
                               sample['Calibrated 14C Age'])
                              for sample in core]))
        tck,u=splprep(xyvals,s=200000)
        x_i,y_i = splev(np.linspace(0,1,100),tck)
        core['all']['age/depth model'] = x_i,y_i

class UseModel(cscience.components.BaseComponent):

    visible_name = 'Assign Ages Using Age-Depth Model'
    #inputs = {'all':('age/depth model',)}
    outputs = {'Model Age': ('float', 'years', True)}

    def run_component(self, core):
        #so this component is assuming that the age-depth model has already
        #been interpolated using some method, and is now associating ages
        #based on that model with all points along the depth curve.
        age_model = core['all']['age/depth model']
        print age_model
        for sample in core:
            sample['Model Age'] = UncertainQuantity(age_model(sample['depth']),
                                                    'years')

        #TODO: figure out uncertainty...
