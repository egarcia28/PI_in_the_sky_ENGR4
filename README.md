# PI_in_the_sky_ENGR4_KAZ_AND_ELIAS
## Planning
### Project Outline
We will create a monocopter (maple seed-inspired flying machine) that will liftoff, hover for a few seconds, and then float back to the ground, all while collecting data on the acceleration. If we have time, we will aim to add remote control of altitude, and ambitiously try to add directional control.

### [Schedule](https://docs.google.com/document/d/1pQayeEdMNE8SRu3rC_TPZwJRhBuPcFR0BpK4Ck0BQyY/edit?usp=sharing)
Here is our week by week shedule that we hope to stick to throughout the project timeline.

### Materials (both planned and actual)
* PICO
* Accelerometer
* 420w brushless motor
* 50A speed controller
* 850mah 11.1v battery
* 3d printed components
* Jumper wires
* Bolts, nuts, and washers
* Aviation Tape
* 9mm Wooden Dowel
* pico circuit board
* A safe emotional and mental work enviornment
* A collection of cymbals and singing bowls in order to assist in the allignment of chakras (sadly, in our actual project/work environment we were unable to aquire these materials)

### Function
The function of our monocopter will be a single winged design with thrust provided by a single motor and propeller

### What we need to learn
We will need to learn and understand lots of the physics surrounding the balance and lift of the monocopter. For example, on most systems, the center of rotation is the same as the center of mass, but with a monocopter it is displaced slightly leading to more unstable flight if launched from the center of mass rather than rotation.

### How will we know we are succcesful?
We will know we are succesful when we build and code a fully functioning monocopter that is passively stable, collects acecleration data, and returns to the ground safely.

## Saftey concerns/Risk Mitigation
### Concerns
* Uncontrolled flight leading to human + flying machine disagreement
* Fast motor + sharp propeller + human fingers = BAD NEWS BEARS
* Energetic imbalance during project development affecting team well-being
* Overexertion and stress leading to reduced focus and creativity

### Mitigations
* Motor will not start until saftey switch has been flipped off, and 10 seconds after launch button has been pressed
* Saftey glasses worn AT ALL TIMES while launching
* significant human buffer given to monocopter prior and during launch (20-30 ish ft?)
* Integrate mindfulness practices into weekly team meetings to address and balance energy levels.
* Encourage regular breaks and provide resources for stress management.
* Foster a supportive team environment to share and address individual concerns, promoting overall well-being.
* Periodic group meditation sessions to enhance focus and maintain a harmonious work atmosphere.

## Sketches
### Code block diagram
An early [code block diagram](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/code.jpg). Although we origionally did this as a requirement, it ended up being very useful, and we pretty much followed it verbatim.

### Potential design sketches
Some [design sketches](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/sketch.jpg), after preliminary research we roughly understood what the different designs for a monocopter type aircraft were, and each of their pros and cons. 


# [IMPORTANT!!](https://docs.google.com/document/d/1OX2BLcDlC8bTRmJvsCjCM4g4kqTqf-fzR08P1DxjED0/edit?usp=sharing)

# CAD

[Link to CAD Model](https://cvilleschools.onshape.com/documents/25e12063cab2a4f64ef09985/w/c376eafbf39511a0f2f7abef/e/96b13dd0f25b07f70c6d5a76?renderMode=0&uiState=665d4fda66f61d0d8f60b6aa)

## Overall concepts based on research:
1. There are three different types of monocopter(which all have their own usual sizes):
  * Sword-Style: Usually large, these have the motor on the opposite side of the wing. [Bad Example](https://www.youtube.com/watch?v=Me9bTUYIJ6c&list=PLzDYnh_tvZtTz4YUezmdNgfOjBsz4fjhH)  
  * T-shape: Usually small, the motor is positioned on an arm at a right angle to the wing. [Example](https://www.youtube.com/watch?v=u23Hqq8QbeE) 
  * Prop-on-Wing: Usually Medium sized, the motor is mounted on the wing. This is the design we went with, because we didn't have the right tools to build a large wing, and we didn't have the right sized motor for a the T-shape. [Example](https://www.youtube.com/watch?v=I_6EjX8T9Ag) 
2. All the monocopters of a comparable size we saw used a brushless DC motor ([BLDC](https://en.wikipedia.org/wiki/Brushless_DC_electric_motor)), which has an incredible thrust to weight ratio, so is perfect for small aircrafts.
3. The wing profile must decrease in angle of attack as it reaches the tip. This is to create equal thrust across the propeller, as seen in commercial propellers.

![blade-pitch](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/116c315f-17cf-48aa-896f-9e41a6a3908a)

4. To achieve optimal thrust, the monocopter should rotate around the base of the wing, on the front.
5. The center of rotation and center of mass are slightly different, but the effect is small enough that it doesn't matter.
6. There are multiple ways to control the direction of a monocopter, you can either use an aileron, or sinusoidal control of the motor (This doesn't matter that much, we didn't reach a stage that we would be able to add directional control).
7. [Wing Loading](https://en.wikipedia.org/wiki/Wing_loading#:~:text=Wing%20loading%20is%20a%20useful,have%20a%20lower%20stalling%20speed.) should be lower than 10 kg/m^2

## Research links
[My Best Friends EVAR!!](https://www.youtube.com/@airlabsutd2880/videos)

[SUTD Airlab's Design](https://www.youtube.com/watch?v=I_6EjX8T9Ag)

[Other Cool Prop-on-wing](https://www.youtube.com/watch?v=4-bzkRC0yoo)

[Other T-shape](https://ifl.ae.gatech.edu/2020/05/20/monocopter-zhiyuan-nick-zhang/)

[Another Banger by SUTD Airlab](https://www.bitcraze.io/2022/08/single-actuator-monocopters-sams/)

[Big Bad Science paper about flight dynamics](https://www.sciencedirect.com/science/article/abs/pii/S1270963820310634)

[Center of rotation stuff](https://physics.stackexchange.com/questions/212931/instantaneous-centre-of-rotation)

[Google patent for monocopter](https://patents.google.com/patent/US8366055B2/en)

[Lockheed Martin's Monocopter ( VERY BAD WAR PEOPLE!! :( )](https://www.youtube.com/watch?v=jtU1ZsjAqsE)

[Really Fun Monocopter](https://www.youtube.com/watch?v=HCg5Zve1oao)


## Basic Design:

![Basic Design For Wing](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/33724939-66e7-4272-9635-c159ba56d0ff)

This basic design is based on [SUTD's AIR Lab's design](https://www.youtube.com/watch?v=I_6EjX8T9Ag). We never printed this version, because there were too many things to tweak and fix. However, this was the first time we got to visualize what the final project would resemble. Also around this time I started…

## CFD!!!:
Computational fluid dynamics, or CFD ([Wikipedia link to spare you a google](https://en.wikipedia.org/wiki/Computational_fluid_dynamics#:~:text=Computational%20fluid%20dynamics%20(CFD)%20is,problems%20that%20involve%20fluid%20flows.)) is basically asking a computer to test if something works. In a professional setting, this greatly decreases prototype material costs, cuts the cost of using an air tunnel, and can be a very powerful tool to test a design quickly. The two CFD programs I used were [ANSYS student](https://www.ansys.com/academic/students/ansys-student) and [SimScale](https://www.simscale.com/) both of which are free!(under a few conditions). I ended only using SimScale for simulation, because ANSYS would've taken to long to learn (Simscale is basically a kiddie version of ANSYS). First I simulated the airfoil by itself 
![content](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/a8992b73-74a3-4100-91fb-7e482f47b8d5)

and then I simulated the whole rotating design 
![Screenshot 2024-06-03 12 37 06 AM](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/79abe983-0b2f-4778-904a-f44e1b9b9372)

Both simulations showed positive result (downward thrust in both), which lead me to me attempting my…
 
## First Design:

![Previous Design For Wing](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/9c649523-cb9f-4790-bf37-fd0715f5840c)

![Top view of V1 wing](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/v1%20top%20wing.jpg)
_Top view of V1 wing_

After tuning up the basic design (somehow the first design didn't even use airfoil???? I guess I just decided to freehand it??????(don't worry I added an airfoil before I printed)), I printed out the first prototype, which looked much like my friends at SUTD's. However, see issues - first launch, which lead me to redesign the basket, and issues - second launch lead me to doubt the amount of lift generated by the airfoil, so… 

## Final Design:
I changed from NACA 2415 to NACA 6409, prioritizing the lift coefficient at 0 degrees angle of attack. Also, the lid to the counterweight is  In the process, I moved the motor housing to the end, and changed the access to the motor bolts. I designed 3D skids, as issues - second launch had convinced us that launching off of the pole did not work. This is the monocopter that you see in launches 3 - 5.
![Final CAD Wing](https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/fd228e67-4a2e-41d5-9fa1-883403526a57)

![Profile v3](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/profile%20v3.jpg)
_Side profile of V3_

![Top view v3](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/top%20view%20v3%20(1).jpg)
_Top view of V3_
  
## Circuit Diagram
![Wiring Diagram](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/wiring.jpg)
_This is our circuit diagram, we used an integrated circuit board for our final product_

## Motor Shenanigans
After some very preliminary research we quickly realized that we would have to use a brushless motor for its excellent weight to thrust ratio, making it perftect for anything airborne. However, when looking for examples of using a brushless motor with circuit python/a raspberry pico we found next to nothing (save [this](https://hackaday.io/project/167826-brushless-nerf-titan50) nerf gun). After much fiddling and testing we settled on a solution. Using an Electronic Speed Controller, a small and compact 850mah 11.1v 3 cell lipo battery, and the [Samguk](https://www.getfpv.com/dys-samguk-series-wei-2207-2300kv-motor.html) brushless motor (SAMGUK in hand, the world I had), we were able to get the brushless motor working. Because brushless motors (like continuous servos) run with PWM, we can just treat is as such. An unfamiliar part of this process was the calibration. Unlike servos, brushless motors need to be calibrated which took some figuring out (lots of listening to subtley different beeps) but we eventually got it down and detailed everything below. One wierd quirk of using an ESC with the pico is that out of the 3 25 guage wires leading off the ESC, only 2 are used (signal and ground). The other wire (the red one) only creates problems, sending high voltage back into the pico causing (obvious) problems. Because regular continuous servos have 3 very simillar wires we began by using all 3 eventually frying the board. Although it seems counter intuitive, DO NOT USE THE RED WIRE when using an ESC and pico in congruence.  

### Step by Step Calibration
* Step 1: Connect the signal pin and ground pin from the ESC to the pico and wire a potentiometer referencing [this](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/calibration%20wiring.jpg) wiring diagram *the wiring diagram should have the motor signal pin in GP1 and potentiometer signal pin in GP26, sorry for the confusion*
* Step 2: Run [this](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/CalibrationCode.py) calibration code on the pico
* Step 3: Ensure that the potentiometer is in the full throttle position and connect the battery to the ESC
* Step 4: Wait for the 2 beeps that indicate the ESC is in calibration mode
* Step 5: Rotate the potentiometer to its lowest throttle position and wait for the beeps that indicate that the motor is calibrated
* Step 6: Disconnect then reconnect the battery and you should have a fully calibrated motor that changes its throttle based on the potentiometer's value

This code can also help give a foundation on how to control the motor, -1 is its lowest throttle position and 1 is its highest.

# Code

[Here](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/finalCode.py) is our final code prototype.

## Sweeping thoughts and generalizations
The code is essentially a frankenstiened version of the [Data Storage assignment](https://github.com/egarcia28/Engineering_4_Notebook?tab=readme-ov-file#raspberry_pi_data_storage_1) we did earlier in the year, and a for loop that controls the timings and throttle of the motor. At first we used arbitrary numbers in the for loop for testing purposes, but soon came to the realization that it was going to get very confusing very fast. After swithing over to variables for the for loop timings things functioned better, but not perfect. Even still, not every variable affects the thing it is supposed to, and the timings are still fidly. Data collection worked alot smoother than when I did the [Data Storage assignment](https://github.com/egarcia28/Engineering_4_Notebook?tab=readme-ov-file#raspberry_pi_data_storage_1)(worked first time we tested it). The motor aspect of the code was breifly mentioned [above](https://github.com/egarcia28/PI_in_the_sky_ENGR4/tree/main?tab=readme-ov-file#motor-shenanigans) but it essentially runs the same as a continuous servo, using pwm, and controlled by myservo.throttle(). Although, wiring does differ so be careful (explained above).

## Interesting Oddities or Tittilating Eccentricities
During the first 2 launches all of our wiring was done on the backpack circuit board for the pico. For launches 3-5 we switched the accelerometer to a [JST-SH 4-Pin Cable](https://thepihut.com/products/stemma-qt-qwiic-jst-sh-4-pin-cable) (I think?) connected from the circuit board to the accelerometer. This cable helps easily connect I2C devices with a single connection, sda and scl pins are hard wired to be GP4 and GP5. This switch helped eliminate mistrust in our wiring and made testing and wiring much easier. When we were first prototyping code without data collection, we used delay in our for loop, but once we added data collection into the mix, we realized that we wouldn't be able to use delay and would have to scrap most of our timings and base everything off of the board's time (time.monotonic()). During tests 3 and 4 the data, liraries, code, and boot.py were all wiped from the pico. This was either due to the BOOTSEL button being held down in the electronics cabin, or a buggy pico. Luckily, for our 5th launch the timings, data collection, and wiping luck all came together to allow a clean test where decent data was collected and timings were adhered to.


# Failed launches and other issues
### 1st Launch

https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/69b73770-86e2-46dc-af3f-addbff94155d

_A video of our 1st launch attempt_

For our first 2 launches we opted to use a pole to launch off of. Our idea was that the monocopter would be free to spin about its center of rotation/COM which would be impaled by the pole, the monocopter would then produce upwards thrust and move up off the pole. Obviously this came with some challenges evident in the first 2 launch videos. The pole created immense forces on the monocopter that essentially tore it apart, in this video you can see the electronics compartment break and fly off.

### 2nd Launch

https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/a6804a56-957a-4fab-a2d4-1103b6716793

_A video of our 2nd launch attempt_

We again opted to use a pole for our second launch, making changes to the support for the electronics cabin and other small changes to the wing's design (a groove for the motor's wires rather than a hole through the wing, flipping the electronics cabin and removing honycombing, etc.). This launch also suffured due to our metheod of launching, the pole again created huge force on the wing leading to the motor flying off a solid 30ft! More importantly, after this launch we decided that the pole was actually keeping us on the ground.

### 3rd Launch



https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/e9ad2624-27aa-4048-b8bc-475bc167ab0a


_A video of our 3rd launch attempt_
For our 3rd launch we decided to transition to another design for launching. We created a pair of skids to add to the wing so it could freely rotate on the ground allowing the monocopter to find its own center of rotation. We also decided to launch in the basketball court for a smooth floor and protective fences, we also used a large cardboard box to reduce friction even more. The skids worked decently well on the box but we ran into some trouble with it, after the monocopter left the box it skipped off the ground and failed. Luckily due to this new launching method we faced much less damage after the failed launch, the only damage was to the prop which only unscrewed itself from the motor.

### 4th/5th Launch


https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/784caf88-4769-432f-9536-8c7c63dace71


_A video of our 4th launch attempt_


https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/0e759ecd-6952-43de-a88b-3ef4a2c21fba
  

_A video of our 5th launch attempt_
  
We kept with the pole-less launch technique in the basketball court for the 4th and 5th launches, however, we decided against using the cardboard box base due to the skipping it caused in our 3rd launch. Generally the launches went well and the monocopter even left the ground (albeit while upside down). The primary issue with these launches was the design of the skids, they had too much friction and caused the monocopter to skip, eventually flipping over. The non pole launching method ended up being significantly better, even allowing us to test 2 times in one day due to the lack of intense force created by the pole.


# Data Analysis

[Link to Data](https://docs.google.com/spreadsheets/d/1bM0AhUifLfCkbIBh3z-04M-wDFiiEIocgrdV81zR7K8/edit?usp=sharing)

https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/b57e180a-b8e6-4365-b505-820613dcf733

Note: The last section should read "Prop Unscrews" instead of "Prop," but for some reason the video didn't want to do that, so I respected its' decision.

## Ramifications of data:

### Problems
1. Landing gear design needs to be changed, as the inversions are clearly caused by the bumps. 
2. Things to fix with data collection
* Accelerometer is not positioned well to determine the orientation of the craft
* Accelerometer at rest reads 12.912 m/s acceleration, misreading somehow
* End noise is unexplained, did the accelerometer come lose?
* In raw data the time reset halfway through?

### Data:
1.Rotational acceleration due to prop thrust is around 5.59 rad/s^2 (Data: 1 rotation from rest takes 1.5 seconds)
2.Using the [lift formula](https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/lifteq.html#:~:text=The%20lift%20equation%20states%20that,times%20the%20wing%20area%20A.&text=For%20given%20air%20conditions%2C%20shape,Cl%20to%20determine%20the%20lift.), and experimental data for [Lift Coefficient](https://www.jetir.org/papers/JETIR2104199.pdf), and [Air Density](https://macinstruments.com/blog/what-is-the-density-of-air-at-stp/#:~:text=According%20to%20the%20International%20Standard,%3A%200.0765%20lb%2Fft%5E3), and data from the model, (335 g for mass, 0.0522 m^2 for area of wing, radius = 0.284 m) and some math for rotation, we get that it would have to be rotating at a speed of 70.593 rad/s (11.2 rev/s) to achieve enough lift for liftoff. Based on these results I would recommend a change to the wing which creates more lift, either a change of airfoils or increasing angle of attack or area of wing, which would increase the lift generated by the wing.

# Final reflections:

## What I'd fix if I had more time:
1. MORE LIFT. in data, I discuss this more
2. Move the lid of the counterweight back to the top, for better access
3. Change the design of the skids to reduce forward pitch
4. Bring back the cardboard, to reduce friction on the launching ground 

## Regrets:
* We should have abandoned the pole after the first launch
* We should have focused more on data, as our data collection is very limited
* Benny was so so close to flying!!! We should've stuck to the schedule more. 

## Final Thoughts pt. I
The more I think about it, this was crazy ambitious project. There is very little out there about monocopters (Actually some guy, Francis Graham wrote a whole book about them, but it's out of stock (●´⌓`●) ), except a whole lot of videos where they work perfectly and never explain it. We took a lot of enthusiasm and optimism from those videos, but in terms of content, they really didn't help. Also, the physics behind the monocopter is very complex (Mr. Manning said "ask Mr. Eckols" Mr Eckols said "Weeelllll, bErNioUli's principle is…" ) and may require many more brain cells than could be mustered from our undeveloped frontal lobes. Other troubles included our initial use of a center stake on the first two launches, which never was going to work out, and that our overpowered motor keep on ripping pieces off(And we never even balanced our chakras!). However, my adventures with Benny were not fruitless. Along the way, I learned some of CFD, and though it didn't help in the slightest for Benny's flights, CFD is a powerful tool for projects and something I'm definitely going to use in the future. I also got up close and personal with BLDC motors, and learned that they're just big continuous servos if you treat them nicely. And like every book, the real friends were the prize you made along the way. BENNY 4EVER!

## What we did well
* We iterated well before actually facricating any of our and design and testing final code on it 
* We spent a sizeable time on research to perfect our design intentions
* But we still had enough time to be one of the first groups to do a test launch
* Our design was easily adaptable, and when we needed to change launching methods it was very simple

## The moments when tragedy struck
* The first launch where the electronics cabin broke off (I was at a 70% confidence level in it's ability to fly)
* The second launch where the motor launched 30ft breaking its connections (I was at a 50% confidence level in it's ability to fly)
* When the 1st motor we were testing with inexplicably stopped working
* When I forgot to wear safety glasses while testing the second motor with a prop attached without safety glasses (I still feel really really bad about this, :( SORRY MR.MILLER)
* When I broke the wing with a dowel while trying to remove support material
* When I fried the pico because the red wire was plugged in on the ESC
* When all our data from launch 3 was wiped

## Final Thoughts pt. II
Im glad we went the direction we did with our project, although it may have been ambitious, and not fully functional in the end. I genuninely learned alot about aerodynamics specifically realting to wings and airfoils. Although not entirely necesarry, I am indebted to the research we did into CFD and brushless motor use and specification. Although the true physics are far beyond our level, it was really cool seeing principles at play that we were concomitantly learning about in physics (torqe, moments of inertia, N2L, etc.). The primary regret I hold is in regard to the ammout we were able to test, the most rewarding days (not to mention fun) were those where we went outside to launch. They were also the days we learned the most, not only about our project, but everyone else's too. I'm also proud of the reasearch and dedication to it that both of us, but specifically Kaz showed. Not only was it fascinating and useful, but also inspiring to see someone else just as passionate in the project as myself (maybe even more so) doing their own research and learning alongside myself. Another new aspect that was just as motivating was the assignment of coding reponsibility on myself, this was completely new to me as I had never been on the coding side of the fence for a project. This helped motivate me not only to finish the code, but also to learn how it worked and how to write better code in the future. All in all, I'm more than happy with the direction of our project, how we functioned as a team, our eventual product, and the ways I pushed myself throughout the past semester.

# Extra final flight (it flew!!)
On the last day of class we were able to do one final test launch, after modifying the skid. This helped us acheive our [Final Flight](https://github.com/egarcia28/PI_in_the_sky_ENGR4/blob/main/images/finalflight.mp4). We extended the skid much further 
out foreward to avoid the skipping and nosediving of our previous skids. Luckily, this actually worked and we acheived flight, albeit for a very short time and at a very low height. Although not the success I wanted, it was the success we got. In terms of data for this flight, we decided not to collect any because our code misteriously stopped working just before our launch, however, it began to work when we removed the code in charge of data collection so we decided to continue without collecting data.

<div align="center">
	<img src="https://github.com/egarcia28/PI_in_the_sky_ENGR4/assets/113209502/40c1150c-5168-432b-9b6c-262b4e0f4fab">
</div>




