// The planetarium library is designed to create real-time projections on 
// spherical domes. It is based on the FullDome project by Christopher 
// Warnow (ch.warnow@gmx.de):
// https://github.com/mphasize/FullDome
//
// A brief descrition on how it works: a 360° view of the scene is generated
// by rendering the scene 6 times from each direction: positive x, negative x, 
// positive y, and so on. The output of each rendering is stored inside a cube map 
// texture, which is then applied on a sphere representing the dome.
// Hence, the library calls the draw() method 6 times per frame in order to update  
// the corresponding side of the cube map texture (in reality, only 5 times since  
// the bottom side of the cube map is not invisible on the dome). 
// So, it is important to keep in mind that if you need to perform some calculation
// only one time per frame, then the code for those calculations should be put inside
// the pre() method.

//the above doc is from the original 'Basic' example for the
//planetarium package
//I simply rewrote it as i needed. 
//if you can run this, then you should beable to find the original
//code in the package's folder
//*********************************************************
//note: this version of the code has not been tested well *
//      some of the formulas might need minor tweeking    *
//      to make them accurate enough for presentation     *
//*********************************************************

import codeanticode.planetarium.*; //for 3d in the dome
import oscP5.*; //for networking to super collider
import netP5.*; //also for networking to super collider

PImage tex; //i dont use this anymore, but incase you change something, it is here
PShape s;
//cubex,y,z -> center object location
//rot,rat,rut, axis rotation, i never got around to using them
//radius, theta and pitch are for polar cooridinates
//theta is side to side
//pitch is top to bottom
float cubeX, cubeY, cubeZ, g, theta, pitch, radius;
int zero;
float[] spk = new float[5]; //for the five speakers

OscP5 osc;
NetAddress sc;

void setup() {
  
  g = 0; //this is our time parameter for automated paths of the object
  osc = new OscP5(this, 12000); //setup OSC
  sc =  new NetAddress("127.0.0.1", 57120); //where we are going, i think
  size(600, 600, Dome.RENDERER);
  //size(displayWidth, displayHeight, Dome.RENDERER); //fullscreen, doesnt seem to work
  //tex = loadImage("ship.png");
  s = loadShape("ship2.obj"); 
  //scale the center based on the display, or else everything gets all screwy
  zero = width;
  if(height > width){zero = height;}//pick the biggest display parameter
  zero = 86*((zero-600)/100)+217; //this is based on measurements, seems to work
  cubeZ=zero; //the above line might need some tweeking
}

// Called one time per frame.
void pre() {
  //clear the buckets, meaning the spk array
  for(int i = 0; i<spk.length; i++)
   {
     spk[i] = 0;
   }
  buckets(); //call buckets(), initial calculation of speaker volume will occur
  OscMessage msg = new OscMessage("/cube"); //create a new message with the name
  //'/cube', is stored in msg[0]
   msg.add(radius); //put the radius in the message, for reverb control
   for(int i = 0; i<spk.length; i++)
   {
     spk[i]=(sq(sin(pitch))*spk[i])+(sq(cos(pitch))/spk.length); //recalculate the amplitude
     //for each speaker based on the pitch, ill explain this in a paper
     //but note, the pythagorean identity sin^2+cos^2=1
     //and if the summation of spk[i] (for all i) equals 1,
     //then we always have 1 as the 'total' volume
     if(spk[i]<0.001){spk[i]=0;}//if the volume is too quiet, shut it off
     msg.add(spk[i]); //add the amplitude of a particular speaker to the message
   }
   osc.send(msg, sc); //send the message to Super Collider
}

// with this package the draw method is Called five times per frame.
//thats why a lot of stuff goes in the pre() method
//just updates the postion visually, adds lights, stuff like that
void draw() {
  background(0);
  
  pushMatrix();  
  translate(width/2, height/2, 300);
  
  lights();
  
  stroke(0);  
  fill(150);
  pushMatrix(); //push for every visual 'object'
  translate(cubeX, cubeY, cubeZ);  
  //box(50); //leftovers
  //texture(tex);
  shape(s);
  popMatrix();
  popMatrix();//a pop for every push is necessary
}

//for controling the ship with the keyboard
void keyPressed() {
  if (key == CODED) {
    if (keyCode == DOWN) 
    {
      if(cubeZ >= zero){}//do nothing
      else
      {
        //this and the above if statement
        //keep the object from going 'under' 
        //the dome
        cubeZ += 2;
      }
    }
    else if (keyCode == UP) {cubeZ -= 2;}
  }
  else{
    //these control the x and y axis, pretend
    // awsd are 4 arrows. 
    //you will notice you cannot hold these buttons
    //the way you can with the coded keys
    if(key == 'a'){cubeX -= 1;}
    if(key == 'd'){cubeX += 1;}
    if(key == 's'){cubeY += 1;}
    if(key == 'w'){cubeY -= 1;}
  }  
}


void buckets()
{
  //for the path of the object
  //comment out from here
  /*cubeX = 20*sin(g);
  cubeY = 20*cos(g);
  g+=.01;
  if(g>5*PI){g = 0;}//restart
  //to here, to control the ship manually*/
  //the bleow 2 lines are simple calculations
  radius = sqrt((cubeX*cubeX) + (cubeY*cubeY) + sq(zero-cubeZ));
  pitch = acos((zero - cubeZ)/radius);
  //and then one complex calculation
  if(cubeX==0)
  {cubeX = -0.0001;}// prevents divide by 0 error
  theta = atan(cubeY/cubeX);
  //println(theta); //troubleshooting stuff
  
  //below is a flow control way to get the correct distrubution
  //of speaker amplitude based on an index, based on the theta value
  //so first we need the index, which is tricky
  float index = (theta + (3*PI/2));
  if(cubeX>0)
  {
    index=PI+index;
  }
  //the above code is to deal with limits of my theta value
  //because of the range(or maybe its domain) of arctan
  index+= PI/16;//offset 
  index%=(2*PI); //ensure 
  index =((2*PI) - index);//on the day we tested the first version of this
  //particular setup, i relised i had based everything backwards from the actual setup
  //the above line was what i used to correct that, so it is ineffecient but convenient
  //println(index);  //some trouble shooting stuff
  //println("hello everbody");
  
  
  //'index+=PI/16' is for offset, so i calculate for inbetween speakers 
  //rather than to the right(or maybe its the left) of a speaker
  //it gives the proper illusion of a smooth sonic transition
  //and then we select based on the index
  if(index <= PI/8){
    spk[0] = 1;
  }//1
  if((index <= PI/4) && (index >= PI/8)){
    spk[0]=0.666;
    spk[1]=0.333;
  }//2
  if((index <= 3*PI/8) && (index >= PI*2/8)){
    spk[0]=0.333;
    spk[1]=0.666;
  }//3
  if((index <= 4*PI/8) && (index >= PI*3/8)){
    spk[1] = 1;
  }
  if((index <= 5*PI/8) && (index >= PI*4/8)){
    spk[1]=0.5;
    spk[2]=0.5;
  }//5
  if((index <= 6*PI/8) && (index >= PI*5/8)){
    spk[2]=1;
  }
  if((index <= 7*PI/8) && (index >= PI*6/8)){
    spk[2]=0.75;
    spk[3]=0.25;
  }
  if((index <= PI) && (index >= PI*7/8)){
    spk[2]=0.5;
    spk[3]=0.5;
  }//8
  if((index <= 9*PI/8) && (index >= PI)){
    spk[2]=0.25;
    spk[3]=0.75;
  }
  if((index <= 10*PI/8) && (index >= 9*PI/8)){
    spk[3] = 1;
  }
  if((index <= 11*PI/8) && (index >= 10*PI/8)){
    spk[3]=0.75;
    spk[4]=0.25;
  }
  if((index <= 12*PI/8) && (index >= 11*PI/8)){
    spk[3]=0.5;
    spk[4]=0.5;
  }//12
  if((index <= 13*PI/8) && (index >= 12*PI/8)){
    spk[3]=0.25;
    spk[4]=0.75;
  }
  if((index <= 14*PI/8) && (index >= 13*PI/8)){
    spk[4]=1;
  }
  if((index <= 15*PI/8) && (index >= 14*PI/8)){
    spk[4]=0.666;
    spk[0]=0.333;
  }
  if((index <= 2*PI) && (index >= 15*PI/8)){
    spk[4]=0.333;
    spk[0]=0.666;
  }//16
}
