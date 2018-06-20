public class Model{
	public double AdaptivecaR(double Manage_speeD,double VibratioN,double Electric_enginE,double DistancE,double Fuel_enginE){
		double expr = 0.4*Math.max(0, Math.min(100.0, -0.25*Electric_enginE + 0.5*Fuel_enginE)) + 0.4*Math.max(0, Math.min(100.0, 0.5*Electric_enginE - 0.25*Fuel_enginE + 0.5*((VibratioN <= 0.0) ? (
   100.0
)
: ((VibratioN <= 10.0 && VibratioN > 0) ? (
   50.0*Math.abs(0.1*VibratioN - 1.0) + 50.0
)
: ((VibratioN > 10.0 && VibratioN < 20.0) ? (
   -50.0*Math.abs(0.1*VibratioN - 1.0) + 50.0
)
: (
   0
)))))) + 0.6*Math.max(0, Math.min(100.0, Math.min(-0.5*Manage_speeD + 1.0*Max(Electric_enginE, Fuel_enginE), Math.max(Manage_speeD, 1.0*((DistancE >= 25.0) ? (
   100.0
)
: ((DistancE >= 10.0) ? (
   50.0*Math.abs(0.0666666666666667*DistancE - 0.666666666666667) + 50.0
)
: ((DistancE > 5.0) ? (
   -50.0*Math.abs(0.2*DistancE - 2.0) + 50.0
)
: (
   0
))))))));
		return expr;
	}
}
