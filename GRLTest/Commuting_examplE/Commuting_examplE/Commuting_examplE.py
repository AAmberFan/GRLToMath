def Commuting_examplE( Express_buS,Regular_buS,Average_work_timE,Hitch_a_ridE,Minimize_infrastructure_cosT,Minimize_travel_timE,Average_ongoing_cosT,Take_own_caR):
	expr = 0.6667*max(0, min(100.0, 0.6*Minimize_infrastructure_cosT + 0.4*max(0, min(100.0, 1.0*((100.0) if (Average_ongoing_cosT <= 60.0) else (((50.0*abs(0.025*Average_ongoing_cosT - 2.5) + 50.0) if (Average_ongoing_cosT <= 100.0) else (((-50.0*abs(0.01*Average_ongoing_cosT - 1.0) + 50.0) if (Average_ongoing_cosT < 200.0) else (((0) if (True) else None))))))))))) + 0.6667*max(0, min(100.0, 0.5*Minimize_travel_timE + 0.5*max(0, min(100.0, 1.0*((100.0) if (Average_work_timE >= 60.0) else (((50.0*abs(0.0181818181818182*Average_work_timE - 0.0909090909090909) + 50.0) if (Average_work_timE >= 5.0) else (((-50.0*abs(0.2*Average_work_timE - 1.0) + 50.0) if (Average_work_timE > 0) else (((0) if (True) else None)))))))))))
	return expr
