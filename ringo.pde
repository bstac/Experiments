import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
//AudioPlayer song;
AudioInput song;
BeatDetect beat;

AudioSample kick;
AudioSample snare;
AudioSample hat;
AudioSample crash;
AudioSample jazz;
AudioSample stick;

int ft = 7; //pattern length, 0 included
int hd = 7;
int hands=-1;  //not so literally,
int feet = -1; //represents counters for patterns of the drummer
int counter=0;
int count=0;
int tripper = 32; //trigger delay, like the max speed of a hand
int tripper2 = 26;
float whether = 2; //energy threshold, sensitivity
float weather = 4;
float accu=0.0;
float acc2=0.0;
boolean trip = false;
boolean trip2 = false;
boolean bHand= false;
boolean bFeet= false;
boolean TIME = false;

int FRAME_RATE = 128;
float BPM = 200;
float waiter = 60000.0/BPM;
float lastEvent = 0;

float aRadius;
float bRadius;
float cRadius;
float dRadius;
float eRadius;
float fRadius;
float gRadius;
float hRadius;
float iRadius;
float jRadius;
float kRadius;
float lRadius;
float mRadius;

void setup()
{
  frameRate(FRAME_RATE);
  size(800, 600);
  minim = new Minim(this);
  
  // load BD.wav from the data folder
  kick = minim.loadSample( "BD.mp3", 512); //file and buffer size
  // if a file doesn't exist, loadSample will return null
  if ( kick == null ) println("Didn't get kick!");
  
  // load SD.wav from the data folder
  snare = minim.loadSample("SD.wav", 512);
  if ( snare == null ) println("Didn't get snare!");
  
  hat = minim.loadSample("HH.wav", 512);
  if ( hat == null ) println("Didn't get high hat!");
  
  crash = minim.loadSample("CH.wav", 512);
  if ( crash == null ) println("Didn't get high crash!");
  
  jazz = minim.loadSample("SH.wav", 512);
  if ( jazz == null ) println("Didn't get high jazz ride hat!");
  
  stick = minim.loadSample("DS.wav", 512);
  if ( stick == null ) println("Didn't get high drum stick click!");
  
  
  
  
  //"Albert Hofmann.mp3" "Rain Has Tone.mp3" "Xtal.mp3" "PrimaryColors.mp3"
  //"MichiganJ.mp3" "Words.mp3" "cloudNineVer.mp3"
  //song = minim.loadFile("Xtal.mp3", 1024);
  //song.play();
  song = minim.getLineIn(Minim.MONO, 512);
  // a beat detection object song SOUND_ENERGY mode with a sensitivity of 10 milliseconds
  // 1024, 1024
  beat = new BeatDetect(song.bufferSize(), song.sampleRate());
  
  ellipseMode(RADIUS);

  aRadius = 20;
  bRadius = 20;
  cRadius = 20;
  dRadius = 20;
  eRadius = 20;
  fRadius = 20;
  gRadius = 20;
  hRadius = 20;
  iRadius = 20;
  jRadius = 20;
  kRadius = 20;
  lRadius = 15;
  mRadius = 15;
}



void draw()
{
  background(0);
  beat.detect(song.mix);//song.mix
  
  if(millis()>=waiter+lastEvent)
  {
    TIME=true;
    feet++;
    hands++;
    lastEvent=millis();
    //println(waiter + ": " + lastEvent + ": "+feet + ": "+ hands);
  }
  
  float a = map(aRadius, 20, 80, 60, 255);
  float b = map(bRadius, 20, 80, 60, 255);
  float c = map(cRadius, 20, 80, 60, 255);
  float d = map(dRadius, 20, 80, 60, 255);
  float e = map(eRadius, 20, 80, 60, 255);
  float f = map(fRadius, 20, 80, 60, 255);
  float g = map(gRadius, 20, 80, 60, 255);
  float h = map(hRadius, 20, 80, 60, 255);
  float i = map(iRadius, 20, 80, 60, 255);
  float j = map(jRadius, 20, 80, 60, 255);
  float k = map(kRadius, 20, 80, 60, 255);
  float l = map(lRadius, 20, 80, 60, 255);
  float m = map(mRadius, 20, 80, 60, 255);
  
  
  if (beat.isRange(0,1,2)){aRadius = 60;accu+=1;acc2+=1/11;}
  if (beat.isRange(1,2,2)){bRadius = 60;accu+=1/2;acc2+=1/11;}
  if (beat.isRange(2,3,2)){cRadius = 60;accu+=1/3;acc2+=1/11;}
  if (beat.isRange(3,4,2)){dRadius = 60;accu+=1/4;acc2+=1/11;}
  if (beat.isRange(4,5,2)){eRadius = 60;accu+=1.0/5;acc2+=1.0/11;}
  if (beat.isRange(5,6,2)){fRadius = 60;accu+=1.0/6;acc2+=1.0/11;}
  if (beat.isRange(6,7,2)){gRadius = 60;accu+=1.0/7;acc2+=1.0/11;}
  if (beat.isRange(7,8,2)){hRadius = 60;accu+=1.0/8;acc2+=1.0/11;}
  if (beat.isRange(8,9,2)){iRadius = 60;accu+=1.0/9;acc2+=1.0/11;}
  if (beat.isRange(9,10,2)){jRadius = 60;accu+=1.0/10;acc2+=1.0/11;}
  if (beat.isRange(10,11,2)){kRadius = 60;accu+=1.0/11;acc2+=1.0/11;}
  
  int temp = int(accu);
  if(!trip && accu>whether) 
  {
    lRadius = 100;
    accu = 0;
    trip = true;
    bHand=true;
  }
  
  if(temp>weather && !trip2 && acc2>weather)
  {
    mRadius = 100;
    acc2 = 0;
    trip2 = true;
    bFeet=true;
  }
  
  if(bHand && TIME)
  {
    if(hands>hd){hands = 0;}
    //if(hands==1 ){snare.trigger();}//stick.trigger();}}|| hands==3 || hands==5 || hands==7
    //if(hands==2 || hands==4 || hands==6 || hands==7){jazz.trigger();}
    //if(hands==2){}//stick.trigger();}
    //if(hands==6){}//crash.trigger();}
    //jazz.trigger();
    
    bHand=false;
  }
  if(TIME)
  {
    if(feet==4){snare.trigger();}//feet>ft){feet = 0;}
    if(bFeet){kick.trigger();}
    else{if(feet==0 || feet==2){kick.trigger();}else{hat.trigger();}}
    bFeet=false;
  }

  TIME=false;
  
  fill(240, 0, 14, a);
  ellipse(width/7, height/4, aRadius, aRadius);
  aRadius *= 0.995;
  fill(0, 30, 255, b);
  ellipse(2*width/7, height/4, bRadius, bRadius);
  bRadius *= 0.990;
  fill(200, 30, 255, c);
  ellipse(3*width/7, height/4, cRadius, cRadius);
  cRadius *= 0.985;
  fill(10, 25, 200, d);
  ellipse(4*width/7, height/4, dRadius, dRadius);
  dRadius *= 0.980;
  fill(60, 255, 0, e);
  ellipse(5*width/7, height/4, eRadius, eRadius);
  eRadius *= 0.975;
  fill(14, 250, 180, f);
  ellipse(6*width/7, height/4, fRadius, fRadius);
  fRadius *= 0.970;
  fill(200, 30, 255, g);
  ellipse(width/6, 2*height/4, gRadius, gRadius);
  gRadius *= 0.965;
  fill(200, 30, 255, h);
  ellipse(2*width/6, 2*height/4, hRadius, hRadius);
  hRadius *= 0.960;
  fill(0, 200, 255, i);
  ellipse(3*width/6, 2*height/4, iRadius, iRadius);
  iRadius *= 0.955;
  fill(119, 100, 25, j);
  ellipse(4*width/6, 2*height/4, jRadius, jRadius);
  jRadius *= 0.950;
  fill(200, 30, 255, k);
  ellipse(5*width/6, 2*height/4, kRadius, kRadius);
  kRadius *= 0.945;
  fill(250, 200, 0, l);
  ellipse(4*width/6, 3*height/4, lRadius, lRadius);
  lRadius *= 0.987;
  fill(45, 200, 250, m);
  ellipse(2*width/6, 3*height/4, mRadius, mRadius);
  mRadius *= 0.987;
 
  if ( aRadius < 20 ) aRadius = 20;
  if ( bRadius < 20 ) bRadius = 20;
  if ( cRadius < 20 ) cRadius = 20;
  if ( dRadius < 20 ) dRadius = 20;
  if ( eRadius < 20 ) eRadius = 20;
  if ( fRadius < 20 ) fRadius = 20;
  if ( gRadius < 20 ) gRadius = 20;
  if ( hRadius < 20 ) hRadius = 20;
  if ( iRadius < 20 ) iRadius = 20;
  if ( jRadius < 20 ) jRadius = 20;
  if ( kRadius < 20 ) kRadius = 20;
  if ( lRadius < 15 ) lRadius = 15;
  if ( mRadius < 15 ) mRadius = 15;
  
  if(trip){counter++;}
  if(counter>tripper){trip=false;counter=0;}
  
  if(trip2){count++;}
  if(count>tripper2){trip2=false;count=0;}
  
}
