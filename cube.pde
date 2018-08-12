//check out wolfram spherical coordinates
//
/*

NOTES: wednesday, june 18th
an object is a center point and an array of vectors built from it. 
for the cubes points, or should i just do list of vectors?


this should go into a new class called object, instantiated by a 
number of points argument, used to create a 3 dimensional array
then filled through another method, one point at a time? this sucks.

lets focus on just a cube object, not as a data structure
as a 3d array, with a center point value

functions I will need
 change();
 toSphere();
 toTwoDim();
 calcRot();
 calcRat(); //this doesnt make sense as a nomclat, i am using
 //rot for theta and rat for pitch, unless i have that backwards
 also...added rut, on sat 21 june, i think its necessary
 but my brain is starting to hurt
 
 change() has to describe the path for the center point the 
 rotation for rat and rot, calc's() should take the array
 and perform a transformation for the rotation change
 
 then, once we have the new postions,
 we can redraw using to's(), which will be rewritten to take
 an array, and then a loop in draw to print that sucker out.

 (rem: if this was a network
 project, a mobile device could have a 3d game on it that works 
 with the dome. say its two players, all the objects are created 
 in detail for each device and the dome computer, but only the
 updates on {position, rat, rot} would have to be constantly sent, 
 and other game states could be sent less frequently)
 
 notes sat the 21st, 
 
 //code for looping through the values of the cube
 
 for(int i = 0; i < cuboid.length; i++)
{
  for(int j = 0; j < cuboid[i].length; j++)
  {
    print(" " + cuboid[i][j] + ",");
  }
  println("");
}


notes:
sunday 22nd june, 3:30am
good electro music, almost got my x rotation
it seems like i messed up the equation some where

notes:
tuesday 25th june, 7:00pm
rotations might be working and the problems i notice are due
to the dome curvature i was planning for. BIG problem
right now seems to be acos(), only works from 1 to -1,
geometrically, it wouldnt make sense for it not to, I need
to figure out why im getting values that don't make sense

NOTES:
thursday 26th june 12:47am
all seems well, fixed the acos() problem
suprisingly made everything work out, atleast
seemingly. begin modularizing into classes
*/


import oscP5.*;
import netP5.*;


//below values are for the cubes center
float xx =0, yy = 0, zz = 2;
//below values are for rotation of the cube
float rot = 0, rat = 0, rut = 0;
//2d array for 8 coordinates, corners of cube, 
//relative to the center
float[][] cuboid = new float[8][3];
//2d array for 8 coordinates, corners of cube, 
//absolute to the center
float[][] cub = new float[8][3];
//2d for the cube in 2d (for the screen), with radius
float[][] cube = new float[8][3];

float g = .001;
int count;

//from the online tutorial at vimeo.com/71100719

OscP5 osc;
NetAddress sc;



void setup()
{
  osc = new OscP5(this, 12000);
  sc =  new NetAddress("127.0.0.1", 57120);
  ellipseMode(CENTER);
  stroke(255);
  //create cube
//verified to work
int ct = -1, cnt = -1;
count = -1;
for(int i = 7; i >= 0; i--)
{
  cuboid[i][0] = count;
  cuboid[i][1] = cnt;
  cuboid[i][2] = ct;
  ct *= -1;
  if(i%2 == 0)
  {
    cnt *= -1;
    if(i%4 == 0)
    {
      count *= -1;
    }
  }
}
  count = 0;
  size(displayWidth, displayHeight);
  if (frame != null) {
    frame.setResizable(true);
  }
}

boolean sketchFullScreen() {
  return true;}
  // Also from Preferences "Run sketches on display 2" for dome.
//

void draw()
{
  if(count%3==0)
  {
  change();
  toTwoDim();
  }
  background(0);
  for(int i = 0; i < cube.length; i++)
  {
    ellipse(cube[i][0] + width/2 ,cube[i][1]+height/2,20/cube[i][2],20/cube[i][2]);
  }
  count++;
}


void change()
{
  //g is like time, or para-metric
    g+= PI/64;
    //im no longer sure what the below 
    //code is doing for me, need to play with it
    if(g>4*PI)
    {
      g = 0.001;
    }
    
    //these work as individuals but not all together
    rut = -g; //for z
    rot = g; //for x
    //rat = g/7; //for y
    
    //for simple translations
    zz = 1.5 + cos(g);
    xx = g - 4;
    //yy = -8 + g;
    //zz = sin(g) + 2;
    //for the helix
    //xx = sin(g);
    //yy = cos(g);
    //zz = g;     //can also be used for simple translation above
  //change to the right position
    //g * 10 //for when the helix is up
    OscMessage msg = new OscMessage("/cube");
    msg.add(sqrt((xx*xx)+(yy*yy)+(zz*zz)));
    msg.add(atan(yy/xx));
    osc.send(msg, sc);
  float x,y,z;
  for(int i = 0; i < cuboid.length; i++)
  {
    //around the x axis
    y = (cos(rot)*cuboid[i][1])-(sin(rot)*cuboid[i][2]);
    z = (sin(rot)*cuboid[i][1])+(cos(rot)*cuboid[i][2]);
    // around the y axis
    x = (cos(rat)*cuboid[i][0])-(sin(rat)*z);
    z = (sin(rat)*cuboid[i][0])+(cos(rat)*z);
    //around the z axis
    float x2 = x;
    x = (cos(rut)*x2)-(sin(rut)*y);
    y = (sin(rut)*x2)+(cos(rut)*y);
    
    //convert to real world position
    // can be replaced with x y z, 
    cub[i][0] = x/10 + xx;
    cub[i][1] = y/10 + yy;
    cub[i][2] = z/10 + zz;
  }
}

void toTwoDim()
{  //bear with me, this is going to be an all in one
  float x,y,z,r,t,u,ex,wy;
  for(int i = 0; i < cuboid.length; i++)
  {
    x = cub[i][0];
    y = cub[i][1];
    z = cub[i][2];
    //sphere
    r = (x*x) + (y*y) + (z*z); 
    r = sqrt(r);
   
    if(r < 1)
    {
      r = 1;
    }
    
    //acos hs a range -1 to 1
    //      spits out PI to 0
    //ex = z/r;
    t = acos(z/r);
    u = atan(y/x);
    
    if(x<0){u = (PI)+u;}
    cube[i][0] = (-t)*cos(u)*width/(PI);
    cube[i][1] = (-t)*sin(u)*height/(PI);
    cube[i][2] = r;
  }
}









