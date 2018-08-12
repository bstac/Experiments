//this is for the dome, 5 speakers
//synth structure is taken from video 3 of
//the youtube SC tutorial series.
//i went back to learn about synths,
//and it turns out they were using reverb and everything i wanted
//to control
//this is the updated one, for what i need
//ps, pretend Hz stands for decibals.
//i screwed up when i named it and im in a rush
(
SynthDef.new(\pulseTest, {
	arg rate=2, ampHz1=1, ampHz2=1, ampHz3=1, ampHz4=1, ampHz5=1,fund=40, maxPartial=4, width=0.5, revb=0.5;
	var  sig1, sig2, sig3, sig4, sig5, amp1, amp2, amp3, amp4, amp5, freq, rev;
	rev = revb;
	amp1 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz1;
	amp2 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz2;
	amp3 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz3;
	amp4 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz4;
	amp5 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz5;
	freq = LFNoise0.kr(4).exprange(fund, fund*maxPartial).round(fund);
	freq = freq * LFPulse.kr(8, add:1);
	sig1 = Pulse.ar(freq, width, amp1);
	sig2 = Pulse.ar(freq, width, amp2);
	sig3 = Pulse.ar(freq, width, amp3);
	sig4 = Pulse.ar(freq, width, amp4);
	sig5 = Pulse.ar(freq, width, amp5);
	sig1 = FreeVerb.ar(sig1, rev, rev, 0.25);
	sig2 = FreeVerb.ar(sig2, rev, rev, 0.25);
	sig3 = FreeVerb.ar(sig3, rev, rev, 0.25);
	sig4 = FreeVerb.ar(sig4, rev, rev, 0.25);
	sig5 = FreeVerb.ar(sig5, rev, rev, 0.25);
	Out.ar(0, sig1);
	Out.ar(1, sig2);
	Out.ar(2, sig3);
	Out.ar(3, sig4);
	Out.ar(4, sig5);
}).add;
)

x = Synth.new(\pulseTest);

(
OSCdef('cubeListener',
	{
		arg msg;
		x.set(\revb, (msg[1]));
		x.set(\ampHz1, (msg[2]));
		x.set(\ampHz2, (msg[3]));
		x.set(\ampHz3, (msg[4]));
		x.set(\ampHz4, (msg[5]));
		x.set(\ampHz5, (msg[6]));
	},
	"/cube");
)

//guitar input stuff
// scope input; silent output
{ Amplitude.kr(SoundIn.ar(0)); }.scope;


{FreeVerb.ar(SoundIn.ar([0,1]).distort)}.play

{FreeVerb.ar(SoundIn.ar([0,1]).distort,0.8,0.6,0.3,1,0)}.play

{PingPong.ar(SoundIn.ar(0).distort)}.play //broke'

{AllpassL.ar(SoundIn.ar(0).distort)}.play

{SoundIn.ar(0).distort}.play;

b = Buffer.alloc(s, 1024, 1); // for sampling rates 44100 and 48000
//b = Buffer.alloc(s, 2048, 1); // for sampling rates 88200 and 96000

d = Buffer.read(s, Platform.resourceDir +/+ "sounds/a11wlk01.wav");


(
x = {
var in, fft, array;

//in = PlayBuf.ar(1, d, BufRateScale.kr(d), 1, 0, 1);

in = {FreeVerb.ar(SoundIn.ar([0,1]).distort,0.8,0.6,0.3,1,0)}.play;

fft = FFT(b, in);

array = MFCC.kr(fft);

array.size.postln;

Out.kr(0, array);

Out.ar(0,Pan2.ar(in));
}.play
)

(
SynthDef("pitchFollow1",{
    var in, amp, freq, hasFreq, out;
    in = Mix.new(SoundIn.ar([0,1]));
    amp = Amplitude.kr(in, 0.05, 0.05);
    # freq, hasFreq = Pitch.kr(in, ampThreshold: 0.02, median: 7);
	//vvvvvvv---only the blelow line was orginally commented out.---vvvvvvvv
    //freq = Lag.kr(freq.cpsmidi.round(1).midicps, 0.05);
    out = Mix.new(VarSaw.ar(freq * [0.5,1,2], 0, LFNoise1.kr(0.3,0.1,0.1), amp));
    //out = SinOsc.ar(freq,0,1,0).squared;//this is my line, sucks.
	//try with an envelope, try the default
    6.do({
        out = AllpassN.ar(out, 0.040, [0.040.rand,0.040.rand], 2)
    });
    Out.ar(0,out)
}).play(s);
)

(
SynthDef("pitchFollow1",{
    var in, amp, freq, hasFreq, out;
    in = Mix.new(SoundIn.ar([0]));
    amp = Amplitude.kr(in, 0.05, 0.05);
    # freq, hasFreq = Pitch.kr(in, ampThreshold: 0.02, median: 7);
	~test = freq.poll;
    Out.ar(0,in)
}).play(s);
)

NetAddr.localAddr;
o = Server.local.options;
o.inDevice = "Built-in Microph"
o.inDevice = "MOTU UltraLite mk3 Hybrid";
o.outDevice = "MOTU UltraLite mk3 Hybrid";
o.outDevice = "Built-in Output"
s.freeAll;
s.plotTree;
s.meter;
s.reboot;
s.boot;
s.quit;

/* ----------------- SuperCollider code ---------------------------- */
//this is all from
//http://basislager.wikidot.com/supercollider-processing
// execute the following code line by line resp. block by block from top
~netAddr = NetAddr("127.0.0.1", 5001); // should be working with this ip and port-number ...
~oscResp = OSCresponder(~netAddr, '/toprocessing', {arg frq; [frq].postln}).add;//{ arg time, resp, msg; [time, msg].postln }).add;


~test.value;
~test = 44;
(
var in, freq;
in = Mix.new(SoundIn.ar([0]));
freq = Pitch.kr(in, ampThreshold: 0.02, median: 7);
~test = freq.postln;
)


(
~task = Task({
    loop({
        1.wait;
    //amp = Amplitude.kr(in, 0.05, 0.05);
		~netAddr.sendMsg("/toprocessing",~test.numberview);
//        nil.alwaysYield;
		~test.numberview;
    });
}).stop.reset.play;
)

// just for testing - send messages manually line by line
~netAddr.sendMsg("/toprocessing", 1, 5.0, "not you");
// just for testing - send messages manually line by line
~netAddr.sendMsg("/toprocessing", "you", "not you");
// strange: processing seems to receive these messages in an array, which i just can't achieve in a Task, it seems ...
~netAddr.sendMsg("/toprocessing", 1, 1.3, 77);
~netAddr.sendMsg("/toprocessing", ~test);

// should send to processing with a 15 secs delay, though i didn't recognize it when i tried it
~netAddr.sendBundle(15, ["/toprocessing", 1, 1.3, 77]);

~task.stop;
~task.reset;
~oscResp.remove;
~netAddr.disconnect;



