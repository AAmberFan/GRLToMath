def AdaptivecaR( Manage_speeD,VibratioN,Electric_enginE,DistancE,Fuel_enginE):
	expr = 0.4*max(0, min(100.0, -0.25*Electric_enginE + 0.5*Fuel_enginE)) + 0.4*max(0, min(100.0, 0.5*Electric_enginE - 0.25*Fuel_enginE + 0.5*((100.0) if (VibratioN <= 0.0) else (((50.0*abs(0.1*VibratioN - 1.0) + 50.0) if (VibratioN <= 10.0 and VibratioN > 0) else (((-50.0*abs(0.1*VibratioN - 1.0) + 50.0) if (VibratioN > 10.0 and VibratioN < 20.0) else (((0) if (True) else None))))))))) + 0.6*max(0, min(100.0, -0.5*Manage_speeD + 1.0*max(Electric_enginE, Fuel_enginE), max(Manage_speeD, 1.0*((100.0) if (DistancE >= 25.0) else (((50.0*abs(0.0666666666666667*DistancE - 0.666666666666667) + 50.0) if (DistancE >= 10.0) else (((-50.0*abs(0.2*DistancE - 2.0) + 50.0) if (DistancE > 5.0) else (((0) if (True) else None))))))))))
	return expr