                                                            SOLAR DESALINATION RATES
  

                                                     Key Findings
1. Optimal cover angle was found near 30°, confirming typical solar still design literature.
2. Freshwater yield scales withs with basin area but shows diminishing yield per unit area.
3. Extremely small cover angles (0-10) reduce efficiency due to lower effective heat absorption.


                                                Abstract
    To demonstrate that computational modelling and optimization can be used to engineer effecient designs. THis study shows that inclination at moderate angles outperforms the more extreme deisgns and demonstrates the relation between condensation efficiency, thermal absoption and geometry. 
                                              
                                            Efficiency 
The optimal angle identified (~30°) deviates from the theoretical 45° expectation in ideal evaporation models, highlighting the influence of thermal losses and geometry in practical systems. 
The results indicate that yield per unit area (l/m²) decreased with an scales with in area which reveals that solar stills with smaller basin area give much beter yield than sills with larger surface area.
This phenomena can be attributed to surface area of large-stills which causes increased loss of thermal energy to the surroundings.

                                            
                                             Introduction
This method of removing salt from seawater makes seawater potable i.e drinkable, it can also be used to purify sewage water by sepearting harmful salts and compounds from water. This method is used at pilot scalee for for olive mill wastewater treatment[1]. 
 
 This project presents a computational simulation of a solar desalination system using a simplified thermal energy balance model. The goal is to estimate freshwater yield under different geometric and operating conditions. The simulation models evaporation in a solar still by considering solar heat input, thermal losses, and latent heat of vaporization. This study employs different cover angles, basin surface areas, and operating times.

Freshwater yield is recorded, and a mass–time curve is plotted to analyze change in rate of evaporation. 


                                               IMPORTANT TERMINOLOGY 
Basin area: area of land where water ends into.
Desalination: act of removing salt from water 
Cover angle: tilt of cover (in our case plane glass) that sits above salinated water. 
Cover: water vapours hit the cover and trickle slowly into the a cup (collection resorvoir) 

The following study assumes 
1. Solar intensity assumed constant (e.g., 800 W/m²)
2. Water temperature assumed uniform throughout the fluid
3. Ambient temperature constant(at 25 degree celsius)
4. No wind losses 
5. Perfect condensation efficiency
6. Water density ≈ 1 kg/L
7. Simplified linear-heat model
8. No wind or connective disturbance
 


                                                      MATHAMETICAL MODEL
1.         Evaporation mass 'm'
                  m=Q.f-Q.i/L.v
           m=mass of water vapourised (for our convenience we assumed 1kg=1litre)
           Q.f=total solar energy absorbed by water in container(Joules) 
           Q.i=total solar energy lost to surroundings(Joules)
           L.v=latent heat of vapourisation of water(Joules/kg) 

2.          Solar energy absorbed 'Q.f'
                   Q.f=I*A*n*t
            Q.f=total solar energy absorbed by water in container(Joules)
            A=area of container (m²)
            n=efficiency of heat absorption of solar energy based on cover angle(unitless)
            t=time water sits under sun (seconds)

3.           Heat loss to environment(Q.i)
                   Q.i=K.l*(T.w-T.a)*t
              K.l=energy loss coeffecient(Joules/Celsius*hour)
              T.w=temperature of water(Celsius)
              T.a=temperature of surroundings/room temperature(celsius)
              t=time wter sits under sun(seconds)

4.           Optimal solar efficiency
                   n=n.b*(1−0.002⋅(θ−30)2)
              n=efficiency of heat absorption of solar energy based on cover angle(unitless)
              n.b=base heat absorption efficency of still  (unitless)
              30° is most optimal angle for maximum desalination. Closer the angle to 30 more effeciently the water will absorb the heat hence more water will be evaporated.


                                          SIMULATIONAL APPROACH
A computer-based simulation was developed using python to calculate water yield of a solar still which perform desalination of a constant area under different operaating conditions. This simulation simulated various operating conditions and based on energy output andlosses. 
This simulation consists of folowing variables;
1.Basin area - 0.02-0.05 m²
2.Cover angle - 10-90° 
3. Operating time - 0.2-0.5 hours 
                                           
                                           Thermal Modelling
The heat absorbed by saline water whose efficiency of heat absorption varied because of cover angle. Heat loss to to atmosphere was calculated using difference in ambient temperature of surroundings and water.
The net heat used up during evaporation was calculated using latent heat of vaporisation of water which was used to find out the mass of water that had been converted to vapours. 
                                         
                                        
1. Solar heat was calculated
2. Loss to environment was calculated
3. Losses were subtracted and net heat used is calculated
4. Net evaporation rate is claculated
5. Freshwater yield is recorded
6. Mass vs time curve is plotted

                                          D
                                           Optimization
This included finding the ideal angle between 10-90° and and basin area between 0.02-0.5 m². We used class 12 mathematics based application of derivatives to find optimal rate.
                                           Limitations

1. The model assumes steady-state thermal behavior, which may overestimate efficiency under fluctuating conditions.
2. Changes in heat due to environment fluctuation were not included.

   
          FILES ATTACHED
    0. License
    1. Readme.md
    2. Solar-desaination-rates.py
    3. Evaporated-mass-vs-hours-curve
    4. Solar-still-dataCSV 
    5. Optimization-of-curve-angle.py 
    6. Optimization-of-basin-area.py
    7. Optimzation-curve-cover-angle
    8. Optimization-curve-basin-area


