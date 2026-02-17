                                                           # SOLAR DESALINATION RATES
    Repository Contents
- Simulation scripts  
- Optimization modules  
- CSV datasets  
- Result plots

Key Findings

1. Optimal cover angle was found near 30°, confirming typical solar still design literature.
2. Freshwater yield increases with basin area but shows diminishing yield per unit area.
3. Extremely steep cover angles reduce efficiency due to lower effective heat absorption.
4. Micro-scale optimization (0.02–0.05 m²) revealed strong sensitivity to geometric variations.


  Tech stack
 1. Python
 2.  NumPy
 3.  MatPlotLib

                                                Abstract
    To demonstrate that computational modelling and optimization can be used to engineer effecient designs. THis study shows that inclination at moderate angles outperforms the more extreme deisgns and demonstrates the relation between condensation efficiency, thermal absoption and geometry. 
                                              
                                             Insight 
The optimal angle identified (~30°) deviates from the theoretical 45° expectation in ideal evaporation models, highlighting the influence of thermal losses and geometry in practical systems. 
The results indicate that yield per unit area (l/m²) decreased with an increase in area which reveals that solar stills with smaller basin area give much beter yield than sills with larger surface area.

                                            
                                             BASIC PRINCIPLE
  Heat from the sun (solar energy) heats the water it evaporates and settles upon the a transpaent glass sitting above the water gradually the water drips down the glass into a container as it cools down. This method of removing salt from seawater makes seawater potable i.e drinkable, it can also be used to purify sewage water by sepearting harmful salts and compounds from water. This method is used at pilot scalee for for olive mill wastewater treatment[1]. 
 
 Overview:   This project presents a computational simulation of a solar desalination system using a simplified thermal energy balance model. The goal is to estimate freshwater yield under different geometric and operating conditions. The simulation models evaporation in a solar still by considering solar heat input, thermal losses, and latent heat of vaporization. This study employs different cover angles, basin surface areas, and operating times.

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
A computer-based simulation was developed using python to calculate water yield of a solar still which perform desalination of a constant area under different operaating conditions. This simulation simulated various operating conditions and based on energy output, evaporation rates and losses. 
This simulation consists of folowing variables;
1.Basin area - 0.02-0.05 m²
2.Cover angle - 10-90° 
3. Operating time - 0.2-0.5 hours 
                                           
                                           Thermal Modelling
The heat absorbed by saline water whose efficiency of heat absorption varied because of cover angle. Heat loss to to atmosphere was calculated using difference in ambient temperature of surroundings and water.
The net heat used up during evaporation was calculated using latent heat of vaporisation of water which was used to find out the mass of water that had been converted to vapours. 
                                         
                                         Iterative Computation 
1. Solar heat was calculated
2. Loss to environment was calculated
3. Losses were subtracted and net heat used is calculated
4. Net evaporation rate is claculated
5. Freshwater yield is recorded
6. Mass vs time curve is plotted

                                          Data storage
The simulation resuts were stored in CSV format they documented-
a) Cover angle 
b) basin area 
c) Time for given evaporation

                                           Optimization
To optimize the model brute-force search method was used to find the ideal angle for maximaum heat absorption by water. This included finding the ideal angle between 10-90° and and basin area between 0.02-0.5 m². This was implemented using the model where the highest yield of water was tracked. 

                                            Visulaisation 
The resultant values were visualized using Python's Matplotlib library. Mass–time curves and optimization plots were generated to illustrate performance trends and identify optimal configurations.
 
                                           Limitations

1. The model assumes steady-state thermal behavior.
2. Changes in heat due to environment fluctuation were not included.
3. No experimental validation was performed.

                    
                                          
                                            CITATIONS
   [1] https://www.sciencedirect.com/science/article/abs/pii/S0959652622022934
   
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


