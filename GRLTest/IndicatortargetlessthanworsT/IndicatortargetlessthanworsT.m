function expr=IndicatortargetlessthanworsT( Indicator2)
	expr = ((Indicator2 <= 100.0).*(100.0) + (~(Indicator2 <= 100.0)).*( ...
(Indicator2 < 500.0).*(1.0*abs(1.25e-5*Indicator2 - 0.00625) + 50.0) + (~(Indicator2 < 500.0)).*( ...
(Indicator2 > 500.0 & Indicator2 < 800.0).*(-1.0*abs(1.66666666666667e-5*Indicator2 - 0.00833333333333333) + 50.0) + (~(Indicator2 > 500.0 & Indicator2 < 800.0)).*(0))))
end
