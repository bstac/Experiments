// processing code 

import oscP5.*; 
import netP5.*; 
  
OscP5 oscP5; 
NetAddress myRemoteLocation; 

void setup() { 
  size(400,400); 
  frameRate(25); 
  /* start oscP5, listening for incoming messages at port 49110 */ 
  oscP5 = new OscP5(this,5001); 
  
  myRemoteLocation = new NetAddress("127.0.0.1",5001); 
} 


void draw() { 
  background(0);   
} 


/* incoming osc message are forwarded to the oscEvent method. */ 
void oscEvent(OscMessage theOscMessage) { 
  //print("### received an osc message."); 
  print(" addrpattern: "+theOscMessage.addrPattern()); 
  println(" typetag: "+theOscMessage.typetag()); 
  if(theOscMessage.checkTypetag("b")){println(theOscMessage.get(0).booleanValue());}
  else if(theOscMessage.checkTypetag("f")){println(theOscMessage.get(0).floatValue());}
  else if(theOscMessage.checkTypetag("i")){println(theOscMessage.get(0).intValue());}
  else{println(theOscMessage.get(0));}
} 

