IndicatorconnecttoelE <- function( Indicator3){
	expr = ifelse(Indicator3 <= -100.0,25.0,ifelse(Indicator3 >= -100.0 & Indicator3 < 200.0,1.0*min(100.0, 0.25*abs(1.66666666666667e-5*Indicator3 - 0.00333333333333333) + 12.5),ifelse(Indicator3 > 200.0 & Indicator3 < 500.0,1.0*max(0, -0.25*abs(1.66666666666667e-5*Indicator3 - 0.00333333333333333) + 12.5),0))) }