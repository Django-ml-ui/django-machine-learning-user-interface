from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from input.forms import IndexForm
import pandas as pd
import joblib
from .apps import InterfaceConfig
from input.params import y_column_name


class Index(TemplateView):
    template_name = 'interface/index.html'

    def get(self, request, *args, **kwargs):
        form = IndexForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = IndexForm(request.POST)
        if form.is_valid():

            # add cleaned form data here:
            # e.g. variable_1 = form.cleaned_data['variable_1']
            #      variable_2 = form.cleaned_data['variable_2']




            if 'predict' in request.POST:
                X = {'X':[
                    # list x variables here:
                    # e.g. variable_1, variable_2

                    ]}
                X = pd.DataFrame(X)
                X = X.transpose()
                mdl = InterfaceConfig.model
                Y = mdl.predict(X)
                result =Y 
                result = pd.DataFrame(Y, columns = [y_column_name])
                
                # If your model output is categorical use this replace function to make output more readable e.g. if your 
                # output is 1 and 0 you can rename it to "Yes" and "No" for better redeability
                # result = result.replace({1:'Passenger Survives', 0:'Passenger Does not Survive'})

                result = result.to_csv(header=None,index=False)
            form = IndexForm()
        args = {'form': form , 'result':result}
        return render(request, self.template_name, args)