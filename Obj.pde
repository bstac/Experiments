/*

NOTE.
6/30/14 12:37pm
Things I Need:

1)center point
2)array for 3d cartesian relative to center
3)array for absolute 3d cartesian, adjusted with rotations
4)array for 2d cartesian
5)array for polygon faces
  -holds each vertice's index, from 2d cart. array
6)a way to make sure the polygons are drawn in order 
  -from greatest to least radius
  -measured by each faces closest radius
  -try an array of indexes ordered when the radius is calc'ed
7)x y and z rotation functions
  -maybe could be done as is, use update functoins instead
8)center point update function
9)collision detection
  -ummmmm....?
  -boolean on or off
  -ummmm.....!!!!
10)way to change vertices reletave to center
  -boolean on or off
  -.....!?
11)colors for polygons
  -eventually fill patterns? 
  -how could that work tho?
  -(sigh).....!?
12) function toTwo()
  -maybe copy as is...some what.
13)constructor that sets 'er up!

//points 6,9, and 10, and maybe some others, could be
//time consuming, conside multithreading, or, loop count
//style pipelining, maybe even in the draw loop. 
*/

class Obj {
  
  //below values are for the cubes center
float x, y, z;
//below values are for rotation of the cube
//mandatory start 
//these might be stupid
float rot, rat, rut;
//2d array for 8 coordinates, corners of cube, 
//relative to the center
float[][] objDef;
//2d array for 8 coordinates, corners of cube, 
//absolute to the center
float[][] spinDef;
//2d for the cube in 2d (for the screen), with radius
float[][] printed;

Obj(float[][] ob, float xx, float yy, float zz)
{
  objDef = new float[ob.length][ob[0].length];
  spinDef= new float[ob.length][ob[0].length];
  printed = new float[ob.length][ob[0].length];
  arrayCopy(ob,objDef);
  x = xx;
  y = yy;
  z = zz;  
  rot = 0; 
  rat = 0; 
  rut = 0;
}

void display()
{
  spin();
  toTwoDim();
  for(int i = 0; i < printed.length; i++)
  {
    ellipse(printed[i][0] + width/2 ,printed[i][1]+height/2,20/printed[i][2],20/printed[i][2]);
  }
}

void spin()
{
  float xx,yy,zz;
  for(int i = 0; i < objDef.length; i++)
  {
    //around the x axis
    yy = (cos(rot)*objDef[i][1])-(sin(rot)*objDef[i][2]);
    zz = (sin(rot)*objDef[i][1])+(cos(rot)*objDef[i][2]);
    // around the y axis
    xx = (cos(rat)*objDef[i][0])-(sin(rat)*zz);
    zz = (sin(rat)*objDef[i][0])+(cos(rat)*zz);
    //around the z axis
    float x2 = xx;
    xx = (cos(rut)*x2)-(sin(rut)*yy);
    yy = (sin(rut)*x2)+(cos(rut)*yy);
    
    //convert to real world position
    // can be replaced with x y z, 
    spinDef[i][0] = xx/10 + x;
    spinDef[i][1] = yy/10 + y;
    spinDef[i][2] = zz/10 + z;
  }
}


void toTwoDim()
{  //bear with me
  float xx,yy,zz,r,t,u;
  for(int i = 0; i < spinDef.length; i++)
  {
    xx = spinDef[i][0];
    yy = spinDef[i][1];
    zz = spinDef[i][2];
    //sphere
    r = (xx*xx) + (yy*yy) + (zz*zz); 
    r = sqrt(r);
   
    if(r < 1)
    {
      r = 1;
    }
    
    //acos hs a range -1 to 1
    //      spits out PI to 0
    //ex = z/r;
    t = acos(zz/r);
    u = atan(yy/xx);
    
    if(xx<0){u = (PI)+u;} //what is this?
    printed[i][0] = (-t)*cos(u)*width/(PI);
    printed[i][1] = (-t)*sin(u)*height/(PI);
    printed[i][2] = r;
  }
 }
}
