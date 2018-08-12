/**

For now this is a protoType, and good way to design a drum machine per song. 

constructors:
BeatDetect();
BeatDetect(timeSize, sampleRate);

  * This sketch demonstrates how to use the BeatDetect object song SOUND_ENERGY mode.<br />
  * You must call <code>detect</code> every frame and then you can use <code>isOnset</code>
  * to track the beat of the music.
  * <p>
  * This sketch plays an entire song, so it may be a little slow to load.
  * <p>
  * For more information about Minim and additional features, 
  * visit http://code.compartmental.net/minim/
  
The BeatDetect class allows you to analyze an audio stream for beats (rhythmic onsets). Beat Detection Algorithms by Frederic Patin describes beats in the following way:
The human listening system determines the rhythm of music by detecting a pseudo periodical succession of beats. The signal which is intercepted by the ear contains a certain energy, 
this energy is converted into an electrical signal which the brain interprets. Obviously, The more energy the sound transports, the louder the sound will seem. But a sound will be heard 
as a beat only if his energy is largely superior to the sound's energy history, that is to say if the brain detects a brutal variation in sound energy. Therefore if the ear intercepts 
a monotonous sound with sometimes big energy peaks it will detect beats, however, if you play a continuous loud sound you will not perceive any beats. Thus, the beats are big variations 
of sound energy.
In fact, the two algorithms in this class are based on two algorithms described in that paper.
To use this class, inside of draw() you must first call detect(), passing the AudioBuffer you want to analyze. You may then use the isXXX functions to find out what beats have occurred 
in that frame. For example, you might use isKick() to cause a circle to pulse.

BeatDetect has two modes: sound energy tracking and frequency energy tracking. In sound energy mode, the level of the buffer, as returned by level(), is used as the instant energy 
in each frame. Beats, then, are spikes in this value, relative to the previous one second of sound. In frequency energy mode, the same process is used but instead of tracking the 
level of the buffer, an FFT is used to obtain a spectrum, which is then divided into average bands using logAverages(), and each of these bands is tracked individually. The result 
is that it is possible to track sounds that occur in different parts of the frequency spectrum independently (like the kick drum and snare drum).

In sound energy mode you use isOnset() to query the algorithm and in frequency energy mode you use isOnset(int i), isKick(), isSnare(), and isRange() to 
query particular frequnecy bands or ranges of frequency bands. It should be noted that isKick(), isSnare(), and isHat() merely call isRange() with values 
determined by testing the algorithm against music with a heavy beat and they may not be appropriate for all kinds of music. If you find they are performing 
poorly with your music, you should use isRange() directly to locate the bands that provide the most meaningful information for you.
  */
  
import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
AudioPlayer song;
BeatDetect beat;

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
  //Framerate();
  size(800, 600);
  minim = new Minim(this);
  
  
  //"Albert Hofmann.mp3" "Rain Has Tone.mp3" "Xtal.mp3" "PrimaryColors.mp3"
  //"MichiganJ.mp3" "Words.mp3" "cloudNineVer.mp3"
  song = minim.loadFile("Rain Has Tone.mp3", 1024);
  song.play();
  // a beat detection object song SOUND_ENERGY mode with a sensitivity of 10 milliseconds
  beat = new BeatDetect(1024, 1024);
  
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
  beat.detect(song.mix);
  
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
  
  
  if (beat.isRange(0,1,2)) 
  {
    aRadius = 60;
    accu+=1;
    acc2+=1/11;
  }
  if (beat.isRange(1,2,2)) 
  {
    bRadius = 60;
    accu+=1/2;
    acc2+=1/11;
  }
  if (beat.isRange(2,3,2)) 
  {
    cRadius = 60;
    accu+=1/3;
    acc2+=1/11;
  }
  if (beat.isRange(3,4,2)) 
  {
    dRadius = 60;
    accu+=1/4;
    acc2+=1/11;
  }
  if (beat.isRange(4,5,2)) 
  {
    eRadius = 60;
    accu+=1.0/5;
    acc2+=1.0/11;
  }
  if (beat.isRange(5,6,2)) 
  {
    fRadius = 60;
    accu+=1.0/6;
    acc2+=1.0/11;
  }
  if (beat.isRange(6,7,2)) 
  {
    gRadius = 60;
    accu+=1.0/7;
    acc2+=1.0/11;
  }
  if (beat.isRange(7,8,2)) 
  {
    hRadius = 60;
    accu+=1.0/8;
    acc2+=1.0/11;
  }
  if (beat.isRange(8,9,2)) 
  {
    iRadius = 60;
    accu+=1.0/9;
    acc2+=1.0/11;
  }
  if (beat.isRange(9,10,2)) 
  {
    jRadius = 60;
    accu+=1.0/10;
    acc2+=1.0/11;
  }
  if (beat.isRange(10,11,2)) 
  {
    kRadius = 60;
    accu+=1.0/11;
    acc2+=1.0/11;
  }
  if(!trip && accu>whether) 
  {
    lRadius = 100;
    accu = 0;
    trip = true;
  }
  
  if(!trip2 && acc2>weather)
  {
    mRadius = 100;
    acc2 = 0;
    trip2 = true;
  }

  
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
