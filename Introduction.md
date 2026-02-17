                                                           # SOLAR DESALINATION RATES
    FILES ATTACHED
    0. License
    1. Readme.md
    2. Solar-desaination-rates.py
    3. Evaporated-mass-vs-hours-curve
    4. Solar-still-data.csv 
    5. Desalination-through-solar-still-process-diagram

This code contains results of a personal project I undertook during end of my class 11 exams, I experimented with evaporation rate of salinated water. My setup consisted of a solar still made using foil, glass water and a transparent cup which was covered again with mirror and then put under sun for hours

How to run? (in command prompt enter)
python solar_desalination.py 
 
 OBJECTIVE:  Simulate thermal desalination(using python) to optimize basin area and cover angle for maximum water yield of fresh potable water. 

IMPORTANT TERMINOLOGY 
Basin area: area of land where water ends into.
Desalination: act of removing salt from water 
Cover angle: tilt of cover (in our case plane glass) that sits above salinated water. 
Cover: water vapours hit the cover and trickle slowly into the a cup (collection resorvoir) 
 
MATERIALS
Aluminium foil
Plane glass/plastic 
Transparent glass/cup to collect water
Broad mouthed transparent container
Water 
Stands
Measuring cup

IMPORTANT FORMULAES 
1.         Evaporation mass 'm'
                  m=Q.f-Q.i/L.v
           m=mass of water vapourised (for our convenience we assumed 1kg=1litre)
           Q.f=total solar energy absorbed by water in container(Joules) 
           Q.i=total solar energy lost to surroundings(Joules)
           L.v=latent heat of vapourisation of water(Joules/kg) 

2.          Solar energy absorbed 'Q.f'
                   Q.f=I*A*n*t
            Q.f=total solar energy absorbed by water in container(Joules)
            A=area of container (metre^2)
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
              30 degrees is most optimal angle for maximum desalination. Closer the angle to 30 more effeciently the water will absorb the heat hence more water will be evaporated.

          FILES ATTACHED
          0. License
          1. Readme.md
          2. Solar-desaination-rates.py
          3. Evaporated-mass-vs-hours-curve
          4. Solar-still-data.csv 
          5. Desalination-through-solar-still-process-diagram

