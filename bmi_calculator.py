def bmi_calculators(height,weight):
   height_convert = int(height)
   weight_convert = int(weight)
   bmi = round((weight_convert/(height_convert)**2)*10000,1)
   if bmi < 18.5:
     return  ("Under weight",bmi)
   elif bmi < 24.9:
     return  ("Normal weight",bmi)
   elif bmi < 29.9:
     return  ("Over weight",bmi)
   else:
     return  ("Obese",bmi)

    

   

   

